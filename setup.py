"""
Flask-Jsoncat
-------------

This library helps to understand the basic building blocks of a flask extension.
"""
from setuptools import setup


setup(
    name='Flask-HelloExt',
    version='1.0',
    url='http://mczlatan-bourne.github.io',
    license='BSD',
    author='Olakanmi Oluwole',
    author_email='wole@playngonline.com',
    description='This library helps to understand the basic building blocks of a flask extension.',
    long_description=__doc__,
    py_modules=['flask_helloext'],
    #packages=[],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

