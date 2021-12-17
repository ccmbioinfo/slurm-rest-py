# V0036Node


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | computer architecture | [optional] 
**burstbuffer_network_address** | **str** | BcastAddr | [optional] 
**boards** | **int** | total number of boards per node | [optional] 
**boot_time** | **int** | timestamp of node boot | [optional] 
**comment** | **str** | Arbitrary comment | [optional] 
**cores** | **int** | number of cores per socket | [optional] 
**cpu_binding** | **int** | Default task binding | [optional] 
**cpu_load** | **int** | CPU load * 100 | [optional] 
**free_memory** | **int** | free memory in MiB | [optional] 
**cpus** | **int** | configured count of cpus running on the node | [optional] 
**features** | **str** |  | [optional] 
**active_features** | **str** | list of a node&#39;s available features | [optional] 
**gres** | **str** | list of a node&#39;s generic resources | [optional] 
**gres_drained** | **str** | list of drained GRES | [optional] 
**gres_used** | **str** | list of GRES in current use | [optional] 
**mcs_label** | **str** | mcs label if mcs plugin in use | [optional] 
**name** | **str** | node name to slurm | [optional] 
**next_state_after_reboot** | **str** |  | [optional] 
**address** | **str** | state after reboot | [optional] 
**hostname** | **str** | node&#39;s hostname | [optional] 
**state** | **str** | current node state | [optional] 
**operating_system** | **str** | operating system | [optional] 
**owner** | **str** | User allowed to use this node | [optional] 
**port** | **int** | TCP port number of the slurmd | [optional] 
**real_memory** | **int** | configured MB of real memory on the node | [optional] 
**reason** | **str** | reason for node being DOWN or DRAINING | [optional] 
**reason_changed_at** | **int** | Time stamp when reason was set | [optional] 
**reason_set_by_user** | **str** | User that set the reason | [optional] 
**slurmd_start_time** | **int** | timestamp of slurmd startup | [optional] 
**sockets** | **int** | total number of sockets per node | [optional] 
**threads** | **int** | number of threads per core | [optional] 
**temporary_disk** | **int** | configured MB of total disk in TMP_FS | [optional] 
**weight** | **int** | arbitrary priority of node for scheduling | [optional] 
**tres** | **str** | TRES on node | [optional] 
**slurmd_version** | **str** | Slurmd version | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


