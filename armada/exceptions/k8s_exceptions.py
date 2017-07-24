#Copyright 2017 The Armada Authors.
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

class KubernetesException(exception_client.ExceptionClient):
    '''Base class for the k8s handler exception and error handling.'''

    message = 'An unknown Kubernetes handler error occured.'

class KubeConfigException(exception_client.ExceptionClient):
    '''Exception that occurs when there is an error loading the Kube config file.'''
	

	message  = 'There was an error loading the Kubernetes config file.'
