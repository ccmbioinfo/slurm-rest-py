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
from slurm_rest.model.dbv0036_job_step_statistics_cpu import Dbv0036JobStepStatisticsCPU
from slurm_rest.model.dbv0036_job_step_statistics_energy import Dbv0036JobStepStatisticsEnergy
globals()['Dbv0036JobStepStatisticsCPU'] = Dbv0036JobStepStatisticsCPU
globals()['Dbv0036JobStepStatisticsEnergy'] = Dbv0036JobStepStatisticsEnergy
from slurm_rest.model.dbv0036_job_step_statistics import Dbv0036JobStepStatistics


class TestDbv0036JobStepStatistics(unittest.TestCase):
    """Dbv0036JobStepStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDbv0036JobStepStatistics(self):
        """Test Dbv0036JobStepStatistics"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Dbv0036JobStepStatistics()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
