#!/bin/env python

import hmac, base64, hashlib
import struct, time, array, sys

def gen_hotpvalue(hmac_sha1):
    offset = int(hmac_sha1[-1], 16)
    bin_code = int(hmac_sha1[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
    hotpvalue = str(bin_code)
    return hotpvalue

def type_long_to_byte_array(long_num):
    byte_array = array.array('B')
    for i in reversed(range(0, 8)):
        byte_array.insert(0, long_num & 0xff)
        long_num >>= 8
    return byte_array

def get_hotp(key, counter, digits=6):
    b_counter = type_long_to_byte_array(counter)
    hmac_sha1 = hmac.new(key=key, msg=b_counter, digestmod=hashlib.sha1).hexdigest()
    return gen_hotpvalue(hmac_sha1)[-digits:]

def get_totp(key, digits=6, timelapse=30):
    counter = int(time.time() / timelapse)
    return get_hotp(key, counter, digits=digits)

secret = input('Enter a numerical key of 20 digits :\n')
nb = input('How many HOTP do you want :\n')
print("Your HOTP(s) :")
for i in range(1, int(nb) + 1):
    print(i, "-", get_hotp((int(secret)).to_bytes(10, byteorder='big'), i))
print("Your TOTP with 30sec timelapse :")
print(get_totp((int(secret)).to_bytes(10, byteorder='big')))
