# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

from istsos.entity.baseEntity import BaseEntity
from istsos.entity.om_base_entity.timeElements import TimeInterval
from istsos.entity.om_base_entity.geoJson import Coordinates2D
from istsos.entity.featureOfInterest import SamplingType
import collections


class Offering(BaseEntity):
    """ObservationOffering entity: an ObservationOffering groups collections
    of observations produced by one procedure."""

    json_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "results": {"type": "boolean"},
            "name": {"type": "string"},
            "procedure": {"type": "string"},
            "systemType": {"type": "string"},
            "procedure_description_format": {
                "type": "array",
                "items": [
                    {
                        "type": "string",
                        "enum": [
                            "http://www.opengis.net/sensorML/1.0.1"
                        ]
                    }
                ]
            },
            "observable_property": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer"
                            },
                            "name": {
                                "oneOf": [
                                    {
                                        "type": "null"
                                    },
                                    {
                                        "type": "string"
                                    }
                                ]
                            },
                            "definition": {
                                "type": "string"
                            },
                            "uom": {
                                "oneOf": [
                                    {
                                        "type": "null"
                                    },
                                    {
                                        "type": "string"
                                    }
                                ]
                            },
                            "type": {
                                "oneOf": [
                                    {
                                        "type": "null"
                                    },
                                    {
                                        "type": "string"
                                    }
                                ]
                            },
                            "column": {
                                "oneOf": [
                                    {
                                        "type": "null"
                                    },
                                    {
                                        "type": "string"
                                    }
                                ]
                            },
                            "constraint": {
                                "type": "object",
                                "properties": {
                                    "inteval": {
                                        "type": "array",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "role": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            "observation_type": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer"
                            },
                            "definition": {
                                "type": "string"
                            },
                            "description": {
                                "type": "string"
                            }
                        }
                    }
                ]
            },
            "observed_area": {
                "type": "object",
                "properties": {
                    "lower_corner": Coordinates2D.json_schema,
                    "upper_corner": Coordinates2D.json_schema
                }
            },
            "phenomenon_time": {
                "oneOf": [
                    TimeInterval.json_schema,
                    {"type": "null"}
                ]
            },
            "result_time": {
                "oneOf": [
                    TimeInterval.json_schema,
                    {"type": "null"}
                ]
            },
            "foi_type": SamplingType.json_schema
        }
    }

    def get_op_definition_list(self):
        """Return a list of Observed Properties"""
        return [op['definition'] for op in self['observable_property']]

    def get_ot_definition_list(self):
        """Return a list of Observation Types"""
        return [ot['definition'] for ot in self['observation_type']]

    def get_observed_property(self, definition):
        for observed_property in self['observable_property']:
            if definition == observed_property['definition']:
                return observed_property
        return None

    def get_observation_type(self, definition):
        for observation_type in self['observation_type']:
            if definition == observation_type['definition']:
                return observation_type
        return None

    def set_column(self, definition, column_name):
        observed_property = self.get_observed_property(definition)
        if observed_property is not None:
            observed_property['column'] = column_name
