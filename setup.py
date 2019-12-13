#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


setup(
    name='dask-scheduler',
    version='0.1',
    license='MIT',
    description='Simple CLI for starting dask scheduler servers including those on queueing systems like SLURM and PBS',
    author='Samuel D. Lotz',
    author_email='samuel.lotz@salotz.info',
    url='https://github.com/salotz/dask_scheduler',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    keywords=[
        'dask', 'SLURM', 'jobqueue', 'distributed'
    ],
    install_requires=[
        'dask',
        'distributed',
        'dask-jobqueue',
        'click',
    ],
    setup_requires=[
    ],
    entry_points={
        'console_scripts': [
            'dask_scheduler = scheduler:cli',
        ]
    },
)
