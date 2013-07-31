Log formatter for OpenStack services to use with logstash.


Usage:

1- Create a logging.conf configuration, example for nova check the sample
   here: https://github.com/openstack/nova/blob/stable/grizzly/etc/nova/logging_sample.conf

2- Change logging configuration respectively to use the logstasher formatter
   logstasher.LogStashFormatter, if you don't know how please read upon how
   to work with python logging module here: http://docs.python.org/2/library/logging.config.html#module-logging.config

3- Add to the openstack service configuration the attribute log_config and set it
   to the path of the logging configuration file that you just created.

4- (Re)start the service and enjoy.
