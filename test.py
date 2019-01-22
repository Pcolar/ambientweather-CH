#!/usr/bin/python
""" Ambient Weather to CSV """

from python_library import *

import csv
import json
import requests
import sys
import importlib
# parameter file including access keys
## needed due to '-' in import filename
test_secrets = importlib.import_module("test-secrets")

# initialize local variables
json_messages={}
result_d={}
response=""
rec_count=0
output_filename="ambient_CH_"+datetime.datetime.now().strftime("%Y%m%d%H%M")+".csv"

# Set CSV Header & line format
csv_header = ['Temperature (F)','Humidity (%)','Wind Speed (mph)','Wind Gust (mph)','Daily Rainfall Totals (in)','Monthly Rainfall Totals (in)','Yearly Rainfall Totals (in)','UV Radiation Index','Date/Time']
csv_output_elements = [u'tempf',u'humidity',u'windspeedmph',u'windgustmph',u'dailyrainin',u'monthlyrainin',u'yearlyrainin',u'uv',u'date']

# construct api parameters
## Consider moving the URL into test_secrets
url="https://api.ambientweather.net/v1/devices/" + test_secrets.macAddress
api_key="?apiKey="
app_key="&applicationKey="

# number of records to retrieve
## Consider moving this into test_secrets
app_limit="&limit=21"

# build querystring
api_querystring=api_key + test_secrets.apiKey + app_key + test_secrets.appKey + app_limit
api_headers={'Content-Type': 'application/json','Accept': 'application/json'}

# Retrieve content from API
#log_message("sending: " + url + api_querystring)
try:
   response = requests.get(url + api_querystring, headers=api_headers)
except:
   json_messages['message'] = "get request failed"
   json_messages['exit status'] = "error"
   log_json_message(json_messages)
   exit(1)

if response.status_code != 200:
   if response.status_code == 429:
	json_messages['message'] = "API Limit Exceeded"
        json_messages['return_code'] = response.status
        json_messages['exit status'] = "warning"
   else:
	json_messages['message'] = "Retrieval failed"
        json_messages['return_code'] = response.status_code
        json_messages['url'] = url + api_querystring
        json_messages['exit status'] = "error"
   log_json_message(json_messages)
   exit(1)

# load content
result_set=json.loads(response.text)
json_messages['records retrieved'] = len(result_set)
if len(result_set) == 0:
   json_messages['message'] = "No content retrieved"
   json_messages['exit status'] = "error"
   log_json_message(json_messages)
   exit(1)

# create output file & write header row
try:
   output_file = open(output_filename, 'w')
   csvwriter = csv.writer(output_file, dialect='excel')
except:
   json_messages['message'] = "Output file creation failed"
   json_messages['exit status'] = "error"
   log_json_message(json_messages)
   exit(1)

csvwriter.writerow(csv_header)


# ETL processing result set
for i in range(0, len(result_set)):
   # convert to a Dict for key lookup
   result_d=result_set[i]
   # Translate temperature
   if result_d[u'tempf'] < 60:
     result_d[u'tempf']="Too cold"
   elif result_d[u'tempf']  > 85:
     result_d[u'tempf']="Too hot"
   else:
     result_d[u'tempf']="Goldilocks"
   # build the output values in key order
   csv_output=['null']*len(csv_output_elements)
   j=0
   for key in csv_output_elements:
     csv_output[j]=result_d[key]
     j +=1
   csvwriter.writerow(csv_output)
   rec_count += 1

# cleanup and exit
output_file.close()
json_messages['rows exported'] = rec_count
json_messages['output file'] = output_filename
json_messages['exit status'] = "normal"
log_json_message(json_messages)

exit(0)
