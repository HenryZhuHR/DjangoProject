
METHOD_ERROR = {
    "error": {
        "error_code": 110,
        "error_msg": "Access token invalid or no longer valid"
    }
}


def NO_PARAM_GET_ERROR(param_name: str):
    return {
        "error": {
            "error_code": 11,
            "error_msg": 'no param %s get'%param_name
        }
    }
