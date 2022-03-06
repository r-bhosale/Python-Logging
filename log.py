from datetime import datetime
import errno
from genericpath import exists
import logging
import os

filename = "log_" + datetime.now().strftime("%Y-%d-%m")
print(os.path)

#create folder
try:
    if not os.path.exists('Log'):
       os.makedirs("Log")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

#create logfile
try:
    if not os.path.exists("Log/"+filename):
        open("Log/"+filename,"w")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

logging.basicConfig(filename="Log/"+filename,level=logging.DEBUG,format='[%(asctime)s] %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
#logging.info('Log Entry Here.')