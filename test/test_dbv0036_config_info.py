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
from slurm_rest.model.dbv0036_account import Dbv0036Account
from slurm_rest.model.dbv0036_association import Dbv0036Association
from slurm_rest.model.dbv0036_error import Dbv0036Error
from slurm_rest.model.dbv0036_qos import Dbv0036Qos
from slurm_rest.model.dbv0036_tres_list import Dbv0036TresList
from slurm_rest.model.dbv0036_user import Dbv0036User
from slurm_rest.model.dbv0036_wckey import Dbv0036Wckey
globals()['Dbv0036Account'] = Dbv0036Account
globals()['Dbv0036Association'] = Dbv0036Association
globals()['Dbv0036Error'] = Dbv0036Error
globals()['Dbv0036Qos'] = Dbv0036Qos
globals()['Dbv0036TresList'] = Dbv0036TresList
globals()['Dbv0036User'] = Dbv0036User
globals()['Dbv0036Wckey'] = Dbv0036Wckey
from slurm_rest.model.dbv0036_config_info import Dbv0036ConfigInfo


class TestDbv0036ConfigInfo(unittest.TestCase):
    """Dbv0036ConfigInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDbv0036ConfigInfo(self):
        """Test Dbv0036ConfigInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Dbv0036ConfigInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
