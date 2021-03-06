# coding: utf-8

"""
    dacat-api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.8.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Datafile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, path=None, size=None, time=None, chk=None, uid=None, gid=None, perm=None):
        """
        Datafile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'path': 'str',
            'size': 'float',
            'time': 'datetime',
            'chk': 'str',
            'uid': 'str',
            'gid': 'str',
            'perm': 'str'
        }

        self.attribute_map = {
            'path': 'path',
            'size': 'size',
            'time': 'time',
            'chk': 'chk',
            'uid': 'uid',
            'gid': 'gid',
            'perm': 'perm'
        }

        self._path = path
        self._size = size
        self._time = time
        self._chk = chk
        self._uid = uid
        self._gid = gid
        self._perm = perm

    @property
    def path(self):
        """
        Gets the path of this Datafile.
        Relative path of the file within the dataset folder

        :return: The path of this Datafile.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Datafile.
        Relative path of the file within the dataset folder

        :param path: The path of this Datafile.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

    @property
    def size(self):
        """
        Gets the size of this Datafile.
        Uncompressed file size in bytes

        :return: The size of this Datafile.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this Datafile.
        Uncompressed file size in bytes

        :param size: The size of this Datafile.
        :type: float
        """

        self._size = size

    @property
    def time(self):
        """
        Gets the time of this Datafile.
        Time of file creation on disk, format according to chapter 5.6 internet date/time format in RFC 3339. Local times without timezone/offset info are automatically transformed to UTC using the timezone of the API server

        :return: The time of this Datafile.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this Datafile.
        Time of file creation on disk, format according to chapter 5.6 internet date/time format in RFC 3339. Local times without timezone/offset info are automatically transformed to UTC using the timezone of the API server

        :param time: The time of this Datafile.
        :type: datetime
        """

        self._time = time

    @property
    def chk(self):
        """
        Gets the chk of this Datafile.
        Checksum for the file, e.g. its sha-2 hashstring

        :return: The chk of this Datafile.
        :rtype: str
        """
        return self._chk

    @chk.setter
    def chk(self, chk):
        """
        Sets the chk of this Datafile.
        Checksum for the file, e.g. its sha-2 hashstring

        :param chk: The chk of this Datafile.
        :type: str
        """

        self._chk = chk

    @property
    def uid(self):
        """
        Gets the uid of this Datafile.
        optional: user ID name as seen on filesystem

        :return: The uid of this Datafile.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this Datafile.
        optional: user ID name as seen on filesystem

        :param uid: The uid of this Datafile.
        :type: str
        """

        self._uid = uid

    @property
    def gid(self):
        """
        Gets the gid of this Datafile.
        optional: group ID name as seen on filesystem

        :return: The gid of this Datafile.
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """
        Sets the gid of this Datafile.
        optional: group ID name as seen on filesystem

        :param gid: The gid of this Datafile.
        :type: str
        """

        self._gid = gid

    @property
    def perm(self):
        """
        Gets the perm of this Datafile.
        optional: Posix permission bits

        :return: The perm of this Datafile.
        :rtype: str
        """
        return self._perm

    @perm.setter
    def perm(self, perm):
        """
        Sets the perm of this Datafile.
        optional: Posix permission bits

        :param perm: The perm of this Datafile.
        :type: str
        """

        self._perm = perm

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
        if not isinstance(other, Datafile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
