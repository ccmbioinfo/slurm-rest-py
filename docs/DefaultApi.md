# slurm_rest.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurm_v0035_diag_get**](DefaultApi.md#slurm_v0035_diag_get) | **GET** /slurm/v0.0.35/diag | get diagnostics
[**slurm_v0035_job_job_id_delete**](DefaultApi.md#slurm_v0035_job_job_id_delete) | **DELETE** /slurm/v0.0.35/job/{job_id} | cancel or signal job
[**slurm_v0035_job_job_id_get**](DefaultApi.md#slurm_v0035_job_job_id_get) | **GET** /slurm/v0.0.35/job/{job_id} | get job info
[**slurm_v0035_job_job_id_post**](DefaultApi.md#slurm_v0035_job_job_id_post) | **POST** /slurm/v0.0.35/job/{job_id} | update job
[**slurm_v0035_job_submit_post**](DefaultApi.md#slurm_v0035_job_submit_post) | **POST** /slurm/v0.0.35/job/submit | submit new job
[**slurm_v0035_jobs_get**](DefaultApi.md#slurm_v0035_jobs_get) | **GET** /slurm/v0.0.35/jobs | get list of jobs
[**slurm_v0035_node_node_name_get**](DefaultApi.md#slurm_v0035_node_node_name_get) | **GET** /slurm/v0.0.35/node/{node_name} | get node info
[**slurm_v0035_nodes_get**](DefaultApi.md#slurm_v0035_nodes_get) | **GET** /slurm/v0.0.35/nodes | get all node info
[**slurm_v0035_partition_partition_name_get**](DefaultApi.md#slurm_v0035_partition_partition_name_get) | **GET** /slurm/v0.0.35/partition/{partition_name} | get partition info
[**slurm_v0035_partitions_get**](DefaultApi.md#slurm_v0035_partitions_get) | **GET** /slurm/v0.0.35/partitions | get all partition info
[**slurm_v0035_ping_get**](DefaultApi.md#slurm_v0035_ping_get) | **GET** /slurm/v0.0.35/ping | ping test


# **slurm_v0035_diag_get**
> slurm_v0035_diag_get()

get diagnostics

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get diagnostics
        api_instance.slurm_v0035_diag_get()
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_diag_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | dictionary of statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0035_job_job_id_delete**
> slurm_v0035_job_job_id_delete(job_id)

cancel or signal job

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
from slurm_rest.model.signal import Signal
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
    api_instance = default_api.DefaultApi(api_client)
    job_id = 1 # int | Slurm Job ID
    signal = Signal(None) # Signal | signal to send to job (optional)

    # example passing only required values which don't have defaults set
    try:
        # cancel or signal job
        api_instance.slurm_v0035_job_job_id_delete(job_id)
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_job_job_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # cancel or signal job
        api_instance.slurm_v0035_job_job_id_delete(job_id, signal=signal)
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_job_job_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |
 **signal** | **Signal**| signal to send to job | [optional]

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

# **slurm_v0035_job_job_id_get**
> slurm_v0035_job_job_id_get(job_id)

get job info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    job_id = 1 # int | Slurm Job ID

    # example passing only required values which don't have defaults set
    try:
        # get job info
        api_instance.slurm_v0035_job_job_id_get(job_id)
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_job_job_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |

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
**200** | job information |  -  |
**500** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0035_job_job_id_post**
> slurm_v0035_job_job_id_post(job_id, job_properties)

update job

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
from slurm_rest.model.job_properties import JobProperties
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
    api_instance = default_api.DefaultApi(api_client)
    job_id = 1 # int | Slurm Job ID
    job_properties = JobProperties(None) # JobProperties | update job

    # example passing only required values which don't have defaults set
    try:
        # update job
        api_instance.slurm_v0035_job_job_id_post(job_id, job_properties)
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_job_job_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Slurm Job ID |
 **job_properties** | [**JobProperties**](JobProperties.md)| update job |

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

# **slurm_v0035_job_submit_post**
> slurm_v0035_job_submit_post(job_properties)

submit new job

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
from slurm_rest.model.job_properties import JobProperties
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
    api_instance = default_api.DefaultApi(api_client)
    job_properties = JobProperties(None) # JobProperties | submit new job

    # example passing only required values which don't have defaults set
    try:
        # submit new job
        api_instance.slurm_v0035_job_submit_post(job_properties)
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_job_submit_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_properties** | [**JobProperties**](JobProperties.md)| submit new job |

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
**200** | job submitted |  -  |
**500** | job rejected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0035_jobs_get**
> slurm_v0035_jobs_get()

get list of jobs

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get list of jobs
        api_instance.slurm_v0035_jobs_get()
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_jobs_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | array of all job information in slurmctld |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0035_node_node_name_get**
> slurm_v0035_node_node_name_get(node_name)

get node info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    node_name = "node_name_example" # str | Slurm Node Name

    # example passing only required values which don't have defaults set
    try:
        # get node info
        api_instance.slurm_v0035_node_node_name_get(node_name)
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_node_node_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Slurm Node Name |

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
**200** | node information |  -  |
**500** | node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0035_nodes_get**
> slurm_v0035_nodes_get()

get all node info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get all node info
        api_instance.slurm_v0035_nodes_get()
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_nodes_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | nodes information |  -  |
**500** | no nodes in cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0035_partition_partition_name_get**
> slurm_v0035_partition_partition_name_get(partition_name)

get partition info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    partition_name = "partition_name_example" # str | Slurm Partition Name

    # example passing only required values which don't have defaults set
    try:
        # get partition info
        api_instance.slurm_v0035_partition_partition_name_get(partition_name)
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_partition_partition_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Slurm Partition Name |

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
**200** | partition information |  -  |
**500** | partition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0035_partitions_get**
> slurm_v0035_partitions_get()

get all partition info

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get all partition info
        api_instance.slurm_v0035_partitions_get()
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_partitions_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | partitions information |  -  |
**500** | no partitions in cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0035_ping_get**
> slurm_v0035_ping_get()

ping test

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ping test
        api_instance.slurm_v0035_ping_get()
    except slurm_rest.ApiException as e:
        print("Exception when calling DefaultApi->slurm_v0035_ping_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

