#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re
from collections import OrderedDict

from setuptools import setup

with io.open('dbdoc/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='dbdoc',
    version=version,
    url='https://github.com/faeli/dbdoc',
    project_urls=OrderedDict((
        ('Documentation', 'https://github.com/faeli/dbdoc/wiki'),
        ('Code', 'https://github.com/faeli/dbdoc'),
        ('Issue tracker', 'https://github.com/faeli/dbdoc/issues'),
    )),
    license='Apache License 2.0',
    author='Feng pengbin',
    author_email='fengpengbin@live.cn',
    maintainer='Feng pengbin',
    maintainer_email='fengpengbin@live.cn',
    description='A simple database doc with one html file',
    packages=['dbdoc'],
    include_package_data=True,
    zip_safe=False,
    data_files=['dbdoc/style.css'],
    platforms='any',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=[
        'SQLAlchemy>=1.2',
        'click>=5.1',
    ],
)