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
from slurm_rest.model.dbv0036_cluster_info_associations import Dbv0036ClusterInfoAssociations
from slurm_rest.model.dbv0036_cluster_info_controller import Dbv0036ClusterInfoController
from slurm_rest.model.dbv0036_response_tres import Dbv0036ResponseTres
globals()['Dbv0036ClusterInfoAssociations'] = Dbv0036ClusterInfoAssociations
globals()['Dbv0036ClusterInfoController'] = Dbv0036ClusterInfoController
globals()['Dbv0036ResponseTres'] = Dbv0036ResponseTres
from slurm_rest.model.dbv0036_cluster_info import Dbv0036ClusterInfo


class TestDbv0036ClusterInfo(unittest.TestCase):
    """Dbv0036ClusterInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDbv0036ClusterInfo(self):
        """Test Dbv0036ClusterInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Dbv0036ClusterInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
