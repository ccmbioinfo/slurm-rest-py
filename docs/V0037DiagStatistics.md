# V0037DiagStatistics

Slurm statistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parts_packed** | **int** | partition records packed | [optional] 
**req_time** | **int** | generation time | [optional] 
**req_time_start** | **int** | data since | [optional] 
**server_thread_count** | **int** | Server thread count | [optional] 
**agent_queue_size** | **int** | Agent queue size | [optional] 
**agent_count** | **int** | Agent count | [optional] 
**agent_thread_count** | **int** | Agent thread count | [optional] 
**dbd_agent_queue_size** | **int** | DBD Agent queue size | [optional] 
**gettimeofday_latency** | **int** | Latency for 1000 calls to gettimeofday() | [optional] 
**schedule_cycle_max** | **int** | Main Schedule max cycle | [optional] 
**schedule_cycle_last** | **int** | Main Schedule last cycle | [optional] 
**schedule_cycle_total** | **int** | Main Schedule cycle iterations | [optional] 
**schedule_cycle_mean** | **int** | Average time for Schedule Max cycle | [optional] 
**schedule_cycle_mean_depth** | **int** | Average depth for Schedule Max cycle | [optional] 
**schedule_cycle_per_minute** | **int** | Main Schedule Cycles per minute | [optional] 
**schedule_queue_length** | **int** | Main Schedule Last queue length | [optional] 
**jobs_submitted** | **int** | Job submitted | [optional] 
**jobs_started** | **int** | Job started | [optional] 
**jobs_completed** | **int** | Job completed | [optional] 
**jobs_canceled** | **int** | Job cancelled | [optional] 
**jobs_failed** | **int** | Job failed | [optional] 
**jobs_pending** | **int** | Job pending | [optional] 
**jobs_running** | **int** | Job running | [optional] 
**job_states_ts** | **int** | Job states timestamp | [optional] 
**bf_backfilled_jobs** | **int** | Total backfilled jobs (since last slurm start) | [optional] 
**bf_last_backfilled_jobs** | **int** | Total backfilled jobs (since last stats cycle start) | [optional] 
**bf_backfilled_het_jobs** | **int** | Total backfilled heterogeneous job components | [optional] 
**bf_cycle_counter** | **int** | Backfill Schedule Total cycles | [optional] 
**bf_cycle_mean** | **int** | Backfill Schedule Mean cycle | [optional] 
**bf_cycle_max** | **int** | Backfill Schedule Max cycle time | [optional] 
**bf_last_depth** | **int** | Backfill Schedule Last depth cycle | [optional] 
**bf_last_depth_try** | **int** | Backfill Schedule Mean cycle (try sched) | [optional] 
**bf_depth_mean** | **int** | Backfill Schedule Depth Mean | [optional] 
**bf_depth_mean_try** | **int** | Backfill Schedule Depth Mean (try sched) | [optional] 
**bf_cycle_last** | **int** | Backfill Schedule Last cycle time | [optional] 
**bf_queue_len** | **int** | Backfill Schedule Last queue length | [optional] 
**bf_queue_len_mean** | **int** | Backfill Schedule Mean queue length | [optional] 
**bf_when_last_cycle** | **int** | Last cycle timestamp | [optional] 
**bf_active** | **bool** | Backfill Schedule currently active | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


