==============
serpentine_isg
==============


.. .. image:: https://img.shields.io/pypi/v/serpentine_isg.svg
..         :target: https://pypi.python.org/pypi/serpentine_isg

.. .. image:: https://img.shields.io/travis/markgrivainis/serpentine_isg.svg
..         :target: https://travis-ci.com/markgrivainis/serpentine_isg

.. .. image:: https://readthedocs.org/projects/serpentine-isg/badge/?version=latest
..         :target: https://serpentine-isg.readthedocs.io/en/latest/?version=latest
..         :alt: Documentation Status




A script to convert coordinates into a serpentine pattern


* Free software: MIT
.. * Documentation: https://serpentine-isg.readthedocs.io.

Installation
-------------

I recommend using pipx_

.. code-block:: shell

        pipx install git+https://github.com/MarkGrivainis/serpentine_isg.git
                         

But it can also be installed using pip

.. code-block:: shell

        pip install git+https://github.com/MarkGrivainis/serpentine_isg.git


.. _pipx: https://github.com/pypa/pipx

Usage
-----

Reorder by row using serpentine

.. code-block:: shell

        serpentine_isg --row <file-path>

Serpentine the column coordinates

.. code-block:: shell

        serpentine_isg --col <file-path>

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
