# -*- coding: utf-8 -*-


import csv
import logging
from datetime import datetime, date
import src.helpermethods
import os


def generic_parser(inputfile,trim_lines_from_top,remove_last_lines):
    try:
        outlist = []
        if(os.path.exists(inputfile)):
            tempfile =  src.helpermethods.trimfiles(inputfile,trim_lines_from_top,remove_last_lines)
            with open(tempfile, 'r', newline='', encoding="utf-8") as csvFile:
                reader = csv.reader(csvFile)
                for row in reader:
                    outlist.append(row[0])
            csvFile.close()
            src.helpermethods.write_file(inputfile,outlist)
            src.helpermethods.cleanup(tempfile)
        else:
            logging.error("Generic_parser__ No Temp file..")
    except Exception as e:
        logging.error("Generic_parser__ "+str(e))
        print(e)   
    

def ft_abuse_blocklist(inputfile):
    try:
        if(os.path.exists(inputfile)):
            trim_lines_from_top=9
            remove_last_lines=1
            outlist = []
            tempfile= src.helpermethods.trimfiles(inputfile,trim_lines_from_top,remove_last_lines)
            Today_date = date.today()
            if(os.path.exists(tempfile)):
                with open(tempfile, 'r', newline='', encoding="utf-8") as csvFile:
                    reader = csv.reader(csvFile)
                    for row in reader:
                        try:
                            Lst_date1 = datetime.strptime(row[3], '%Y-%m-%d').date()
                            result1 = src.helpermethods.diff_dates(Today_date, Lst_date1)     
                            if(result1 > 7):
                                outlist.append(row[1])
                        except ValueError:
                            pass
                csvFile.close()
                src.helpermethods.write_file(inputfile,outlist)
                src.helpermethods.cleanup(tempfile)
            else:
                logging.error("ft_abuse_blocklist__ temp file missing")
    except Exception as e:
        logging.error("ft_abuse_blocklist()... "+str(e))
        print(e)
        
        
            

    
def uh_abuse_blockeddlist(inputfile):
    try:
        if(os.path.exists(inputfile)):
            trim_lines_from_top=9
            remove_last_lines=0
            outlist = []
            tempfile = src.helpermethods.trimfiles(inputfile,trim_lines_from_top,remove_last_lines)
            if(os.path.exists(tempfile)):
                with open(tempfile, 'r', newline='', encoding="utf-8") as csvFile:
                    reader = csv.reader(csvFile)
                    for row in reader:
                        try:
                            if(row[3] == 'online'):
                                outlist.append(row[2])
                        except ValueError:
                            pass
                csvFile.close()
                src.helpermethods.write_file(inputfile,outlist)
                src.helpermethods.cleanup(tempfile)
            else:
                logging.error("uh_abuse_blockeddlist__ No Temp file..")
    except Exception as e:
        logging.error("uh_abuse_blockeddlist()... "+str(e))
        print(e)         



def osint_bambenekconsulting(inputfile,trim_lines_from_top,remove_last_lines):
    try:
        outlist = []
        if(os.path.exists(inputfile)):
            tempfile =  src.helpermethods.trimfiles(inputfile,trim_lines_from_top,remove_last_lines)
            if(os.path.exists(tempfile)):
                with open(tempfile, 'r', newline='', encoding="utf-8") as csvFile:
                    reader = csv.reader(csvFile)
                    for row in reader:
                        try:
                            outlist.append(row[0])
                        except ValueError:
                            pass
                csvFile.close()
                src.helpermethods.write_file(inputfile,outlist)
                src.helpermethods.cleanup(tempfile)
            else:
                logging.error("osint_bambenekconsulting_parser__ No Temp file..")
    except Exception as e:
        logging.error("osint_bambenekconsulting_parser__ "+str(e))
        print(e) 



def phishtank_parser(inputfile,trim_lines_from_top,remove_last_lines):
    try:
        if(os.path.exists(inputfile)):
            outlist = []
            tempfile = src.helpermethods.trimfiles(inputfile,trim_lines_from_top,remove_last_lines)
            if(os.path.exists(tempfile)):
                with open(tempfile, 'r', newline='', encoding="utf-8") as csvFile:
                    reader = csv.reader(csvFile)
                    for row in reader:
                        try:
                            if(row[6] == 'yes'):
                                outlist.append(row[1])
                        except ValueError:
                            pass
                csvFile.close()
                src.helpermethods.write_file(inputfile,outlist)
                src.helpermethods.cleanup(tempfile)
            else:
                logging.error("Phistank_parser__ No Temp file..")
    except Exception as e:
        logging.error("Phistank_parser__  "+str(e))
        print(e)  