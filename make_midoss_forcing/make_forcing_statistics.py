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

import numpy as np
import h5py
import os
import yaml

def wind_speed_dir(u_wind, v_wind):
    """Calculate wind speed and direction from u and v wind components.

    :kbd:`u_wind` and :kbd:`v_wind` may be either scalar numbers or
    :py:class:`numpy.ndarray` objects,
    and the elements of the return value will be of the same type.

    :arg u_wind: u-direction component of wind vector.

    :arg v_wind: v-direction component of wind vector.

    :returns: 2-tuple containing the wind speed and direction.
              The :py:attr:`speed` attribute holds the wind speed(s),
              and the :py:attr:`dir` attribute holds the wind
              direction(s).
    :rtype: :py:class:`collections.namedtuple`
    """
    speed = np.sqrt(u_wind**2 + v_wind**2)
    dir = np.arctan2(v_wind, u_wind)
    dir = np.rad2deg(dir + (dir < 0) * 2 * np.pi)
    return speed, dir

def add_to_dict(group, timeseries, dict24, dict168, start_hour):
    dict24[group] = {'min': "%.4g" % np.min(timeseries[start_hour:start_hour+24]),
                         'max': "%.4g" % np.max(timeseries[start_hour:start_hour+24]),
                         'mean': "%.4g" % np.mean(timeseries[start_hour:start_hour+24]),
                         'std': "%.4g" % np.std(timeseries[start_hour:start_hour+24])}

    dict168[group] = {'min': "%.4g" % np.min(timeseries[start_hour:start_hour+168]),
                         'max': "%.4g" % np.max(timeseries[start_hour:start_hour+168]),
                         'mean': "%.4g" % np.mean(timeseries[start_hour:start_hour+168]),
                         'std': "%.4g" % np.std(timeseries[start_hour:start_hour+168])}

    return dict24, dict168

def make_forcing_statistics(path, GridX, GridY, start_hour):
    files =[]
    for r, d, f in os.walk(path):
        for file in f:
            if '.hdf5' in file:
                files.append(os.path.join(r, file))
    stats24_dict = {'variable':{'mean':2, 'min':1, 'max':5, 'std':6}}
    stats168_dict = {'variable':{'mean':2, 'min':1, 'max':5, 'std':6}}

    for file in files:
        with h5py.File(file, 'r') as f:
            for group in list(f['Results'].keys()):
                timeseries = np.array([])
                for time in list(f['Results'][group].keys()):
                    if np.ndim(f['Results'][group][time][:]) == 3:
                        timeseries = np.append(timeseries, f['Results'][group][time][-1, GridX, GridY])
                    else:
                        timeseries = np.append(timeseries, f['Results'][group][time][GridX, GridY])
                stats24_dict, stats168_dict = add_to_dict(group, timeseries, stats24_dict, stats168_dict, start_hour)
                if group == 'wind velocity X':
                    windx = timeseries
                if group == 'wind velocity Y':
                    windy = timeseries
                if group == 'velocity U':
                    currentsu = timeseries
                if group == 'velocity V':
                    currentsv = timeseries
                if group == 'Stokes U':
                    stokesu = timeseries
                if group == 'Stokes V':
                    stokesv = timeseries

    windspeed, winddir = wind_speed_dir(windx, windy)
    stats24_dict, stats168_dict = add_to_dict('wind speed', windspeed, stats24_dict, stats168_dict, start_hour)
    stats24_dict, stats168_dict = add_to_dict('wind direction', winddir, stats24_dict, stats168_dict, start_hour)

    currentsspeed, currentsdir = wind_speed_dir(currentsu, currentsv)
    stats24_dict, stats168_dict = add_to_dict('currents speed', currentsspeed, stats24_dict, stats168_dict, start_hour)
    stats24_dict, stats168_dict = add_to_dict('currents direction', currentsdir, stats24_dict, stats168_dict, start_hour)
    
    stokesspeed, stokesdir = wind_speed_dir(stokesu, stokesv)
    stats24_dict, stats168_dict = add_to_dict('stokes speed', stokesspeed, stats24_dict, stats168_dict, start_hour)
    stats24_dict, stats168_dict = add_to_dict('stokes direction', stokesdir, stats24_dict, stats168_dict, start_hour)
    
    del stats24_dict['variable']
    del stats168_dict['variable']
    
    with open(path + '24h_forcing_stats.yaml', 'w') as outfile:
        yaml.dump(stats24_dict,outfile, default_flow_style=False)

    with open(path + '168h_forcing_stats.yaml', 'w') as outfile:
        yaml.dump(stats168_dict, outfile, default_flow_style=False)

    
make_forcing_statistics('/ocean/vdo/MIDOSS/mohid-forcing/zero_winds/04jan20-11jan20/', 249, 342, 2)
