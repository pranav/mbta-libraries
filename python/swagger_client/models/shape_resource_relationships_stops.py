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


class ShapeResourceRelationshipsStops(object):
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
        'links': 'ShapeResourceRelationshipsStopsLinks',
        'data': 'list[ShapeResourceRelationshipsStopsData]'
    }

    attribute_map = {
        'links': 'links',
        'data': 'data'
    }

    def __init__(self, links=None, data=None):
        """
        ShapeResourceRelationshipsStops - a model defined in Swagger
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
        Gets the links of this ShapeResourceRelationshipsStops.

        :return: The links of this ShapeResourceRelationshipsStops.
        :rtype: ShapeResourceRelationshipsStopsLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this ShapeResourceRelationshipsStops.

        :param links: The links of this ShapeResourceRelationshipsStops.
        :type: ShapeResourceRelationshipsStopsLinks
        """

        self._links = links

    @property
    def data(self):
        """
        Gets the data of this ShapeResourceRelationshipsStops.

        :return: The data of this ShapeResourceRelationshipsStops.
        :rtype: list[ShapeResourceRelationshipsStopsData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this ShapeResourceRelationshipsStops.

        :param data: The data of this ShapeResourceRelationshipsStops.
        :type: list[ShapeResourceRelationshipsStopsData]
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
        if not isinstance(other, ShapeResourceRelationshipsStops):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
