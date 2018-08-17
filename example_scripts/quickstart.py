#!/usr/bin/env python3

from __future__ import print_function

import sys
import plotbar


def main():

    test_data = {'A':1, 'B':2}
    file_name = '../example_plots/test.html'

    pb = plotbar.hub.Hub()
    plotbar.plot.barplot(
        test_data,
        file_name,
        'plotly'
    )
    return

if __name__ == '__main__':
    main( )
