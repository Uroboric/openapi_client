# coding: utf-8

"""
    DM.API Account

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dm_api_account.models.info_bb_text import InfoBbText

class TestInfoBbText(unittest.TestCase):
    """InfoBbText unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InfoBbText:
        """Test InfoBbText
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InfoBbText`
        """
        model = InfoBbText()
        if include_optional:
            return InfoBbText(
                value = '',
                parse_mode = 'Common'
            )
        else:
            return InfoBbText(
        )
        """

    def testInfoBbText(self):
        """Test InfoBbText"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
