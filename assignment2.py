#!user/bin/env python
# -*- coding: utf-8 -*-
"""Part 1"""

import urllib2

def downloadData(url):
    """fetches info from a url.
    Args:
        url (srt): url address of website
    Returns:
        fetches website info
    Example:
        downloadData(www.facebook.com)
    """
    response = urllib2.urlopon(url)
    html = response.read()