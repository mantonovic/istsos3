# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction
import istsos


class ObservationType(CompositeAction):
    """Rest api used to manage unit of measures
    """

    @asyncio.coroutine
    def before(self, request):

        if request.get_action() != 'retrieve':
            raise Exception('Method {} not supported'.format(request.get_action()))

    @asyncio.coroutine
    def after(self, request):
        """Render the result of the request
        """

        response = Response.get_template()

        if request.get_action() == 'retrieve':
            response['data'] = istsos.get_observation_types()

        request['response'] = Response(response)
