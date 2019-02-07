# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'none'

# API metadata
API_TITLE = 'MAX'
API_DESC = 'An API for serving models'
API_VERSION = '0.1'

# default model
MODEL_NAME = ''
DEFAULT_MODEL_PATH = 'assets/{}'.format(MODEL_NAME)
