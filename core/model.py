from maxfw.model import MAXModelWrapper

import logging
from config import DEFAULT_MODEL_PATH

logger = logging.getLogger()


class ModelWrapper(MAXModelWrapper):

    MODEL_META_DATA = {
        'id': 'ID',
        'name': 'MODEL NAME',
        'description': 'DESCRIPTION',
        'type': 'MODEL TYPE',
        'source': 'MODEL SOURCE',
        'license': 'LICENSE'
    }

    def __init__(self, path=DEFAULT_MODEL_PATH):
        logger.info('Loading model from: {}...'.format(path))

        # Load the graph

        # Set up instance variables and required inputs for inference

        logger.info('Loaded model')

    def _pre_process(self, inp):
        return inp

    def _post_process(self, result):
        return result

    def _predict(self, x):
        return x
