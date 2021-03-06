#!/usr/bin/env python

from distutils.core import setup

setup(name='klikatko',
      version='0.1',
      description='CIIRC B635 Annontation Tools',
      author='Libor Wagner',
      author_email='libor.wagner@cvut.cz',
      packages=['klikatko'],
      scripts=['bin/klikatko'],
      install_requires=[
          'pillow',
          'docopt',
          'numpy',
          'pandas',
      ],
      console=['bin/klikatko'],
     )
