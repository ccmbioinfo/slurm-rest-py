"""
    Slurm Rest API

    API to access and control Slurm.  # noqa: E501

    The version of the OpenAPI document: 0.0.37
    Contact: sales@schedmd.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import slurm_rest
from slurm_rest.model.dbv0037_association_short_info import Dbv0037AssociationShortInfo
from slurm_rest.model.dbv0037_coordinator_info import Dbv0037CoordinatorInfo
globals()['Dbv0037AssociationShortInfo'] = Dbv0037AssociationShortInfo
globals()['Dbv0037CoordinatorInfo'] = Dbv0037CoordinatorInfo
from slurm_rest.model.dbv0037_account import Dbv0037Account


class TestDbv0037Account(unittest.TestCase):
    """Dbv0037Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDbv0037Account(self):
        """Test Dbv0037Account"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Dbv0037Account()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
