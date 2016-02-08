#!user/bin/env python
# -*- coding: utf-8 -*-
"""Part 1"""

import sys
import urllib2
import csv
import datetime
import logging
import argparse



def downloadData(url):
    """fetches info from a url.
    Args:
        url (srt): url address of website
    Returns:
        fetches website info
    Example:
        downloadData(www.facebook.com)
    """
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
    return html

def processData(urlcontent):
    """Processes data retrieved from CSV file from url.
    """
    cr = csv.reader(urlcontent)
    datadict = {}

    for row in cr:
        cust_id = row[0] #Assuming ID is first on spreadsheet, followed by name, b-day
        name = row[1]
        linecount = 1
        try:
            bday = datetime.datetime(row[2])
        except:
            logging.debug('Incorrect date format for entry')


        if cust_id not in datadict:
            datadict[cust_id] = (name, bday)
            linecount += 1

    return datadict

def displayPerson(id, personData):
    datadict = processData(personData)
    try:
        person_info = datadict.get(id, default=None)
    except:
        print "No user found with that ID"
    return "Person{} is {} with a birthday " \
           "of {}".format(id, person_info[0], person_info[1])

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-url', type=str)
        args = parser.parse_args()
        csvData = downloadData(args)
    except Exception:
        LOG_FILENAME = 'errors.log'
        logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
        logging.debug(("The following error occured: {}".format(Exception))
        sys.exit()
    personData = processData(csvData)
    return personData





