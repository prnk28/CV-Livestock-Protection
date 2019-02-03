# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OauthAccess(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, access_token=None, data=None, expires_in=None, refresh_token=None, scope=None, token_type=None):
        """
        OauthAccess - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_token': 'str',
            'data': 'list[NameValue]',
            'expires_in': 'str',
            'refresh_token': 'str',
            'scope': 'str',
            'token_type': 'str'
        }

        self.attribute_map = {
            'access_token': 'access_token',
            'data': 'data',
            'expires_in': 'expires_in',
            'refresh_token': 'refresh_token',
            'scope': 'scope',
            'token_type': 'token_type'
        }

        self._access_token = access_token
        self._data = data
        self._expires_in = expires_in
        self._refresh_token = refresh_token
        self._scope = scope
        self._token_type = token_type

    @property
    def access_token(self):
        """
        Gets the access_token of this OauthAccess.
        Access token information.

        :return: The access_token of this OauthAccess.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this OauthAccess.
        Access token information.

        :param access_token: The access_token of this OauthAccess.
        :type: str
        """

        self._access_token = access_token

    @property
    def data(self):
        """
        Gets the data of this OauthAccess.
        

        :return: The data of this OauthAccess.
        :rtype: list[NameValue]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this OauthAccess.
        

        :param data: The data of this OauthAccess.
        :type: list[NameValue]
        """

        self._data = data

    @property
    def expires_in(self):
        """
        Gets the expires_in of this OauthAccess.
        

        :return: The expires_in of this OauthAccess.
        :rtype: str
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this OauthAccess.
        

        :param expires_in: The expires_in of this OauthAccess.
        :type: str
        """

        self._expires_in = expires_in

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this OauthAccess.
        

        :return: The refresh_token of this OauthAccess.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this OauthAccess.
        

        :param refresh_token: The refresh_token of this OauthAccess.
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def scope(self):
        """
        Gets the scope of this OauthAccess.
        Must be set to \"api\".

        :return: The scope of this OauthAccess.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this OauthAccess.
        Must be set to \"api\".

        :param scope: The scope of this OauthAccess.
        :type: str
        """

        self._scope = scope

    @property
    def token_type(self):
        """
        Gets the token_type of this OauthAccess.
        

        :return: The token_type of this OauthAccess.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this OauthAccess.
        

        :param token_type: The token_type of this OauthAccess.
        :type: str
        """

        self._token_type = token_type

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other