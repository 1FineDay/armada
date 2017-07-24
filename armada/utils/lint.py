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

ARMADA_DEFINITION = 'armada'
RELEASE_PREFIX = 'release_prefix'
CHARTS_DEFINITION = 'charts'

from armada.exceptions import lint_exceptions

def valid_manifest(config):
    if not isinstance(config.get(ARMADA_DEFINITION, None), dict):
        raise InvalidArmadaObjectException()
    armada_config = config.get('armada')

    if not isinstance(armada_config.get(RELEASE_PREFIX), basestring):
	raise InvalidReleaseException()
    if not isinstance(armada_config.get(CHARTS_DEFINITION), list):
	raise InvalidChartDefinitionException()
    for group in armada_config.get('charts'):
        for chart in group.get('chart_group'):
            if not isinstance(chart.get('chart').get('name'), basestring):
		raise InvalidChartNameException()
    return True
