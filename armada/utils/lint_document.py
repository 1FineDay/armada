# Copyright 2017 The Armada Authors.
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

RELEASE_KEYWORD = 'release'
PREFIX_KEYWORD = 'release_prefix'


import yaml

def validate_armada_documents(file):
    documents = yaml.safe_load_all()
    validate_manifest_document(documents)
    validate_chart_group_document(documents)
    validate_chart_document(documents)

def validate_manifest_document(documents):
    manifest_documents = []
    for document in documents:
        if document.get('schema') == 'armada/Manifest/v1':
            manifest_documents.append(document)
            manifest_data = document.get('data')
            if not manifest_data.get(RELEASE_KEYWORD, False):
                raise Exception('Missing %s keyword in manifest',
                                RELEASE_KEYWORD)
            if not isinstance(manifest_data.get('chart_groups'),
                              list) and not manifest_data.get(
                                  'chart_groups', False):
                raise Exception('Missing %s values. Expecting a list type')

        if len(manifest_documents) > 1:
            raise Exception('Schema %s must be uniqe. please check for '
                            'multiple definitions', 'armada/Manifest/v1')

def validate_chart_group_document(documents):
    for document in documents:
        if document.get('schema') == 'armada/ChartGroup/v1':
            manifest_data = document.get('data')
            if not isinstance(manifest_data.get('chart_group'),
                              list) and not manifest_data.get(
                                  'chart_group', False):
                raise Exception('Missing %s values. Expecting a list type')

def validate_chart_document(documents):
    for document in documents:
        if document.get('schema') == 'armada/Chart/v1':
            manifest_data = document.get('data')
            if not isinstance(manifest_data.get(RELEASE_KEYWORD),
                              basestring) and not manifest_data.get(
                                  RELEASE_KEYWORD, False):
                raise Exception(
                    'Missing %s values. Expecting a list type',
                    RELEASE_KEYWORD, document.get('metadata').get('name'))
