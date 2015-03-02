# -*- coding: utf-8 -*-

from setuptools import setup

import redis_drs

# README.rst dynamically generated:
with open('README.rst', 'w') as f:
    f.write(redis_drs.__doc__)

NAME = 'redis_drs'

def read(file):
    with open(file, 'r') as f:
        return f.read().strip()

setup(
    name=NAME,
    version=read('VERSION'),
    description='',
    long_description=read('README.rst'),
    author='Mike Burr',
    author_email='mburr@unintuitive.org',
    url='https://github.com/stnbu/{0}'.format(NAME),
    download_url='https://github.com/stnbu/{0}/archive/master.zip'.format(NAME),
    provides=[NAME],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
    packages=[NAME],
    keywords=[],
    test_suite='test',
    requires=['redis'],
)
