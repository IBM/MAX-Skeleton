#
# Copyright 2018-2019 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

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
