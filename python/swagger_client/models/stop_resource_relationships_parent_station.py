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


class StopResourceRelationshipsParentStation(object):
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
        'links': 'StopResourceRelationshipsParentStationLinks',
        'data': 'StopResourceRelationshipsParentStationData'
    }

    attribute_map = {
        'links': 'links',
        'data': 'data'
    }

    def __init__(self, links=None, data=None):
        """
        StopResourceRelationshipsParentStation - a model defined in Swagger
        """

        self._links = None
        self._data = None

        if links is not None:
          self.links = links
        if data is not None:
          self.data = data

    @property
    def links(self):
        """
        Gets the links of this StopResourceRelationshipsParentStation.

        :return: The links of this StopResourceRelationshipsParentStation.
        :rtype: StopResourceRelationshipsParentStationLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this StopResourceRelationshipsParentStation.

        :param links: The links of this StopResourceRelationshipsParentStation.
        :type: StopResourceRelationshipsParentStationLinks
        """

        self._links = links

    @property
    def data(self):
        """
        Gets the data of this StopResourceRelationshipsParentStation.

        :return: The data of this StopResourceRelationshipsParentStation.
        :rtype: StopResourceRelationshipsParentStationData
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this StopResourceRelationshipsParentStation.

        :param data: The data of this StopResourceRelationshipsParentStation.
        :type: StopResourceRelationshipsParentStationData
        """

        self._data = data

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
        if not isinstance(other, StopResourceRelationshipsParentStation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
