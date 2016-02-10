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

    for linenumber, row in enumerate(cr):
        cust_id = str(row[0]) #Assuming ID is first on spreadsheet, followed by name, b-day
        name = str(row[1])
        try:
            bday = datetime.datetime.strptime(str(row[2]), '%b %d %Y %I:%M%p')
        except:
            logger.Assignment2('Error processing line %s for ID %s' % cust_id % linenumber)

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
    global logger = logging.getLogger('assignment2')
    logger.setLevel(logging.ERROR)
    fh = logging.FileHandler('error.log')
    fh.setLevel(logger.Error)
    logger.addHandler(fh)
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-url', type=str)
        args = parser.parse_args()
        csvData = downloadData(args)
    except Exception:
        sys.exit()
    personData = processData(csvData)


    return personData

if __name__ == '__main__':
    main()



