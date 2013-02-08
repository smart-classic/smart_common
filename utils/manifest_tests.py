'''Module providing manifest tests for the SMART API Verifier'''
# Developed by: Nikolai Schwertner
#
# Revision history:
#     2012-05-14 Initial release

# Standard module imports
from jsonschema import Draft3Validator

URLPATTERN = "^[\w\-_]+\://([a-zA-Z0-9\-\.]+(:[a-zA-Z0-9]*)?)?/?([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~])*[^\.\,\)\(\s]$"
  
def app_manifest_structure_validator (manifest):
    '''A structure test for an app manifest's JSON'''
    
    messages = []
    schema = {
            "type":"object",
            "properties":{
                "author": {
                    "type":"string"
                },
                "description": {
                    "type":"string",
                    "required":True
                },
                "icon": {
                    "type":"string",
                    "pattern":URLPATTERN
                },
                "id": {
                    "type":"string",
                    "required":True
                },
                "index": {
                    "type":"string",
                    "pattern":URLPATTERN
                },
                "oauth_callback": {
                    "type":"string",
                    "pattern":URLPATTERN
                },
                "mode": {
                    "type":"string",
                    "enum":["ui","background","frame_ui"],
                    "required":True
                },
                "name": {
                    "type":"string",
                    "required":True
                },
                "optimalBrowserEnvironments": {
                    "type":"array",
                    "items":{
                            "type":"string",
                            "enum":["desktop","tablet","mobile"]
                    },
                    "uniqueItems":True
                },
                "requires": {
                    "type":"object",
                    "patternProperties": {
                        URLPATTERN: {
                            "type":"object",
                            "properties":{
                                "codes":{
                                    "type":"array",
                                    "items":{
                                            "type":"string",
                                            "pattern":URLPATTERN
                                    },
                                    "uniqueItems":True
                                },
                                "methods":{
                                    "type":"array",
                                    "items":{
                                            "type":"string",
                                            "enum":["GET","PUT","POST","DELETE"]
                                    },
                                    "uniqueItems":True
                                }
                            },
                            "additionalProperties":False
                        }
                    },
                    "additionalProperties":False
                },
                "scope": {
                    "type":"string",
                    "enum":["record"]
                },
                "smart_version": {
                    "type":"string",
                    "pattern":"^[\d]+(?:\.[\d]+){0,2}$"
                },
                "supportedBrowserEnvironments": {
                    "type":"array",
                    "items": {
                        "type":"string",
                        "enum":["desktop","tablet","mobile"]
                    },
                    "uniqueItems":True
                },
                "version": {
                    "type":"string"
                }
            },
            "additionalProperties":False
        }
        
    v = Draft3Validator(schema)
    for error in sorted(v.iter_errors(manifest), key=str):
        messages.append(str(error))
     
    # custom validation (not possible with JSON Schema)
    if len(messages) == 0:
        keys = manifest.keys()

        if manifest["mode"] in ("ui","frame_ui"):
            if "icon" not in keys:
                messages.append ("There should be an 'icon' propery for non-background apps")
            if "index" not in keys:
                messages.append ("There should be an 'index' propery for non-background apps")
        elif manifest["mode"] == "background":
            if "index" in keys or "oauth_callback" in keys or "optimalBrowserEnvironments" in keys or "supportedBrowserEnvironments" in keys:
                messages.append ("Background apps should not have 'index', 'oauth_callback', 'supportedBrowserEnvironments', or 'optimalBrowserEnvironments' properties in their manifest")

    return messages
    
def container_manifest_structure_validator (manifest):
    '''A structure test for a container manifest's JSON'''
    
    messages = []
    schema = {
        "type":"object",
        "properties":{
            "admin": {
                "type":"string",
                "required":True
            },
            "api_base": {
                "type":"string",
                "pattern":URLPATTERN,
                "required":True
            },
            "capabilities": {
                "type":"object",
                "required":True,
                "patternProperties": {
                    URLPATTERN: {
                        "type":"object",
                        "properties":{
                            "codes":{
                                "type":"array",
                                "items":{
                                        "type":"string",
                                        "pattern":URLPATTERN
                                },
                                "uniqueItems":True
                            },
                            "methods":{
                                "type":"array",
                                "items":{
                                        "type":"string",
                                        "enum":["GET","PUT","POST","DELETE"]
                                },
                                "uniqueItems":True
                            }
                        },
                        "additionalProperties":False
                    }
                },
                "additionalProperties":False
            },
            "description": {
                "type":"string",
                "required":True
            },
            "launch_urls": {
                "type":"object",
                "required":True,
                "properties":{
                    "authorize_token": {
                        "type":"string",
                        "pattern":URLPATTERN,
                        "required":True
                    },
                    "exchange_token": {
                        "type":"string",
                        "pattern":URLPATTERN,
                        "required":True
                    },
                    "request_token": {
                        "type":"string",
                        "pattern":URLPATTERN,
                        "required":True
                    }
                },
                "additionalProperties":False
            },
            "name": {
                "type":"string",
                "required":True
            },
            "smart_version": {
                "type":"string",
                "pattern":"^[\d]+(?:\.[\d]+){0,2}$",
                "required":True
            }
        },
        "additionalProperties":False
    }
        
    v = Draft3Validator(schema)
    for error in sorted(v.iter_errors(manifest), key=str):
        messages.append(str(error))

    return messages
