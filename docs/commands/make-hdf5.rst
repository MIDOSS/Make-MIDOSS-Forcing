..  Copyright 2019-2020, the MIDOSS project contributors, The University of British Columbia,
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


.. _make-hdf5-Command:

****************************
:command:`make-hdf5` Command
****************************

The :command:`make-hdf5` command creates a collection of HDF5 forcing files to drive a MIDOSS-MOHID run.
The HDF5 forcing files are calculated from the output of 3 other models that are assumed to have already been run for the time period for which MIDOSS-MOHID is to be run:

* Output from SalishSeaCast NEMO is used to calculate forcing fields for variables:

  * u-direction component of seawater current
  * v-direction component of seawater current
  * w-direction seawater current component
  * seawater salinity
  * seawater temperature
  * sea surface height
  * time-varying z-layer thickness from NEMO VVL
  * vertical eddy diffusivity

* Output from the Environment and Climate Change Canada (ECCC) High Resolution Deterministic Prediction System (HRDPS) that has been process to be used as forcing for the SalishSeaCast NEMO model is used to calculate forcing fields for variables:

  * u-direction component of wind velocity
  * v-direction component of wind velocity

* Output from the Strait of Georgia configuration of WaveWatch III™ driven by currents from the SalishSeaCast NEMO model and winds from HRDPS is used to calculate forcing fields for variables:

  * sea surface witecap coverage fraction
  * mean period of wind waves from variance of spectral density of second frequency moment
  * mean wave length of wind waves
  * significant height of wind waves
  * u-direction component of sea surface Stokes drift
  * v-direction component of sea surface Stokes drift


.. _make-hdf5-Usage:

Usage
=====

The see information about the arguments for :command:`make-hdf5` use :command:`make-hdf5 --help`.
For example:

.. code-block:: bash

    $ make-hdf5 --help

.. code-block:: text

    Usage: make-hdf5 [OPTIONS] YAML_FILENAME [%Y-%m-%d] [N_DAYS]

      Create HDF5 forcing files for a MIDOSS-MOHID run.

      YAML_FILENAME: File path/name of YAML file to control HDF5 forcing files
      creation.

      [%Y-%m-%d]: Date on which to start HDF5 forcing files creation.

      N_DAYS: Number of days plus 1 of HDF5 forcing to create in each file.
      Use 1 to create 2 days of forcing which is what is required for a 1 day
      MOHID run.

    Options:
      --version  Show the version and exit.
      --help     Show this message and exit.


.. _make-hdf5-YAML-FileExample:

:command:`make-hdf5` YAML File Example
======================================

The paths to the collections of SalishSeaCast NEMO,
HRDPS,
and WaveWatch III™ files from which the HDF5 forcing files are calculated are defined in the YAML file that :command:`make-hdf5` reads.
The destination directory for the HDF5 forcing files,
the names for those files,
and the variables that are stored in them are also defined in the YAML file.

Here is a commented example of a YAML file:

.. literalinclude:: make-hdf5.yaml.example
   :language: yaml
