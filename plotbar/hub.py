#!/usr/bin/env python3

from __future__ import print_function

import sys
import glob

# import rpy2.robjects as robjects
# from rpy2.robjects import r

import plotly


class Hub():
    def __init__(self, params = None):
        """
        Python plot interface to plotting modules

        Could hold functions for folder creation file path generation etc.

        Coudl provide defaults for all plot functions, e.g. which plot library
        to use
        """
        print(
            'Initialized plotbar'
        )
        self.params = {}
        if params is not None:
            self.update_params( params )
        else:
            pass

        return


    # def update_params(self, params):
    #     for k, v in params.items():
    #         if k.startswith('_'):
    #             continue
    #         if k not in self.params.keys():
    #             self.print_info(
    #                 'Unknown new parameter {0} set to {1}'.format(
    #                     k,
    #                     v
    #                 )
    #             )
    #             self.params[ k ] = v
    #         elif self.params[ k ] != v:
    #             self.print_info(
    #                 'Updated parameter: {0} to {1} (Former: {2})'.format(
    #                     k,
    #                     v,
    #                     self.params[k]
    #                 )
    #             )
    #             self.params[ k ] = v
    #         else:
    #             pass
    #     return


if __name__ == '__main__':
    print(__doc__)
