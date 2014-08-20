from setuptools import setup
import sys


setup(
    name = 'Sola',
    version = '0.1',
    author = "Thomas Huang",
    author_email='lyanghwy@gmail.com',
    description = "A Framework for reuse",
    license = "GPL",
    keywords = "Framework",
    url='https://github.com/thomashuang/Leaf',
    long_description=open('README.rst').read(),
    packages = ['sola', 'sola.web'],
    install_requires = ['setuptools'],
    classifiers=(
        "Development Status :: Production/Alpha",
        "License :: GPL",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: framework"
        )
    )