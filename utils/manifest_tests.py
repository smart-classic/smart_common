'''Module providing manifest tests for the SMART API Verifier'''
# Developed by: Nikolai Schwertner
#
# Revision history:
#     2012-05-14 Initial release

# Standard module imports
from jsonschema import Draft3Validator
import string
import re

def isurl (str):
    if isinstance(str, basestring) and (str.startswith("http://") or str.startswith("https://")):
        return True
    else:
        return False
  
def app_manifest_structure_validator (manifest):
    '''A structure test for an app manifest's JSON'''
    
    messages = []
    schema = {
            "type":"object",
            "$schema": "http://json-schema.org/draft-03/schema",
            "id": "#",
            "required":False,
            "properties":{
                "author": {
                    "type":"string",
                    "id": "author",
                    "required":False
                },
                "description": {
                    "type":"string",
                    "id": "description",
                    "required":True
                },
                "icon": {
                    "type":"string",
                    "id": "icon",
                    "required":False
                },
                "id": {
                    "type":"string",
                    "id": "id",
                    "required":True
                },
                "index": {
                    "type":"string",
                    "id": "index",
                    "required":False
                },
                "mode": {
                    "type":"string",
                    "enum" : ["ui","background","frame_ui"],
                    "id": "mode",
                    "required":True
                },
                "name": {
                    "type":"string",
                    "id": "name",
                    "required":True
                },
                "optimalBrowserEnvironments": {
                    "type":"array",
                    "id": "optimalBrowserEnvironments",
                    "required":False,
                    "items":
                        {
                            "type":"string",
                            "id": "0",
                            "required":False
                        }
                    

                },
                "requires": {
                    "type":"object",
                    "id": "requires",
                    "required":False
                },
                "scope": {
                    "type":"string",
                    "id": "scope",
                    "required":False
                },
                "smart_version": {
                    "type":"string",
                    "id": "smart_version",
                    "required":False
                },
                "supportedBrowserEnvironments": {
                    "type":"array",
                    "id": "supportedBrowserEnvironments",
                    "required":False,
                    "items":
                        {
                            "type":"string",
                            "id": "0",
                            "required":False
                        }
                    

                },
                "version": {
                    "type":"string",
                    "id": "version",
                    "required":False
                }
            }
        }
        
    v = Draft3Validator(schema)
    for error in sorted(v.iter_errors(manifest), key=str):
        messages.append(str(error))

    return messages
    
def container_manifest_structure_validator (manifest):
    '''A structure test for a container manifest's JSON'''
    
    messages = []
    schema = {
        "type":"object",
        "$schema": "http://json-schema.org/draft-03/schema",
        "id": "#",
        "required":False,
        "properties":{
            "admin": {
                "type":"string",
                "id": "admin",
                "required":True
            },
            "api_base": {
                "type":"string",
                "id": "api_base",
                "required":True
            },
            "capabilities": {
                "type":"object",
                "id": "capabilities",
                "required":True,
            },
            "description": {
                "type":"string",
                "id": "description",
                "required":True
            },
            "launch_urls": {
                "type":"object",
                "id": "launch_urls",
                "required":True,
                "properties":{
                    "authorize_token": {
                        "type":"string",
                        "id": "authorize_token",
                        "required":True
                    },
                    "exchange_token": {
                        "type":"string",
                        "id": "exchange_token",
                        "required":True
                    },
                    "request_token": {
                        "type":"string",
                        "id": "request_token",
                        "required":True
                    }
                }
            },
            "name": {
                "type":"string",
                "id": "name",
                "required":True
            },
            "smart_version": {
                "type":"string",
                "id": "smart_version",
                "required":True
            }
        }
    }
        
    v = Draft3Validator(schema)
    for error in sorted(v.iter_errors(manifest), key=str):
        messages.append(str(error))

    return messages