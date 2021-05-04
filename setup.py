#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name='restaurant',
    version='1.0.0',

    package_dir={'': 'src'},
    packages=find_packages(where='src'),

    include_package_data=True,

    python_requires='>=3.7, <4',
    install_requires=[
        'click'
    ],

    entry_points={
        'console_scripts': [
            'restaurant = restaurant.__main__:main'
        ]
    }
)
