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
from armada.handlers.tiller import Tiller

class Status(api.BaseResource):
    def on_get(self, req, resp):
        '''
        get tiller status
        '''
        try:
            message = {
                'tiller': Tiller().tiller_status()
            }

            if message.get('tiller'):
                resp.data = json.dumps(message)
                resp.status = HTTP_200
            else:
                resp.data = json.dumps(message)
                resp.status = HTTP_404

            resp.content_type = 'application/json'
        except Exception:
            self.error(req.contex, "Unable to find resources")
            self.return_error(
                resp,
                HTTP_404,
                message="Unable to find resources"
            )


class Release(api.BaseResource):
    def on_get(self, req, resp):
        '''
        get tiller releases
        '''

        try:
            # Get tiller releases
            handler = Tiller()
            releases = {}
            for release in handler.list_releases():
                releases[release.name] = release.namespace

            resp.data = json.dumps({'releases': releases})
            resp.content_type = 'application/json'
            resp.status = HTTP_200
        except Exception:
            self.error(req.contex, "Unable to find Armada Releases")
            self.return_error(
                resp,
                HTTP_404,
                message='Unable to find Armada Releases'
            )
