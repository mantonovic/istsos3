# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.actions.action import CompositeAction


class Provider(CompositeAction):
    """Rest api used to manage observed property
    """

    @asyncio.coroutine
    def before(self, request):
        yield from self.add_retriever('Provider')

    @asyncio.coroutine
    def after(self, request):
        """Render the result of the request following the OGC:SOS 2.0.0 standard.
        """
        request['response'] = {"data": request['provider']}
