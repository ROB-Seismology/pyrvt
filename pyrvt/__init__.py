#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import tools, motions, peak_calculators

from pkg_resources import get_distribution

__all__ = [
    'tools',
    'motions',
    'peak_calculators',
]

__author__ = 'Albert Kottke'
__copyright__ = 'Copyright 2016 Albert Kottke'
__license__ = 'MIT'
__title__ = 'pyrvt'
__version__ = get_distribution('pyrvt').version
