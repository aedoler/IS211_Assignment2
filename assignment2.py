#!user/bin/env python
# -*- coding: utf-8 -*-
"""Part 1"""

import urllib2
import urllib
import csv
import datetime
import logging

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
    filecontent = downloadData(urlcontent)
    cr = csv.reader(filecontent)
    datadict = {}
    try:
        for row in cr:
            cust_id = row[0] #Assuming ID is first on spreadsheet, followed by name, b-day
            name = row[1]
            bday = datetime.date(row[2])
            if cust_id not in datadict:
                datadict[cust_id] = (name, bday)
    except Exception:
        logging.basicConfig(filename='error.log',level=logging.DEBUG)
        logging.debug('Something was in the incorrect format')
    return datadict

def displayPerson(id, personData):
    process


print processData('http://winterolympicsmedals.com/medals.csv')

