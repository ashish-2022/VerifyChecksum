#!/bin/python

import hashlib
import os
import sys

match=1

if len(sys.argv) < 2:
    sys.exit('Usage: %s filename' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: File "%s" was not found!' % sys.argv[1])

eSHA1 = raw_input('Expected SHA1: ')
eSHA256 = raw_input('Expected SHA256: ')
eMD5 = raw_input('Expected MD5: ')

with open(sys.argv[1], 'rb') as f:
    contents = f.read()
    aSHA1 = hashlib.sha1(contents).hexdigest()
    aSHA256 = hashlib.sha256(contents).hexdigest()
    #md5 accepts only chunks of 128*N bytes
    md5 = hashlib.md5()
    for i in range(0, len(contents), 8192):
        md5.update(contents[i:i+8192])
    aMD5 = md5.hexdigest()

print "\n------------------------------------------------------------------------"
print "RESULTS:"
print "------------------------------------------------------------------------"
if eSHA1 == aSHA1:
    print "SHA1   PASS"
else:
    print "SHA1   FAIL"
    print "Actual: "+aSHA1
    match=0

if eSHA256 == aSHA256:
    print "SHA256 PASS"
else:
    print "SHA256 FAIL"
    print "Actual: "+aSHA256
    match=0

if eMD5 == aMD5:
    print "MD5    PASS"
else:
    print "MD5    FAIL"
    print "Actual: "+aMD5
    match=0

if match == 0:
    print "Verification failed, values does not match"
else:
    print "Verification Successful"

