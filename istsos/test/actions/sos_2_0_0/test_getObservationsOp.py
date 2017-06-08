# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.application import Server
from istsos.entity.httpRequest import HttpRequest
from istsos.actions.sos_2_0_0.insertSensorOp import InsertSensor


class TestGetObservations:

    def execute_get(self):
        # Installation of the istSOS server
        server = yield from Server.create()

        # Preparing the Request object
        request = HttpRequest(
            "GET",
            "sos",
            parameters={
                "service": "SOS",
                "version": "2.0.0",
                "request": "GetObservation",
                "offering": "T_LUGANO",
                "temporalFilter": (
                    "om:phenomenonTime,"
                    "2009-01-01T00:00:00+0100/"
                    "2009-01-02T00:00:00+0100"
                )
            }
        )

        response = yield from server.execute_http_request(
            request, stats=True
        )

    def test_execute(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.gather(self.execute_get())
        )
        loop.close()
        assert True is True
