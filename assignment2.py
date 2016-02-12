#!user/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 2.
Input to calls program in terminal with argparse:
python assignment2.py --url
https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv
"""

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
handler = logging.FileHandler(LOG_FILENAME)
handler.setLevel(logging.ERROR)
logger.addHandler(handler)


def downloadData(url):
    """fetches info from a url.
    Args:
        url (srt): url address of website
    Returns:
        fetches website info
    Example:
        downloadData(www.facebook.com)
        :rtype: object
    """
    response = urllib2.urlopen(url)

    return response


def processData(csvData):
    """Processes data retrieved from CSV file from url.
    """
    cr = csv.reader(csvData)
    next(cr, None)
    format = '%d/%m/%Y'
    bday = 1
    datadict = {}

    for linenumber, row in enumerate(cr):
        cust_id = row[0]  # Assuming ID is first on spreadsheet, followed by name, b-day
        name = row[1]
        try:
            bday = datetime.datetime.strptime(row[2], format)
        except ValueError:
            logger.error('Error processing line {} for ID {}'.format(linenumber, cust_id))

        datadict[cust_id] = (name, bday)

    return datadict


def displayPerson(id, personData):
    """Returns person' data based on input ID
    """
    try:
        print "Person {} is {} with a birthday " \
              "of {}".format(id, personData[id][0], personData[id][1])
        main() # keep program running

    except:
        print "No user found with that ID, please try again"
        main() # keep program running


def main():
    """Allows for user input in command line with parser.
    :rtype: object
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    args = parser.parse_args()
    print args
    # urlinput = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    if args == None:
        sys.exit()
    csvData = downloadData(args.url)
    personData = processData(csvData)

    userinput = (raw_input('Please input an ID: '))
    while userinput <= 0:
        sys.exit()
    else:
        displayPerson(userinput, personData)


if __name__ == '__main__':
    main()
