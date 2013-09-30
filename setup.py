# -*- coding: utf-8 -*-
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name="sakura",
    version="1.0",
    description="stdrickforce's ubuntu rapid configuration solution",
    long_description=open("README.md").read(),
    author="[STD]Rick_Force",
    author_email="stdrickforce@gmail.com",
    packages=find_packages(),
    pacakage_data={},
    install_requires=[
        "celery>=3.0.23",
        "email>=4.0.2",
        "flask>=0.10.1",
        "redis>=2.8.0",
        "sqlalchemy>=0.8.0",
    ]
)
