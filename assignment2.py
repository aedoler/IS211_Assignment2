#!user/bin/env python
# -*- coding: utf-8 -*-
"""Part 1"""

import urllib2
import csv

def downloadData(url):
    """fetches info from a url.
    Args:
        url (srt): url address of website
    Returns:
        fetches website info
    Example:
        downloadData(www.facebook.com)
    """
    response = urllib2.urlopen(url)
    html = response.read()
    return html

def processData(url):
    filecontent = downloadData(url)
    cr = csv.reader(filecontent)
    return cr

print processData('http://winterolympicsmedals.com/medals.csv')

