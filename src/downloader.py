# -*- coding: utf-8 -*-

import urllib.request
import shutil
import logging


def getFile(url,file_name):
    # Download the file from `url` and save it locally under `file_name`:
    try:
        with urllib.request.urlopen(url,timeout=10) as response, open(file_name,'wb') as out_file:
            logging.info('Downloading... '+url)
            shutil.copyfileobj(response, out_file)
    except Exception as err:  
        print("Failed to Download Threatlist from "+str(url)+" with Error "+str(err))
        logging.error('Download failed for '+str(url)+' with error: '+str(err))
