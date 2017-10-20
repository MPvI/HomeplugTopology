
from uuid import getnode
import urllib.request as urllib2
import json
import codecs

dic = {}
url = "http://macvendors.co/api/"

def get():
    return [int(hex(getnode())[i:i + 2], 16) for i in range(2, len(hex(getnode())), 2)]

def checkVendor(mac):
    oui = rawMacToString(mac[0:3])
    if oui not in dic:
        # print("Maybe the internet knows about " + rawMacToString(mac[0:3]) + "?")
        request = urllib2.Request(url + rawMacToString(mac), headers={'User-Agent': "API Browser"})
        response = urllib2.urlopen(request)
        reader = codecs.getreader("utf-8")
        obj = json.load(reader(response))
        if 'company' in obj['result']:
            dic[oui] = str(obj['result']['company'])
        else:
            dic[oui] = rawMacToString(mac[0:3])
    return dic[oui]

def getVendorMac(mac):
    return checkVendor(mac) + "_" + rawMacToString(mac[3:6])

def rawMacToString(mac):
    return codecs.encode(mac, 'hex').decode('utf-8')
