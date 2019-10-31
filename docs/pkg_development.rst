..  Copyright 2019, the MIDOSS project contributors, The University of British Columbia,
..  and Dalhousie University.
..
..  Licensed under the Apache License, Version 2.0 (the "License");
..  you may not use this file except in compliance with the License.
..  You may obtain a copy of the License at
..
..     https://www.apache.org/licenses/LICENSE-2.0
..
..  Unless required by applicable law or agreed to in writing, software
..  distributed under the License is distributed on an "AS IS" BASIS,
..  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
..  See the License for the specific language governing permissions and
..  limitations under the License.


.. _Make-MIDOSS-ForcingPackagedDevelopment:

**********************************************************
:kbd:`make_midoss_forcing` Package Development
**********************************************************


.. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: Licensed under the Apache License, Version 2.0
.. image:: https://img.shields.io/badge/python-3.6+-blue.svg
    :target: https://docs.python.org/3.7/
    :alt: Python Version
.. image:: https://img.shields.io/badge/version%20control-hg-blue.svg
    :target: https://bitbucket.org/midoss/make-midoss-forcing/
    :alt: Mercurial on Bitbucket
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://black.readthedocs.io/en/stable/
    :alt: The uncompromising Python code formatter
.. image:: https://readthedocs.org/projects/make-midoss-forcing/badge/?version=latest
    :target: https://make-midoss-forcing.readthedocs.io/en/latest/
    :alt: Documentation Status
.. image:: https://img.shields.io/bitbucket/issues/midoss/make-midoss-forcing.svg
    :target: https://bitbucket.org/midoss/make-midoss-forcing/issues?status=new&status=open
    :alt: Issue Tracker

The Make-MIDOSS-Forcing package (:kbd:`make_midoss_forcing`) is Make Salish Sea HDF5 Forcing Files for MIDOSS Runs


.. _Make-MIDOSS-ForcingPythonVersions:

Python Versions
===============

.. image:: https://img.shields.io/badge/python-3.6+-blue.svg
    :target: https://docs.python.org/3.7/
    :alt: Python Version

The :kbd:`make_midoss_forcing` package is developed and tested using `Python`_ 3.7 or later.
The package uses some Python language features that are not available in versions prior to 3.6,
in particular:

* `formatted string literals`_
  (aka *f-strings*)
* the `file system path protocol`_

.. _Python: https://www.python.org/
.. _formatted string literals: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
.. _file system path protocol: https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep519


.. _Make-MIDOSS-ForcingGettingTheCode:

Getting the Code
================

.. image:: https://img.shields.io/badge/version%20control-hg-blue.svg
    :target: https://bitbucket.org/midoss/make-midoss-forcing/
    :alt: Mercurial on Bitbucket

Clone the code and documentation `repository`_ from Bitbucket with:

.. _repository: https://bitbucket.org/midoss/make-midoss-forcing/

.. code-block:: bash

    $ hg clone ssh://hg@bitbucket.org/midoss/make-midoss-forcing Make-MIDOSS-Forcing

or

.. code-block:: bash

    $ hg clone https://your_userid@bitbucket.org/midoss/make-midoss-forcing Make-MIDOSS-Forcing

if you don't have `ssh key authentication`_ set up on Bitbucket
(replace :kbd:`you_userid` with you Bitbucket userid,
or copy the link from the :guilabel:`Clone` action pop-up on the `repository`_ page).

.. _ssh key authentication: https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html


.. _Make-MIDOSS-ForcingDevelopmentEnvironment:

Development Environment
=======================

Setting up an isolated development environment using `Conda`_ is recommended.
Assuming that you have the `Anaconda Python Distribution`_ or `Miniconda3`_ installed,
you can create and activate an environment called :kbd:`make-midoss-forcing` that will have all of the Python packages necessary for development,
testing,
and building the documentation with the commands below.

.. _Conda: https://conda.io/docs/
.. _Anaconda Python Distribution: https://www.anaconda.com/download/
.. _Miniconda3: https://conda.io/docs/install/quick.html

.. code-block:: bash

    $ cd Make-MIDOSS-Forcing
    $ conda env create -f env/environment-dev.yaml
    $ source activate make-midoss-forcing
    (make-midoss-forcing)$ pip install --editable .

The :kbd:`--editable` option in the :command:`pip install` command above installs the package from the cloned repo via symlinks so that the installed package will be automatically updated as the repo evolves.

To deactivate the environment use:

.. code-block:: bash

    (make-midoss-forcing)$ source deactivate


.. _Make-MIDOSS-ForcingCodingStyle:

Coding Style
============

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://black.readthedocs.io/en/stable/
    :alt: The uncompromising Python code formatter

The :kbd:`Make-MIDOSS-Forcing` package uses the `black`_ code formatting tool to maintain a coding style that is very close to `PEP 8`_.

.. _black: https://black.readthedocs.io/en/stable/
.. _PEP 8: https://www.python.org/dev/peps/pep-0008/

:command:`black` is installed as part of the :ref:`Make-MIDOSS-ForcingDevelopmentEnvironment` setup.

To run :command:`black` on the entire code-base use:

.. code-block:: bash

    $ cd Make-MIDOSS-Forcing
    $ conda activate make_midoss_forcing
    (make-midoss-forcing)$ black ./

in the repository root directory.
The output looks something like::

  **add example black output**


.. _Make-MIDOSS-ForcingBuildingTheDocumentation:

Building the Documentation
==========================

.. image:: https://readthedocs.org/projects/make-midoss-forcing/badge/?version=latest
    :target: https://make-midoss-forcing.readthedocs.io/en/latest/
    :alt: Documentation Status

The documentation for the :kbd:`Make-MIDOSS-Forcing` package is written in `reStructuredText`_ and converted to HTML using `Sphinx`_.
Creating a :ref:`Make-MIDOSS-ForcingDevelopmentEnvironment` as described above includes the installation of Sphinx.
Building the documentation is driven by the :file:`docs/Makefile`.
With your :kbd:`salishsea-nowcast` development environment activated,
use:

.. _reStructuredText: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Sphinx: http://www.sphinx-doc.org/en/master/

.. code-block:: bash

    (make-midoss-forcing)$ (cd docs && make clean html)

to do a clean build of the documentation.
The output looks something like::

  **add example Sphinx output**

The HTML rendering of the docs ends up in :file:`docs/_build/html/`.
You can open the :file:`index.html` file in that directory tree in your browser to preview the results of the build.

If you have write access to the `repository`_ on Bitbucket,
whenever you push changes to Bitbucket the documentation is automatically re-built and rendered at https://make-midoss-forcing.readthedocs.io/en/latest/.


.. _Make-MIDOSS-ForcingLinkCheckingTheDocumentation:

Link Checking the Documentation
-------------------------------

Sphinx also provides a link checker utility which can be run to find broken or redirected links in the docs.
With your :kbd:`make-midoss-forcing)` environment activated,
use:

.. code-block:: bash

    (make-midoss-forcing))$ cd Make-MIDOSS-Forcing)/docs/
    (make-midoss-forcing)) docs$ make linkcheck

The output looks something like::

  **add example linkcheck output**

Look for any errors in the above output or in _build/linkcheck/output.txt


.. _Make-MIDOSS-ForcingRunningTheUnitTests:

Running the Unit Tests
======================

The test suite for the :kbd:`Make-MIDOSS-Forcing` package is in :file:`Make-MIDOSS-Forcing/tests/`.
The `pytest`_ tool is used for test parametrization and as the test runner for the suite.

.. _pytest: https://docs.pytest.org/en/latest/

With your :kbd:`make-midoss-forcing` development environment activated,
use:

.. code-block:: bash

    (make-midoss-forcing)$ cd Make-MIDOSS-Forcing/
    (make-midoss-forcing)$ py.test

to run the test suite.
The output looks something like::

  **add example pytest output**

You can monitor what lines of code the test suite exercises using the `coverage.py`_ tool with the command:

.. _coverage.py: https://coverage.readthedocs.io/en/latest/

.. code-block:: bash

    (make-midoss-forcing)$ cd Make-MIDOSS-Forcing/
    (make-midoss-forcing)$ coverage run -m py.test

and generate a test coverage report with:

.. code-block:: bash

    (make-midoss-forcing)$ coverage report

to produce a plain text report,
or

.. code-block:: bash

    (make-midoss-forcing)$ coverage html

to produce an HTML report that you can view in your browser by opening :file:`Make-MIDOSS-Forcing/htmlcov/index.html`.


.. _Make-MIDOSS-ForcingVersionControlRepository:

Version Control Repository
==========================

.. image:: https://img.shields.io/badge/version%20control-hg-blue.svg
    :target: https://bitbucket.org/midoss/make-midoss-forcing/
    :alt: Mercurial on Bitbucket

The :kbd:`Make-MIDOSS-Forcing` package code and documentation source files are available as a `Mercurial`_ repository at https://bitbucket.org/midoss/make-midoss-forcing/.

.. _Mercurial: https://www.mercurial-scm.org/


.. _Make-MIDOSS-ForcingIssueTracker:

Issue Tracker
=============

.. image:: https://img.shields.io/bitbucket/issues/midoss/make-midoss-forcing.svg
    :target: https://bitbucket.org/midoss/make-midoss-forcing/issues?status=new&status=open
    :alt: Issue Tracker

Development tasks,
bug reports,
and enhancement ideas are recorded and managed in the issue tracker at https://bitbucket.org/midoss/make-midoss-forcing/issues.


License
=======

.. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: Licensed under the Apache License, Version 2.0

The code and documentation of the Make MIDOSS Forcing project
are copyright 2019 the MIDOSS project contributors, The University of British Columbia,
and Dalhousie University.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
