import json
from datetime import datetime
from functools import wraps
from flask import g, request, redirect, url_for, jsonify

from funcs.string import str_equals, is_str_empty, sanitize

class RouteDecorators:
    
    @staticmethod
    def admin_key_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'key' in request.args:
                keystr = sanitize(request.args.get('key', default=None, type=str))

            else:
                return jsonify({
                    "response_code": 505,
                    "response_message": "Missing argument(s)."
                })

            if keystr is None:
                return jsonify({
                    "response_code": 605,
                    "response_message": "Missing argument(s). Null values."
                })

            with open("data/admin_keys.json") as e:
                data = json.load(e)

            if keystr not in data["admin_keys"]:
                return jsonify({
                    "response_code": 303,
                    "response_message": "Invalid key."
                })

            return f(*args, **kwargs)
        return decorated_function
    
    @staticmethod
    def log(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            current_date = datetime.now().strftime("%B %d, %Y %I:%M%p")
            arguments = ""

            for x,y in request.args.items():
                arguments += f"[{x} - {y}]"

            print(f"[{request.remote_addr}] Accessed {request.path} with args {arguments} on {current_date}")

            return f(*args, **kwargs)
        return decorated_function
    
    @staticmethod
    def validate_request(f): # check for the secret useragent and public api key
        @wraps(f)
        def decorated_function(*args, **kwargs):
            #try:
            #    #data = request.args.items()
            #    #
            #    #for (x,y) in data:
            #    #    if y is None or y == "" or x is None or x == "":
            #    #        return jsonify({
            #    #            "response_code": 303,
            #    #            "response_message": "Request is missing arguments."
            #    #        })
#
            #    #secret_key = request.args.get("secret")
##
            #    #if not str_equals(secret_key, "faggotassnigger"):
            #    #    return jsonify({
            #    #            "response_code": 303,
            #    #            "response_message": "Secret key missing."
            #    #        })
            #    #        
            #    #if not str_equals(request.user_agent.string, "APSDFISUSDFPESDFGR23DSFG8957623FSDGGFDSG8975623895T982375TOBWD87FG"):
            #    #    return jsonify({
            #    #            "response_code": 303,
            #    #            "response_message": "User-Agent missmatch."
            #    #        })
#
            #except:
            #    return jsonify({
            #        "response_code": 303,
            #        "response_message": "Error validating request."
            #    })

            return f(*args, **kwargs)
        return decorated_function
    
    @staticmethod
    def blacklist_check():
        pass # check for blacklisted useragent / ip / hwid
    