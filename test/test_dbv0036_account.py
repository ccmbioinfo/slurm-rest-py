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
from slurm_rest.model.dbv0036_association_short_info import Dbv0036AssociationShortInfo
from slurm_rest.model.dbv0036_coordinator_info import Dbv0036CoordinatorInfo
globals()['Dbv0036AssociationShortInfo'] = Dbv0036AssociationShortInfo
globals()['Dbv0036CoordinatorInfo'] = Dbv0036CoordinatorInfo
from slurm_rest.model.dbv0036_account import Dbv0036Account


class TestDbv0036Account(unittest.TestCase):
    """Dbv0036Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDbv0036Account(self):
        """Test Dbv0036Account"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Dbv0036Account()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()