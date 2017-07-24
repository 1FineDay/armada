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
#

import json
from falcon import HTTP_200, HTTP_404

from armada import api
from armada.utils.lint import validate_manifest

class Validate(api.BaseResource):
    '''
    apply armada endpoint service
    '''

    def on_post(self, req, resp):
        try:
            message = {
                'valid': validate_manifest(open(self.req_json(req)))
            }

            if message.get('valid'):
                resp.data = json.dumps(message)
                resp.status = HTTP_200

            resp.content_type = 'application/json'

        except Exception:
            self.error(req.contex, "Failed: Invalid Armada Manifest")
            self.return_error(
                resp,
                HTTP_404,
                message="Failed: Invalid Armada Manifest"
            )
