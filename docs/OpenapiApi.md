# slurm_rest.OpenapiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openapi_get**](OpenapiApi.md#openapi_get) | **GET** /openapi | Retrieve OpenAPI Specification
[**openapi_json_get**](OpenapiApi.md#openapi_json_get) | **GET** /openapi.json | Retrieve OpenAPI Specification
[**openapi_v3_get**](OpenapiApi.md#openapi_v3_get) | **GET** /openapi/v3 | Retrieve OpenAPI Specification
[**openapi_yaml_get**](OpenapiApi.md#openapi_yaml_get) | **GET** /openapi.yaml | Retrieve OpenAPI Specification


# **openapi_get**
> openapi_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import openapi_api
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
    api_instance = openapi_api.OpenapiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve OpenAPI Specification
        api_instance.openapi_get()
    except slurm_rest.ApiException as e:
        print("Exception when calling OpenapiApi->openapi_get: %s\n" % e)
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
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_json_get**
> openapi_json_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import openapi_api
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
    api_instance = openapi_api.OpenapiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve OpenAPI Specification
        api_instance.openapi_json_get()
    except slurm_rest.ApiException as e:
        print("Exception when calling OpenapiApi->openapi_json_get: %s\n" % e)
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
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_v3_get**
> openapi_v3_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import openapi_api
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
    api_instance = openapi_api.OpenapiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve OpenAPI Specification
        api_instance.openapi_v3_get()
    except slurm_rest.ApiException as e:
        print("Exception when calling OpenapiApi->openapi_v3_get: %s\n" % e)
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
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_yaml_get**
> openapi_yaml_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (token):
* Api Key Authentication (user):

```python
import time
import slurm_rest
from slurm_rest.api import openapi_api
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
    api_instance = openapi_api.OpenapiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve OpenAPI Specification
        api_instance.openapi_yaml_get()
    except slurm_rest.ApiException as e:
        print("Exception when calling OpenapiApi->openapi_yaml_get: %s\n" % e)
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
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

