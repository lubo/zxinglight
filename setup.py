# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages, Extension


def read(file_path):
    with open(file_path) as fp:
        return fp.read()


libraries = [
    'zxing'
]
if sys.platform == 'darwin':
    libraries.append('iconv')


setup(
    name='zxinglight',
    version='1.0.0',
    description='A simple ZXing C++ wrapper',
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: C++',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    keywords=[
        'zxing',
        'barcode',
        'QR code'
    ],
    author='Ľubomír Kučera',
    author_email='lubomir.kucera.jr@gmail.com',
    url='https://github.com/Lubo/zxinglight',
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
            libraries=libraries,
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
            'nose',
            'pep8-naming'
        ]
    }
)
