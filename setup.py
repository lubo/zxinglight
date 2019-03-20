# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages, Extension

with open('README.rst') as readme:
    long_description = readme.read()

ext_libraries = [
    'zxing'
]

if sys.platform == 'darwin':
    ext_libraries += [
        'iconv'
    ]

setup(
    name='zxinglight',
    version='1.0.1',
    description='A simple ZXing C++ wrapper',
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: C++',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    keywords=[
        'zxing',
        'barcode',
        'QR code'
    ],
    author='Ľubomír Kučera',
    author_email='lubomir.kucera.jr@gmail.com',
    url='https://github.com/lubo/zxinglight',
    license='MIT',
    packages=find_packages(exclude=[
        'tests'
    ]),
    ext_modules=[
        Extension(
            name='zxinglight._zxinglight',
            language='c++',
            sources=[
                'zxinglight/_zxinglight.cpp'
            ],
            extra_compile_args=[
                '-std=c++11'
            ],
            libraries=ext_libraries,
        ),
    ],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'setuptools',
    ],
    install_requires=[
        'Pillow'
    ],
    extras_require={
        'docs': [
            'Sphinx',
            'sphinx-autobuild',
            'sphinx_rtd_theme'
        ],
        'test': [
            'flake8',
            'flake8-bugbear',
            'nose',
            'pep8-naming'
        ]
    }
)
