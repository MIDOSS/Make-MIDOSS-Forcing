..  Copyright 2019-2021, the MIDOSS project contributors, The University of British Columbia,
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
.. image:: https://img.shields.io/badge/python-3.8+-blue.svg
    :target: https://docs.python.org/3.9/
    :alt: Python Version
.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/MIDOSS/Make-MIDOSS-Forcing
    :alt: Git on GitHub
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://black.readthedocs.io/en/stable/
    :alt: The uncompromising Python code formatter
.. image:: https://readthedocs.org/projects/make-midoss-forcing/badge/?version=latest
    :target: https://make-midoss-forcing.readthedocs.io/en/latest/
    :alt: Documentation Status
.. image:: https://github.com/MIDOSS/Make-MIDOSS-Forcing/workflows/sphinx-linkcheck/badge.svg
      :target: https://github.com/MIDOSS/Make-MIDOSS-Forcing/actions?query=workflow:sphinx-linkcheck
      :alt: Sphinx linkcheck
.. image:: https://img.shields.io/github/issues/MIDOSS/Make-MIDOSS-Forcing?logo=github
    :target: https://github.com/MIDOSS/Make-MIDOSS-Forcing/issues
    :alt: Issue Tracker

The Make-MIDOSS-Forcing package (:kbd:`make_midoss_forcing`) is Make Salish Sea HDF5 Forcing Files for MIDOSS Runs


.. _Make-MIDOSS-ForcingPythonVersions:

Python Versions
===============

.. image:: https://img.shields.io/badge/python-3.8+-blue.svg
    :target: https://docs.python.org/3.9/
    :alt: Python Version

The :kbd:`make_midoss_forcing` package is developed and tested using `Python`_ 3.9.
It is intended to work in environments using Python>=3.8.
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

.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/MIDOSS/Make-MIDOSS-Forcing
    :alt: Git on GitHub

Clone the code and documentation `repository`_ from GitHub with:

.. _repository: https://github.com/MIDOSS/Make-MIDOSS-Forcing

.. code-block:: bash

    $ git clone git@github.com:MIDOSS/Make-MIDOSS-Forcing.git


.. _Make-MIDOSS-ForcingDevelopmentEnvironment:

Development Environment
=======================

Setting up an isolated development environment using `Conda`_ is recommended.
Assuming that you have `Miniconda`_ installed,
you can create and activate an environment called :kbd:`make-midoss-forcing` that will have all of the Python packages necessary for development,
testing,
and building the documentation with the commands below.

.. _Conda: https://conda.io/en/latest/
.. _Miniconda: https://docs.conda.io/en/latest/miniconda.html

.. code-block:: bash

    $ cd Make-MIDOSS-Forcing
    $ conda env create -f envs/environment-dev.yaml
    $ conda activate make-midoss-forcing
    (make-midoss-forcing)$ python3 -m pip install --editable .

The :kbd:`--editable` option in the :command:`pip install` command above installs the package from the cloned repo via symlinks so that the installed package will be automatically updated as the repo evolves.

To deactivate the environment use:

.. code-block:: bash

    (make-midoss-forcing)$ conda deactivate


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

  reformatted /media/doug/warehouse/MIDOSS/Make-MIDOSS-Forcing/make_midoss_forcing/forcing_paths.py
  All done! ✨ 🍰 ✨
  1 file reformatted, 6 files left unchanged.


.. _Make-MIDOSS-ForcingBuildingTheDocumentation:

Building the Documentation
==========================

.. image:: https://readthedocs.org/projects/make-midoss-forcing/badge/?version=latest
    :target: https://make-midoss-forcing.readthedocs.io/en/latest/
    :alt: Documentation Status

The documentation for the :kbd:`Make-MIDOSS-Forcing` package is written in `reStructuredText`_ and converted to HTML using `Sphinx`_.

.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Sphinx: https://www.sphinx-doc.org/en/master/

If you have write access to the `repository`_ on GitHub,
whenever you push changes to GitHub the documentation is automatically re-built and rendered at https://make-midoss-forcing.readthedocs.io/en/latest/.

Additions,
improvements,
and corrections to these docs are *always* welcome.

The quickest way to fix typos, etc. on existing pages is to use the :guilabel:`Edit on GitHub` link in the upper right corner of the page to get to the online editor for the page on `GitHub`_.

.. _GitHub: https://github.com/MIDOSS/Make-MIDOSS-Forcing

For more substantial work,
and to add new pages,
follow the instructions in the :ref:`Make-MIDOSS-ForcingDevelopmentEnvironment` section above.
In the development environment you can build the docs locally instead of having to push commits to GitHub to trigger a `build on readthedocs.org`_ and wait for it to complete.
Below are instructions that explain how to:

.. _build on readthedocs.org: https://readthedocs.org/projects/make-midoss-forcing/builds/

* build the docs with your changes,
  and preview them in Firefox

* check the docs for broken links


.. _Make-MIDOSS-ForcingBuildingAndPreviewingTheDocumentation:

Building and Previewing the Documentation
-----------------------------------------

Building the documentation is driven by the :file:`docs/Makefile`.
With your :kbd:`make-midoss-forcing` environment activated,
use:

.. code-block:: bash

    (make-midoss-forcing)$ (cd docs && make clean html)

to do a clean build of the documentation.
The output looks something like::

  Running Sphinx v2.2.1
  making output directory... done
  building [mo]: targets for 0 po files that are out of date
  building [html]: targets for 2 source files that are out of date
  updating environment: [new config] 2 added, 0 changed, 0 removed
  reading sources... [100%] pkg_development
  looking for now-outdated files... none found
  pickling environment... done
  checking consistency... done
  preparing documents... done
  writing output... [100%] pkg_development
  generating indices...  genindexdone
  writing additional pages...
  done
  copying static files... ... done
  copying extra files... done
  dumping search index in English (code: en)... done
  dumping object inventory... done
  build succeeded.

  The HTML pages are in _build/html.

The HTML rendering of the docs ends up in :file:`docs/_build/html/`.
You can open the :file:`index.html` file in that directory tree in your browser to preview the results of the build.

If you have write access to the `repository`_ on GitHub,
whenever you push changes to Bitbucket the documentation is automatically re-built and rendered at https://make-midoss-forcing.readthedocs.io/en/latest/.


.. _Make-MIDOSS-ForcingLinkCheckingTheDocumentation:

Link Checking the Documentation
-------------------------------

.. image:: https://github.com/MIDOSS/Make-MIDOSS-Forcing/workflows/sphinx-linkcheck/badge.svg
      :target: https://github.com/MIDOSS/Make-MIDOSS-Forcing/actions?query=workflow:sphinx-linkcheck
      :alt: Sphinx linkcheck

Sphinx also provides a link checker utility which can be run to find broken or redirected links in the docs.
With your :kbd:`make-midoss-forcing)` environment activated,
use:

.. code-block:: bash

    (make-midoss-forcing))$ cd Make-MIDOSS-Forcing)/docs/
    (make-midoss-forcing)) docs$ make linkcheck

The output looks something like::

  Running Sphinx v2.2.1
  loading pickled environment... done
  building [mo]: targets for 0 po files that are out of date
  building [linkcheck]: targets for 2 source files that are out of date
  updating environment: 0 added, 1 changed, 0 removed
  reading sources... [100%] pkg_development
  looking for now-outdated files... none found
  pickling environment... done
  checking consistency... done
  preparing documents... done
  writing output... [ 50%] index
  (line   37) ok        https://img.shields.io/badge/license-Apache%202-cb2533.svg
  (line   37) ok        https://www.apache.org/licenses/LICENSE-2.0
  (line   47) ok        https://www.apache.org/licenses/LICENSE-2.0
  writing output... [100%] pkg_development
  (line   21) ok        https://docs.python.org/3.8/
  (line   55) ok        https://www.python.org/
  (line   59) ok        https://docs.python.org/3/reference/lexical_analysis.html#f-strings
  (line   61) ok        https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep519
  (line   21) ok        https://black.readthedocs.io/en/stable/
  (line   21) ok        https://bitbucket.org/midoss/make-midoss-forcing/
  (line   21) ok        https://bitbucket.org/midoss/make-midoss-forcing/issues?status=new&status=open
  (line  103) ok        https://conda.io/en/latest/
  (line   21) ok        https://make-midoss-forcing.readthedocs.io/en/latest/
  (line   71) ok        https://bitbucket.org/midoss/make-midoss-forcing/
  (line  138) ok        https://www.python.org/dev/peps/pep-0008/
  (line  164) ok        https://make-midoss-forcing.readthedocs.io/en/latest/
  (line  103) ok        https://docs.conda.io/en/latest/miniconda.html
  (line   77) ok        https://bitbucket.org/midoss/make-midoss-forcing/
  (line  211) ok        https://make-midoss-forcing.readthedocs.io/en/latest/
  (line  170) ok        http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
  (line  170) ok        http://www.sphinx-doc.org/en/master/
  (line  103) ok        https://www.anaconda.com/distribution/
  (line  241) ok        https://docs.pytest.org/en/latest/
  (line   21) ok        https://img.shields.io/badge/python-3.6+-blue.svg
  (line   21) ok        https://img.shields.io/badge/version%20control-hg-blue.svg
  (line  259) ok        https://coverage.readthedocs.io/en/latest/
  (line   21) ok        https://img.shields.io/badge/code%20style-black-000000.svg
  (line   21) ok        https://readthedocs.org/projects/make-midoss-forcing/badge/?version=latest
  (line  301) ok        https://img.shields.io/bitbucket/issues/midoss/make-midoss-forcing.svg
  (line  307) ok        https://bitbucket.org/midoss/make-midoss-forcing/issues
  (line   91) ok        https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html
  (line  293) ok        https://www.mercurial-scm.org/
  (line   21) ok        https://img.shields.io/bitbucket/issues/midoss/make-midoss-forcing.svg

  build finished.

Look for any errors in the above output or in _build/linkcheck/output.txt

:command:`make linkcheck` is run monthly via a `scheduled GitHub Actions workflow`_

.. _scheduled GitHub Actions workflow: https://github.com/MIDOSS/Make-MIDOSS-Forcing/actions?query=workflow%3Asphinx-linkcheck


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

You can monitor what lines of code the test suite exercises using the `coverage.py`_ and `pytest-cov`_ tools with the command:

.. _coverage.py: https://coverage.readthedocs.io/en/latest/
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/

.. code-block:: bash

    (make-midoss-forcing)$ cd Make-MIDOSS-Forcing/
    (make-midoss-forcing)$ pytest --cov=./

The test coverage report will be displayed below the test suite run output.

Alternatively,
you can use

.. code-block:: bash

    (make-midoss-forcing)$ pytest --cov=./ --cov-report html

to produce an HTML report that you can view in your browser by opening :file:`Make-MIDOSS-Forcing/htmlcov/index.html`.


.. _Make-MIDOSS-ForcingVersionControlRepository:

Version Control Repository
==========================

.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/MIDOSS/Make-MIDOSS-Forcing
    :alt: Git on GitHub

The :kbd:`Make-MIDOSS-Forcing` package code and documentation source files are available as a `Git`_ repository at https://github.com/MIDOSS/Make-MIDOSS-Forcing.

.. _Git: https://git-scm.com/


.. _Make-MIDOSS-ForcingIssueTracker:

Issue Tracker
=============

.. image:: https://img.shields.io/github/issues/MIDOSS/Make-MIDOSS-Forcing?logo=github
    :target: https://github.com/MIDOSS/Make-MIDOSS-Forcing/issues
    :alt: Issue Tracker

Development tasks,
bug reports,
and enhancement ideas are recorded and managed in the issue tracker at https://github.com/MIDOSS/Make-MIDOSS-Forcing/issues.


License
=======

.. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: Licensed under the Apache License, Version 2.0

The code and documentation of the Make MIDOSS Forcing project
are copyright 2019-2021 the `MIDOSS project contributors`_, The University of British Columbia,
and Dalhousie University.

.. _MIDOSS project contributors: https://github.com/MIDOSS/docs/blob/master/CONTRIBUTORS.rst

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
