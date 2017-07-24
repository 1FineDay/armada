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

import exception_client

class ArmadaException(exception_client.ExceptionClient):
    '''Base class for Armada handler exception and error handling.'''

    message = 'An unknown Armada handler error occured.'

class UnknownChartSourceException(exception_client.ExceptionClient):
    '''Exception for unknown chart source type.'''

    def __init__(self, chart_name, source_type):
        self._chart_name = chart_name
        self._source_type = source_type

        self._message = 'Unknown source type \"' + self._source_type + '\" for \
                        chart \"' + self._chart_name + '\"'

        super(UnknownChartSourceException, self).__init__(self._message)

class PreFlightCheckException(exception_client.ExceptionClient):
	'''Generic Exception that occurs during Pre-Flight checks'''
	
class PostFlightOpsException(exception_client.ExceptionClient):
	'''Generic exception that occurs during the post-flight operations'''

	message = 'An error occured during the post flight operations.'	
