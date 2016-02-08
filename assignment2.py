#!user/bin/env python
# -*- coding: utf-8 -*-
"""Part 1"""

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
            logging.debug('Date in incorrect format')

        if cust_id not in datadict:
            datadict[cust_id] = (name, bday)
            linecount += 1

    return datadict

def displayPerson(id, personData):
    datadict = processData(personData)
    try:
        person_info = datadict.get(id)
    except:
        print "No user found with that ID"
    return datadict

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-url')
        args = parser.parse_args()



