# django.core.handlers.wsgi.WSGIRequest


# Create your views here.
import json
import logging
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from common import ERROR

logger = logging.getLogger(__name__)

# POST test
def post_api(request:WSGIRequest):
    if not request.method=='POST':
        return JsonResponse(ERROR.METHOD_ERROR)
    
    json_data = json.loads(request.body.decode())

    if 'name' not in json_data:
        logger.error('got no param : name')
        return JsonResponse(ERROR.NO_PARAM_GET_ERROR('name'))

    return JsonResponse({
        'success':{
            'result':1024
        }
    })