#  Copyright 2019, the MIDOSS project contributors, The University of British Columbia,
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

from datetime import timedelta
import os

import numpy


def salishseacast_paths(timestart, timeend, path, filetype):
    """Generate paths for Salish Seacast forcing

    :arg timestart: date from when to start concatenating
    :type string: :py:class:'str'

    :arg timeend: date at which to stop concatenating
    :type string: :py:class:'str'

    :arg path: path of input files
    :type string: :py:class:'str'

    :returns tuple: three tuples containing the arguments to pass to hdf5 file generator functions
    :rtype: :py:class:`tuple'
    """

    # generate list of dates from daterange given
    daterange = [timestart, timeend]

    # append all filename strings within daterange to lists
    filelist = []
    for day in range(numpy.diff(daterange)[0].days + 1):
        datestamp = daterange[0] + timedelta(days=day)
        datestr1 = datestamp.strftime("%d%b%y").lower()
        datestr2 = datestamp.strftime("%Y%m%d")

        # check if file exists. exit if it does not. add path to list if it does.
        file_path = f"{path}{datestr1}/SalishSea_1h_{datestr2}_{datestr2}_{filetype}.nc"
        if not os.path.exists(file_path):
            print(f"File {file_path} not found. Check Directory and/or Date Range.")
            return False
        filelist.append(file_path)

    return filelist


def hrdps_paths(timestart, timeend, path):
    """Generate wind input file paths

    :arg timestart: date from when to start concatenating
    :type string: :py:class:'str'

    :arg timeend: date at which to stop concatenating
    :type string: :py:class:'str'

    :arg path: path of input files
    :type string: :py:class:'str'

    :returns tuple: tuple containing the arguments to pass to hdf5 file generator function
    :rtype: :py:class:`tuple'
    """

    # generate list of dates from daterange given
    daterange = [timestart, timeend]

    # append all filename strings within daterange to list
    wind_files = []
    for day in range(numpy.diff(daterange)[0].days + 1):
        datestamp = daterange[0] + timedelta(days=day)

        month = datestamp.month
        if month < 10:
            month = f"0{str(month)}"

        day = datestamp.day
        if day < 10:
            day = f"0{str(day)}"

        year = str(datestamp.year)

        # check if file exists. exit if it does not. add path to list if it does.
        wind_path = f"{path}ops_y{year}m{month}d{day}.nc"
        if not os.path.exists(wind_path):
            print(f"File {wind_path} not found. Check Directory and/or Date Range.")
            return
        wind_files.append(wind_path)

    return wind_files


def ww3_paths(timestart, timeend, path):
    """Generate Wave Watch 3 input files paths

    :arg timestart: date from when to start concatenating
    :type string: :py:class:'str'

    :arg timeend: date at which to stop concatenating
    :type string: :py:class:'str'

    :arg path: path of input files
    :type string: :py:class:'str'

    :returns tuple: tuple containing the arguments to pass to hdf5 file generator function
    :rtype: :py:class:`tuple'
    """
    # generate list of dates from daterange given
    months = {
        1: "jan",
        2: "feb",
        3: "mar",
        4: "apr",
        5: "may",
        6: "jun",
        7: "jul",
        8: "aug",
        9: "sep",
        10: "oct",
        11: "nov",
        12: "dec",
    }
    daterange = [timestart, timeend]
    # append all filename strings within daterange to list
    wave_files = []
    for day in range(numpy.diff(daterange)[0].days + 1):
        datestamp = daterange[0] + timedelta(days=day)
        datestr2 = datestamp.strftime("%Y%m%d").lower()
        monthnm = months[datestamp.month]

        day = datestamp.day
        if day < 10:
            day = f"0{str(day)}"

        year = str(datestamp.year)[2:4]
        wave_path = f"{path}{day}{monthnm}{year}/SoG_ww3_fields_{datestr2}.nc"
        if not os.path.exists(wave_path):
            wave_path = (
                f"{path}{day}{monthnm}{year}/SoG_ww3_fields_{datestr2}_{datestr2}.nc"
            )
        if not os.path.exists(wave_path):
            print(f"File {wave_path} not found. Check Directory and/or Date Range.")
            return False
        wave_files.append(wave_path)

    return wave_files
