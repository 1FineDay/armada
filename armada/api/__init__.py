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

import json
import logging
import uuid

from falcon import request, HTTP_200

LOG = logging.getLogger(__name__)

class BaseResource(object):

    def __init__(self):
        self.authorized_roles = []

    def on_options(self, req, resp):
        self_attrs = dir(self)
        methods = ['GET', 'POST', 'DELETE']
        allowed_methods = []

        for m in methods:
            if 'on_{}'.format(m.lower()) in self_attrs:
                allowed_methods.append(m)

        resp.headers['Allow'] = ','.join(allowed_methods)
        resp.status = HTTP_200

    def authorize_roles(self, role_list):
        authorized = set(self.authorized_roles)
        applied = set(role_list)

        if authorized.isdisjoint(applied):
            return False
        else:
            return True

    def req_json(self, req):
        content_length = req.content_length
        content_type = req.content_type
        expected_type = 'application/json'
        if content_length is None or content_length == 0:
            return None

        if content_type is not None or content_type.lower() == expected_type:
            raw_body = req.stream.read(req.content_length or 0)
            if raw_body is None:
                return None

            try:
                return json.loads(raw_body.decode('utf-8'))
            except Exception as e:
                raise Exception('Invalid JSON in body: %s'.format(e))

    def return_error(self, resp, status_code, message="", retry=False):
        message = {
            'type': 'error',
            'message': message,
            'retry': retry
        }
        resp.body = json.dumps(message)
        resp.status = status_code

    def log_error(self, ctx, level, msg):
        extra = {
            'user': 'N/A',
            'req_id': 'N/A',
            'external_ctx': 'N/A',
        }

        if ctx is not None:
            extra = {
                'user': ctx.user,
                'req_id': ctx.request_id,
                'external_ctx': ctx.external_marker,
            }

        LOG.log(level, msg, extra=extra)

    def debug(self, ctx, msg):
        self.log_error(ctx, logging.DEBUG, msg)

    def info(self, ctx, msg):
        self.log_error(ctx, logging.INFO, msg)

    def warn(self, ctx, msg):
        self.log_error(ctx, logging.WARN, msg)

    def error(self, ctx, msg):
        self.log_error(ctx, logging.ERROR, msg)

class ArmadaRequestContext(object):

    def __init__(self):
        self.log_level = 'ERROR'
        self.user = None
        self.roles = ['anyone']
        self.request_id = str(uuid.uuid4())
        self.external_marker = None

    def set_log_level(self, level):
        if level in ['error', 'info', 'debug']:
            self.log_level = level

    def set_user(self, user):
        self.user = user

    def add_role(self, role):
        self.roles.append(role)

    def add_roles(self, roles):
        self.roles.extend(roles)

    def remove_role(self, role):
        self.roles = [x for x in self.roles if x != role]

    def set_external_marker(self, marker):
        self.external_marker = str(marker)[:20]

class ArmadaRequest(request.Request):
    context_type = ArmadaRequestContext
