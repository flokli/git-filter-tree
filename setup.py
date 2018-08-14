#!/usr/bin/env python3
import io

from setuptools import setup


def long_description():
    """Compose a long description for PyPI."""
    long_description = ''
    try:
        with io.open('README.rst', 'rt', encoding='utf8') as f:
            long_description += f.read()
        with io.open('CHANGES.rst', 'rt', encoding='utf8') as f:
            long_description += f.read()
    except (IOError, UnicodeDecodeError):
        pass
    return long_description


setup(
    name='git-filter-tree',
    version='2.1.0',
    description='Efficient tree filtering (examples)',
    long_description=long_description(),
    author='Thomas Gläßle',
    author_email='thomas@coldfix.de',
    url='https://github.com/coldfix/git-filter-tree',
    license='GPLv3',
    packages=['git_filter_tree'],
    entry_points = {
        'console_scripts': [
            'git-filter-tree = git_filter_tree.__main__:main',
        ],
    },
    install_requires=[
        'pygit2',
    ],
    classifiers= [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Version Control :: Git',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
)
