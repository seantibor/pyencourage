"One line encouragement for programmers (encouragement as a service)"

from __future__ import absolute_import
from .pyencourage import get_encouragement, get_encouragements


__project__      = 'pyencourage'
__version__      = '0.1.3'
__keywords__     = ['pyencourage', 'pyencouragement', 'encouragement', 'encourage']
__author__       = 'Sean Tibor'
__author_email__ = 'sean.tibor@gmail.com'
__url__          = 'https://github.com/seantibor/pyencourage'
__platforms__    = 'ALL'

__classifiers__ = [
    "Development Status :: 4 - Beta",
    "Topic :: Utilities",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
]

__entry_points__ = {
    'console_scripts': [
        'pyencourage = pyencouragecli.pyencourage:main',
        'pyencouragement = pyencouragecli.pyencouragement:main',
    ],
}

__requires__ = []

__extra_requires__ = {
    'doc':   ['mkdocs'],
    'test':  ['pytest', 'coverage', 'tox'],
}
