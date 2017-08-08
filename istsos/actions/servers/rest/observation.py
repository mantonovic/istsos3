# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.actions.action import CompositeAction

from istsos.actions.builders.rest.offeringFilterBuilder import OfferingFilterBuilder
from istsos.actions.builders.rest.procedureFilterBuilder import ProcedureFilterBuilder
from istsos.actions.builders.rest.observedPropertyFilterBuilder import ObservedPropertyFilterBuilder
from istsos.actions.builders.rest.temporalFilterBuilder import TemporalFilterBuilder


class Observation(CompositeAction):
    """Rest api used to manage unit of measures
    """

    @asyncio.coroutine
    def before(self, request):

        if request['method'] == 'GET':

            self.add(TemporalFilterBuilder())
            self.add(OfferingFilterBuilder())
            self.add(ProcedureFilterBuilder())
            self.add(ObservedPropertyFilterBuilder())

            yield from self.add_retriever('Offerings')
            yield from self.add_retriever('Observations')

        else:
            raise Exception('Method {} not supported'.format(request['method']))

    @asyncio.coroutine
    def after(self, request):
        """Render the result of the request following the OGC:SOS 2.0.0 standard.
        """

        if request['method'] == 'GET':
            request['response'] = {'data': request['observations']}
