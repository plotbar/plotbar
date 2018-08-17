#!/usr/bin/env python3

from __future__ import print_function

import sys
import glob
import plotbar.layouts
import plotbar.pbplotly
# import plotbar.pbrpy

'''
Could also be a class?
'''


def barplot(data, file_name, plot_lib, layout=None):
    '''

    '''
    if layout is None:
        layout = plotbar.layouts.DEFAULT_LAYOUT
    if plot_lib is None:
        plot_lib = 'plotly'

    if plot_lib == 'plotly':
        plotbar.pbplotly.plotly_barplot(
            data,
            file_name,
            layout
        )
    return


if __name__ == '__main__':
    print(__doc__)
