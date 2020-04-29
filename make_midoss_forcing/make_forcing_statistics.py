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
    speed_dir = namedtuple('speed_dir', 'speed, dir')
    return speed_dir(speed, dir)

def make_zeds_to_multi(grid):
    dz = np.array(grid.variables['e3t_0'])
    dz = np.squeeze(dz)
    dz = dz[:,yind,xind]
    #print(dz)
    return(dz[0:4])

def make_forcing_statistics(path, GridX, GridY, grid_path=('/data/vdo/MEOPAR/grid/mesh_mask201702.nc', output):
    files =[]
    for r, d, f in os.walk(path):
        for file in f:
            if '.hdf5' in file:
                files.append(os.path.join(r, file))
    stats_dict = {'variable':{'mean':2, 'min':1, 'max':5, 'std':6}}
    
    with open(nc.Dataset(grid_path):
        zeds_to_multi = make_zeds_to_multi(grid)    

    for file in files:
        with h5py.File(file, 'r') as f:
            for group in list(f['Results'].keys()):
                timeseries = np.array([])
                for time in list(f['Results'][group].keys()):
                    if np.ndim(f['Results'][group][time][:]) == 3:
                        timeseries = np.append(timeseries, f['Results'][group][time][-1, GridX, GridY])
                    else:
                        timeseries = np.append(timeseries, f['Results'][group][time][GridX, GridY])
                stats_dict[group] = {'min': "%.4g" % np.min(timeseries),
                                     'max': "%.4g" % np.max(timeseries),
                                     'mean': "%.4g" % np.mean(timeseries), 
                                     'std': "%.4g" % np.std(timeseries)}
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
    stats_dict['wind speed'] = {'min': "%.4g" % np.min(windspeed),
                                'max': "%.4g" % np.max(windspeed),
                                'mean': "%.4g" % np.mean(windspeed),
                                'std': "%.4g" % np.std(windspeed)}
    stats_dict['wind direction'] = {'min': "%.4g" % np.min(winddir),
                                'max': "%.4g" % np.max(winddir),
                                'mean': "%.4g" % np.mean(winddir),
                                'std': "%.4g" % np.std(winddir)}

    currentsspeed, currentsdir = wind_speed_dir(currentsu, currentsv)
    stats_dict['currents speed'] = {'min': "%.4g" % np.min(currentsspeed),
                                    'max': "%.4g" % np.max(currentsspeed),
                                    'mean': "%.4g" % np.mean(currentsspeed),
                                    'std': "%.4g" % np.std(currentsspeed)}
     stats_dict['currents direction'] = {'min': "%.4g" % np.min(currentsdir),
                                    'max': "%.4g" % np.max(currentsdir),
                                    'mean': "%.4g" % np.mean(currentsdir),
                                    'std': "%.4g" % np.std(currentsdir)}
    stokesspeed, stokesdir = wind_speed_dir(stokesu, stokesv)
    stats_dict['stokes speed'] = {'min': "%.4g" % np.min(stokesspeed),
                                  'max': "%.4g" % np.max(stokesspeed),
                                  'mean': "%.4g" % np.mean(stokesspeed),
                                  'std': "%.4g" % np.std(stokesspeed)}
    stats_dict['stokes direction'] = {'min': "%.4g" % np.min(stokesdir),
                                  'max': "%.4g" % np.max(stokesdir),
                                  'mean': "%.4g" % np.mean(stokesdir),
                                  'std': "%.4g" % np.std(stokesdir)}    

    del stats_dict['variable']
    with open(output, 'w') as outfile:
        yaml.dump(stats_dict, outfile, default_flow_style=False)

    
#make_stats_file('/results2/MIDOSS/forcing/SalishSeaCast/MF0/21nov17-28nov17/', 249, 342, '/results2/MIDOSS/forcing/SalishSeaCast/MF0/21nov17-28nov17/stats.yaml')
