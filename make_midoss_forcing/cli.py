#  Copyright 2019-2020, the MIDOSS project contributors, The University of British Columbia,
#  and Dalhousie University.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""Command-line interfaces for tools in Make-MIDOSS-Forcing package.
"""
import click

from make_midoss_forcing import make_hdf5


@click.command(help=make_hdf5.create_hdf5.__doc__)
@click.version_option()
@click.argument("yaml_filename", type=click.Path(exists=True))
@click.argument("start_date", type=click.DateTime(formats=("%Y-%m-%d",)))
@click.argument("n_days", default=0, type=click.IntRange(min=0))
def make_hdf5_cli(yaml_filename, start_date, n_days):
    """Command-line interface for :py:mod:`make_midoss_forcing.make_hdf5`.

    Please see:

        make-hdf5 --help

    :param str yaml_filename: File path/name of YAML file to control HDF5 forcing files creation.

    :param start_date: Date on which to start HDF5 forcing files creation.
    :type start_date: :py:class:`datetime.datetime`

    :param int n_days: Number of days plus 1 of HDF5 forcing to create in each file.
                       Use 1 to create 2 days of forcing which is what is required for a
                       1 day MOHID run.
    """
    make_hdf5.create_hdf5(yaml_filename, start_date, n_days)
