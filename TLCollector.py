'Log/ticollectorlog.log'# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:01:36 2019

@author: jdhillon
"""

import os, sys
import json
import src.parsers
import logging 
from src.downloader import getFile


def main():
    Configdata=load_config()
    i=1
    total_obj=len(Configdata['Threatlist'])
    for jsonblock in Configdata['Threatlist']:
        currentstatus=str("Data Collected for "+str(i)+"/"+str(total_obj)+" Threatlists")
        progress(i, total_obj, status=currentstatus)
        if(str(jsonblock['Enabled']).lower() == "true"):
            outputfile=(os.path.join(os.path.dirname(os.path.realpath(__file__)),"output","temp_"+jsonblock['OutputFile']))
           # print(outputfile)
           # sys.exit()
            if(jsonblock['Parser'].lower() == "ft_abuse_blocklist"):
                getFile(jsonblock['SourceFile'],outputfile)
                src.parsers.ft_abuse_blocklist(outputfile)
            elif(jsonblock['Parser'].lower() == "urlhaus_abuse_blockeddomainlist"):
                getFile(jsonblock['SourceFile'],outputfile)
                src.parsers.uh_abuse_blockeddlist(outputfile)
            elif(jsonblock['Parser'].lower() == "zeustracker_abuse_blockeddomainlist"):
                getFile(jsonblock['SourceFile'],outputfile)
            elif(jsonblock['Parser'].lower() == "zeustracker_abuse_blockediplist"):
                getFile(jsonblock['SourceFile'],outputfile)
                src.parsers.generic_parser(outputfile,6,0)
            elif(jsonblock['Parser'].lower() == "osint_bambenekconsulting"):
                getFile(jsonblock['SourceFile'],outputfile)
                src.parsers.osint_bambenekconsulting(outputfile,18,0)
            elif(jsonblock['Parser'].lower() == "phishtank_parser"):
                getFile(jsonblock['SourceFile'],outputfile)
                src.parsers.phishtank_parser(outputfile,1,0)
            elif(jsonblock['Parser'].lower() == "generic_parser_noedit"):
                getFile(jsonblock['SourceFile'],outputfile)
                src.parsers.generic_parser(outputfile,0,0)
            elif(jsonblock['Parser'].lower() == "generic_parser_1_0"):
                getFile(jsonblock['SourceFile'],outputfile)
                src.parsers.generic_parser(outputfile,1,0)
            else:
                print("####### NO parser Found #########  "+str(outputfile))
        i=i+1
    logging.info('Finished... ')
        

def load_config():
    try:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'Config.json'), 'r', encoding='utf8') as f:
            Configdata = json.load(f)
        return Configdata
    except Exception as err:
        print("Failed to read Configuration file with Error "+str(err))


def progress(count, total, status=''):
    bar_len = 50
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '#' * filled_len + ' ' * (bar_len - filled_len)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write('\n\n\t\t%s %s%s  %s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


    
if __name__ == "__main__":
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',  filemode='a', datefmt='%d-%b-%y %H:%M:%S', filename=os.path.join(os.path.dirname(os.path.realpath(__file__)),'Log','ticollectorlog.log'), level=logging.DEBUG)
    main() 
