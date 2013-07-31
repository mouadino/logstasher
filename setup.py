from setuptools import setup, find_packages


setup(
    name="logstasher",
    version="0.1",
    author="Mouad Benchchaoui",
    author_email="m.benchchaoui@cloudbau.de",
    description="TODO",
    license="BSD",
    keywords="logging formatting openstack logstash",
    install_requires=['tzlocal==1.0'],
    py_modules=['logstasher'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
