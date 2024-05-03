from setuptools import setup

setup(
    name='apparata',
    version='0.1.0',
    description='A collection of useful functions for generating random data.',
    author='Nishant Gerald',
    author_email='mail@nishantgerald.com',
    packages=['apparata'],
    install_requires=[
        'faker',
        'random',
        'pandas',
    ],
)
