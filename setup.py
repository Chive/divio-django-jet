# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from divio_django_jet import __version__


setup(
    name='divio-django-jet',
    version=__version__,
    description=open('README.rst').read(),
    author='Divio AG',
    author_email='info@divio.com',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[
        'django-jet==1.0.4',
    ],
    include_package_data=True,
    zip_safe=False,
)
