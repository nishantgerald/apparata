from setuptools import setup

setup(
    name='apparata',
    version='0.1.2',
    url='https://github.com/nishantgerald/apparata',
    license='MIT',
    description='A collection of useful functions for generating random data.',
    author='Nishant Gerald',
    author_email='nishantgerald@gmail.com',
    packages=['apparata'],
    install_requires=['faker', 'pandas'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)