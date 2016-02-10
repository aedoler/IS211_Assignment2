#!user/bin/env python
# -*- coding: utf-8 -*-
"""Part 1"""

import sys
import urllib2
import csv
import datetime
import logging
import logging.handlers
import argparse

LOG_FILENAME = 'error.log'
logger = logging.getLogger('assignment2')
logger.setLevel(logging.ERROR)
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20,
                                               backupCount=5,
                                               )
logger.addHandler(handler)

def downloadData(url):
    """fetches info from a url.
    Args:
        url (srt): url address of website
    Returns:
        fetches website info
    Example:
        downloadData(www.facebook.com)
    """
    response = urllib2.urlopen(str(url))

    return response
﻿
def processData(csvData):
    """Processes data retrieved from CSV file from url.
    """
    cr = csv.reader(csvData)
    next(cr, None)
    format = '%d/%m/%Y'
    bday = 1
    datadict = {}

    for linenumber, row in enumerate(cr):
        cust_id = row[0] #Assuming ID is first on spreadsheet, followed by name, b-day
        name = row[1]
        try:
            bday = datetime.datetime.strptime(row[2], format)
        except TypeError:
            print('Error processing line {} for ID {}'.format(linenumber, cust_id))


        datadict[cust_id] = (name, bday)

    return datadict

def displayPerson(id, personData):

    try:
        personData.get(id, default=None)
    except:
        print "No user found with that ID"
    message = "Person{} is {} with a birthday " \
           "of {}".format(id, personData[id][0], personData[id][1])
    return message

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-url', type=str)
        args = parser.parse_args()
    except Exception:
        sys.exit()
    csvData = downloadData(args)
    personData = processData(csvData)

    userinput = int(raw_input('Please input an ID: '))
    while userinput <= 0:
        sys.exit()
    else:
        displayPerson(userinput, personData)

    return personData

if __name__ == '__main__':
    main()



