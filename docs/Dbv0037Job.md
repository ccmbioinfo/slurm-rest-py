# Dbv0037Job

Single job description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account charged by job | [optional] 
**comment** | [**Dbv0036JobComment**](Dbv0036JobComment.md) |  | [optional] 
**allocation_nodes** | **str** | Nodes allocated to job | [optional] 
**array** | [**Dbv0036JobArray**](Dbv0036JobArray.md) |  | [optional] 
**time** | [**Dbv0036JobTime**](Dbv0036JobTime.md) |  | [optional] 
**association** | [**Dbv0037AssociationShortInfo**](Dbv0037AssociationShortInfo.md) |  | [optional] 
**cluster** | **str** | Assigned cluster | [optional] 
**constraints** | **str** | Constraints on job | [optional] 
**derived_exit_code** | [**Dbv0037JobExitCode**](Dbv0037JobExitCode.md) |  | [optional] 
**exit_code** | [**Dbv0037JobExitCode**](Dbv0037JobExitCode.md) |  | [optional] 
**flags** | **[str]** | List of properties of job | [optional] 
**group** | **str** | User&#39;s group to run job | [optional] 
**het** | [**Dbv0036JobHet**](Dbv0036JobHet.md) |  | [optional] 
**job_id** | **int** | Job id | [optional] 
**name** | **str** | Assigned job name | [optional] 
**mcs** | [**Dbv0036JobMcs**](Dbv0036JobMcs.md) |  | [optional] 
**nodes** | **str** | List of nodes allocated for job | [optional] 
**partition** | **str** | Assigned job&#39;s partition | [optional] 
**priority** | **int** | Priority | [optional] 
**qos** | **str** | Assigned qos name | [optional] 
**required** | [**Dbv0036JobRequired**](Dbv0036JobRequired.md) |  | [optional] 
**kill_request_user** | **str** | User who requested job killed | [optional] 
**reservation** | [**Dbv0036JobReservation**](Dbv0036JobReservation.md) |  | [optional] 
**state** | [**Dbv0037JobState**](Dbv0037JobState.md) |  | [optional] 
**steps** | [**[Dbv0037JobStep]**](Dbv0037JobStep.md) | Job step description | [optional] 
**tres** | [**Dbv0037JobTres**](Dbv0037JobTres.md) |  | [optional] 
**user** | **str** | Job user | [optional] 
**wckey** | [**Dbv0036JobWckey**](Dbv0036JobWckey.md) |  | [optional] 
**working_directory** | **str** | Directory where job was initially started | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


