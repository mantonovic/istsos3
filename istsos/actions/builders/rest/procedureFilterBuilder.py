# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.entity.filters.proceduresFilter import ProceduresFilter
from istsos.actions.builders.procedureFilterBuilder import (
    ProcedureFilterBuilder
)


class ProcedureFilterBuilder(ProcedureFilterBuilder):

    @asyncio.coroutine
    def process(self, request):
        if request['method'] == 'GET':
            procedures_filter = request.get_parameter('procedure')

            if procedures_filter is not None:
                tmpl = ProceduresFilter.get_template()
                procedures_filter = procedures_filter.split(',')
                if len(procedures_filter) > 0:
                    tmpl['procedures'] = procedures_filter
                    request.set_filter(ProceduresFilter(json_source=tmpl))
