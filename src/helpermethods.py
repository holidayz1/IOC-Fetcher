# -*- coding: utf-8 -*-

import os
import logging
from pathlib import Path


def diff_dates(date1, date2):
    try: 
        return abs(date2-date1).days
    except Exception as e:
        logging.error(e)
        print(e)              
        

def trimfiles(inputfile,trim_lines_from_top,remove_last_lines):
    try:
        if(os.path.isfile(inputfile)):    
            lines = open(inputfile, 'r', encoding='utf-8').readlines() 
            opentempfile=os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'output','tempfile.csv')
            with open(opentempfile, 'w', encoding="utf-8") as f:
                if(remove_last_lines!=0):
                    f.writelines(lines[trim_lines_from_top:-remove_last_lines])
                else:
                    f.writelines(lines[trim_lines_from_top:])
            return opentempfile
        else:
            logging.error("No Files Found... ") 
    except Exception as e:
        logging.error("Trimfiles... "+str(e))
        print(e)
        
 
def write_file(inputfile,objlist):
    try: 
        outputfile=inputfile.replace('temp_','new_')     
        with open(outputfile, 'w', encoding="utf-8") as f:
            for item in objlist:
                f.write("%s\n" % item)
        f.close()
        filemgmnt(outputfile)
        cleanup(inputfile)
    except Exception as e:
        logging.error(e)
        print(e)


def cleanup(dfile):
    try:
        if os.path.exists(dfile):
            os.remove(dfile)
            logging.info('Deleting... '+dfile)
        else:
            print("The File  Doesn't exist")
    except Exception as e:
        logging.error("cleanup()..  "+str(e))
        print(e)


def filemgmnt(outputfile):
    try:
        currentfile=outputfile.replace('new_','')
        if (os.path.exists(currentfile)):
            oldfile1=os.path.join(Path(outputfile).parent,"old",str(os.path.basename(currentfile)).replace('.txt','1.txt'))
            if (os.path.exists(oldfile1)):
                oldfile2=oldfile1.replace('1.txt','2.txt')
                if(os.path.exists(oldfile2)):
                    oldfile3=oldfile2.replace('2.txt','3.txt')
                    if(os.path.exists(oldfile3)):
                        cleanup(oldfile3)
                    os.rename(oldfile2, oldfile3)
                os.rename(oldfile1, oldfile2)
            os.rename(currentfile, oldfile1)
        os.rename(outputfile, currentfile)
    except Exception as e:
        logging.error(e)
        print(e)                
       
