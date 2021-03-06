#!/usr/bin/env python3
#
# Copyright (c) 2019 Roberto Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

"""Unload all worker."""

import empower_core.command as command


def do_cmd(gargs, *_):
    """Unload all workers. """

    headers = command.get_headers(gargs)

    url = '/api/v1/workers'
    _, data = command.connect(gargs, ('GET', url), 200, headers=headers)

    for entry in data.values():

        worker_id = entry['service_id']

        url = '/api/v1/workers/%s' % worker_id
        command.connect(gargs, ('DELETE', url), 204, headers=headers)

        print(worker_id)
