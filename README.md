# slurm-rest
API to access and control Slurm.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.37
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.schedmd.com/](https://www.schedmd.com/)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import slurm_rest
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import slurm_rest
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import slurm_rest
from pprint import pprint
from slurm_rest.api import default_api
from slurm_rest.model.job_properties import JobProperties
from slurm_rest.model.signal import Signal
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurm_rest.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'


# Enter a context with an instance of the API client
with slurm_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    
    try:
        # get diagnostics
        api_instance.slurm_v0035_diag_get()
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_diag_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**slurm_v0035_diag_get**](docs/DefaultApi.md#slurm_v0035_diag_get) | **GET** /slurm/v0.0.35/diag | get diagnostics
*DefaultApi* | [**slurm_v0035_job_job_id_delete**](docs/DefaultApi.md#slurm_v0035_job_job_id_delete) | **DELETE** /slurm/v0.0.35/job/{job_id} | cancel or signal job
*DefaultApi* | [**slurm_v0035_job_job_id_get**](docs/DefaultApi.md#slurm_v0035_job_job_id_get) | **GET** /slurm/v0.0.35/job/{job_id} | get job info
*DefaultApi* | [**slurm_v0035_job_job_id_post**](docs/DefaultApi.md#slurm_v0035_job_job_id_post) | **POST** /slurm/v0.0.35/job/{job_id} | update job
*DefaultApi* | [**slurm_v0035_job_submit_post**](docs/DefaultApi.md#slurm_v0035_job_submit_post) | **POST** /slurm/v0.0.35/job/submit | submit new job
*DefaultApi* | [**slurm_v0035_jobs_get**](docs/DefaultApi.md#slurm_v0035_jobs_get) | **GET** /slurm/v0.0.35/jobs | get list of jobs
*DefaultApi* | [**slurm_v0035_node_node_name_get**](docs/DefaultApi.md#slurm_v0035_node_node_name_get) | **GET** /slurm/v0.0.35/node/{node_name} | get node info
*DefaultApi* | [**slurm_v0035_nodes_get**](docs/DefaultApi.md#slurm_v0035_nodes_get) | **GET** /slurm/v0.0.35/nodes | get all node info
*DefaultApi* | [**slurm_v0035_partition_partition_name_get**](docs/DefaultApi.md#slurm_v0035_partition_partition_name_get) | **GET** /slurm/v0.0.35/partition/{partition_name} | get partition info
*DefaultApi* | [**slurm_v0035_partitions_get**](docs/DefaultApi.md#slurm_v0035_partitions_get) | **GET** /slurm/v0.0.35/partitions | get all partition info
*DefaultApi* | [**slurm_v0035_ping_get**](docs/DefaultApi.md#slurm_v0035_ping_get) | **GET** /slurm/v0.0.35/ping | ping test
*OpenapiApi* | [**openapi_get**](docs/OpenapiApi.md#openapi_get) | **GET** /openapi | Retrieve OpenAPI Specification
*OpenapiApi* | [**openapi_json_get**](docs/OpenapiApi.md#openapi_json_get) | **GET** /openapi.json | Retrieve OpenAPI Specification
*OpenapiApi* | [**openapi_v3_get**](docs/OpenapiApi.md#openapi_v3_get) | **GET** /openapi/v3 | Retrieve OpenAPI Specification
*OpenapiApi* | [**openapi_yaml_get**](docs/OpenapiApi.md#openapi_yaml_get) | **GET** /openapi.yaml | Retrieve OpenAPI Specification
*SlurmApi* | [**slurmctld_cancel_job**](docs/SlurmApi.md#slurmctld_cancel_job) | **DELETE** /slurm/v0.0.37/job/{job_id} | cancel or signal job
*SlurmApi* | [**slurmctld_cancel_job_0**](docs/SlurmApi.md#slurmctld_cancel_job_0) | **DELETE** /slurm/v0.0.36/job/{job_id} | cancel or signal job
*SlurmApi* | [**slurmctld_diag**](docs/SlurmApi.md#slurmctld_diag) | **GET** /slurm/v0.0.37/diag | get diagnostics
*SlurmApi* | [**slurmctld_diag_0**](docs/SlurmApi.md#slurmctld_diag_0) | **GET** /slurm/v0.0.36/diag | get diagnostics
*SlurmApi* | [**slurmctld_get_job**](docs/SlurmApi.md#slurmctld_get_job) | **GET** /slurm/v0.0.37/job/{job_id} | get job info
*SlurmApi* | [**slurmctld_get_job_0**](docs/SlurmApi.md#slurmctld_get_job_0) | **GET** /slurm/v0.0.36/job/{job_id} | get job info
*SlurmApi* | [**slurmctld_get_jobs**](docs/SlurmApi.md#slurmctld_get_jobs) | **GET** /slurm/v0.0.37/jobs | get list of jobs
*SlurmApi* | [**slurmctld_get_jobs_0**](docs/SlurmApi.md#slurmctld_get_jobs_0) | **GET** /slurm/v0.0.36/jobs | get list of jobs
*SlurmApi* | [**slurmctld_get_node**](docs/SlurmApi.md#slurmctld_get_node) | **GET** /slurm/v0.0.37/node/{node_name} | get node info
*SlurmApi* | [**slurmctld_get_node_0**](docs/SlurmApi.md#slurmctld_get_node_0) | **GET** /slurm/v0.0.36/node/{node_name} | get node info
*SlurmApi* | [**slurmctld_get_nodes**](docs/SlurmApi.md#slurmctld_get_nodes) | **GET** /slurm/v0.0.37/nodes | get all node info
*SlurmApi* | [**slurmctld_get_nodes_0**](docs/SlurmApi.md#slurmctld_get_nodes_0) | **GET** /slurm/v0.0.36/nodes | get all node info
*SlurmApi* | [**slurmctld_get_partition**](docs/SlurmApi.md#slurmctld_get_partition) | **GET** /slurm/v0.0.37/partition/{partition_name} | get partition info
*SlurmApi* | [**slurmctld_get_partition_0**](docs/SlurmApi.md#slurmctld_get_partition_0) | **GET** /slurm/v0.0.36/partition/{partition_name} | get partition info
*SlurmApi* | [**slurmctld_get_partitions**](docs/SlurmApi.md#slurmctld_get_partitions) | **GET** /slurm/v0.0.37/partitions | get all partition info
*SlurmApi* | [**slurmctld_get_partitions_0**](docs/SlurmApi.md#slurmctld_get_partitions_0) | **GET** /slurm/v0.0.36/partitions | get all partition info
*SlurmApi* | [**slurmctld_get_reservation**](docs/SlurmApi.md#slurmctld_get_reservation) | **GET** /slurm/v0.0.37/reservation/{reservation_name} | get reservation info
*SlurmApi* | [**slurmctld_get_reservations**](docs/SlurmApi.md#slurmctld_get_reservations) | **GET** /slurm/v0.0.37/reservations | get all reservation info
*SlurmApi* | [**slurmctld_ping**](docs/SlurmApi.md#slurmctld_ping) | **GET** /slurm/v0.0.37/ping | ping test
*SlurmApi* | [**slurmctld_ping_0**](docs/SlurmApi.md#slurmctld_ping_0) | **GET** /slurm/v0.0.36/ping | ping test
*SlurmApi* | [**slurmctld_submit_job**](docs/SlurmApi.md#slurmctld_submit_job) | **POST** /slurm/v0.0.37/job/submit | submit new job
*SlurmApi* | [**slurmctld_submit_job_0**](docs/SlurmApi.md#slurmctld_submit_job_0) | **POST** /slurm/v0.0.36/job/submit | submit new job
*SlurmApi* | [**slurmctld_update_job**](docs/SlurmApi.md#slurmctld_update_job) | **POST** /slurm/v0.0.37/job/{job_id} | update job
*SlurmApi* | [**slurmctld_update_job_0**](docs/SlurmApi.md#slurmctld_update_job_0) | **POST** /slurm/v0.0.36/job/{job_id} | update job
*SlurmApi* | [**slurmdbd_add_clusters**](docs/SlurmApi.md#slurmdbd_add_clusters) | **POST** /slurmdb/v0.0.36/clusters | Add clusters
*SlurmApi* | [**slurmdbd_add_clusters_0**](docs/SlurmApi.md#slurmdbd_add_clusters_0) | **POST** /slurmdb/v0.0.37/clusters | Add clusters
*SlurmApi* | [**slurmdbd_add_wckeys**](docs/SlurmApi.md#slurmdbd_add_wckeys) | **POST** /slurmdb/v0.0.36/wckeys | Add wckeys
*SlurmApi* | [**slurmdbd_add_wckeys_0**](docs/SlurmApi.md#slurmdbd_add_wckeys_0) | **POST** /slurmdb/v0.0.37/wckeys | Add wckeys
*SlurmApi* | [**slurmdbd_delete_account**](docs/SlurmApi.md#slurmdbd_delete_account) | **DELETE** /slurmdb/v0.0.36/account/{account_name} | Delete account
*SlurmApi* | [**slurmdbd_delete_account_0**](docs/SlurmApi.md#slurmdbd_delete_account_0) | **DELETE** /slurmdb/v0.0.37/account/{account_name} | Delete account
*SlurmApi* | [**slurmdbd_delete_association**](docs/SlurmApi.md#slurmdbd_delete_association) | **DELETE** /slurmdb/v0.0.36/association | Delete association
*SlurmApi* | [**slurmdbd_delete_association_0**](docs/SlurmApi.md#slurmdbd_delete_association_0) | **DELETE** /slurmdb/v0.0.37/association | Delete association
*SlurmApi* | [**slurmdbd_delete_cluster**](docs/SlurmApi.md#slurmdbd_delete_cluster) | **DELETE** /slurmdb/v0.0.36/cluster/{cluster_name} | Delete cluster
*SlurmApi* | [**slurmdbd_delete_cluster_0**](docs/SlurmApi.md#slurmdbd_delete_cluster_0) | **DELETE** /slurmdb/v0.0.37/cluster/{cluster_name} | Delete cluster
*SlurmApi* | [**slurmdbd_delete_qos**](docs/SlurmApi.md#slurmdbd_delete_qos) | **DELETE** /slurmdb/v0.0.36/qos/{qos_name} | Delete QOS
*SlurmApi* | [**slurmdbd_delete_qos_0**](docs/SlurmApi.md#slurmdbd_delete_qos_0) | **DELETE** /slurmdb/v0.0.37/qos/{qos_name} | Delete QOS
*SlurmApi* | [**slurmdbd_delete_user**](docs/SlurmApi.md#slurmdbd_delete_user) | **DELETE** /slurmdb/v0.0.36/user/{user_name} | Delete user
*SlurmApi* | [**slurmdbd_delete_user_0**](docs/SlurmApi.md#slurmdbd_delete_user_0) | **DELETE** /slurmdb/v0.0.37/user/{user_name} | Delete user
*SlurmApi* | [**slurmdbd_delete_wckey**](docs/SlurmApi.md#slurmdbd_delete_wckey) | **DELETE** /slurmdb/v0.0.36/wckey/{wckey} | Delete wckey
*SlurmApi* | [**slurmdbd_delete_wckey_0**](docs/SlurmApi.md#slurmdbd_delete_wckey_0) | **DELETE** /slurmdb/v0.0.37/wckey/{wckey} | Delete wckey
*SlurmApi* | [**slurmdbd_diag**](docs/SlurmApi.md#slurmdbd_diag) | **GET** /slurmdb/v0.0.36/diag | Get slurmdb diagnostics
*SlurmApi* | [**slurmdbd_diag_0**](docs/SlurmApi.md#slurmdbd_diag_0) | **GET** /slurmdb/v0.0.37/diag | Get slurmdb diagnostics
*SlurmApi* | [**slurmdbd_get_account**](docs/SlurmApi.md#slurmdbd_get_account) | **GET** /slurmdb/v0.0.36/account/{account_name} | Get account info
*SlurmApi* | [**slurmdbd_get_account_0**](docs/SlurmApi.md#slurmdbd_get_account_0) | **GET** /slurmdb/v0.0.37/account/{account_name} | Get account info
*SlurmApi* | [**slurmdbd_get_accounts**](docs/SlurmApi.md#slurmdbd_get_accounts) | **GET** /slurmdb/v0.0.36/accounts | Get account list
*SlurmApi* | [**slurmdbd_get_accounts_0**](docs/SlurmApi.md#slurmdbd_get_accounts_0) | **GET** /slurmdb/v0.0.37/accounts | Get account list
*SlurmApi* | [**slurmdbd_get_association**](docs/SlurmApi.md#slurmdbd_get_association) | **GET** /slurmdb/v0.0.36/association | Get association info
*SlurmApi* | [**slurmdbd_get_association_0**](docs/SlurmApi.md#slurmdbd_get_association_0) | **GET** /slurmdb/v0.0.37/association | Get association info
*SlurmApi* | [**slurmdbd_get_associations**](docs/SlurmApi.md#slurmdbd_get_associations) | **GET** /slurmdb/v0.0.36/associations | Get association list
*SlurmApi* | [**slurmdbd_get_associations_0**](docs/SlurmApi.md#slurmdbd_get_associations_0) | **GET** /slurmdb/v0.0.37/associations | Get association list
*SlurmApi* | [**slurmdbd_get_cluster**](docs/SlurmApi.md#slurmdbd_get_cluster) | **GET** /slurmdb/v0.0.36/cluster/{cluster_name} | Get cluster info
*SlurmApi* | [**slurmdbd_get_cluster_0**](docs/SlurmApi.md#slurmdbd_get_cluster_0) | **GET** /slurmdb/v0.0.37/cluster/{cluster_name} | Get cluster info
*SlurmApi* | [**slurmdbd_get_clusters**](docs/SlurmApi.md#slurmdbd_get_clusters) | **GET** /slurmdb/v0.0.36/clusters | Get cluster list
*SlurmApi* | [**slurmdbd_get_clusters_0**](docs/SlurmApi.md#slurmdbd_get_clusters_0) | **GET** /slurmdb/v0.0.37/clusters | Get cluster list
*SlurmApi* | [**slurmdbd_get_db_config**](docs/SlurmApi.md#slurmdbd_get_db_config) | **GET** /slurmdb/v0.0.36/config | Dump all configuration information
*SlurmApi* | [**slurmdbd_get_db_config_0**](docs/SlurmApi.md#slurmdbd_get_db_config_0) | **GET** /slurmdb/v0.0.37/config | Dump all configuration information
*SlurmApi* | [**slurmdbd_get_job**](docs/SlurmApi.md#slurmdbd_get_job) | **GET** /slurmdb/v0.0.36/job/{job_id} | Get job info
*SlurmApi* | [**slurmdbd_get_job_0**](docs/SlurmApi.md#slurmdbd_get_job_0) | **GET** /slurmdb/v0.0.37/job/{job_id} | Get job info
*SlurmApi* | [**slurmdbd_get_jobs**](docs/SlurmApi.md#slurmdbd_get_jobs) | **GET** /slurmdb/v0.0.36/jobs | Get job list
*SlurmApi* | [**slurmdbd_get_jobs_0**](docs/SlurmApi.md#slurmdbd_get_jobs_0) | **GET** /slurmdb/v0.0.37/jobs | Get job list
*SlurmApi* | [**slurmdbd_get_qos**](docs/SlurmApi.md#slurmdbd_get_qos) | **GET** /slurmdb/v0.0.36/qos | Get QOS list
*SlurmApi* | [**slurmdbd_get_qos_0**](docs/SlurmApi.md#slurmdbd_get_qos_0) | **GET** /slurmdb/v0.0.37/qos | Get QOS list
*SlurmApi* | [**slurmdbd_get_single_qos**](docs/SlurmApi.md#slurmdbd_get_single_qos) | **GET** /slurmdb/v0.0.36/qos/{qos_name} | Get QOS info
*SlurmApi* | [**slurmdbd_get_single_qos_0**](docs/SlurmApi.md#slurmdbd_get_single_qos_0) | **GET** /slurmdb/v0.0.37/qos/{qos_name} | Get QOS info
*SlurmApi* | [**slurmdbd_get_tres**](docs/SlurmApi.md#slurmdbd_get_tres) | **GET** /slurmdb/v0.0.36/tres | Get TRES info
*SlurmApi* | [**slurmdbd_get_tres_0**](docs/SlurmApi.md#slurmdbd_get_tres_0) | **GET** /slurmdb/v0.0.37/tres | Get TRES info
*SlurmApi* | [**slurmdbd_get_user**](docs/SlurmApi.md#slurmdbd_get_user) | **GET** /slurmdb/v0.0.36/user/{user_name} | Get user info
*SlurmApi* | [**slurmdbd_get_user_0**](docs/SlurmApi.md#slurmdbd_get_user_0) | **GET** /slurmdb/v0.0.37/user/{user_name} | Get user info
*SlurmApi* | [**slurmdbd_get_users**](docs/SlurmApi.md#slurmdbd_get_users) | **GET** /slurmdb/v0.0.36/users | Get user list
*SlurmApi* | [**slurmdbd_get_users_0**](docs/SlurmApi.md#slurmdbd_get_users_0) | **GET** /slurmdb/v0.0.37/users | Get user list
*SlurmApi* | [**slurmdbd_get_wckey**](docs/SlurmApi.md#slurmdbd_get_wckey) | **GET** /slurmdb/v0.0.36/wckey/{wckey} | Get wckey info
*SlurmApi* | [**slurmdbd_get_wckey_0**](docs/SlurmApi.md#slurmdbd_get_wckey_0) | **GET** /slurmdb/v0.0.37/wckey/{wckey} | Get wckey info
*SlurmApi* | [**slurmdbd_get_wckeys**](docs/SlurmApi.md#slurmdbd_get_wckeys) | **GET** /slurmdb/v0.0.36/wckeys | Get wckey list
*SlurmApi* | [**slurmdbd_get_wckeys_0**](docs/SlurmApi.md#slurmdbd_get_wckeys_0) | **GET** /slurmdb/v0.0.37/wckeys | Get wckey list
*SlurmApi* | [**slurmdbd_set_db_config**](docs/SlurmApi.md#slurmdbd_set_db_config) | **POST** /slurmdb/v0.0.36/config | Load all configuration information
*SlurmApi* | [**slurmdbd_set_db_config_0**](docs/SlurmApi.md#slurmdbd_set_db_config_0) | **POST** /slurmdb/v0.0.37/config | Load all configuration information
*SlurmApi* | [**slurmdbd_update_account**](docs/SlurmApi.md#slurmdbd_update_account) | **POST** /slurmdb/v0.0.36/accounts | Update accounts
*SlurmApi* | [**slurmdbd_update_account_0**](docs/SlurmApi.md#slurmdbd_update_account_0) | **POST** /slurmdb/v0.0.37/accounts | Update accounts
*SlurmApi* | [**slurmdbd_update_tres**](docs/SlurmApi.md#slurmdbd_update_tres) | **POST** /slurmdb/v0.0.36/tres | Set TRES info
*SlurmApi* | [**slurmdbd_update_tres_0**](docs/SlurmApi.md#slurmdbd_update_tres_0) | **POST** /slurmdb/v0.0.37/tres | Set TRES info
*SlurmApi* | [**slurmdbd_update_users**](docs/SlurmApi.md#slurmdbd_update_users) | **POST** /slurmdb/v0.0.36/users | Update user
*SlurmApi* | [**slurmdbd_update_users_0**](docs/SlurmApi.md#slurmdbd_update_users_0) | **POST** /slurmdb/v0.0.37/users | Update user


## Documentation For Models

 - [Dbv0036Account](docs/Dbv0036Account.md)
 - [Dbv0036AccountInfo](docs/Dbv0036AccountInfo.md)
 - [Dbv0036AccountResponse](docs/Dbv0036AccountResponse.md)
 - [Dbv0036Association](docs/Dbv0036Association.md)
 - [Dbv0036AssociationDefault](docs/Dbv0036AssociationDefault.md)
 - [Dbv0036AssociationMax](docs/Dbv0036AssociationMax.md)
 - [Dbv0036AssociationMaxJobs](docs/Dbv0036AssociationMaxJobs.md)
 - [Dbv0036AssociationMaxJobsPer](docs/Dbv0036AssociationMaxJobsPer.md)
 - [Dbv0036AssociationMaxPer](docs/Dbv0036AssociationMaxPer.md)
 - [Dbv0036AssociationMaxPerAccount](docs/Dbv0036AssociationMaxPerAccount.md)
 - [Dbv0036AssociationMaxTres](docs/Dbv0036AssociationMaxTres.md)
 - [Dbv0036AssociationMaxTresMinutes](docs/Dbv0036AssociationMaxTresMinutes.md)
 - [Dbv0036AssociationMaxTresMinutesPer](docs/Dbv0036AssociationMaxTresMinutesPer.md)
 - [Dbv0036AssociationMaxTresPer](docs/Dbv0036AssociationMaxTresPer.md)
 - [Dbv0036AssociationMin](docs/Dbv0036AssociationMin.md)
 - [Dbv0036AssociationShortInfo](docs/Dbv0036AssociationShortInfo.md)
 - [Dbv0036AssociationUsage](docs/Dbv0036AssociationUsage.md)
 - [Dbv0036AssociationsInfo](docs/Dbv0036AssociationsInfo.md)
 - [Dbv0036ClusterInfo](docs/Dbv0036ClusterInfo.md)
 - [Dbv0036ClusterInfoAssociations](docs/Dbv0036ClusterInfoAssociations.md)
 - [Dbv0036ClusterInfoController](docs/Dbv0036ClusterInfoController.md)
 - [Dbv0036ConfigInfo](docs/Dbv0036ConfigInfo.md)
 - [Dbv0036ConfigResponse](docs/Dbv0036ConfigResponse.md)
 - [Dbv0036CoordinatorInfo](docs/Dbv0036CoordinatorInfo.md)
 - [Dbv0036Diag](docs/Dbv0036Diag.md)
 - [Dbv0036DiagRPCs](docs/Dbv0036DiagRPCs.md)
 - [Dbv0036DiagRollups](docs/Dbv0036DiagRollups.md)
 - [Dbv0036DiagTime](docs/Dbv0036DiagTime.md)
 - [Dbv0036DiagTime1](docs/Dbv0036DiagTime1.md)
 - [Dbv0036DiagUsers](docs/Dbv0036DiagUsers.md)
 - [Dbv0036Error](docs/Dbv0036Error.md)
 - [Dbv0036Job](docs/Dbv0036Job.md)
 - [Dbv0036JobArray](docs/Dbv0036JobArray.md)
 - [Dbv0036JobArrayLimits](docs/Dbv0036JobArrayLimits.md)
 - [Dbv0036JobArrayLimitsMax](docs/Dbv0036JobArrayLimitsMax.md)
 - [Dbv0036JobArrayLimitsMaxRunning](docs/Dbv0036JobArrayLimitsMaxRunning.md)
 - [Dbv0036JobComment](docs/Dbv0036JobComment.md)
 - [Dbv0036JobExitCode](docs/Dbv0036JobExitCode.md)
 - [Dbv0036JobExitCodeSignal](docs/Dbv0036JobExitCodeSignal.md)
 - [Dbv0036JobHet](docs/Dbv0036JobHet.md)
 - [Dbv0036JobInfo](docs/Dbv0036JobInfo.md)
 - [Dbv0036JobMcs](docs/Dbv0036JobMcs.md)
 - [Dbv0036JobRequired](docs/Dbv0036JobRequired.md)
 - [Dbv0036JobReservation](docs/Dbv0036JobReservation.md)
 - [Dbv0036JobState](docs/Dbv0036JobState.md)
 - [Dbv0036JobStep](docs/Dbv0036JobStep.md)
 - [Dbv0036JobStepCPU](docs/Dbv0036JobStepCPU.md)
 - [Dbv0036JobStepCPURequestedFrequency](docs/Dbv0036JobStepCPURequestedFrequency.md)
 - [Dbv0036JobStepNodes](docs/Dbv0036JobStepNodes.md)
 - [Dbv0036JobStepStatistics](docs/Dbv0036JobStepStatistics.md)
 - [Dbv0036JobStepStatisticsCPU](docs/Dbv0036JobStepStatisticsCPU.md)
 - [Dbv0036JobStepStatisticsEnergy](docs/Dbv0036JobStepStatisticsEnergy.md)
 - [Dbv0036JobStepStep](docs/Dbv0036JobStepStep.md)
 - [Dbv0036JobStepStepHet](docs/Dbv0036JobStepStepHet.md)
 - [Dbv0036JobStepStepTask](docs/Dbv0036JobStepStepTask.md)
 - [Dbv0036JobStepStepTres](docs/Dbv0036JobStepStepTres.md)
 - [Dbv0036JobStepStepTresRequested](docs/Dbv0036JobStepStepTresRequested.md)
 - [Dbv0036JobStepTasks](docs/Dbv0036JobStepTasks.md)
 - [Dbv0036JobStepTime](docs/Dbv0036JobStepTime.md)
 - [Dbv0036JobTime](docs/Dbv0036JobTime.md)
 - [Dbv0036JobTimeSystem](docs/Dbv0036JobTimeSystem.md)
 - [Dbv0036JobTimeTotal](docs/Dbv0036JobTimeTotal.md)
 - [Dbv0036JobTimeUser](docs/Dbv0036JobTimeUser.md)
 - [Dbv0036JobTres](docs/Dbv0036JobTres.md)
 - [Dbv0036JobWckey](docs/Dbv0036JobWckey.md)
 - [Dbv0036Qos](docs/Dbv0036Qos.md)
 - [Dbv0036QosInfo](docs/Dbv0036QosInfo.md)
 - [Dbv0036QosLimits](docs/Dbv0036QosLimits.md)
 - [Dbv0036QosLimitsMax](docs/Dbv0036QosLimitsMax.md)
 - [Dbv0036QosLimitsMaxAccruing](docs/Dbv0036QosLimitsMaxAccruing.md)
 - [Dbv0036QosLimitsMaxAccruingPer](docs/Dbv0036QosLimitsMaxAccruingPer.md)
 - [Dbv0036QosLimitsMaxJobs](docs/Dbv0036QosLimitsMaxJobs.md)
 - [Dbv0036QosLimitsMaxJobsPer](docs/Dbv0036QosLimitsMaxJobsPer.md)
 - [Dbv0036QosLimitsMaxTres](docs/Dbv0036QosLimitsMaxTres.md)
 - [Dbv0036QosLimitsMaxTresMinutes](docs/Dbv0036QosLimitsMaxTresMinutes.md)
 - [Dbv0036QosLimitsMaxTresMinutesPer](docs/Dbv0036QosLimitsMaxTresMinutesPer.md)
 - [Dbv0036QosLimitsMaxTresPer](docs/Dbv0036QosLimitsMaxTresPer.md)
 - [Dbv0036QosLimitsMaxWallClock](docs/Dbv0036QosLimitsMaxWallClock.md)
 - [Dbv0036QosLimitsMaxWallClockPer](docs/Dbv0036QosLimitsMaxWallClockPer.md)
 - [Dbv0036QosLimitsMin](docs/Dbv0036QosLimitsMin.md)
 - [Dbv0036QosLimitsMinTres](docs/Dbv0036QosLimitsMinTres.md)
 - [Dbv0036QosLimitsMinTresPer](docs/Dbv0036QosLimitsMinTresPer.md)
 - [Dbv0036QosPreempt](docs/Dbv0036QosPreempt.md)
 - [Dbv0036ResponseAccountDelete](docs/Dbv0036ResponseAccountDelete.md)
 - [Dbv0036ResponseAssociationDelete](docs/Dbv0036ResponseAssociationDelete.md)
 - [Dbv0036ResponseClusterAdd](docs/Dbv0036ResponseClusterAdd.md)
 - [Dbv0036ResponseClusterDelete](docs/Dbv0036ResponseClusterDelete.md)
 - [Dbv0036ResponseQosDelete](docs/Dbv0036ResponseQosDelete.md)
 - [Dbv0036ResponseTres](docs/Dbv0036ResponseTres.md)
 - [Dbv0036ResponseUserDelete](docs/Dbv0036ResponseUserDelete.md)
 - [Dbv0036ResponseUserUpdate](docs/Dbv0036ResponseUserUpdate.md)
 - [Dbv0036ResponseWckeyAdd](docs/Dbv0036ResponseWckeyAdd.md)
 - [Dbv0036ResponseWckeyDelete](docs/Dbv0036ResponseWckeyDelete.md)
 - [Dbv0036TresInfo](docs/Dbv0036TresInfo.md)
 - [Dbv0036TresList](docs/Dbv0036TresList.md)
 - [Dbv0036User](docs/Dbv0036User.md)
 - [Dbv0036UserAssociations](docs/Dbv0036UserAssociations.md)
 - [Dbv0036UserDefault](docs/Dbv0036UserDefault.md)
 - [Dbv0036UserInfo](docs/Dbv0036UserInfo.md)
 - [Dbv0036Wckey](docs/Dbv0036Wckey.md)
 - [Dbv0036WckeyInfo](docs/Dbv0036WckeyInfo.md)
 - [Dbv0037Account](docs/Dbv0037Account.md)
 - [Dbv0037AccountInfo](docs/Dbv0037AccountInfo.md)
 - [Dbv0037AccountResponse](docs/Dbv0037AccountResponse.md)
 - [Dbv0037Association](docs/Dbv0037Association.md)
 - [Dbv0037AssociationMax](docs/Dbv0037AssociationMax.md)
 - [Dbv0037AssociationMaxTres](docs/Dbv0037AssociationMaxTres.md)
 - [Dbv0037AssociationMaxTresMinutes](docs/Dbv0037AssociationMaxTresMinutes.md)
 - [Dbv0037AssociationMaxTresMinutesPer](docs/Dbv0037AssociationMaxTresMinutesPer.md)
 - [Dbv0037AssociationMaxTresPer](docs/Dbv0037AssociationMaxTresPer.md)
 - [Dbv0037AssociationShortInfo](docs/Dbv0037AssociationShortInfo.md)
 - [Dbv0037AssociationsInfo](docs/Dbv0037AssociationsInfo.md)
 - [Dbv0037ClusterInfo](docs/Dbv0037ClusterInfo.md)
 - [Dbv0037ClusterInfoAssociations](docs/Dbv0037ClusterInfoAssociations.md)
 - [Dbv0037ConfigInfo](docs/Dbv0037ConfigInfo.md)
 - [Dbv0037ConfigResponse](docs/Dbv0037ConfigResponse.md)
 - [Dbv0037CoordinatorInfo](docs/Dbv0037CoordinatorInfo.md)
 - [Dbv0037Diag](docs/Dbv0037Diag.md)
 - [Dbv0037Error](docs/Dbv0037Error.md)
 - [Dbv0037Job](docs/Dbv0037Job.md)
 - [Dbv0037JobExitCode](docs/Dbv0037JobExitCode.md)
 - [Dbv0037JobInfo](docs/Dbv0037JobInfo.md)
 - [Dbv0037JobState](docs/Dbv0037JobState.md)
 - [Dbv0037JobStep](docs/Dbv0037JobStep.md)
 - [Dbv0037JobStepStep](docs/Dbv0037JobStepStep.md)
 - [Dbv0037JobStepStepTres](docs/Dbv0037JobStepStepTres.md)
 - [Dbv0037JobStepStepTresRequested](docs/Dbv0037JobStepStepTresRequested.md)
 - [Dbv0037JobTres](docs/Dbv0037JobTres.md)
 - [Dbv0037Qos](docs/Dbv0037Qos.md)
 - [Dbv0037QosInfo](docs/Dbv0037QosInfo.md)
 - [Dbv0037QosLimits](docs/Dbv0037QosLimits.md)
 - [Dbv0037QosLimitsMax](docs/Dbv0037QosLimitsMax.md)
 - [Dbv0037QosLimitsMaxTres](docs/Dbv0037QosLimitsMaxTres.md)
 - [Dbv0037QosLimitsMaxTresMinutes](docs/Dbv0037QosLimitsMaxTresMinutes.md)
 - [Dbv0037QosLimitsMaxTresMinutesPer](docs/Dbv0037QosLimitsMaxTresMinutesPer.md)
 - [Dbv0037QosLimitsMaxTresPer](docs/Dbv0037QosLimitsMaxTresPer.md)
 - [Dbv0037QosLimitsMin](docs/Dbv0037QosLimitsMin.md)
 - [Dbv0037QosLimitsMinTres](docs/Dbv0037QosLimitsMinTres.md)
 - [Dbv0037QosLimitsMinTresPer](docs/Dbv0037QosLimitsMinTresPer.md)
 - [Dbv0037ResponseAccountDelete](docs/Dbv0037ResponseAccountDelete.md)
 - [Dbv0037ResponseAssociationDelete](docs/Dbv0037ResponseAssociationDelete.md)
 - [Dbv0037ResponseClusterAdd](docs/Dbv0037ResponseClusterAdd.md)
 - [Dbv0037ResponseClusterDelete](docs/Dbv0037ResponseClusterDelete.md)
 - [Dbv0037ResponseQosDelete](docs/Dbv0037ResponseQosDelete.md)
 - [Dbv0037ResponseTres](docs/Dbv0037ResponseTres.md)
 - [Dbv0037ResponseUserDelete](docs/Dbv0037ResponseUserDelete.md)
 - [Dbv0037ResponseUserUpdate](docs/Dbv0037ResponseUserUpdate.md)
 - [Dbv0037ResponseWckeyAdd](docs/Dbv0037ResponseWckeyAdd.md)
 - [Dbv0037ResponseWckeyDelete](docs/Dbv0037ResponseWckeyDelete.md)
 - [Dbv0037TresInfo](docs/Dbv0037TresInfo.md)
 - [Dbv0037TresList](docs/Dbv0037TresList.md)
 - [Dbv0037User](docs/Dbv0037User.md)
 - [Dbv0037UserAssociations](docs/Dbv0037UserAssociations.md)
 - [Dbv0037UserInfo](docs/Dbv0037UserInfo.md)
 - [Dbv0037Wckey](docs/Dbv0037Wckey.md)
 - [Dbv0037WckeyInfo](docs/Dbv0037WckeyInfo.md)
 - [JobProperties](docs/JobProperties.md)
 - [Signal](docs/Signal.md)
 - [SignalOneOf](docs/SignalOneOf.md)
 - [V0036Diag](docs/V0036Diag.md)
 - [V0036Error](docs/V0036Error.md)
 - [V0036JobProperties](docs/V0036JobProperties.md)
 - [V0036JobResources](docs/V0036JobResources.md)
 - [V0036JobResponseProperties](docs/V0036JobResponseProperties.md)
 - [V0036JobSubmission](docs/V0036JobSubmission.md)
 - [V0036JobSubmissionResponse](docs/V0036JobSubmissionResponse.md)
 - [V0036JobsResponse](docs/V0036JobsResponse.md)
 - [V0036Node](docs/V0036Node.md)
 - [V0036NodeAllocation](docs/V0036NodeAllocation.md)
 - [V0036NodesResponse](docs/V0036NodesResponse.md)
 - [V0036Partition](docs/V0036Partition.md)
 - [V0036PartitionsResponse](docs/V0036PartitionsResponse.md)
 - [V0036Ping](docs/V0036Ping.md)
 - [V0036Pings](docs/V0036Pings.md)
 - [V0036Signal](docs/V0036Signal.md)
 - [V0037Diag](docs/V0037Diag.md)
 - [V0037DiagStatistics](docs/V0037DiagStatistics.md)
 - [V0037Error](docs/V0037Error.md)
 - [V0037JobProperties](docs/V0037JobProperties.md)
 - [V0037JobResources](docs/V0037JobResources.md)
 - [V0037JobResponseProperties](docs/V0037JobResponseProperties.md)
 - [V0037JobSubmission](docs/V0037JobSubmission.md)
 - [V0037JobSubmissionResponse](docs/V0037JobSubmissionResponse.md)
 - [V0037JobsResponse](docs/V0037JobsResponse.md)
 - [V0037Node](docs/V0037Node.md)
 - [V0037NodeAllocation](docs/V0037NodeAllocation.md)
 - [V0037NodesResponse](docs/V0037NodesResponse.md)
 - [V0037Partition](docs/V0037Partition.md)
 - [V0037PartitionsResponse](docs/V0037PartitionsResponse.md)
 - [V0037Ping](docs/V0037Ping.md)
 - [V0037Pings](docs/V0037Pings.md)
 - [V0037Reservation](docs/V0037Reservation.md)
 - [V0037ReservationPurgeCompleted](docs/V0037ReservationPurgeCompleted.md)
 - [V0037ReservationsResponse](docs/V0037ReservationsResponse.md)
 - [V0037Signal](docs/V0037Signal.md)


## Documentation For Authorization


## token

- **Type**: API key
- **API key parameter name**: X-SLURM-USER-TOKEN
- **Location**: HTTP header


## user

- **Type**: API key
- **API key parameter name**: X-SLURM-USER-NAME
- **Location**: HTTP header


## Author

sales@schedmd.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in slurm_rest.apis and slurm_rest.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from slurm_rest.api.default_api import DefaultApi`
- `from slurm_rest.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import slurm_rest
from slurm_rest.apis import *
from slurm_rest.models import *
```

