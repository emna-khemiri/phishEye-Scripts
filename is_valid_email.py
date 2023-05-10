# -*- coding: utf-8 -*-
"""is_valid_email

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zraiClqcOyfvS865ZrPv0OzQu-0aq7Pn
"""

import re
import email.utils
import dns.resolver
import dns.exception

# a function to check if an email address is valid and exists
def is_valid_email(email_address):
    # Use the parseaddr() function to extract the email address from the string
    address = email.utils.parseaddr(email_address)[1]

    # Use regular expressions to validate the format of the email address
    if not re.match(r"[^@]+@[^@]+\.[^@]+", address):
        return 0

    # Use dnspython to check if the domain in the email address exists and has MX records
    try:
        domain = address.split('@')[1]
        answers = dns.resolver.query(domain, 'MX',lifetime=120)
        return 1
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.exception.Timeout):
        return 0