# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='livechat',
    version=version,
    description='A live chat inside ERPNext.',
    author='Semilimes',
    author_email='support@semilimes.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
