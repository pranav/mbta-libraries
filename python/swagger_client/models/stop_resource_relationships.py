# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com

    OpenAPI spec version: 3.0
    Contact: developer@mbta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StopResourceRelationships(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'parent_station': 'StopResourceRelationshipsParentStation'
    }

    attribute_map = {
        'parent_station': 'parent_station'
    }

    def __init__(self, parent_station=None):
        """
        StopResourceRelationships - a model defined in Swagger
        """

        self._parent_station = None

        if parent_station is not None:
          self.parent_station = parent_station

    @property
    def parent_station(self):
        """
        Gets the parent_station of this StopResourceRelationships.

        :return: The parent_station of this StopResourceRelationships.
        :rtype: StopResourceRelationshipsParentStation
        """
        return self._parent_station

    @parent_station.setter
    def parent_station(self, parent_station):
        """
        Sets the parent_station of this StopResourceRelationships.

        :param parent_station: The parent_station of this StopResourceRelationships.
        :type: StopResourceRelationshipsParentStation
        """

        self._parent_station = parent_station

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, StopResourceRelationships):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
