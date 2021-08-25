#!/usr/bin/env python3

from jwcrypto import jws
import argparse
import zlib
import json

# get filename as first and only argument
parser = argparse.ArgumentParser(description="reads text file containing Quebec COVID-19 vaccination proof QR code raw data and returns readable content")
parser.add_argument('filename')
args = parser.parse_args()

rawdata = open(args.filename,"r").read()

header_removed = rawdata.replace("shc:/","")

parsed_chars = [header_removed[i:i+2] for i in range(0, len(header_removed), 2)]

parsed_text = ""
for char in parsed_chars:
    parsed_text = parsed_text + chr(int(char)+45)


jwstoken = jws.JWS()
jwstoken.deserialize(parsed_text)
# hack to extract payload without signature validation
# needed as we don't have the public key
payload = jwstoken.objects['payload']

# decompress with zlib header removed as per doc
decompressed_data = zlib.decompress(payload, -zlib.MAX_WBITS)
#print(decompressed_data)

parsed_json = json.loads(decompressed_data)
print(json.dumps(parsed_json, indent=4, sort_keys=True))