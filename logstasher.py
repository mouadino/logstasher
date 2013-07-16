"""Logger formatter ready LogStash."""
import os
import sys
import json
import socket
import logging
from datetime import datetime

import tzlocal


class LogStashFormatter(logging.Formatter): 
    """Logging formatter that format messages as a JSON to make them easily
    shippable to LogStash.

    """

    extra_attributes = ['request_id', 'user', 'tenant', 'levelname']
        
    def __init__(self, fmt=None, datefmt=None):
        if fmt:
            raise ValueError("'fmt' argument is obsolete in LogStashFormatter")
	self._source_hostname = socket.gethostname()
        super(LogStashFormatter, self).__init__(fmt=fmt, datefmt=datefmt)
        if not self.datefmt:
            self.datefmt = '%Y-%m-%dT%H:%M:%S%z'

    def format(self, record):
        # record.created field is set to a timestamp which mean that we
        # can't convert it to timezone aware object, so we are resetting it
        # here as a datetime object and convert it to the local timezone.
        created = datetime.fromtimestamp(record.created)
        created = tzlocal.get_localzone().localize(created)
    
        fields = {
	    '@source_host': self._source_hostname,
            '@message': record.getMessage(),
            '@timestamp': created.strftime(self.datefmt),
        }

        extra_fields = fields['@fields'] = {}
        for attr_name in self.extra_attributes:        
            attr_val = getattr(record, attr_name, None)
            if attr_val:
                extra_fields[attr_name] = attr_val

        # Get which service logged this message. 
	extra_fields['service'] = os.path.basename(sys.argv[0])

        # Detect exceptions and add a tag and a new field for that.
        if record.exc_info:
            fields['@tags'] = ['exception']
            extra_fields['traceback'] = self.formatException(record.exc_info)

        return json.dumps(fields)
