"""
    Slurm Rest API

    API to access and control Slurm.  # noqa: E501

    The version of the OpenAPI document: 0.0.37
    Contact: sales@schedmd.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import slurm_rest
from slurm_rest.api.slurm_api import SlurmApi  # noqa: E501


class TestSlurmApi(unittest.TestCase):
    """SlurmApi unit test stubs"""

    def setUp(self):
        self.api = SlurmApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_slurmctld_cancel_job(self):
        """Test case for slurmctld_cancel_job

        cancel or signal job  # noqa: E501
        """
        pass

    def test_slurmctld_cancel_job_0(self):
        """Test case for slurmctld_cancel_job_0

        cancel or signal job  # noqa: E501
        """
        pass

    def test_slurmctld_diag(self):
        """Test case for slurmctld_diag

        get diagnostics  # noqa: E501
        """
        pass

    def test_slurmctld_diag_0(self):
        """Test case for slurmctld_diag_0

        get diagnostics  # noqa: E501
        """
        pass

    def test_slurmctld_get_job(self):
        """Test case for slurmctld_get_job

        get job info  # noqa: E501
        """
        pass

    def test_slurmctld_get_job_0(self):
        """Test case for slurmctld_get_job_0

        get job info  # noqa: E501
        """
        pass

    def test_slurmctld_get_jobs(self):
        """Test case for slurmctld_get_jobs

        get list of jobs  # noqa: E501
        """
        pass

    def test_slurmctld_get_jobs_0(self):
        """Test case for slurmctld_get_jobs_0

        get list of jobs  # noqa: E501
        """
        pass

    def test_slurmctld_get_node(self):
        """Test case for slurmctld_get_node

        get node info  # noqa: E501
        """
        pass

    def test_slurmctld_get_node_0(self):
        """Test case for slurmctld_get_node_0

        get node info  # noqa: E501
        """
        pass

    def test_slurmctld_get_nodes(self):
        """Test case for slurmctld_get_nodes

        get all node info  # noqa: E501
        """
        pass

    def test_slurmctld_get_nodes_0(self):
        """Test case for slurmctld_get_nodes_0

        get all node info  # noqa: E501
        """
        pass

    def test_slurmctld_get_partition(self):
        """Test case for slurmctld_get_partition

        get partition info  # noqa: E501
        """
        pass

    def test_slurmctld_get_partition_0(self):
        """Test case for slurmctld_get_partition_0

        get partition info  # noqa: E501
        """
        pass

    def test_slurmctld_get_partitions(self):
        """Test case for slurmctld_get_partitions

        get all partition info  # noqa: E501
        """
        pass

    def test_slurmctld_get_partitions_0(self):
        """Test case for slurmctld_get_partitions_0

        get all partition info  # noqa: E501
        """
        pass

    def test_slurmctld_get_reservation(self):
        """Test case for slurmctld_get_reservation

        get reservation info  # noqa: E501
        """
        pass

    def test_slurmctld_get_reservations(self):
        """Test case for slurmctld_get_reservations

        get all reservation info  # noqa: E501
        """
        pass

    def test_slurmctld_ping(self):
        """Test case for slurmctld_ping

        ping test  # noqa: E501
        """
        pass

    def test_slurmctld_ping_0(self):
        """Test case for slurmctld_ping_0

        ping test  # noqa: E501
        """
        pass

    def test_slurmctld_submit_job(self):
        """Test case for slurmctld_submit_job

        submit new job  # noqa: E501
        """
        pass

    def test_slurmctld_submit_job_0(self):
        """Test case for slurmctld_submit_job_0

        submit new job  # noqa: E501
        """
        pass

    def test_slurmctld_update_job(self):
        """Test case for slurmctld_update_job

        update job  # noqa: E501
        """
        pass

    def test_slurmctld_update_job_0(self):
        """Test case for slurmctld_update_job_0

        update job  # noqa: E501
        """
        pass

    def test_slurmdbd_add_clusters(self):
        """Test case for slurmdbd_add_clusters

        Add clusters  # noqa: E501
        """
        pass

    def test_slurmdbd_add_clusters_0(self):
        """Test case for slurmdbd_add_clusters_0

        Add clusters  # noqa: E501
        """
        pass

    def test_slurmdbd_add_wckeys(self):
        """Test case for slurmdbd_add_wckeys

        Add wckeys  # noqa: E501
        """
        pass

    def test_slurmdbd_add_wckeys_0(self):
        """Test case for slurmdbd_add_wckeys_0

        Add wckeys  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_account(self):
        """Test case for slurmdbd_delete_account

        Delete account  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_account_0(self):
        """Test case for slurmdbd_delete_account_0

        Delete account  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_association(self):
        """Test case for slurmdbd_delete_association

        Delete association  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_association_0(self):
        """Test case for slurmdbd_delete_association_0

        Delete association  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_cluster(self):
        """Test case for slurmdbd_delete_cluster

        Delete cluster  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_cluster_0(self):
        """Test case for slurmdbd_delete_cluster_0

        Delete cluster  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_qos(self):
        """Test case for slurmdbd_delete_qos

        Delete QOS  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_qos_0(self):
        """Test case for slurmdbd_delete_qos_0

        Delete QOS  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_user(self):
        """Test case for slurmdbd_delete_user

        Delete user  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_user_0(self):
        """Test case for slurmdbd_delete_user_0

        Delete user  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_wckey(self):
        """Test case for slurmdbd_delete_wckey

        Delete wckey  # noqa: E501
        """
        pass

    def test_slurmdbd_delete_wckey_0(self):
        """Test case for slurmdbd_delete_wckey_0

        Delete wckey  # noqa: E501
        """
        pass

    def test_slurmdbd_diag(self):
        """Test case for slurmdbd_diag

        Get slurmdb diagnostics  # noqa: E501
        """
        pass

    def test_slurmdbd_diag_0(self):
        """Test case for slurmdbd_diag_0

        Get slurmdb diagnostics  # noqa: E501
        """
        pass

    def test_slurmdbd_get_account(self):
        """Test case for slurmdbd_get_account

        Get account info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_account_0(self):
        """Test case for slurmdbd_get_account_0

        Get account info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_accounts(self):
        """Test case for slurmdbd_get_accounts

        Get account list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_accounts_0(self):
        """Test case for slurmdbd_get_accounts_0

        Get account list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_association(self):
        """Test case for slurmdbd_get_association

        Get association info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_association_0(self):
        """Test case for slurmdbd_get_association_0

        Get association info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_associations(self):
        """Test case for slurmdbd_get_associations

        Get association list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_associations_0(self):
        """Test case for slurmdbd_get_associations_0

        Get association list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_cluster(self):
        """Test case for slurmdbd_get_cluster

        Get cluster info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_cluster_0(self):
        """Test case for slurmdbd_get_cluster_0

        Get cluster info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_clusters(self):
        """Test case for slurmdbd_get_clusters

        Get cluster list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_clusters_0(self):
        """Test case for slurmdbd_get_clusters_0

        Get cluster list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_db_config(self):
        """Test case for slurmdbd_get_db_config

        Dump all configuration information  # noqa: E501
        """
        pass

    def test_slurmdbd_get_db_config_0(self):
        """Test case for slurmdbd_get_db_config_0

        Dump all configuration information  # noqa: E501
        """
        pass

    def test_slurmdbd_get_job(self):
        """Test case for slurmdbd_get_job

        Get job info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_job_0(self):
        """Test case for slurmdbd_get_job_0

        Get job info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_jobs(self):
        """Test case for slurmdbd_get_jobs

        Get job list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_jobs_0(self):
        """Test case for slurmdbd_get_jobs_0

        Get job list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_qos(self):
        """Test case for slurmdbd_get_qos

        Get QOS list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_qos_0(self):
        """Test case for slurmdbd_get_qos_0

        Get QOS list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_single_qos(self):
        """Test case for slurmdbd_get_single_qos

        Get QOS info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_single_qos_0(self):
        """Test case for slurmdbd_get_single_qos_0

        Get QOS info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_tres(self):
        """Test case for slurmdbd_get_tres

        Get TRES info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_tres_0(self):
        """Test case for slurmdbd_get_tres_0

        Get TRES info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_user(self):
        """Test case for slurmdbd_get_user

        Get user info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_user_0(self):
        """Test case for slurmdbd_get_user_0

        Get user info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_users(self):
        """Test case for slurmdbd_get_users

        Get user list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_users_0(self):
        """Test case for slurmdbd_get_users_0

        Get user list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_wckey(self):
        """Test case for slurmdbd_get_wckey

        Get wckey info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_wckey_0(self):
        """Test case for slurmdbd_get_wckey_0

        Get wckey info  # noqa: E501
        """
        pass

    def test_slurmdbd_get_wckeys(self):
        """Test case for slurmdbd_get_wckeys

        Get wckey list  # noqa: E501
        """
        pass

    def test_slurmdbd_get_wckeys_0(self):
        """Test case for slurmdbd_get_wckeys_0

        Get wckey list  # noqa: E501
        """
        pass

    def test_slurmdbd_set_db_config(self):
        """Test case for slurmdbd_set_db_config

        Load all configuration information  # noqa: E501
        """
        pass

    def test_slurmdbd_set_db_config_0(self):
        """Test case for slurmdbd_set_db_config_0

        Load all configuration information  # noqa: E501
        """
        pass

    def test_slurmdbd_update_account(self):
        """Test case for slurmdbd_update_account

        Update accounts  # noqa: E501
        """
        pass

    def test_slurmdbd_update_account_0(self):
        """Test case for slurmdbd_update_account_0

        Update accounts  # noqa: E501
        """
        pass

    def test_slurmdbd_update_tres(self):
        """Test case for slurmdbd_update_tres

        Set TRES info  # noqa: E501
        """
        pass

    def test_slurmdbd_update_tres_0(self):
        """Test case for slurmdbd_update_tres_0

        Set TRES info  # noqa: E501
        """
        pass

    def test_slurmdbd_update_users(self):
        """Test case for slurmdbd_update_users

        Update user  # noqa: E501
        """
        pass

    def test_slurmdbd_update_users_0(self):
        """Test case for slurmdbd_update_users_0

        Update user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
