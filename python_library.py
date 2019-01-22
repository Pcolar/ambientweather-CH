"""Python Library"""
__copyright__ = "Copyright (C) 2019 David Pcolar"
__license__ = "BSD Version 3 License"

import datetime
import os
import requests

# Loggily credentials are for djpcolar.loggily.com
# Normally loaded from a credentials file...
loggily_URI="http://logs-01.loggly.com/inputs/3f233490-d5c7-42f0-bdfb-c9d0a51888c6/tag/http/"

def log_message(message):
    """print out  in log message format"""
    print "%s:  %s" % (datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), message)

def log_json_message(log_message):
    """print out  in json tagged log message format"""
    log_message['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    print json.dumps(log_message)
    log_message={}

def loggily_json_message(log_message):
    """Push message to Loggily in json tagged log message format"""
    log_message['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    payload=json.dumps(log_message)
    response = requests.post(loggily_URI, data=payload)
    if response.status != 200:
        print response
    log_message={}

def get_uuidv4():
    """ Call service for UUID v4  """
    response = requests.get('https://www.uuidgenerator.net/api/version4')
    if response.status_code is 200:
      uuid=r.text
      log_message("UUID: " + uuid)
    return uuid

def load_from_environment(return_args, *argv):
# read content from environment variables
# environment arg names are passed as strings and returned in a dictionary.
# not found is returned as a null string

    for arg in argv:
       if  arg in os.environ:
          return_args[arg] = os.environ[arg]
#         print arg + " value is: " + return_args[arg]
       else:
          return_args[arg] = None
    return(0)

