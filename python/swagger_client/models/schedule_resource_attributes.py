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


class ScheduleResourceAttributes(object):
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
        'timepoint': 'bool',
        'stop_sequence': 'int',
        'pickup_type': 'int',
        'drop_off_type': 'int',
        'direction_id': 'int',
        'departure_time': 'str',
        'arrival_time': 'str'
    }

    attribute_map = {
        'timepoint': 'timepoint',
        'stop_sequence': 'stop_sequence',
        'pickup_type': 'pickup_type',
        'drop_off_type': 'drop_off_type',
        'direction_id': 'direction_id',
        'departure_time': 'departure_time',
        'arrival_time': 'arrival_time'
    }

    def __init__(self, timepoint=None, stop_sequence=None, pickup_type=None, drop_off_type=None, direction_id=None, departure_time=None, arrival_time=None):
        """
        ScheduleResourceAttributes - a model defined in Swagger
        """

        self._timepoint = None
        self._stop_sequence = None
        self._pickup_type = None
        self._drop_off_type = None
        self._direction_id = None
        self._departure_time = None
        self._arrival_time = None

        if timepoint is not None:
          self.timepoint = timepoint
        if stop_sequence is not None:
          self.stop_sequence = stop_sequence
        if pickup_type is not None:
          self.pickup_type = pickup_type
        if drop_off_type is not None:
          self.drop_off_type = drop_off_type
        if direction_id is not None:
          self.direction_id = direction_id
        if departure_time is not None:
          self.departure_time = departure_time
        if arrival_time is not None:
          self.arrival_time = arrival_time

    @property
    def timepoint(self):
        """
        Gets the timepoint of this ScheduleResourceAttributes.
        | Value   | `*/attributes/arrival_time` and `*/attributes/departure_time` | |---------|---------------------------------------------------------------| | `true`  | Exact                                                         | | `false` | Estimates                                                     |  See [GTFS `stop_times.txt` `timepoint`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :return: The timepoint of this ScheduleResourceAttributes.
        :rtype: bool
        """
        return self._timepoint

    @timepoint.setter
    def timepoint(self, timepoint):
        """
        Sets the timepoint of this ScheduleResourceAttributes.
        | Value   | `*/attributes/arrival_time` and `*/attributes/departure_time` | |---------|---------------------------------------------------------------| | `true`  | Exact                                                         | | `false` | Estimates                                                     |  See [GTFS `stop_times.txt` `timepoint`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :param timepoint: The timepoint of this ScheduleResourceAttributes.
        :type: bool
        """

        self._timepoint = timepoint

    @property
    def stop_sequence(self):
        """
        Gets the stop_sequence of this ScheduleResourceAttributes.
        The sequence the `stop_id` is arrived at during the `trip_id`.  The stop sequence is monotonically increasing along the trip, but the `stop_sequence` along the `trip_id` are not necessarily consecutive.  See [GTFS `stop_times.txt` `stop_sequence`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :return: The stop_sequence of this ScheduleResourceAttributes.
        :rtype: int
        """
        return self._stop_sequence

    @stop_sequence.setter
    def stop_sequence(self, stop_sequence):
        """
        Sets the stop_sequence of this ScheduleResourceAttributes.
        The sequence the `stop_id` is arrived at during the `trip_id`.  The stop sequence is monotonically increasing along the trip, but the `stop_sequence` along the `trip_id` are not necessarily consecutive.  See [GTFS `stop_times.txt` `stop_sequence`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :param stop_sequence: The stop_sequence of this ScheduleResourceAttributes.
        :type: int
        """

        self._stop_sequence = stop_sequence

    @property
    def pickup_type(self):
        """
        Gets the pickup_type of this ScheduleResourceAttributes.
        How the vehicle departs from `stop_id`.  | Value | Description                                   | |-------|-----------------------------------------------| | `0`   | Regularly scheduled pickup                    | | `1`   | No pickup available                           | | `2`   | Must phone agency to arrange pickup           | | `3`   | Must coordinate with driver to arrange pickup |  See [GTFS `stop_times.txt` `pickup_type`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :return: The pickup_type of this ScheduleResourceAttributes.
        :rtype: int
        """
        return self._pickup_type

    @pickup_type.setter
    def pickup_type(self, pickup_type):
        """
        Sets the pickup_type of this ScheduleResourceAttributes.
        How the vehicle departs from `stop_id`.  | Value | Description                                   | |-------|-----------------------------------------------| | `0`   | Regularly scheduled pickup                    | | `1`   | No pickup available                           | | `2`   | Must phone agency to arrange pickup           | | `3`   | Must coordinate with driver to arrange pickup |  See [GTFS `stop_times.txt` `pickup_type`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :param pickup_type: The pickup_type of this ScheduleResourceAttributes.
        :type: int
        """

        self._pickup_type = pickup_type

    @property
    def drop_off_type(self):
        """
        Gets the drop_off_type of this ScheduleResourceAttributes.
        How the vehicle arrives at `stop_id`.  | Value | Description                                   | |-------|-----------------------------------------------| | `0`   | Regularly scheduled drop off                  | | `1`   | No drop off available                         | | `2`   | Must phone agency to arrange pickup           | | `3`   | Must coordinate with driver to arrange pickup |  See [GTFS `stop_times.txt` `drop_off_type`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :return: The drop_off_type of this ScheduleResourceAttributes.
        :rtype: int
        """
        return self._drop_off_type

    @drop_off_type.setter
    def drop_off_type(self, drop_off_type):
        """
        Sets the drop_off_type of this ScheduleResourceAttributes.
        How the vehicle arrives at `stop_id`.  | Value | Description                                   | |-------|-----------------------------------------------| | `0`   | Regularly scheduled drop off                  | | `1`   | No drop off available                         | | `2`   | Must phone agency to arrange pickup           | | `3`   | Must coordinate with driver to arrange pickup |  See [GTFS `stop_times.txt` `drop_off_type`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :param drop_off_type: The drop_off_type of this ScheduleResourceAttributes.
        :type: int
        """

        self._drop_off_type = drop_off_type

    @property
    def direction_id(self):
        """
        Gets the direction_id of this ScheduleResourceAttributes.
        Direction in which trip is traveling: `0` or `1`.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.  

        :return: The direction_id of this ScheduleResourceAttributes.
        :rtype: int
        """
        return self._direction_id

    @direction_id.setter
    def direction_id(self, direction_id):
        """
        Sets the direction_id of this ScheduleResourceAttributes.
        Direction in which trip is traveling: `0` or `1`.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.  

        :param direction_id: The direction_id of this ScheduleResourceAttributes.
        :type: int
        """

        self._direction_id = direction_id

    @property
    def departure_time(self):
        """
        Gets the departure_time of this ScheduleResourceAttributes.
        Time when the trip departs the given stop. `null` if the last stop (`*/relationships/stop/data/id`) on the trip (`*/relationships/trip/data/id`).  See [GTFS `stop_times.txt` `departure_time`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :return: The departure_time of this ScheduleResourceAttributes.
        :rtype: str
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        """
        Sets the departure_time of this ScheduleResourceAttributes.
        Time when the trip departs the given stop. `null` if the last stop (`*/relationships/stop/data/id`) on the trip (`*/relationships/trip/data/id`).  See [GTFS `stop_times.txt` `departure_time`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :param departure_time: The departure_time of this ScheduleResourceAttributes.
        :type: str
        """

        self._departure_time = departure_time

    @property
    def arrival_time(self):
        """
        Gets the arrival_time of this ScheduleResourceAttributes.
        Time when the trip arrives at the given stop.  `null` if the first stop (`*/relationships/stop/data/id`) on the trip (`*/relationships/trip/data/id`).  See [GTFS `stop_times.txt` `arrival_time`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :return: The arrival_time of this ScheduleResourceAttributes.
        :rtype: str
        """
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, arrival_time):
        """
        Sets the arrival_time of this ScheduleResourceAttributes.
        Time when the trip arrives at the given stop.  `null` if the first stop (`*/relationships/stop/data/id`) on the trip (`*/relationships/trip/data/id`).  See [GTFS `stop_times.txt` `arrival_time`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) 

        :param arrival_time: The arrival_time of this ScheduleResourceAttributes.
        :type: str
        """

        self._arrival_time = arrival_time

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
        if not isinstance(other, ScheduleResourceAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
