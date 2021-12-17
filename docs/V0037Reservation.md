# V0037Reservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **str** | Allowed accounts | [optional] 
**burst_buffer** | **str** | Reserved burst buffer | [optional] 
**core_count** | **int** | Number of reserved cores | [optional] 
**core_spec_cnt** | **int** | Number of reserved specialized cores | [optional] 
**end_time** | **int** | End time of the reservation | [optional] 
**features** | **str** | List of features | [optional] 
**flags** | **[str]** | Reservation options | [optional] 
**groups** | **str** | List of groups permitted to use the reserved nodes | [optional] 
**licenses** | **str** | List of licenses | [optional] 
**max_start_delay** | **int** | Maximum delay in which jobs outside of the reservation will be permitted to overlap once any jobs are queued for the reservation | [optional] 
**name** | **str** | Reservationn name | [optional] 
**node_count** | **int** | Count of nodes reserved | [optional] 
**node_list** | **str** | List of reserved nodes | [optional] 
**partition** | **str** | Partition | [optional] 
**purge_completed** | [**V0037ReservationPurgeCompleted**](V0037ReservationPurgeCompleted.md) |  | [optional] 
**start_time** | **int** | Start time of reservation | [optional] 
**watts** | **int** | amount of power to reserve in watts | [optional] 
**tres** | **str** | List of TRES | [optional] 
**users** | **str** | List of users | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


