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

import numpy
import xarray


class weighting_matrix:
    def __init__(self, path):
        weights_file = xarray.open_dataset(path)
        y, x, weights = weights_file.y, weights_file.x, weights_file.weights
        y1, y2, y3, y4 = (
            y.isel(index=0).values.astype(int),
            y.isel(index=1).values.astype(int),
            y.isel(index=2).values.astype(int),
            y.isel(index=3).values.astype(int),
        )
        x1, x2, x3, x4 = (
            x.isel(index=0).values.astype(int),
            x.isel(index=1).values.astype(int),
            x.isel(index=2).values.astype(int),
            x.isel(index=3).values.astype(int),
        )
        w1, w2, w3, w4 = (
            weights.isel(index=0).values,
            weights.isel(index=1).values,
            weights.isel(index=2).values,
            weights.isel(index=3).values,
        )
        self.y_indices = (y1, y2, y3, y4)
        self.x_indices = (x1, x2, x3, x4)
        self.weights = (w1, w2, w3, w4)


def hrdps(windarr, weighting_matrix_obj):
    shape = windarr.shape
    if len(shape) == 3:
        windarr = numpy.transpose(windarr, [1, 2, 0])
        new_grid = numpy.zeros([898, 398, shape[0]])
    elif len(shape) == 2:
        new_grid = numpy.zeros([898, 398])
    wind_y01, wind_y02, wind_y03, wind_y04 = weighting_matrix_obj.y_indices
    wind_x01, wind_x02, wind_x03, wind_x04 = weighting_matrix_obj.x_indices
    wind_wgt01, wind_wgt02, wind_wgt03, wind_wgt04 = weighting_matrix_obj.weights
    for i in range(898):
        for j in range(398):
            y1, y2, y3, y4 = (
                wind_y01[i][j],
                wind_y02[i][j],
                wind_y03[i][j],
                wind_y04[i][j],
            )
            x1, x2, x3, x4 = (
                wind_x01[i][j],
                wind_x02[i][j],
                wind_x03[i][j],
                wind_x04[i][j],
            )
            w1, w2, w3, w4 = (
                wind_wgt01[i][j],
                wind_wgt02[i][j],
                wind_wgt03[i][j],
                wind_wgt04[i][j],
            )
            s1 = windarr[y1][x1] * w1
            s2 = windarr[y2][x2] * w2
            s3 = windarr[y3][x3] * w3
            s4 = windarr[y4][x4] * w4
            new_grid[i][j] = s1 + s2 + s3 + s4
    new_grid = numpy.transpose(new_grid, [2, 0, 1])
    return new_grid


def wavewatch(wavewatcharr, weighting_matrix_obj):
    shape = wavewatcharr.shape
    ndims = len(shape)
    if ndims == 3:
        wavewatcharr = numpy.transpose(wavewatcharr, [1, 2, 0])
        new_grid = numpy.zeros([898, 398, shape[0]])
    elif ndims == 2:
        new_grid = numpy.zeros([898, 398])
    new_grid[:] = numpy.nan
    # do the inteprolation
    wave_y01, wave_y02, wave_y03, wave_y04 = weighting_matrix_obj.y_indices
    wave_x01, wave_x02, wave_x03, wave_x04 = weighting_matrix_obj.x_indices
    wave_wgt01, wave_wgt02, wave_wgt03, wave_wgt04 = weighting_matrix_obj.weights
    for i in range(898):
        for j in range(398):
            y1, y2, y3, y4 = (
                wave_y01[i][j],
                wave_y02[i][j],
                wave_y03[i][j],
                wave_y04[i][j],
            )
            x1, x2, x3, x4 = (
                wave_x01[i][j],
                wave_x02[i][j],
                wave_x03[i][j],
                wave_x04[i][j],
            )
            w1, w2, w3, w4 = (
                wave_wgt01[i][j],
                wave_wgt02[i][j],
                wave_wgt03[i][j],
                wave_wgt04[i][j],
            )
            if y1 == -9223372036854775808:
                s1 = False
            else:
                s1 = wavewatcharr[y1][x1] * w1
            if y2 == -9223372036854775808:
                s2 = False
            else:
                s2 = wavewatcharr[y2][x2] * w2
            if y3 == -9223372036854775808:
                s3 = False
            else:
                s3 = wavewatcharr[y3][x3] * w3
            if y4 == -9223372036854775808:
                s4 = False
            else:
                s4 = wavewatcharr[y4][x4] * w4
            array = []
            for element in (s1, s2, s3, s4):
                if type(element) is bool:
                    pass
                else:
                    array.append(element)
            if len(array) == 0:
                continue
            else:
                array = numpy.asarray(array)
                nansum = numpy.nansum(array, axis=0)
                new_grid[i][j] = nansum
    if ndims == 3:
        new_grid = numpy.transpose(new_grid, [2, 0, 1])
    return new_grid
