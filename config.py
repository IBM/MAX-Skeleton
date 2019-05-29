# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'none'

# API metadata
API_TITLE = 'MAX Model Name'
API_DESC = 'An API for serving models'
API_VERSION = '0.1'

# default model
MODEL_NAME = 'MAX Model Name'
DEFAULT_MODEL_PATH = 'assets/{}'.format(MODEL_NAME)

# the metadata of the model
MODEL_META_DATA = {
    'id': 'max-model-name',
    'name': 'MAX Model Name',
    'description': 'Describe the framework, training, and general implementation of the model.',
    'type': 'Model Type',
    'source': 'https://developer.ibm.com/exchanges/models/all/[MAX-MODEL-NAME]/',
    'license': 'Apache V2'
}
