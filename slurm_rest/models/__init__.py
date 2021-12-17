# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from slurm_rest.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from slurm_rest.model.dbv0036_account import Dbv0036Account
from slurm_rest.model.dbv0036_account_info import Dbv0036AccountInfo
from slurm_rest.model.dbv0036_account_response import Dbv0036AccountResponse
from slurm_rest.model.dbv0036_association import Dbv0036Association
from slurm_rest.model.dbv0036_association_default import Dbv0036AssociationDefault
from slurm_rest.model.dbv0036_association_max import Dbv0036AssociationMax
from slurm_rest.model.dbv0036_association_max_jobs import Dbv0036AssociationMaxJobs
from slurm_rest.model.dbv0036_association_max_jobs_per import Dbv0036AssociationMaxJobsPer
from slurm_rest.model.dbv0036_association_max_per import Dbv0036AssociationMaxPer
from slurm_rest.model.dbv0036_association_max_per_account import Dbv0036AssociationMaxPerAccount
from slurm_rest.model.dbv0036_association_max_tres import Dbv0036AssociationMaxTres
from slurm_rest.model.dbv0036_association_max_tres_minutes import Dbv0036AssociationMaxTresMinutes
from slurm_rest.model.dbv0036_association_max_tres_minutes_per import Dbv0036AssociationMaxTresMinutesPer
from slurm_rest.model.dbv0036_association_max_tres_per import Dbv0036AssociationMaxTresPer
from slurm_rest.model.dbv0036_association_min import Dbv0036AssociationMin
from slurm_rest.model.dbv0036_association_short_info import Dbv0036AssociationShortInfo
from slurm_rest.model.dbv0036_association_usage import Dbv0036AssociationUsage
from slurm_rest.model.dbv0036_associations_info import Dbv0036AssociationsInfo
from slurm_rest.model.dbv0036_cluster_info import Dbv0036ClusterInfo
from slurm_rest.model.dbv0036_cluster_info_associations import Dbv0036ClusterInfoAssociations
from slurm_rest.model.dbv0036_cluster_info_controller import Dbv0036ClusterInfoController
from slurm_rest.model.dbv0036_config_info import Dbv0036ConfigInfo
from slurm_rest.model.dbv0036_config_response import Dbv0036ConfigResponse
from slurm_rest.model.dbv0036_coordinator_info import Dbv0036CoordinatorInfo
from slurm_rest.model.dbv0036_diag import Dbv0036Diag
from slurm_rest.model.dbv0036_diag_rpcs import Dbv0036DiagRPCs
from slurm_rest.model.dbv0036_diag_rollups import Dbv0036DiagRollups
from slurm_rest.model.dbv0036_diag_time import Dbv0036DiagTime
from slurm_rest.model.dbv0036_diag_time1 import Dbv0036DiagTime1
from slurm_rest.model.dbv0036_diag_users import Dbv0036DiagUsers
from slurm_rest.model.dbv0036_error import Dbv0036Error
from slurm_rest.model.dbv0036_job import Dbv0036Job
from slurm_rest.model.dbv0036_job_array import Dbv0036JobArray
from slurm_rest.model.dbv0036_job_array_limits import Dbv0036JobArrayLimits
from slurm_rest.model.dbv0036_job_array_limits_max import Dbv0036JobArrayLimitsMax
from slurm_rest.model.dbv0036_job_array_limits_max_running import Dbv0036JobArrayLimitsMaxRunning
from slurm_rest.model.dbv0036_job_comment import Dbv0036JobComment
from slurm_rest.model.dbv0036_job_exit_code import Dbv0036JobExitCode
from slurm_rest.model.dbv0036_job_exit_code_signal import Dbv0036JobExitCodeSignal
from slurm_rest.model.dbv0036_job_het import Dbv0036JobHet
from slurm_rest.model.dbv0036_job_info import Dbv0036JobInfo
from slurm_rest.model.dbv0036_job_mcs import Dbv0036JobMcs
from slurm_rest.model.dbv0036_job_required import Dbv0036JobRequired
from slurm_rest.model.dbv0036_job_reservation import Dbv0036JobReservation
from slurm_rest.model.dbv0036_job_state import Dbv0036JobState
from slurm_rest.model.dbv0036_job_step import Dbv0036JobStep
from slurm_rest.model.dbv0036_job_step_cpu import Dbv0036JobStepCPU
from slurm_rest.model.dbv0036_job_step_cpu_requested_frequency import Dbv0036JobStepCPURequestedFrequency
from slurm_rest.model.dbv0036_job_step_nodes import Dbv0036JobStepNodes
from slurm_rest.model.dbv0036_job_step_statistics import Dbv0036JobStepStatistics
from slurm_rest.model.dbv0036_job_step_statistics_cpu import Dbv0036JobStepStatisticsCPU
from slurm_rest.model.dbv0036_job_step_statistics_energy import Dbv0036JobStepStatisticsEnergy
from slurm_rest.model.dbv0036_job_step_step import Dbv0036JobStepStep
from slurm_rest.model.dbv0036_job_step_step_het import Dbv0036JobStepStepHet
from slurm_rest.model.dbv0036_job_step_step_task import Dbv0036JobStepStepTask
from slurm_rest.model.dbv0036_job_step_step_tres import Dbv0036JobStepStepTres
from slurm_rest.model.dbv0036_job_step_step_tres_requested import Dbv0036JobStepStepTresRequested
from slurm_rest.model.dbv0036_job_step_tasks import Dbv0036JobStepTasks
from slurm_rest.model.dbv0036_job_step_time import Dbv0036JobStepTime
from slurm_rest.model.dbv0036_job_time import Dbv0036JobTime
from slurm_rest.model.dbv0036_job_time_system import Dbv0036JobTimeSystem
from slurm_rest.model.dbv0036_job_time_total import Dbv0036JobTimeTotal
from slurm_rest.model.dbv0036_job_time_user import Dbv0036JobTimeUser
from slurm_rest.model.dbv0036_job_tres import Dbv0036JobTres
from slurm_rest.model.dbv0036_job_wckey import Dbv0036JobWckey
from slurm_rest.model.dbv0036_qos import Dbv0036Qos
from slurm_rest.model.dbv0036_qos_info import Dbv0036QosInfo
from slurm_rest.model.dbv0036_qos_limits import Dbv0036QosLimits
from slurm_rest.model.dbv0036_qos_limits_max import Dbv0036QosLimitsMax
from slurm_rest.model.dbv0036_qos_limits_max_accruing import Dbv0036QosLimitsMaxAccruing
from slurm_rest.model.dbv0036_qos_limits_max_accruing_per import Dbv0036QosLimitsMaxAccruingPer
from slurm_rest.model.dbv0036_qos_limits_max_jobs import Dbv0036QosLimitsMaxJobs
from slurm_rest.model.dbv0036_qos_limits_max_jobs_per import Dbv0036QosLimitsMaxJobsPer
from slurm_rest.model.dbv0036_qos_limits_max_tres import Dbv0036QosLimitsMaxTres
from slurm_rest.model.dbv0036_qos_limits_max_tres_minutes import Dbv0036QosLimitsMaxTresMinutes
from slurm_rest.model.dbv0036_qos_limits_max_tres_minutes_per import Dbv0036QosLimitsMaxTresMinutesPer
from slurm_rest.model.dbv0036_qos_limits_max_tres_per import Dbv0036QosLimitsMaxTresPer
from slurm_rest.model.dbv0036_qos_limits_max_wall_clock import Dbv0036QosLimitsMaxWallClock
from slurm_rest.model.dbv0036_qos_limits_max_wall_clock_per import Dbv0036QosLimitsMaxWallClockPer
from slurm_rest.model.dbv0036_qos_limits_min import Dbv0036QosLimitsMin
from slurm_rest.model.dbv0036_qos_limits_min_tres import Dbv0036QosLimitsMinTres
from slurm_rest.model.dbv0036_qos_limits_min_tres_per import Dbv0036QosLimitsMinTresPer
from slurm_rest.model.dbv0036_qos_preempt import Dbv0036QosPreempt
from slurm_rest.model.dbv0036_response_account_delete import Dbv0036ResponseAccountDelete
from slurm_rest.model.dbv0036_response_association_delete import Dbv0036ResponseAssociationDelete
from slurm_rest.model.dbv0036_response_cluster_add import Dbv0036ResponseClusterAdd
from slurm_rest.model.dbv0036_response_cluster_delete import Dbv0036ResponseClusterDelete
from slurm_rest.model.dbv0036_response_qos_delete import Dbv0036ResponseQosDelete
from slurm_rest.model.dbv0036_response_tres import Dbv0036ResponseTres
from slurm_rest.model.dbv0036_response_user_delete import Dbv0036ResponseUserDelete
from slurm_rest.model.dbv0036_response_user_update import Dbv0036ResponseUserUpdate
from slurm_rest.model.dbv0036_response_wckey_add import Dbv0036ResponseWckeyAdd
from slurm_rest.model.dbv0036_response_wckey_delete import Dbv0036ResponseWckeyDelete
from slurm_rest.model.dbv0036_tres_info import Dbv0036TresInfo
from slurm_rest.model.dbv0036_tres_list import Dbv0036TresList
from slurm_rest.model.dbv0036_user import Dbv0036User
from slurm_rest.model.dbv0036_user_associations import Dbv0036UserAssociations
from slurm_rest.model.dbv0036_user_default import Dbv0036UserDefault
from slurm_rest.model.dbv0036_user_info import Dbv0036UserInfo
from slurm_rest.model.dbv0036_wckey import Dbv0036Wckey
from slurm_rest.model.dbv0036_wckey_info import Dbv0036WckeyInfo
from slurm_rest.model.dbv0037_account import Dbv0037Account
from slurm_rest.model.dbv0037_account_info import Dbv0037AccountInfo
from slurm_rest.model.dbv0037_account_response import Dbv0037AccountResponse
from slurm_rest.model.dbv0037_association import Dbv0037Association
from slurm_rest.model.dbv0037_association_max import Dbv0037AssociationMax
from slurm_rest.model.dbv0037_association_max_tres import Dbv0037AssociationMaxTres
from slurm_rest.model.dbv0037_association_max_tres_minutes import Dbv0037AssociationMaxTresMinutes
from slurm_rest.model.dbv0037_association_max_tres_minutes_per import Dbv0037AssociationMaxTresMinutesPer
from slurm_rest.model.dbv0037_association_max_tres_per import Dbv0037AssociationMaxTresPer
from slurm_rest.model.dbv0037_association_short_info import Dbv0037AssociationShortInfo
from slurm_rest.model.dbv0037_associations_info import Dbv0037AssociationsInfo
from slurm_rest.model.dbv0037_cluster_info import Dbv0037ClusterInfo
from slurm_rest.model.dbv0037_cluster_info_associations import Dbv0037ClusterInfoAssociations
from slurm_rest.model.dbv0037_config_info import Dbv0037ConfigInfo
from slurm_rest.model.dbv0037_config_response import Dbv0037ConfigResponse
from slurm_rest.model.dbv0037_coordinator_info import Dbv0037CoordinatorInfo
from slurm_rest.model.dbv0037_diag import Dbv0037Diag
from slurm_rest.model.dbv0037_error import Dbv0037Error
from slurm_rest.model.dbv0037_job import Dbv0037Job
from slurm_rest.model.dbv0037_job_exit_code import Dbv0037JobExitCode
from slurm_rest.model.dbv0037_job_info import Dbv0037JobInfo
from slurm_rest.model.dbv0037_job_state import Dbv0037JobState
from slurm_rest.model.dbv0037_job_step import Dbv0037JobStep
from slurm_rest.model.dbv0037_job_step_step import Dbv0037JobStepStep
from slurm_rest.model.dbv0037_job_step_step_tres import Dbv0037JobStepStepTres
from slurm_rest.model.dbv0037_job_step_step_tres_requested import Dbv0037JobStepStepTresRequested
from slurm_rest.model.dbv0037_job_tres import Dbv0037JobTres
from slurm_rest.model.dbv0037_qos import Dbv0037Qos
from slurm_rest.model.dbv0037_qos_info import Dbv0037QosInfo
from slurm_rest.model.dbv0037_qos_limits import Dbv0037QosLimits
from slurm_rest.model.dbv0037_qos_limits_max import Dbv0037QosLimitsMax
from slurm_rest.model.dbv0037_qos_limits_max_tres import Dbv0037QosLimitsMaxTres
from slurm_rest.model.dbv0037_qos_limits_max_tres_minutes import Dbv0037QosLimitsMaxTresMinutes
from slurm_rest.model.dbv0037_qos_limits_max_tres_minutes_per import Dbv0037QosLimitsMaxTresMinutesPer
from slurm_rest.model.dbv0037_qos_limits_max_tres_per import Dbv0037QosLimitsMaxTresPer
from slurm_rest.model.dbv0037_qos_limits_min import Dbv0037QosLimitsMin
from slurm_rest.model.dbv0037_qos_limits_min_tres import Dbv0037QosLimitsMinTres
from slurm_rest.model.dbv0037_qos_limits_min_tres_per import Dbv0037QosLimitsMinTresPer
from slurm_rest.model.dbv0037_response_account_delete import Dbv0037ResponseAccountDelete
from slurm_rest.model.dbv0037_response_association_delete import Dbv0037ResponseAssociationDelete
from slurm_rest.model.dbv0037_response_cluster_add import Dbv0037ResponseClusterAdd
from slurm_rest.model.dbv0037_response_cluster_delete import Dbv0037ResponseClusterDelete
from slurm_rest.model.dbv0037_response_qos_delete import Dbv0037ResponseQosDelete
from slurm_rest.model.dbv0037_response_tres import Dbv0037ResponseTres
from slurm_rest.model.dbv0037_response_user_delete import Dbv0037ResponseUserDelete
from slurm_rest.model.dbv0037_response_user_update import Dbv0037ResponseUserUpdate
from slurm_rest.model.dbv0037_response_wckey_add import Dbv0037ResponseWckeyAdd
from slurm_rest.model.dbv0037_response_wckey_delete import Dbv0037ResponseWckeyDelete
from slurm_rest.model.dbv0037_tres_info import Dbv0037TresInfo
from slurm_rest.model.dbv0037_tres_list import Dbv0037TresList
from slurm_rest.model.dbv0037_user import Dbv0037User
from slurm_rest.model.dbv0037_user_associations import Dbv0037UserAssociations
from slurm_rest.model.dbv0037_user_info import Dbv0037UserInfo
from slurm_rest.model.dbv0037_wckey import Dbv0037Wckey
from slurm_rest.model.dbv0037_wckey_info import Dbv0037WckeyInfo
from slurm_rest.model.job_properties import JobProperties
from slurm_rest.model.signal import Signal
from slurm_rest.model.signal_one_of import SignalOneOf
from slurm_rest.model.v0036_diag import V0036Diag
from slurm_rest.model.v0036_error import V0036Error
from slurm_rest.model.v0036_job_properties import V0036JobProperties
from slurm_rest.model.v0036_job_resources import V0036JobResources
from slurm_rest.model.v0036_job_response_properties import V0036JobResponseProperties
from slurm_rest.model.v0036_job_submission import V0036JobSubmission
from slurm_rest.model.v0036_job_submission_response import V0036JobSubmissionResponse
from slurm_rest.model.v0036_jobs_response import V0036JobsResponse
from slurm_rest.model.v0036_node import V0036Node
from slurm_rest.model.v0036_node_allocation import V0036NodeAllocation
from slurm_rest.model.v0036_nodes_response import V0036NodesResponse
from slurm_rest.model.v0036_partition import V0036Partition
from slurm_rest.model.v0036_partitions_response import V0036PartitionsResponse
from slurm_rest.model.v0036_ping import V0036Ping
from slurm_rest.model.v0036_pings import V0036Pings
from slurm_rest.model.v0036_signal import V0036Signal
from slurm_rest.model.v0037_diag import V0037Diag
from slurm_rest.model.v0037_diag_statistics import V0037DiagStatistics
from slurm_rest.model.v0037_error import V0037Error
from slurm_rest.model.v0037_job_properties import V0037JobProperties
from slurm_rest.model.v0037_job_resources import V0037JobResources
from slurm_rest.model.v0037_job_response_properties import V0037JobResponseProperties
from slurm_rest.model.v0037_job_submission import V0037JobSubmission
from slurm_rest.model.v0037_job_submission_response import V0037JobSubmissionResponse
from slurm_rest.model.v0037_jobs_response import V0037JobsResponse
from slurm_rest.model.v0037_node import V0037Node
from slurm_rest.model.v0037_node_allocation import V0037NodeAllocation
from slurm_rest.model.v0037_nodes_response import V0037NodesResponse
from slurm_rest.model.v0037_partition import V0037Partition
from slurm_rest.model.v0037_partitions_response import V0037PartitionsResponse
from slurm_rest.model.v0037_ping import V0037Ping
from slurm_rest.model.v0037_pings import V0037Pings
from slurm_rest.model.v0037_reservation import V0037Reservation
from slurm_rest.model.v0037_reservation_purge_completed import V0037ReservationPurgeCompleted
from slurm_rest.model.v0037_reservations_response import V0037ReservationsResponse
from slurm_rest.model.v0037_signal import V0037Signal
