#!/usr/bin/env python

from corsheaders import __version__
from setuptools import setup, find_packages

setup(
    name='django-cors-middleware',
    version=__version__,
    description='django-cors-middleware is a Django application for handling the server headers required for Cross-Orig'
                'in Resource Sharing (CORS). Fork of django-cors-headers.',
    author='Zeste de Savoir',
    author_email='dev@gustavi.net',
    url='https://github.com/zestedesavoir/django-cors-middleware',
    packages=find_packages(),
    license='MIT License',
    keywords='django cors middleware rest api',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[],
    tests_require=['mock >= 1.0'],
    test_suite='tests.main',
)
