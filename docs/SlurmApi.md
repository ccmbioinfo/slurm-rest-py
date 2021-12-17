# slurm_rest.SlurmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurmctld_cancel_job**](SlurmApi.md#slurmctld_cancel_job) | **DELETE** /slurm/v0.0.37/job/{job_id} | cancel or signal job
[**slurmctld_cancel_job_0**](SlurmApi.md#slurmctld_cancel_job_0) | **DELETE** /slurm/v0.0.36/job/{job_id} | cancel or signal job
[**slurmctld_diag**](SlurmApi.md#slurmctld_diag) | **GET** /slurm/v0.0.37/diag | get diagnostics
[**slurmctld_diag_0**](SlurmApi.md#slurmctld_diag_0) | **GET** /slurm/v0.0.36/diag | get diagnostics
[**slurmctld_get_job**](SlurmApi.md#slurmctld_get_job) | **GET** /slurm/v0.0.37/job/{job_id} | get job info
[**slurmctld_get_job_0**](SlurmApi.md#slurmctld_get_job_0) | **GET** /slurm/v0.0.36/job/{job_id} | get job info
[**slurmctld_get_jobs**](SlurmApi.md#slurmctld_get_jobs) | **GET** /slurm/v0.0.37/jobs | get list of jobs
[**slurmctld_get_jobs_0**](SlurmApi.md#slurmctld_get_jobs_0) | **GET** /slurm/v0.0.36/jobs | get list of jobs
[**slurmctld_get_node**](SlurmApi.md#slurmctld_get_node) | **GET** /slurm/v0.0.37/node/{node_name} | get node info
[**slurmctld_get_node_0**](SlurmApi.md#slurmctld_get_node_0) | **GET** /slurm/v0.0.36/node/{node_name} | get node info
[**slurmctld_get_nodes**](SlurmApi.md#slurmctld_get_nodes) | **GET** /slurm/v0.0.37/nodes | get all node info
[**slurmctld_get_nodes_0**](SlurmApi.md#slurmctld_get_nodes_0) | **GET** /slurm/v0.0.36/nodes | get all node info
[**slurmctld_get_partition**](SlurmApi.md#slurmctld_get_partition) | **GET** /slurm/v0.0.37/partition/{partition_name} | get partition info
[**slurmctld_get_partition_0**](SlurmApi.md#slurmctld_get_partition_0) | **GET** /slurm/v0.0.36/partition/{partition_name} | get partition info
[**slurmctld_get_partitions**](SlurmApi.md#slurmctld_get_partitions) | **GET** /slurm/v0.0.37/partitions | get all partition info
[**slurmctld_get_partitions_0**](SlurmApi.md#slurmctld_get_partitions_0) | **GET** /slurm/v0.0.36/partitions | get all partition info
[**slurmctld_get_reservation**](SlurmApi.md#slurmctld_get_reservation) | **GET** /slurm/v0.0.37/reservation/{reservation_name} | get reservation info
[**slurmctld_get_reservations**](SlurmApi.md#slurmctld_get_reservations) | **GET** /slurm/v0.0.37/reservations | get all reservation info
[**slurmctld_ping**](SlurmApi.md#slurmctld_ping) | **GET** /slurm/v0.0.37/ping | ping test
[**slurmctld_ping_0**](SlurmApi.md#slurmctld_ping_0) | **GET** /slurm/v0.0.36/ping | ping test
[**slurmctld_submit_job**](SlurmApi.md#slurmctld_submit_job) | **POST** /slurm/v0.0.37/job/submit | submit new job
[**slurmctld_submit_job_0**](SlurmApi.md#slurmctld_submit_job_0) | **POST** /slurm/v0.0.36/job/submit | submit new job
[**slurmctld_update_job**](SlurmApi.md#slurmctld_update_job) | **POST** /slurm/v0.0.37/job/{job_id} | update job
[**slurmctld_update_job_0**](SlurmApi.md#slurmctld_update_job_0) | **POST** /slurm/v0.0.36/job/{job_id} | update job
[**slurmdbd_add_clusters**](SlurmApi.md#slurmdbd_add_clusters) | **POST** /slurmdb/v0.0.36/clusters | Add clusters
[**slurmdbd_add_clusters_0**](SlurmApi.md#slurmdbd_add_clusters_0) | **POST** /slurmdb/v0.0.37/clusters | Add clusters
[**slurmdbd_add_wckeys**](SlurmApi.md#slurmdbd_add_wckeys) | **POST** /slurmdb/v0.0.36/wckeys | Add wckeys
[**slurmdbd_add_wckeys_0**](SlurmApi.md#slurmdbd_add_wckeys_0) | **POST** /slurmdb/v0.0.37/wckeys | Add wckeys
[**slurmdbd_delete_account**](SlurmApi.md#slurmdbd_delete_account) | **DELETE** /slurmdb/v0.0.36/account/{account_name} | Delete account
[**slurmdbd_delete_account_0**](SlurmApi.md#slurmdbd_delete_account_0) | **DELETE** /slurmdb/v0.0.37/account/{account_name} | Delete account
[**slurmdbd_delete_association**](SlurmApi.md#slurmdbd_delete_association) | **DELETE** /slurmdb/v0.0.36/association | Delete association
[**slurmdbd_delete_association_0**](SlurmApi.md#slurmdbd_delete_association_0) | **DELETE** /slurmdb/v0.0.37/association | Delete association
[**slurmdbd_delete_cluster**](SlurmApi.md#slurmdbd_delete_cluster) | **DELETE** /slurmdb/v0.0.36/cluster/{cluster_name} | Delete cluster
[**slurmdbd_delete_cluster_0**](SlurmApi.md#slurmdbd_delete_cluster_0) | **DELETE** /slurmdb/v0.0.37/cluster/{cluster_name} | Delete cluster
[**slurmdbd_delete_qos**](SlurmApi.md#slurmdbd_delete_qos) | **DELETE** /slurmdb/v0.0.36/qos/{qos_name} | Delete QOS
[**slurmdbd_delete_qos_0**](SlurmApi.md#slurmdbd_delete_qos_0) | **DELETE** /slurmdb/v0.0.37/qos/{qos_name} | Delete QOS
[**slurmdbd_delete_user**](SlurmApi.md#slurmdbd_delete_user) | **DELETE** /slurmdb/v0.0.36/user/{user_name} | Delete user
[**slurmdbd_delete_user_0**](SlurmApi.md#slurmdbd_delete_user_0) | **DELETE** /slurmdb/v0.0.37/user/{user_name} | Delete user
[**slurmdbd_delete_wckey**](SlurmApi.md#slurmdbd_delete_wckey) | **DELETE** /slurmdb/v0.0.36/wckey/{wckey} | Delete wckey
[**slurmdbd_delete_wckey_0**](SlurmApi.md#slurmdbd_delete_wckey_0) | **DELETE** /slurmdb/v0.0.37/wckey/{wckey} | Delete wckey
[**slurmdbd_diag**](SlurmApi.md#slurmdbd_diag) | **GET** /slurmdb/v0.0.36/diag | Get slurmdb diagnostics
[**slurmdbd_diag_0**](SlurmApi.md#slurmdbd_diag_0) | **GET** /slurmdb/v0.0.37/diag | Get slurmdb diagnostics
[**slurmdbd_get_account**](SlurmApi.md#slurmdbd_get_account) | **GET** /slurmdb/v0.0.36/account/{account_name} | Get account info
[**slurmdbd_get_account_0**](SlurmApi.md#slurmdbd_get_account_0) | **GET** /slurmdb/v0.0.37/account/{account_name} | Get account info
[**slurmdbd_get_accounts**](SlurmApi.md#slurmdbd_get_accounts) | **GET** /slurmdb/v0.0.36/accounts | Get account list
[**slurmdbd_get_accounts_0**](SlurmApi.md#slurmdbd_get_accounts_0) | **GET** /slurmdb/v0.0.37/accounts | Get account list
[**slurmdbd_get_association**](SlurmApi.md#slurmdbd_get_association) | **GET** /slurmdb/v0.0.36/association | Get association info
[**slurmdbd_get_association_0**](SlurmApi.md#slurmdbd_get_association_0) | **GET** /slurmdb/v0.0.37/association | Get association info
[**slurmdbd_get_associations**](SlurmApi.md#slurmdbd_get_associations) | **GET** /slurmdb/v0.0.36/associations | Get association list
[**slurmdbd_get_associations_0**](SlurmApi.md#slurmdbd_get_associations_0) | **GET** /slurmdb/v0.0.37/associations | Get association list
[**slurmdbd_get_cluster**](SlurmApi.md#slurmdbd_get_cluster) | **GET** /slurmdb/v0.0.36/cluster/{cluster_name} | Get cluster info
[**slurmdbd_get_cluster_0**](SlurmApi.md#slurmdbd_get_cluster_0) | **GET** /slurmdb/v0.0.37/cluster/{cluster_name} | Get cluster info
[**slurmdbd_get_clusters**](SlurmApi.md#slurmdbd_get_clusters) | **GET** /slurmdb/v0.0.36/clusters | Get cluster list
[**slurmdbd_get_clusters_0**](SlurmApi.md#slurmdbd_get_clusters_0) | **GET** /slurmdb/v0.0.37/clusters | Get cluster list
[**slurmdbd_get_db_config**](SlurmApi.md#slurmdbd_get_db_config) | **GET** /slurmdb/v0.0.36/config | Dump all configuration information
[**slurmdbd_get_db_config_0**](SlurmApi.md#slurmdbd_get_db_config_0) | **GET** /slurmdb/v0.0.37/config | Dump all configuration information
[**slurmdbd_get_job**](SlurmApi.md#slurmdbd_get_job) | **GET** /slurmdb/v0.0.36/job/{job_id} | Get job info
[**slurmdbd_get_job_0**](SlurmApi.md#slurmdbd_get_job_0) | **GET** /slurmdb/v0.0.37/job/{job_id} | Get job info
[**slurmdbd_get_jobs**](SlurmApi.md#slurmdbd_get_jobs) | **GET** /slurmdb/v0.0.36/jobs | Get job list
[**slurmdbd_get_jobs_0**](SlurmApi.md#slurmdbd_get_jobs_0) | **GET** /slurmdb/v0.0.37/jobs | Get job list
[**slurmdbd_get_qos**](SlurmApi.md#slurmdbd_get_qos) | **GET** /slurmdb/v0.0.36/qos | Get QOS list
[**slurmdbd_get_qos_0**](SlurmApi.md#slurmdbd_get_qos_0) | **GET** /slurmdb/v0.0.37/qos | Get QOS list
[**slurmdbd_get_single_qos**](SlurmApi.md#slurmdbd_get_single_qos) | **GET** /slurmdb/v0.0.36/qos/{qos_name} | Get QOS info
[**slurmdbd_get_single_qos_0**](SlurmApi.md#slurmdbd_get_single_qos_0) | **GET** /slurmdb/v0.0.37/qos/{qos_name} | Get QOS info
[**slurmdbd_get_tres**](SlurmApi.md#slurmdbd_get_tres) | **GET** /slurmdb/v0.0.36/tres | Get TRES info
[**slurmdbd_get_tres_0**](SlurmApi.md#slurmdbd_get_tres_0) | **GET** /slurmdb/v0.0.37/tres | Get TRES info
[**slurmdbd_get_user**](SlurmApi.md#slurmdbd_get_user) | **GET** /slurmdb/v0.0.36/user/{user_name} | Get user info
[**slurmdbd_get_user_0**](SlurmApi.md#slurmdbd_get_user_0) | **GET** /slurmdb/v0.0.37/user/{user_name} | Get user info
[**slurmdbd_get_users**](SlurmApi.md#slurmdbd_get_users) | **GET** /slurmdb/v0.0.36/users | Get user list
[**slurmdbd_get_users_0**](SlurmApi.md#slurmdbd_get_users_0) | **GET** /slurmdb/v0.0.37/users | Get user list
[**slurmdbd_get_wckey**](SlurmApi.md#slurmdbd_get_wckey) | **GET** /slurmdb/v0.0.36/wckey/{wckey} | Get wckey info
[**slurmdbd_get_wckey_0**](SlurmApi.md#slurmdbd_get_wckey_0) | **GET** /slurmdb/v0.0.37/wckey/{wckey} | Get wckey info
[**slurmdbd_get_wckeys**](SlurmApi.md#slurmdbd_get_wckeys) | **GET** /slurmdb/v0.0.36/wckeys | Get wckey list
[**slurmdbd_get_wckeys_0**](SlurmApi.md#slurmdbd_get_wckeys_0) | **GET** /slurmdb/v0.0.37/wckeys | Get wckey list
[**slurmdbd_set_db_config**](SlurmApi.md#slurmdbd_set_db_config) | **POST** /slurmdb/v0.0.36/config | Load all configuration information
[**slurmdbd_set_db_config_0**](SlurmApi.md#slurmdbd_set_db_config_0) | **POST** /slurmdb/v0.0.37/config | Load all configuration information
[**slurmdbd_update_account**](SlurmApi.md#slurmdbd_update_account) | **POST** /slurmdb/v0.0.36/accounts | Update accounts
[**slurmdbd_update_account_0**](SlurmApi.md#slurmdbd_update_account_0) | **POST** /slurmdb/v0.0.37/accounts | Update accounts
[**slurmdbd_update_tres**](SlurmApi.md#slurmdbd_update_tres) | **POST** /slurmdb/v0.0.36/tres | Set TRES info
[**slurmdbd_update_tres_0**](SlurmApi.md#slurmdbd_update_tres_0) | **POST** /slurmdb/v0.0.37/tres | Set TRES info
[**slurmdbd_update_users**](SlurmApi.md#slurmdbd_update_users) | **POST** /slurmdb/v0.0.36/users | Update user
[**slurmdbd_update_users_0**](SlurmApi.md#slurmdbd_update_users_0) | **POST** /slurmdb/v0.0.37/users | Update user


# **slurmctld_cancel_job**
> slurmctld_cancel_job(job_id)

cancel or signal job

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_signal import V0037Signal
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    job_id = 1 # int | Slurm Job ID
    signal = V0037Signal("HUP") # V0037Signal | signal to send to job (optional)

    # example passing only required values which don't have defaults set
    try:
        # cancel or signal job
        api_instance.slurmctld_cancel_job(job_id)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_cancel_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # cancel or signal job
        api_instance.slurmctld_cancel_job(job_id, signal=signal)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_cancel_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |
 **signal** | **V0037Signal**| signal to send to job | [optional]

### Return type

void (empty response body)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job cancelled or sent signal |  -  |
**500** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_cancel_job_0**
> slurmctld_cancel_job_0(job_id)

cancel or signal job

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_signal import V0036Signal
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    job_id = 1 # int | Slurm Job ID
    signal = V0036Signal("HUP") # V0036Signal | signal to send to job (optional)

    # example passing only required values which don't have defaults set
    try:
        # cancel or signal job
        api_instance.slurmctld_cancel_job_0(job_id)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_cancel_job_0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # cancel or signal job
        api_instance.slurmctld_cancel_job_0(job_id, signal=signal)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_cancel_job_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |
 **signal** | **V0036Signal**| signal to send to job | [optional]

### Return type

void (empty response body)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job cancelled or sent signal |  -  |
**500** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_diag**
> V0037Diag slurmctld_diag()

get diagnostics

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_diag import V0037Diag
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get diagnostics
        api_response = api_instance.slurmctld_diag()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_diag: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**V0037Diag**](V0037Diag.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_diag_0**
> V0036Diag slurmctld_diag_0()

get diagnostics

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_diag import V0036Diag
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get diagnostics
        api_response = api_instance.slurmctld_diag_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_diag_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**V0036Diag**](V0036Diag.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_job**
> V0037JobsResponse slurmctld_get_job(job_id)

get job info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_jobs_response import V0037JobsResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    job_id = 1 # int | Slurm Job ID

    # example passing only required values which don't have defaults set
    try:
        # get job info
        api_response = api_instance.slurmctld_get_job(job_id)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |

### Return type

[**V0037JobsResponse**](V0037JobsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_job_0**
> V0036JobsResponse slurmctld_get_job_0(job_id)

get job info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_jobs_response import V0036JobsResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    job_id = 1 # int | Slurm Job ID

    # example passing only required values which don't have defaults set
    try:
        # get job info
        api_response = api_instance.slurmctld_get_job_0(job_id)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_job_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |

### Return type

[**V0036JobsResponse**](V0036JobsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_jobs**
> V0037JobsResponse slurmctld_get_jobs()

get list of jobs

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_jobs_response import V0037JobsResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    update_time = 1 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get list of jobs
        api_response = api_instance.slurmctld_get_jobs(update_time=update_time)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_jobs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional]

### Return type

[**V0037JobsResponse**](V0037JobsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_jobs_0**
> V0036JobsResponse slurmctld_get_jobs_0()

get list of jobs

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_jobs_response import V0036JobsResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get list of jobs
        api_response = api_instance.slurmctld_get_jobs_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_jobs_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**V0036JobsResponse**](V0036JobsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_node**
> V0037NodesResponse slurmctld_get_node(node_name)

get node info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_nodes_response import V0037NodesResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    node_name = "node_name_example" # str | Slurm Node Name

    # example passing only required values which don't have defaults set
    try:
        # get node info
        api_response = api_instance.slurmctld_get_node(node_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Slurm Node Name |

### Return type

[**V0037NodesResponse**](V0037NodesResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_node_0**
> V0036NodesResponse slurmctld_get_node_0(node_name)

get node info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_nodes_response import V0036NodesResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    node_name = "node_name_example" # str | Slurm Node Name

    # example passing only required values which don't have defaults set
    try:
        # get node info
        api_response = api_instance.slurmctld_get_node_0(node_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_node_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Slurm Node Name |

### Return type

[**V0036NodesResponse**](V0036NodesResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_nodes**
> V0037NodesResponse slurmctld_get_nodes()

get all node info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_nodes_response import V0037NodesResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    update_time = 1 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get all node info
        api_response = api_instance.slurmctld_get_nodes(update_time=update_time)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional]

### Return type

[**V0037NodesResponse**](V0037NodesResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | no nodes in cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_nodes_0**
> V0036NodesResponse slurmctld_get_nodes_0()

get all node info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_nodes_response import V0036NodesResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get all node info
        api_response = api_instance.slurmctld_get_nodes_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_nodes_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**V0036NodesResponse**](V0036NodesResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | no nodes in cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_partition**
> V0037PartitionsResponse slurmctld_get_partition(partition_name)

get partition info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_partitions_response import V0037PartitionsResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    partition_name = "partition_name_example" # str | Slurm Partition Name
    update_time = 1 # int | Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time. (optional)

    # example passing only required values which don't have defaults set
    try:
        # get partition info
        api_response = api_instance.slurmctld_get_partition(partition_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_partition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get partition info
        api_response = api_instance.slurmctld_get_partition(partition_name, update_time=update_time)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_partition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Slurm Partition Name |
 **update_time** | **int**| Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time. | [optional]

### Return type

[**V0037PartitionsResponse**](V0037PartitionsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_partition_0**
> V0036PartitionsResponse slurmctld_get_partition_0(partition_name)

get partition info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_partitions_response import V0036PartitionsResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    partition_name = "partition_name_example" # str | Slurm Partition Name

    # example passing only required values which don't have defaults set
    try:
        # get partition info
        api_response = api_instance.slurmctld_get_partition_0(partition_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_partition_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Slurm Partition Name |

### Return type

[**V0036PartitionsResponse**](V0036PartitionsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_partitions**
> V0037PartitionsResponse slurmctld_get_partitions()

get all partition info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_partitions_response import V0037PartitionsResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    update_time = 1 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get all partition info
        api_response = api_instance.slurmctld_get_partitions(update_time=update_time)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_partitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional]

### Return type

[**V0037PartitionsResponse**](V0037PartitionsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_partitions_0**
> V0036PartitionsResponse slurmctld_get_partitions_0()

get all partition info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_partitions_response import V0036PartitionsResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get all partition info
        api_response = api_instance.slurmctld_get_partitions_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_partitions_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**V0036PartitionsResponse**](V0036PartitionsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_reservation**
> V0037ReservationsResponse slurmctld_get_reservation(reservation_name)

get reservation info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_reservations_response import V0037ReservationsResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    reservation_name = "reservation_name_example" # str | Slurm Reservation Name
    update_time = 1 # int | Filter if no reservation (not limited to reservation in URL) changed since update_time. (optional)

    # example passing only required values which don't have defaults set
    try:
        # get reservation info
        api_response = api_instance.slurmctld_get_reservation(reservation_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_reservation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get reservation info
        api_response = api_instance.slurmctld_get_reservation(reservation_name, update_time=update_time)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_reservation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Slurm Reservation Name |
 **update_time** | **int**| Filter if no reservation (not limited to reservation in URL) changed since update_time. | [optional]

### Return type

[**V0037ReservationsResponse**](V0037ReservationsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | no reservations found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_get_reservations**
> V0037ReservationsResponse slurmctld_get_reservations()

get all reservation info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_reservations_response import V0037ReservationsResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    update_time = 1 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get all reservation info
        api_response = api_instance.slurmctld_get_reservations(update_time=update_time)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_reservations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional]

### Return type

[**V0037ReservationsResponse**](V0037ReservationsResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | no reservations found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_ping**
> V0037Pings slurmctld_ping()

ping test

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_pings import V0037Pings
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ping test
        api_response = api_instance.slurmctld_ping()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_ping: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**V0037Pings**](V0037Pings.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_ping_0**
> V0036Pings slurmctld_ping_0()

ping test

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_pings import V0036Pings
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ping test
        api_response = api_instance.slurmctld_ping_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_ping_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**V0036Pings**](V0036Pings.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_submit_job**
> V0037JobSubmissionResponse slurmctld_submit_job(v0037_job_submission)

submit new job

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_job_submission_response import V0037JobSubmissionResponse
from slurm_rest.model.v0037_job_submission import V0037JobSubmission
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    v0037_job_submission = V0037JobSubmission(None) # V0037JobSubmission | submit new job

    # example passing only required values which don't have defaults set
    try:
        # submit new job
        api_response = api_instance.slurmctld_submit_job(v0037_job_submission)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_submit_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0037_job_submission** | [**V0037JobSubmission**](V0037JobSubmission.md)| submit new job |

### Return type

[**V0037JobSubmissionResponse**](V0037JobSubmissionResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submitted |  -  |
**0** | job rejected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_submit_job_0**
> V0036JobSubmissionResponse slurmctld_submit_job_0(v0036_job_submission)

submit new job

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_job_submission_response import V0036JobSubmissionResponse
from slurm_rest.model.v0036_job_submission import V0036JobSubmission
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    v0036_job_submission = V0036JobSubmission(None) # V0036JobSubmission | submit new job

    # example passing only required values which don't have defaults set
    try:
        # submit new job
        api_response = api_instance.slurmctld_submit_job_0(v0036_job_submission)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_submit_job_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0036_job_submission** | [**V0036JobSubmission**](V0036JobSubmission.md)| submit new job |

### Return type

[**V0036JobSubmissionResponse**](V0036JobSubmissionResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submitted |  -  |
**0** | job rejected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_update_job**
> slurmctld_update_job(job_id, v0037_job_properties)

update job

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0037_job_properties import V0037JobProperties
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    job_id = 1 # int | Slurm Job ID
    v0037_job_properties = V0037JobProperties(
        account="account_example",
        account_gather_freqency="account_gather_freqency_example",
        argv=[
            "argv_example",
        ],
        array="array_example",
        batch_features="batch_features_example",
        begin_time=1,
        burst_buffer="burst_buffer_example",
        cluster_constraints="cluster_constraints_example",
        comment="comment_example",
        constraints="constraints_example",
        core_specification=1,
        cores_per_socket=1,
        cpu_binding="cpu_binding_example",
        cpu_binding_hint="cpu_binding_hint_example",
        cpu_frequency="cpu_frequency_example",
        cpus_per_gpu="cpus_per_gpu_example",
        cpus_per_task=1,
        current_working_directory="current_working_directory_example",
        deadline="deadline_example",
        delay_boot=1,
        dependency="dependency_example",
        distribution="distribution_example",
        environment={},
        exclusive="user",
        get_user_environment=True,
        gres="gres_example",
        gres_flags="disable-binding",
        gpu_binding="gpu_binding_example",
        gpu_frequency="gpu_frequency_example",
        gpus="gpus_example",
        gpus_per_node="gpus_per_node_example",
        gpus_per_socket="gpus_per_socket_example",
        gpus_per_task="gpus_per_task_example",
        hold=True,
        kill_on_invalid_dependency=True,
        licenses="licenses_example",
        mail_type="mail_type_example",
        mail_user="mail_user_example",
        mcs_label="mcs_label_example",
        memory_binding="memory_binding_example",
        memory_per_cpu=1,
        memory_per_gpu=1,
        memory_per_node=1,
        minimum_cpus_per_node=1,
        minimum_nodes=True,
        name="name_example",
        nice="nice_example",
        no_kill=True,
        nodes=[
            1,
        ],
        open_mode="append",
        partition="partition_example",
        priority="priority_example",
        qos="qos_example",
        requeue=True,
        reservation="reservation_example",
        signal="sig_num",
        sockets_per_node=1,
        spread_job=True,
        standard_error="standard_error_example",
        standard_input="standard_input_example",
        standard_output="standard_output_example",
        tasks=1,
        tasks_per_core=1,
        tasks_per_node=1,
        tasks_per_socket=1,
        thread_specification=1,
        threads_per_core=1,
        time_limit=1,
        time_minimum=1,
        wait_all_nodes=True,
        wckey="wckey_example",
    ) # V0037JobProperties | update job

    # example passing only required values which don't have defaults set
    try:
        # update job
        api_instance.slurmctld_update_job(job_id, v0037_job_properties)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_update_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |
 **v0037_job_properties** | [**V0037JobProperties**](V0037JobProperties.md)| update job |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job information |  -  |
**500** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmctld_update_job_0**
> slurmctld_update_job_0(job_id, v0036_job_properties)

update job

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.v0036_job_properties import V0036JobProperties
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    job_id = 1 # int | Slurm Job ID
    v0036_job_properties = V0036JobProperties(
        account="account_example",
        account_gather_freqency="account_gather_freqency_example",
        argv=[
            "argv_example",
        ],
        array="array_example",
        batch_features="batch_features_example",
        begin_time="begin_time_example",
        burst_buffer="burst_buffer_example",
        cluster_constraints="cluster_constraints_example",
        comment="comment_example",
        constraints="constraints_example",
        core_specification=1,
        cores_per_socket=1,
        cpu_binding="cpu_binding_example",
        cpu_binding_hint="cpu_binding_hint_example",
        cpu_frequency="cpu_frequency_example",
        cpus_per_gpu="cpus_per_gpu_example",
        cpus_per_task=1,
        current_working_directory="current_working_directory_example",
        deadline="deadline_example",
        delay_boot=1,
        dependency="dependency_example",
        distribution="distribution_example",
        environment={},
        exclusive="user",
        get_user_environment=True,
        gres="gres_example",
        gres_flags="disable-binding",
        gpu_binding="gpu_binding_example",
        gpu_frequency="gpu_frequency_example",
        gpus="gpus_example",
        gpus_per_node="gpus_per_node_example",
        gpus_per_socket="gpus_per_socket_example",
        gpus_per_task="gpus_per_task_example",
        hold=True,
        kill_on_invalid_dependency=True,
        licenses="licenses_example",
        mail_type="mail_type_example",
        mail_user="mail_user_example",
        mcs_label="mcs_label_example",
        memory_binding="memory_binding_example",
        memory_per_cpu=1,
        memory_per_gpu=1,
        memory_per_node=1,
        minimum_cpus_per_node=1,
        minimum_nodes=True,
        name="name_example",
        nice="nice_example",
        no_kill=True,
        nodes=[
            1,
        ],
        open_mode="append",
        partition="partition_example",
        priority="priority_example",
        qos="qos_example",
        requeue=True,
        reservation="reservation_example",
        signal="sig_num",
        sockets_per_node=1,
        spread_job=True,
        standard_error="standard_error_example",
        standard_in="standard_in_example",
        standard_out="standard_out_example",
        tasks=1,
        tasks_per_core=1,
        tasks_per_node=1,
        tasks_per_socket=1,
        thread_specification=1,
        threads_per_core=1,
        time_limit=1,
        time_minimum=1,
        wait_all_nodes=True,
        wckey="wckey_example",
    ) # V0036JobProperties | update job

    # example passing only required values which don't have defaults set
    try:
        # update job
        api_instance.slurmctld_update_job_0(job_id, v0036_job_properties)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_update_job_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |
 **v0036_job_properties** | [**V0036JobProperties**](V0036JobProperties.md)| update job |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job information |  -  |
**500** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_add_clusters**
> Dbv0036ResponseClusterAdd slurmdbd_add_clusters()

Add clusters

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_response_cluster_add import Dbv0036ResponseClusterAdd
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Add clusters
        api_response = api_instance.slurmdbd_add_clusters()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_add_clusters: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ResponseClusterAdd**](Dbv0036ResponseClusterAdd.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | Unable to add cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_add_clusters_0**
> Dbv0037ResponseClusterAdd slurmdbd_add_clusters_0()

Add clusters

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_response_cluster_add import Dbv0037ResponseClusterAdd
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Add clusters
        api_response = api_instance.slurmdbd_add_clusters_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_add_clusters_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037ResponseClusterAdd**](Dbv0037ResponseClusterAdd.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | Unable to add cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_add_wckeys**
> Dbv0036ResponseWckeyAdd slurmdbd_add_wckeys()

Add wckeys

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_response_wckey_add import Dbv0036ResponseWckeyAdd
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Add wckeys
        api_response = api_instance.slurmdbd_add_wckeys()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_add_wckeys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ResponseWckeyAdd**](Dbv0036ResponseWckeyAdd.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | Unable to add wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_add_wckeys_0**
> Dbv0037ResponseWckeyAdd slurmdbd_add_wckeys_0()

Add wckeys

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_response_wckey_add import Dbv0037ResponseWckeyAdd
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Add wckeys
        api_response = api_instance.slurmdbd_add_wckeys_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_add_wckeys_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037ResponseWckeyAdd**](Dbv0037ResponseWckeyAdd.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | Unable to add wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_account**
> Dbv0036ResponseAccountDelete slurmdbd_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_response_account_delete import Dbv0036ResponseAccountDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    account_name = "account_name_example" # str | Slurm Account Name

    # example passing only required values which don't have defaults set
    try:
        # Delete account
        api_response = api_instance.slurmdbd_delete_account(account_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Slurm Account Name |

### Return type

[**Dbv0036ResponseAccountDelete**](Dbv0036ResponseAccountDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete account |  -  |
**0** | Unable to delete account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_account_0**
> Dbv0037ResponseAccountDelete slurmdbd_delete_account_0(account_name)

Delete account

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_response_account_delete import Dbv0037ResponseAccountDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    account_name = "account_name_example" # str | Slurm Account Name

    # example passing only required values which don't have defaults set
    try:
        # Delete account
        api_response = api_instance.slurmdbd_delete_account_0(account_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_account_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Slurm Account Name |

### Return type

[**Dbv0037ResponseAccountDelete**](Dbv0037ResponseAccountDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete account |  -  |
**0** | Unable to delete account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_association**
> Dbv0036ResponseAssociationDelete slurmdbd_delete_association(account, user)

Delete association

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_response_association_delete import Dbv0036ResponseAssociationDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    account = "account_example" # str | Account name
    user = "user_example" # str | User name
    cluster = "cluster_example" # str | Cluster name (optional)
    partition = "partition_example" # str | Partition Name (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete association
        api_response = api_instance.slurmdbd_delete_association(account, user)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_association: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete association
        api_response = api_instance.slurmdbd_delete_association(account, user, cluster=cluster, partition=partition)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_association: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Account name |
 **user** | **str**| User name |
 **cluster** | **str**| Cluster name | [optional]
 **partition** | **str**| Partition Name | [optional]

### Return type

[**Dbv0036ResponseAssociationDelete**](Dbv0036ResponseAssociationDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete associations |  -  |
**0** | Association not found or unable to delete association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_association_0**
> Dbv0037ResponseAssociationDelete slurmdbd_delete_association_0(account, user)

Delete association

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_response_association_delete import Dbv0037ResponseAssociationDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    account = "account_example" # str | Account name
    user = "user_example" # str | User name
    cluster = "cluster_example" # str | Cluster name (optional)
    partition = "partition_example" # str | Partition Name (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete association
        api_response = api_instance.slurmdbd_delete_association_0(account, user)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_association_0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete association
        api_response = api_instance.slurmdbd_delete_association_0(account, user, cluster=cluster, partition=partition)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_association_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Account name |
 **user** | **str**| User name |
 **cluster** | **str**| Cluster name | [optional]
 **partition** | **str**| Partition Name | [optional]

### Return type

[**Dbv0037ResponseAssociationDelete**](Dbv0037ResponseAssociationDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete associations |  -  |
**0** | Association not found or unable to delete association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_cluster**
> Dbv0036ResponseClusterDelete slurmdbd_delete_cluster(cluster_name)

Delete cluster

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_response_cluster_delete import Dbv0036ResponseClusterDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    cluster_name = "cluster_name_example" # str | Slurm cluster name

    # example passing only required values which don't have defaults set
    try:
        # Delete cluster
        api_response = api_instance.slurmdbd_delete_cluster(cluster_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Slurm cluster name |

### Return type

[**Dbv0036ResponseClusterDelete**](Dbv0036ResponseClusterDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete cluster |  -  |
**0** | Cluster not found or unable to delete cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_cluster_0**
> Dbv0037ResponseClusterDelete slurmdbd_delete_cluster_0(cluster_name)

Delete cluster

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_response_cluster_delete import Dbv0037ResponseClusterDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    cluster_name = "cluster_name_example" # str | Slurm cluster name

    # example passing only required values which don't have defaults set
    try:
        # Delete cluster
        api_response = api_instance.slurmdbd_delete_cluster_0(cluster_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_cluster_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Slurm cluster name |

### Return type

[**Dbv0037ResponseClusterDelete**](Dbv0037ResponseClusterDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete cluster |  -  |
**0** | Cluster not found or unable to delete cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_qos**
> Dbv0036ResponseQosDelete slurmdbd_delete_qos(qos_name)

Delete QOS

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_response_qos_delete import Dbv0036ResponseQosDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    qos_name = "qos_name_example" # str | Slurm QOS Name

    # example passing only required values which don't have defaults set
    try:
        # Delete QOS
        api_response = api_instance.slurmdbd_delete_qos(qos_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_qos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos_name** | **str**| Slurm QOS Name |

### Return type

[**Dbv0036ResponseQosDelete**](Dbv0036ResponseQosDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete qos |  -  |
**0** | Unable to delete QOS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_qos_0**
> Dbv0037ResponseQosDelete slurmdbd_delete_qos_0(qos_name)

Delete QOS

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_response_qos_delete import Dbv0037ResponseQosDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    qos_name = "qos_name_example" # str | Slurm QOS Name

    # example passing only required values which don't have defaults set
    try:
        # Delete QOS
        api_response = api_instance.slurmdbd_delete_qos_0(qos_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_qos_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos_name** | **str**| Slurm QOS Name |

### Return type

[**Dbv0037ResponseQosDelete**](Dbv0037ResponseQosDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete qos |  -  |
**0** | Unable to delete QOS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_user**
> Dbv0036ResponseUserDelete slurmdbd_delete_user(user_name)

Delete user

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_response_user_delete import Dbv0036ResponseUserDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    user_name = "user_name_example" # str | Slurm User Name

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_response = api_instance.slurmdbd_delete_user(user_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Slurm User Name |

### Return type

[**Dbv0036ResponseUserDelete**](Dbv0036ResponseUserDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete user |  -  |
**0** | User not found or unable to delete user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_user_0**
> Dbv0037ResponseUserDelete slurmdbd_delete_user_0(user_name)

Delete user

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_response_user_delete import Dbv0037ResponseUserDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    user_name = "user_name_example" # str | Slurm User Name

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_response = api_instance.slurmdbd_delete_user_0(user_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_user_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Slurm User Name |

### Return type

[**Dbv0037ResponseUserDelete**](Dbv0037ResponseUserDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete user |  -  |
**0** | User not found or unable to delete user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_wckey**
> Dbv0036ResponseWckeyDelete slurmdbd_delete_wckey(wckey)

Delete wckey

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_response_wckey_delete import Dbv0036ResponseWckeyDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    wckey = "wckey_example" # str | Slurm wckey name

    # example passing only required values which don't have defaults set
    try:
        # Delete wckey
        api_response = api_instance.slurmdbd_delete_wckey(wckey)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_wckey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wckey** | **str**| Slurm wckey name |

### Return type

[**Dbv0036ResponseWckeyDelete**](Dbv0036ResponseWckeyDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete wckey |  -  |
**0** | wckey not found or unable to delete wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_delete_wckey_0**
> Dbv0037ResponseWckeyDelete slurmdbd_delete_wckey_0(wckey)

Delete wckey

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_response_wckey_delete import Dbv0037ResponseWckeyDelete
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    wckey = "wckey_example" # str | Slurm wckey name

    # example passing only required values which don't have defaults set
    try:
        # Delete wckey
        api_response = api_instance.slurmdbd_delete_wckey_0(wckey)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_wckey_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wckey** | **str**| Slurm wckey name |

### Return type

[**Dbv0037ResponseWckeyDelete**](Dbv0037ResponseWckeyDelete.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete wckey |  -  |
**0** | wckey not found or unable to delete wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_diag**
> Dbv0036Diag slurmdbd_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_diag import Dbv0036Diag
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get slurmdb diagnostics
        api_response = api_instance.slurmdbd_diag()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_diag: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036Diag**](Dbv0036Diag.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of statistics |  -  |
**0** | Unable to query diagnostics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_diag_0**
> Dbv0037Diag slurmdbd_diag_0()

Get slurmdb diagnostics

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_diag import Dbv0037Diag
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get slurmdb diagnostics
        api_response = api_instance.slurmdbd_diag_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_diag_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037Diag**](Dbv0037Diag.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of statistics |  -  |
**0** | Unable to query diagnostics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_account**
> Dbv0036AccountInfo slurmdbd_get_account(account_name)

Get account info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_account_info import Dbv0036AccountInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    account_name = "account_name_example" # str | Slurm Account Name

    # example passing only required values which don't have defaults set
    try:
        # Get account info
        api_response = api_instance.slurmdbd_get_account(account_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Slurm Account Name |

### Return type

[**Dbv0036AccountInfo**](Dbv0036AccountInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_account_0**
> Dbv0037AccountInfo slurmdbd_get_account_0(account_name)

Get account info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_account_info import Dbv0037AccountInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    account_name = "account_name_example" # str | Slurm Account Name

    # example passing only required values which don't have defaults set
    try:
        # Get account info
        api_response = api_instance.slurmdbd_get_account_0(account_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_account_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Slurm Account Name |

### Return type

[**Dbv0037AccountInfo**](Dbv0037AccountInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_accounts**
> Dbv0036AccountInfo slurmdbd_get_accounts()

Get account list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_account_info import Dbv0036AccountInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get account list
        api_response = api_instance.slurmdbd_get_accounts()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_accounts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036AccountInfo**](Dbv0036AccountInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_accounts_0**
> Dbv0037AccountInfo slurmdbd_get_accounts_0()

Get account list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_account_info import Dbv0037AccountInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get account list
        api_response = api_instance.slurmdbd_get_accounts_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_accounts_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037AccountInfo**](Dbv0037AccountInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_association**
> Dbv0036AssociationsInfo slurmdbd_get_association()

Get association info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_associations_info import Dbv0036AssociationsInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    cluster = "cluster_example" # str | Cluster name (optional)
    account = "account_example" # str | Account name (optional)
    user = "user_example" # str | User name (optional)
    partition = "partition_example" # str | Partition Name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get association info
        api_response = api_instance.slurmdbd_get_association(cluster=cluster, account=account, user=user, partition=partition)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_association: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional]
 **account** | **str**| Account name | [optional]
 **user** | **str**| User name | [optional]
 **partition** | **str**| Partition Name | [optional]

### Return type

[**Dbv0036AssociationsInfo**](Dbv0036AssociationsInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | Association not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_association_0**
> Dbv0037AssociationsInfo slurmdbd_get_association_0()

Get association info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_associations_info import Dbv0037AssociationsInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    cluster = "cluster_example" # str | Cluster name (optional)
    account = "account_example" # str | Account name (optional)
    user = "user_example" # str | User name (optional)
    partition = "partition_example" # str | Partition Name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get association info
        api_response = api_instance.slurmdbd_get_association_0(cluster=cluster, account=account, user=user, partition=partition)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_association_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster name | [optional]
 **account** | **str**| Account name | [optional]
 **user** | **str**| User name | [optional]
 **partition** | **str**| Partition Name | [optional]

### Return type

[**Dbv0037AssociationsInfo**](Dbv0037AssociationsInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | Association not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_associations**
> Dbv0036AssociationsInfo slurmdbd_get_associations()

Get association list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_associations_info import Dbv0036AssociationsInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get association list
        api_response = api_instance.slurmdbd_get_associations()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_associations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036AssociationsInfo**](Dbv0036AssociationsInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | Association not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_associations_0**
> Dbv0037AssociationsInfo slurmdbd_get_associations_0()

Get association list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_associations_info import Dbv0037AssociationsInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get association list
        api_response = api_instance.slurmdbd_get_associations_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_associations_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037AssociationsInfo**](Dbv0037AssociationsInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | Association not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_cluster**
> Dbv0036ClusterInfo slurmdbd_get_cluster(cluster_name)

Get cluster info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_cluster_info import Dbv0036ClusterInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    cluster_name = "cluster_name_example" # str | Slurm cluster name

    # example passing only required values which don't have defaults set
    try:
        # Get cluster info
        api_response = api_instance.slurmdbd_get_cluster(cluster_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Slurm cluster name |

### Return type

[**Dbv0036ClusterInfo**](Dbv0036ClusterInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster information |  -  |
**0** | Cluster not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_cluster_0**
> Dbv0037ClusterInfo slurmdbd_get_cluster_0(cluster_name)

Get cluster info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_cluster_info import Dbv0037ClusterInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    cluster_name = "cluster_name_example" # str | Slurm cluster name

    # example passing only required values which don't have defaults set
    try:
        # Get cluster info
        api_response = api_instance.slurmdbd_get_cluster_0(cluster_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_cluster_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Slurm cluster name |

### Return type

[**Dbv0037ClusterInfo**](Dbv0037ClusterInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster information |  -  |
**0** | Cluster not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_clusters**
> Dbv0036ClusterInfo slurmdbd_get_clusters()

Get cluster list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_cluster_info import Dbv0036ClusterInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get cluster list
        api_response = api_instance.slurmdbd_get_clusters()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_clusters: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ClusterInfo**](Dbv0036ClusterInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | Cluster not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_clusters_0**
> Dbv0037ClusterInfo slurmdbd_get_clusters_0()

Get cluster list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_cluster_info import Dbv0037ClusterInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get cluster list
        api_response = api_instance.slurmdbd_get_clusters_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_clusters_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037ClusterInfo**](Dbv0037ClusterInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | Cluster not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_db_config**
> Dbv0036ConfigInfo slurmdbd_get_db_config()

Dump all configuration information

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_config_info import Dbv0036ConfigInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Dump all configuration information
        api_response = api_instance.slurmdbd_get_db_config()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_db_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ConfigInfo**](Dbv0036ConfigInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | Unable to dump config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_db_config_0**
> Dbv0037ConfigInfo slurmdbd_get_db_config_0()

Dump all configuration information

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_config_info import Dbv0037ConfigInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Dump all configuration information
        api_response = api_instance.slurmdbd_get_db_config_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_db_config_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037ConfigInfo**](Dbv0037ConfigInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | Unable to dump config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_job**
> Dbv0036JobInfo slurmdbd_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_job_info import Dbv0036JobInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    job_id = 1 # int | Slurm Job ID

    # example passing only required values which don't have defaults set
    try:
        # Get job info
        api_response = api_instance.slurmdbd_get_job(job_id)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |

### Return type

[**Dbv0036JobInfo**](Dbv0036JobInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job description |  -  |
**0** | Unable to find job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_job_0**
> Dbv0037JobInfo slurmdbd_get_job_0(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_job_info import Dbv0037JobInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    job_id = 1 # int | Slurm Job ID

    # example passing only required values which don't have defaults set
    try:
        # Get job info
        api_response = api_instance.slurmdbd_get_job_0(job_id)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_job_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |

### Return type

[**Dbv0037JobInfo**](Dbv0037JobInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job description |  -  |
**0** | Unable to find job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_jobs**
> Dbv0036JobInfo slurmdbd_get_jobs()

Get job list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_job_info import Dbv0036JobInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    submit_time = "submit_time_example" # str | Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    start_time = "start_time_example" # str | Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    end_time = "end_time_example" # str | Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    account = "account_example" # str | Comma delimited list of accounts to match (optional)
    association = "association_example" # str | Comma delimited list of associations to match (optional)
    cluster = "cluster_example" # str | Comma delimited list of cluster to match (optional)
    constraints = "constraints_example" # str | Comma delimited list of constraints to match (optional)
    cpus_max = "cpus_max_example" # str | Number of CPUs high range (optional)
    cpus_min = "cpus_min_example" # str | Number of CPUs low range (optional)
    skip_steps = True # bool | Report job step information (optional)
    disable_wait_for_result = True # bool | Disable waiting for result from slurmdbd (optional)
    exit_code = "exit_code_example" # str | Exit code of job (optional)
    format = "format_example" # str | Comma delimited list of formats to match (optional)
    group = "group_example" # str | Comma delimited list of groups to match (optional)
    job_name = "job_name_example" # str | Comma delimited list of job names to match (optional)
    nodes_max = "nodes_max_example" # str | Number of nodes high range (optional)
    nodes_min = "nodes_min_example" # str | Number of nodes low range (optional)
    partition = "partition_example" # str | Comma delimited list of partitions to match (optional)
    qos = "qos_example" # str | Comma delimited list of QOS to match (optional)
    reason = "reason_example" # str | Comma delimited list of job reasons to match (optional)
    reservation = "reservation_example" # str | Comma delimited list of reservations to match (optional)
    state = "state_example" # str | Comma delimited list of states to match (optional)
    step = "step_example" # str | Comma delimited list of job steps to match (optional)
    node = "node_example" # str | Comma delimited list of used nodes to match (optional)
    wckey = "wckey_example" # str | Comma delimited list of wckeys to match (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get job list
        api_response = api_instance.slurmdbd_get_jobs(submit_time=submit_time, start_time=start_time, end_time=end_time, account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, skip_steps=skip_steps, disable_wait_for_result=disable_wait_for_result, exit_code=exit_code, format=format, group=group, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, state=state, step=step, node=node, wckey=wckey)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_jobs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_time** | **str**| Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional]
 **start_time** | **str**| Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional]
 **end_time** | **str**| Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional]
 **account** | **str**| Comma delimited list of accounts to match | [optional]
 **association** | **str**| Comma delimited list of associations to match | [optional]
 **cluster** | **str**| Comma delimited list of cluster to match | [optional]
 **constraints** | **str**| Comma delimited list of constraints to match | [optional]
 **cpus_max** | **str**| Number of CPUs high range | [optional]
 **cpus_min** | **str**| Number of CPUs low range | [optional]
 **skip_steps** | **bool**| Report job step information | [optional]
 **disable_wait_for_result** | **bool**| Disable waiting for result from slurmdbd | [optional]
 **exit_code** | **str**| Exit code of job | [optional]
 **format** | **str**| Comma delimited list of formats to match | [optional]
 **group** | **str**| Comma delimited list of groups to match | [optional]
 **job_name** | **str**| Comma delimited list of job names to match | [optional]
 **nodes_max** | **str**| Number of nodes high range | [optional]
 **nodes_min** | **str**| Number of nodes low range | [optional]
 **partition** | **str**| Comma delimited list of partitions to match | [optional]
 **qos** | **str**| Comma delimited list of QOS to match | [optional]
 **reason** | **str**| Comma delimited list of job reasons to match | [optional]
 **reservation** | **str**| Comma delimited list of reservations to match | [optional]
 **state** | **str**| Comma delimited list of states to match | [optional]
 **step** | **str**| Comma delimited list of job steps to match | [optional]
 **node** | **str**| Comma delimited list of used nodes to match | [optional]
 **wckey** | **str**| Comma delimited list of wckeys to match | [optional]

### Return type

[**Dbv0036JobInfo**](Dbv0036JobInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**0** | Unable to query jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_jobs_0**
> Dbv0037JobInfo slurmdbd_get_jobs_0()

Get job list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_job_info import Dbv0037JobInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    submit_time = "submit_time_example" # str | Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    start_time = "start_time_example" # str | Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    end_time = "end_time_example" # str | Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    account = "account_example" # str | Comma delimited list of accounts to match (optional)
    association = "association_example" # str | Comma delimited list of associations to match (optional)
    cluster = "cluster_example" # str | Comma delimited list of cluster to match (optional)
    constraints = "constraints_example" # str | Comma delimited list of constraints to match (optional)
    cpus_max = "cpus_max_example" # str | Number of CPUs high range (optional)
    cpus_min = "cpus_min_example" # str | Number of CPUs low range (optional)
    skip_steps = True # bool | Report job step information (optional)
    disable_wait_for_result = True # bool | Disable waiting for result from slurmdbd (optional)
    exit_code = "exit_code_example" # str | Exit code of job (optional)
    format = "format_example" # str | Comma delimited list of formats to match (optional)
    group = "group_example" # str | Comma delimited list of groups to match (optional)
    job_name = "job_name_example" # str | Comma delimited list of job names to match (optional)
    nodes_max = "nodes_max_example" # str | Number of nodes high range (optional)
    nodes_min = "nodes_min_example" # str | Number of nodes low range (optional)
    partition = "partition_example" # str | Comma delimited list of partitions to match (optional)
    qos = "qos_example" # str | Comma delimited list of QOS to match (optional)
    reason = "reason_example" # str | Comma delimited list of job reasons to match (optional)
    reservation = "reservation_example" # str | Comma delimited list of reservations to match (optional)
    state = "state_example" # str | Comma delimited list of states to match (optional)
    step = "step_example" # str | Comma delimited list of job steps to match (optional)
    node = "node_example" # str | Comma delimited list of used nodes to match (optional)
    wckey = "wckey_example" # str | Comma delimited list of wckeys to match (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get job list
        api_response = api_instance.slurmdbd_get_jobs_0(submit_time=submit_time, start_time=start_time, end_time=end_time, account=account, association=association, cluster=cluster, constraints=constraints, cpus_max=cpus_max, cpus_min=cpus_min, skip_steps=skip_steps, disable_wait_for_result=disable_wait_for_result, exit_code=exit_code, format=format, group=group, job_name=job_name, nodes_max=nodes_max, nodes_min=nodes_min, partition=partition, qos=qos, reason=reason, reservation=reservation, state=state, step=step, node=node, wckey=wckey)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_jobs_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_time** | **str**| Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional]
 **start_time** | **str**| Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional]
 **end_time** | **str**| Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] | [optional]
 **account** | **str**| Comma delimited list of accounts to match | [optional]
 **association** | **str**| Comma delimited list of associations to match | [optional]
 **cluster** | **str**| Comma delimited list of cluster to match | [optional]
 **constraints** | **str**| Comma delimited list of constraints to match | [optional]
 **cpus_max** | **str**| Number of CPUs high range | [optional]
 **cpus_min** | **str**| Number of CPUs low range | [optional]
 **skip_steps** | **bool**| Report job step information | [optional]
 **disable_wait_for_result** | **bool**| Disable waiting for result from slurmdbd | [optional]
 **exit_code** | **str**| Exit code of job | [optional]
 **format** | **str**| Comma delimited list of formats to match | [optional]
 **group** | **str**| Comma delimited list of groups to match | [optional]
 **job_name** | **str**| Comma delimited list of job names to match | [optional]
 **nodes_max** | **str**| Number of nodes high range | [optional]
 **nodes_min** | **str**| Number of nodes low range | [optional]
 **partition** | **str**| Comma delimited list of partitions to match | [optional]
 **qos** | **str**| Comma delimited list of QOS to match | [optional]
 **reason** | **str**| Comma delimited list of job reasons to match | [optional]
 **reservation** | **str**| Comma delimited list of reservations to match | [optional]
 **state** | **str**| Comma delimited list of states to match | [optional]
 **step** | **str**| Comma delimited list of job steps to match | [optional]
 **node** | **str**| Comma delimited list of used nodes to match | [optional]
 **wckey** | **str**| Comma delimited list of wckeys to match | [optional]

### Return type

[**Dbv0037JobInfo**](Dbv0037JobInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**0** | Unable to query jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_qos**
> Dbv0036QosInfo slurmdbd_get_qos()

Get QOS list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_qos_info import Dbv0036QosInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get QOS list
        api_response = api_instance.slurmdbd_get_qos()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_qos: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036QosInfo**](Dbv0036QosInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QOS&#39; |  -  |
**0** | QOS not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_qos_0**
> Dbv0037QosInfo slurmdbd_get_qos_0()

Get QOS list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_qos_info import Dbv0037QosInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get QOS list
        api_response = api_instance.slurmdbd_get_qos_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_qos_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037QosInfo**](Dbv0037QosInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QOS&#39; |  -  |
**0** | QOS not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_single_qos**
> Dbv0036QosInfo slurmdbd_get_single_qos(qos_name)

Get QOS info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_qos_info import Dbv0036QosInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    qos_name = "qos_name_example" # str | Slurm QOS Name

    # example passing only required values which don't have defaults set
    try:
        # Get QOS info
        api_response = api_instance.slurmdbd_get_single_qos(qos_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_single_qos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos_name** | **str**| Slurm QOS Name |

### Return type

[**Dbv0036QosInfo**](Dbv0036QosInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS information |  -  |
**0** | QOS not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_single_qos_0**
> Dbv0037QosInfo slurmdbd_get_single_qos_0(qos_name)

Get QOS info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_qos_info import Dbv0037QosInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    qos_name = "qos_name_example" # str | Slurm QOS Name

    # example passing only required values which don't have defaults set
    try:
        # Get QOS info
        api_response = api_instance.slurmdbd_get_single_qos_0(qos_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_single_qos_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos_name** | **str**| Slurm QOS Name |

### Return type

[**Dbv0037QosInfo**](Dbv0037QosInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS information |  -  |
**0** | QOS not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_tres**
> Dbv0036TresInfo slurmdbd_get_tres()

Get TRES info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_tres_info import Dbv0036TresInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get TRES info
        api_response = api_instance.slurmdbd_get_tres()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_tres: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036TresInfo**](Dbv0036TresInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | Unable to retrieve TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_tres_0**
> Dbv0037TresInfo slurmdbd_get_tres_0()

Get TRES info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_tres_info import Dbv0037TresInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get TRES info
        api_response = api_instance.slurmdbd_get_tres_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_tres_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037TresInfo**](Dbv0037TresInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | Unable to retrieve TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_user**
> Dbv0036UserInfo slurmdbd_get_user(user_name)

Get user info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_user_info import Dbv0036UserInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    user_name = "user_name_example" # str | Slurm User Name

    # example passing only required values which don't have defaults set
    try:
        # Get user info
        api_response = api_instance.slurmdbd_get_user(user_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Slurm User Name |

### Return type

[**Dbv0036UserInfo**](Dbv0036UserInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_user_0**
> Dbv0037UserInfo slurmdbd_get_user_0(user_name)

Get user info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_user_info import Dbv0037UserInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    user_name = "user_name_example" # str | Slurm User Name

    # example passing only required values which don't have defaults set
    try:
        # Get user info
        api_response = api_instance.slurmdbd_get_user_0(user_name)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_user_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Slurm User Name |

### Return type

[**Dbv0037UserInfo**](Dbv0037UserInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_users**
> Dbv0036UserInfo slurmdbd_get_users()

Get user list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_user_info import Dbv0036UserInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get user list
        api_response = api_instance.slurmdbd_get_users()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036UserInfo**](Dbv0036UserInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_users_0**
> Dbv0037UserInfo slurmdbd_get_users_0()

Get user list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_user_info import Dbv0037UserInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get user list
        api_response = api_instance.slurmdbd_get_users_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_users_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037UserInfo**](Dbv0037UserInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_wckey**
> Dbv0036WckeyInfo slurmdbd_get_wckey(wckey)

Get wckey info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_wckey_info import Dbv0036WckeyInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    wckey = "wckey_example" # str | Slurm wckey name

    # example passing only required values which don't have defaults set
    try:
        # Get wckey info
        api_response = api_instance.slurmdbd_get_wckey(wckey)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_wckey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wckey** | **str**| Slurm wckey name |

### Return type

[**Dbv0036WckeyInfo**](Dbv0036WckeyInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckey |  -  |
**0** | wckey not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_wckey_0**
> Dbv0037WckeyInfo slurmdbd_get_wckey_0(wckey)

Get wckey info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_wckey_info import Dbv0037WckeyInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)
    wckey = "wckey_example" # str | Slurm wckey name

    # example passing only required values which don't have defaults set
    try:
        # Get wckey info
        api_response = api_instance.slurmdbd_get_wckey_0(wckey)
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_wckey_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wckey** | **str**| Slurm wckey name |

### Return type

[**Dbv0037WckeyInfo**](Dbv0037WckeyInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckey |  -  |
**0** | wckey not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_wckeys**
> Dbv0036WckeyInfo slurmdbd_get_wckeys()

Get wckey list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_wckey_info import Dbv0036WckeyInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get wckey list
        api_response = api_instance.slurmdbd_get_wckeys()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_wckeys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036WckeyInfo**](Dbv0036WckeyInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | wckey not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_get_wckeys_0**
> Dbv0037WckeyInfo slurmdbd_get_wckeys_0()

Get wckey list

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_wckey_info import Dbv0037WckeyInfo
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get wckey list
        api_response = api_instance.slurmdbd_get_wckeys_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_wckeys_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037WckeyInfo**](Dbv0037WckeyInfo.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | wckey not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_set_db_config**
> Dbv0036ConfigResponse slurmdbd_set_db_config()

Load all configuration information

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_config_response import Dbv0036ConfigResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Load all configuration information
        api_response = api_instance.slurmdbd_set_db_config()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_set_db_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ConfigResponse**](Dbv0036ConfigResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Load config |  -  |
**0** | Unable to set config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_set_db_config_0**
> Dbv0037ConfigResponse slurmdbd_set_db_config_0()

Load all configuration information

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_config_response import Dbv0037ConfigResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Load all configuration information
        api_response = api_instance.slurmdbd_set_db_config_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_set_db_config_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037ConfigResponse**](Dbv0037ConfigResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Load config |  -  |
**0** | Unable to set config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_update_account**
> Dbv0036AccountResponse slurmdbd_update_account()

Update accounts

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_account_response import Dbv0036AccountResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update accounts
        api_response = api_instance.slurmdbd_update_account()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_update_account: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036AccountResponse**](Dbv0036AccountResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add/update list of accounts |  -  |
**0** | Unable to add or update accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_update_account_0**
> Dbv0037AccountResponse slurmdbd_update_account_0()

Update accounts

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_account_response import Dbv0037AccountResponse
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update accounts
        api_response = api_instance.slurmdbd_update_account_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_update_account_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037AccountResponse**](Dbv0037AccountResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add/update list of accounts |  -  |
**0** | Unable to add or update accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_update_tres**
> Dbv0036ResponseTres slurmdbd_update_tres()

Set TRES info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_response_tres import Dbv0036ResponseTres
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Set TRES info
        api_response = api_instance.slurmdbd_update_tres()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_update_tres: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ResponseTres**](Dbv0036ResponseTres.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | Unable to update TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_update_tres_0**
> Dbv0037ResponseTres slurmdbd_update_tres_0()

Set TRES info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_response_tres import Dbv0037ResponseTres
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Set TRES info
        api_response = api_instance.slurmdbd_update_tres_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_update_tres_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037ResponseTres**](Dbv0037ResponseTres.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | Unable to update TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_update_users**
> Dbv0036ResponseUserUpdate slurmdbd_update_users()

Update user

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0036_response_user_update import Dbv0036ResponseUserUpdate
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update user
        api_response = api_instance.slurmdbd_update_users()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_update_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0036ResponseUserUpdate**](Dbv0036ResponseUserUpdate.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update users |  -  |
**0** | User not found or not able to update user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdbd_update_users_0**
> Dbv0037ResponseUserUpdate slurmdbd_update_users_0()

Update user

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import slurm_api
from slurm_rest.model.dbv0037_response_user_update import Dbv0037ResponseUserUpdate
from pprint import pprint
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
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update user
        api_response = api_instance.slurmdbd_update_users_0()
        pprint(api_response)
    except slurm_rest.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_update_users_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dbv0037ResponseUserUpdate**](Dbv0037ResponseUserUpdate.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update users |  -  |
**0** | User not found or not able to update user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

