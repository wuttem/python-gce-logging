import logging
from flask import request
from pythongcelogging import GCEFormatter

formatter = GCEFormatter("myservice", "v1.2")
# Register Flask request context
formatter.use_flask_request(request)
# Register User getter
formatter.set_user_getter(lambda: "myuser")

json_handler = logging.StreamHandler()
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

# Provide Attributes
logger.info('Sign up', extra={'method': '52d6ce', 'url': "http://hooli.xyz", "user": "xyz"})

# Error reporting
try:
    raise ValueError('something')
except ValueError:
    logger.error('error', exc_info=True, extra={"response_code": 500})