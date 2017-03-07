Installation
============

Requirements
------------

Before installing ZXingLight, you need to:

1. `Install ZXing C++`_
2. Install C++11 compatible version of g++ (>= 4.8.1)

.. _Install ZXing C++: #installing-zxing-c

Installing ZXing C++
--------------------

Download and install `ZXing C++`_ according to README_.

.. warning::
    Do not forget to use :code:`-DCMAKE_CXX_FLAGS=-fPIC`. Otherwise, linking will fail while
    installing ZXingLight.

.. _ZXing C++: https://github.com/glassechidna/zxing-cpp
.. _README: https://github.com/glassechidna/zxing-cpp/blob/master/README.md#building-using-cmake

Installing ZXingLight
---------------------

ZXingLight can be installed from PyPI using pip:

.. code-block:: bash

    $ pip install zxinglight

Or using setuptools:

.. code-block:: bash

    $ python setup.py install
