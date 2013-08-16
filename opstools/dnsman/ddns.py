#!/usr/bin/env python

import dns.update
import dns.tsigkeyring

key = "BksoRXYLfOcUla1fmwlfv0loL+B1ceqvAQpd/7DgEYzCRGQasbUxQZbP +BFlFkAHyvHOZS5LyMxpPywO6UOQKQ=="
keyring = dns.tsigkeyring.from_text({'keyname' : key})

def dman(zone, name, ttl, type, rr, delete=False):
    if type == 'cname' and len(rr) == 1:
        update = dns.update.Update(name, keyring=keyring)
        update.replace('host', ttl, type, rr)


#dman('111','abc',600,'cname',['192.168.1.1'] )
    
