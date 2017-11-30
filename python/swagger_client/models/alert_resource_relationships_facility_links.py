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


class AlertResourceRelationshipsFacilityLinks(object):
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
        '_self': 'str',
        'related': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'related': 'related'
    }

    def __init__(self, _self=None, related=None):
        """
        AlertResourceRelationshipsFacilityLinks - a model defined in Swagger
        """

        self.__self = None
        self._related = None

        if _self is not None:
          self._self = _self
        if related is not None:
          self.related = related

    @property
    def _self(self):
        """
        Gets the _self of this AlertResourceRelationshipsFacilityLinks.
        Relationship link for facility

        :return: The _self of this AlertResourceRelationshipsFacilityLinks.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this AlertResourceRelationshipsFacilityLinks.
        Relationship link for facility

        :param _self: The _self of this AlertResourceRelationshipsFacilityLinks.
        :type: str
        """

        self.__self = _self

    @property
    def related(self):
        """
        Gets the related of this AlertResourceRelationshipsFacilityLinks.
        Related facility link

        :return: The related of this AlertResourceRelationshipsFacilityLinks.
        :rtype: str
        """
        return self._related

    @related.setter
    def related(self, related):
        """
        Sets the related of this AlertResourceRelationshipsFacilityLinks.
        Related facility link

        :param related: The related of this AlertResourceRelationshipsFacilityLinks.
        :type: str
        """

        self._related = related

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
        if not isinstance(other, AlertResourceRelationshipsFacilityLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other