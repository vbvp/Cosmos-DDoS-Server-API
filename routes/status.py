import validation, datetime, paramiko, psutil
from flask import * 
from routes.decorators import RouteDecorators
from urllib.parse import urlparse

from funcs.string import str_equals, is_str_empty, sanitize

from funcs.validator import Validation

Status = Blueprint("Status", __name__)

@Status.route("/status", methods=["GET"])
@RouteDecorators.log
@RouteDecorators.admin_key_required
def status():
    return {
        "code": 200,
        "cpu": psutil.cpu_percent(),
        "used_ram": psutil.virtual_memory().percent,
        "unsued_ram": psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    }

    
        
