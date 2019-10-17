import numpy as np
import os.path
import math
import sys

from util import check_required_dirs

###   
###  def get_directories():

modeldir  = os.environ["ENSO_MSE_WKDIR_MSE"]+"/model"   #wkdir, defined in ENSO_MSE.py

dirs_to_create = [ modeldir+"/PS",
                   modeldir+"/netCDF/ELNINO" ,
                   modeldir+"/netCDF/LANINA" ]


check_required_dirs( already_exist =[], create_if_nec = dirs_to_create, verbose=2) 
       
###  DRB: sym link to obs no longer necessary because everything is written/read to/from WKDIR


