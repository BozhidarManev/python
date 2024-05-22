# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.30
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1alpha2DriverRequests(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'driver_name': 'str',
        'requests': 'list[V1alpha2ResourceRequest]',
        'vendor_parameters': 'object'
    }

    attribute_map = {
        'driver_name': 'driverName',
        'requests': 'requests',
        'vendor_parameters': 'vendorParameters'
    }

    def __init__(self, driver_name=None, requests=None, vendor_parameters=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha2DriverRequests - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._driver_name = None
        self._requests = None
        self._vendor_parameters = None
        self.discriminator = None

        if driver_name is not None:
            self.driver_name = driver_name
        if requests is not None:
            self.requests = requests
        if vendor_parameters is not None:
            self.vendor_parameters = vendor_parameters

    @property
    def driver_name(self):
        """Gets the driver_name of this V1alpha2DriverRequests.  # noqa: E501

        DriverName is the name used by the DRA driver kubelet plugin.  # noqa: E501

        :return: The driver_name of this V1alpha2DriverRequests.  # noqa: E501
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """Sets the driver_name of this V1alpha2DriverRequests.

        DriverName is the name used by the DRA driver kubelet plugin.  # noqa: E501

        :param driver_name: The driver_name of this V1alpha2DriverRequests.  # noqa: E501
        :type: str
        """

        self._driver_name = driver_name

    @property
    def requests(self):
        """Gets the requests of this V1alpha2DriverRequests.  # noqa: E501

        Requests describes all resources that are needed from the driver.  # noqa: E501

        :return: The requests of this V1alpha2DriverRequests.  # noqa: E501
        :rtype: list[V1alpha2ResourceRequest]
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this V1alpha2DriverRequests.

        Requests describes all resources that are needed from the driver.  # noqa: E501

        :param requests: The requests of this V1alpha2DriverRequests.  # noqa: E501
        :type: list[V1alpha2ResourceRequest]
        """

        self._requests = requests

    @property
    def vendor_parameters(self):
        """Gets the vendor_parameters of this V1alpha2DriverRequests.  # noqa: E501

        VendorParameters are arbitrary setup parameters for all requests of the claim. They are ignored while allocating the claim.  # noqa: E501

        :return: The vendor_parameters of this V1alpha2DriverRequests.  # noqa: E501
        :rtype: object
        """
        return self._vendor_parameters

    @vendor_parameters.setter
    def vendor_parameters(self, vendor_parameters):
        """Sets the vendor_parameters of this V1alpha2DriverRequests.

        VendorParameters are arbitrary setup parameters for all requests of the claim. They are ignored while allocating the claim.  # noqa: E501

        :param vendor_parameters: The vendor_parameters of this V1alpha2DriverRequests.  # noqa: E501
        :type: object
        """

        self._vendor_parameters = vendor_parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha2DriverRequests):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha2DriverRequests):
            return True

        return self.to_dict() != other.to_dict()