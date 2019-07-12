#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 06:06:21 2019

@author: kafayat
"""
#import os
import panda as pd
import netCDF4 
#from ncdump import ncdump
import numpy as np
import matplotlib.pyplot as plt
import glob
import datetime as dt  # Python standard library datetime  module
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid


#def ncdump(data, verb=True):
##    '''
##    ncdump outputs dimensions, variables and their attribute information.
##    The information is similar to that of NCAR's ncdump utility.
##    ncdump requires a valid instance of Dataset.
##
##    Parameters
##    ----------
##    nc_fid : netCDF4.Dataset
##        A netCDF4 dateset object
##    verb : Boolean
##        whether or not nc_attrs, nc_dims, and nc_vars are printed
##
##    Returns
##    -------
##    nc_attrs : list
##        A Python list of the NetCDF file global attributes
##    nc_dims : list
##        A Python list of the NetCDF file dimensions
##    nc_vars : list
##        A Python list of the NetCDF file variables
##    '''
#    def print_ncattr(key):
##        """
##        Prints the NetCDF file attributes for a given key
##
##        Parameters
##        ----------
##        key : unicode
##            a valid netCDF4.Dataset.variables key
##        """
#        try:
#            print "\t\ttype:", repr(data.variables[key].dtype)
#            for ncattr in data.variables[key].ncattrs():
#                print '\t\t%s:' % ncattr,\
#                      repr(data.variables[key].getncattr(ncattr))
#        except KeyError:
#            print "\t\tWARNING: %s does not contain variable attributes" % key
#
#    # NetCDF global attributes
#    nc_attrs = data.ncattrs()
#    if verb:
#        print "NetCDF Global Attributes:"
#        for nc_attr in nc_attrs:
#            print '\t%s:' % nc_attr, repr(data.getncattr(nc_attr))
#    nc_dims = [dim for dim in data.dimensions]  # list of nc dimensions
#    # Dimension shape information.
#    if verb:
#        print "NetCDF dimension information:"
#        for dim in nc_dims:
#            print "\tName:", dim 
#            print "\t\tsize:", len(data.dimensions[dim])
#            print_ncattr(dim)
#    # Variable information.
#    nc_vars = [var for var in data.variables]  # list of nc variables
#    if verb:
#        print "NetCDF variable information:"
#        for var in nc_vars:
#            if var not in nc_dims:
#                print '\tName:', var
#                print "\t\tdimensions:", data.variables[var].dimensions
#                print "\t\tsize:", data.variables[var].size
#                print_ncattr(var)
#    return nc_attrs, nc_dims, nc_vars
#import os
#def main():
#    data=os.listdir("/Volumes/Seagate/sgpmpl00")
#    for f in data:
#        if os.path.isfile(f):
#            rem=netCDF4.Dataset("f")
    #data = netcdf.Dataset('/Volumes/Seagate/sgpmpl00/sgp30smplcmask1zwangC1c120000101000021.cdf','r')

    data=Dataset('/Users/kafayat/Desktop/bsgpmpl2000/sgp30smplcmask1zwangC1.c1.20000710.000004.cdf','r')
   # nc_attrs, nc_dims, nc_vars = ncdump(data)
    basetime=data.variables["base_time"]
    #cbh=data.variables["Cloud_base"]
   # ctb=data.variable["Cloud_top"]
    height=data.variables["height"]
    backscatter=data.variable["backscatter"]
    #print(basetime[:])
    print(basetime[:])

    #print(data.variables["time_offset"][:])
    #print(data.variables["time_offset"][0])
    #print(data.variables["time_offset"][:])
#main()
    #print(data.variables["time"])
    #print(hubc.variables["time"][0])
   # print(data.variables["time_offset"][:]) #[:] says show all data
#data=open("/Volumes/Seagate/AEROSE\ XII/microtops_03042019.txt " ,'r')


# Get a list of all .nc files available in different folders
    #filenames = glob.glob("/Volumes/Seagate/sgpmpl00/sgp30smpl*.cdf")

    #dsmerged = os.Dataset(filenames)
#nc=Dataset(data,'r')
#vn=nc.MFDataset('sgp30smpl*.cdf') 

   # print(dsmerged.variables["time"][:])
#['time','base_time']
# read multiple files (wildcard)
#vn = nc.MFDataset('sgp30smpl*.cdf') 
#l=len(vn)
#os.chdir(data)  # Provide the new path here
#jk
#f = MFDataset(data,'sgp30smpl*.cdf','w')
#print f.variables["time_offset"][:]
#datas = Dataset(data,'r',format='NETCDF4')
# create a file (Dataset object, also the root group).
#cdf = pycdf.CDF('/Users/kafayat/Desktop/bsgpmpl2000')
#rootgrp = Dataset('/Users/kafayat/Desktop/bsgpmpl2000', 'r', format='NETCDF4')
#f = Dataset('sgp30smpl*.nc')
#time = f.variables['time_offset']
#print(rootgrp.file_format)
#rootgrp.close()
#cdf = pycdf.CDF('/path/to/file.cdf')