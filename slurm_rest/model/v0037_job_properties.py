"""
    Slurm Rest API

    API to access and control Slurm.  # noqa: E501

    The version of the OpenAPI document: 0.0.37
    Contact: sales@schedmd.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from slurm_rest.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from slurm_rest.exceptions import ApiAttributeError



class V0037JobProperties(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('exclusive',): {
            'USER': "user",
            'MCS': "mcs",
            'TRUE': "true",
            'FALSE': "false",
        },
        ('gres_flags',): {
            'DISABLE-BINDING': "disable-binding",
            'ENFORCE-BINDING': "enforce-binding",
        },
        ('open_mode',): {
            'APPEND': "append",
            'TRUNCATE': "truncate",
        },
    }

    validations = {
        ('nodes',): {
            'max_items': 2,
            'min_items': 1,
        },
        ('signal',): {
            'regex': {
                'pattern': r'(B:|)sig_num(@sig_time|)',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'environment': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'account': (str,),  # noqa: E501
            'account_gather_freqency': (str,),  # noqa: E501
            'argv': ([str],),  # noqa: E501
            'array': (str,),  # noqa: E501
            'batch_features': (str,),  # noqa: E501
            'begin_time': (int,),  # noqa: E501
            'burst_buffer': (str,),  # noqa: E501
            'cluster_constraints': (str,),  # noqa: E501
            'comment': (str,),  # noqa: E501
            'constraints': (str,),  # noqa: E501
            'core_specification': (int,),  # noqa: E501
            'cores_per_socket': (int,),  # noqa: E501
            'cpu_binding': (str,),  # noqa: E501
            'cpu_binding_hint': (str,),  # noqa: E501
            'cpu_frequency': (str,),  # noqa: E501
            'cpus_per_gpu': (str,),  # noqa: E501
            'cpus_per_task': (int,),  # noqa: E501
            'current_working_directory': (str,),  # noqa: E501
            'deadline': (str,),  # noqa: E501
            'delay_boot': (int,),  # noqa: E501
            'dependency': (str,),  # noqa: E501
            'distribution': (str,),  # noqa: E501
            'exclusive': (str,),  # noqa: E501
            'get_user_environment': (bool,),  # noqa: E501
            'gres': (str,),  # noqa: E501
            'gres_flags': (str,),  # noqa: E501
            'gpu_binding': (str,),  # noqa: E501
            'gpu_frequency': (str,),  # noqa: E501
            'gpus': (str,),  # noqa: E501
            'gpus_per_node': (str,),  # noqa: E501
            'gpus_per_socket': (str,),  # noqa: E501
            'gpus_per_task': (str,),  # noqa: E501
            'hold': (bool,),  # noqa: E501
            'kill_on_invalid_dependency': (bool,),  # noqa: E501
            'licenses': (str,),  # noqa: E501
            'mail_type': (str,),  # noqa: E501
            'mail_user': (str,),  # noqa: E501
            'mcs_label': (str,),  # noqa: E501
            'memory_binding': (str,),  # noqa: E501
            'memory_per_cpu': (int,),  # noqa: E501
            'memory_per_gpu': (int,),  # noqa: E501
            'memory_per_node': (int,),  # noqa: E501
            'minimum_cpus_per_node': (int,),  # noqa: E501
            'minimum_nodes': (bool,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'nice': (str,),  # noqa: E501
            'no_kill': (bool,),  # noqa: E501
            'nodes': ([int],),  # noqa: E501
            'open_mode': (str,),  # noqa: E501
            'partition': (str,),  # noqa: E501
            'priority': (str,),  # noqa: E501
            'qos': (str,),  # noqa: E501
            'requeue': (bool,),  # noqa: E501
            'reservation': (str,),  # noqa: E501
            'signal': (str,),  # noqa: E501
            'sockets_per_node': (int,),  # noqa: E501
            'spread_job': (bool,),  # noqa: E501
            'standard_error': (str,),  # noqa: E501
            'standard_input': (str,),  # noqa: E501
            'standard_output': (str,),  # noqa: E501
            'tasks': (int,),  # noqa: E501
            'tasks_per_core': (int,),  # noqa: E501
            'tasks_per_node': (int,),  # noqa: E501
            'tasks_per_socket': (int,),  # noqa: E501
            'thread_specification': (int,),  # noqa: E501
            'threads_per_core': (int,),  # noqa: E501
            'time_limit': (int,),  # noqa: E501
            'time_minimum': (int,),  # noqa: E501
            'wait_all_nodes': (bool,),  # noqa: E501
            'wckey': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'environment': 'environment',  # noqa: E501
        'account': 'account',  # noqa: E501
        'account_gather_freqency': 'account_gather_freqency',  # noqa: E501
        'argv': 'argv',  # noqa: E501
        'array': 'array',  # noqa: E501
        'batch_features': 'batch_features',  # noqa: E501
        'begin_time': 'begin_time',  # noqa: E501
        'burst_buffer': 'burst_buffer',  # noqa: E501
        'cluster_constraints': 'cluster_constraints',  # noqa: E501
        'comment': 'comment',  # noqa: E501
        'constraints': 'constraints',  # noqa: E501
        'core_specification': 'core_specification',  # noqa: E501
        'cores_per_socket': 'cores_per_socket',  # noqa: E501
        'cpu_binding': 'cpu_binding',  # noqa: E501
        'cpu_binding_hint': 'cpu_binding_hint',  # noqa: E501
        'cpu_frequency': 'cpu_frequency',  # noqa: E501
        'cpus_per_gpu': 'cpus_per_gpu',  # noqa: E501
        'cpus_per_task': 'cpus_per_task',  # noqa: E501
        'current_working_directory': 'current_working_directory',  # noqa: E501
        'deadline': 'deadline',  # noqa: E501
        'delay_boot': 'delay_boot',  # noqa: E501
        'dependency': 'dependency',  # noqa: E501
        'distribution': 'distribution',  # noqa: E501
        'exclusive': 'exclusive',  # noqa: E501
        'get_user_environment': 'get_user_environment',  # noqa: E501
        'gres': 'gres',  # noqa: E501
        'gres_flags': 'gres_flags',  # noqa: E501
        'gpu_binding': 'gpu_binding',  # noqa: E501
        'gpu_frequency': 'gpu_frequency',  # noqa: E501
        'gpus': 'gpus',  # noqa: E501
        'gpus_per_node': 'gpus_per_node',  # noqa: E501
        'gpus_per_socket': 'gpus_per_socket',  # noqa: E501
        'gpus_per_task': 'gpus_per_task',  # noqa: E501
        'hold': 'hold',  # noqa: E501
        'kill_on_invalid_dependency': 'kill_on_invalid_dependency',  # noqa: E501
        'licenses': 'licenses',  # noqa: E501
        'mail_type': 'mail_type',  # noqa: E501
        'mail_user': 'mail_user',  # noqa: E501
        'mcs_label': 'mcs_label',  # noqa: E501
        'memory_binding': 'memory_binding',  # noqa: E501
        'memory_per_cpu': 'memory_per_cpu',  # noqa: E501
        'memory_per_gpu': 'memory_per_gpu',  # noqa: E501
        'memory_per_node': 'memory_per_node',  # noqa: E501
        'minimum_cpus_per_node': 'minimum_cpus_per_node',  # noqa: E501
        'minimum_nodes': 'minimum_nodes',  # noqa: E501
        'name': 'name',  # noqa: E501
        'nice': 'nice',  # noqa: E501
        'no_kill': 'no_kill',  # noqa: E501
        'nodes': 'nodes',  # noqa: E501
        'open_mode': 'open_mode',  # noqa: E501
        'partition': 'partition',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'qos': 'qos',  # noqa: E501
        'requeue': 'requeue',  # noqa: E501
        'reservation': 'reservation',  # noqa: E501
        'signal': 'signal',  # noqa: E501
        'sockets_per_node': 'sockets_per_node',  # noqa: E501
        'spread_job': 'spread_job',  # noqa: E501
        'standard_error': 'standard_error',  # noqa: E501
        'standard_input': 'standard_input',  # noqa: E501
        'standard_output': 'standard_output',  # noqa: E501
        'tasks': 'tasks',  # noqa: E501
        'tasks_per_core': 'tasks_per_core',  # noqa: E501
        'tasks_per_node': 'tasks_per_node',  # noqa: E501
        'tasks_per_socket': 'tasks_per_socket',  # noqa: E501
        'thread_specification': 'thread_specification',  # noqa: E501
        'threads_per_core': 'threads_per_core',  # noqa: E501
        'time_limit': 'time_limit',  # noqa: E501
        'time_minimum': 'time_minimum',  # noqa: E501
        'wait_all_nodes': 'wait_all_nodes',  # noqa: E501
        'wckey': 'wckey',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, environment, *args, **kwargs):  # noqa: E501
        """V0037JobProperties - a model defined in OpenAPI

        Args:
            environment ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Dictionary of environment entries.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            account (str): Charge resources used by this job to specified account.. [optional]  # noqa: E501
            account_gather_freqency (str): Define the job accounting and profiling sampling intervals.. [optional]  # noqa: E501
            argv ([str]): Arguments to the script.. [optional]  # noqa: E501
            array (str): Submit a job array, multiple jobs to be executed with identical parameters. The indexes specification identifies what array index values should be used.. [optional]  # noqa: E501
            batch_features (str): features required for batch script's node. [optional]  # noqa: E501
            begin_time (int): Submit the batch script to the Slurm controller immediately, like normal, but tell the controller to defer the allocation of the job until the specified time.. [optional]  # noqa: E501
            burst_buffer (str): Burst buffer specification.. [optional]  # noqa: E501
            cluster_constraints (str): Specifies features that a federated cluster must have to have a sibling job submitted to it.. [optional]  # noqa: E501
            comment (str): An arbitrary comment.. [optional]  # noqa: E501
            constraints (str): node features required by job.. [optional]  # noqa: E501
            core_specification (int): Count of specialized threads per node reserved by the job for system operations and not used by the application.. [optional]  # noqa: E501
            cores_per_socket (int): Restrict node selection to nodes with at least the specified number of cores per socket.. [optional]  # noqa: E501
            cpu_binding (str): Cpu binding. [optional]  # noqa: E501
            cpu_binding_hint (str): Cpu binding hint. [optional]  # noqa: E501
            cpu_frequency (str): Request that job steps initiated by srun commands inside this sbatch script be run at some requested frequency if possible, on the CPUs selected for the step on the compute node(s).. [optional]  # noqa: E501
            cpus_per_gpu (str): Number of CPUs requested per allocated GPU.. [optional]  # noqa: E501
            cpus_per_task (int): Advise the Slurm controller that ensuing job steps will require ncpus number of processors per task.. [optional]  # noqa: E501
            current_working_directory (str): Instruct Slurm to connect the batch script's standard output directly to the file name.. [optional]  # noqa: E501
            deadline (str): Remove the job if no ending is possible before this deadline (start > (deadline - time[-min])).. [optional]  # noqa: E501
            delay_boot (int): Do not reboot nodes in order to satisfied this job's feature specification if the job has been eligible to run for less than this time period.. [optional]  # noqa: E501
            dependency (str): Defer the start of this job until the specified dependencies have been satisfied completed.. [optional]  # noqa: E501
            distribution (str): Specify alternate distribution methods for remote processes.. [optional]  # noqa: E501
            exclusive (str): The job allocation can share nodes just other users with the \"user\" option or with the \"mcs\" option).. [optional]  # noqa: E501
            get_user_environment (bool): Load new login environment for user on job node.. [optional]  # noqa: E501
            gres (str): Specifies a comma delimited list of generic consumable resources.. [optional]  # noqa: E501
            gres_flags (str): Specify generic resource task binding options.. [optional]  # noqa: E501
            gpu_binding (str): Requested binding of tasks to GPU.. [optional]  # noqa: E501
            gpu_frequency (str): Requested GPU frequency.. [optional]  # noqa: E501
            gpus (str): GPUs per job.. [optional]  # noqa: E501
            gpus_per_node (str): GPUs per node.. [optional]  # noqa: E501
            gpus_per_socket (str): GPUs per socket.. [optional]  # noqa: E501
            gpus_per_task (str): GPUs per task.. [optional]  # noqa: E501
            hold (bool): Specify the job is to be submitted in a held state (priority of zero).. [optional]  # noqa: E501
            kill_on_invalid_dependency (bool): If a job has an invalid dependency, then Slurm is to terminate it.. [optional]  # noqa: E501
            licenses (str): Specification of licenses (or other resources available on all nodes of the cluster) which must be allocated to this job.. [optional]  # noqa: E501
            mail_type (str): Notify user by email when certain event types occur.. [optional]  # noqa: E501
            mail_user (str): User to receive email notification of state changes as defined by mail_type.. [optional]  # noqa: E501
            mcs_label (str): This parameter is a group among the groups of the user.. [optional]  # noqa: E501
            memory_binding (str): Bind tasks to memory.. [optional]  # noqa: E501
            memory_per_cpu (int): Minimum real memory per cpu (MB).. [optional]  # noqa: E501
            memory_per_gpu (int): Minimum memory required per allocated GPU.. [optional]  # noqa: E501
            memory_per_node (int): Minimum real memory per node (MB).. [optional]  # noqa: E501
            minimum_cpus_per_node (int): Minimum number of CPUs per node.. [optional]  # noqa: E501
            minimum_nodes (bool): If a range of node counts is given, prefer the smaller count.. [optional]  # noqa: E501
            name (str): Specify a name for the job allocation.. [optional]  # noqa: E501
            nice (str): Run the job with an adjusted scheduling priority within Slurm.. [optional]  # noqa: E501
            no_kill (bool): Do not automatically terminate a job if one of the nodes it has been allocated fails.. [optional]  # noqa: E501
            nodes ([int]): Request that a minimum of minnodes nodes and a maximum node count.. [optional]  # noqa: E501
            open_mode (str): Open the output and error files using append or truncate mode as specified.. [optional] if omitted the server will use the default value of "append"  # noqa: E501
            partition (str): Request a specific partition for the resource allocation.. [optional]  # noqa: E501
            priority (str): Request a specific job priority.. [optional]  # noqa: E501
            qos (str): Request a quality of service for the job.. [optional]  # noqa: E501
            requeue (bool): Specifies that the batch job should eligible to being requeue.. [optional]  # noqa: E501
            reservation (str): Allocate resources for the job from the named reservation.. [optional]  # noqa: E501
            signal (str): When a job is within sig_time seconds of its end time, send it the signal sig_num.. [optional]  # noqa: E501
            sockets_per_node (int): Restrict node selection to nodes with at least the specified number of sockets.. [optional]  # noqa: E501
            spread_job (bool): Spread the job allocation over as many nodes as possible and attempt to evenly distribute tasks across the allocated nodes.. [optional]  # noqa: E501
            standard_error (str): Instruct Slurm to connect the batch script's standard error directly to the file name.. [optional]  # noqa: E501
            standard_input (str): Instruct Slurm to connect the batch script's standard input directly to the file name specified.. [optional]  # noqa: E501
            standard_output (str): Instruct Slurm to connect the batch script's standard output directly to the file name.. [optional]  # noqa: E501
            tasks (int): Advises the Slurm controller that job steps run within the allocation will launch a maximum of number tasks and to provide for sufficient resources.. [optional]  # noqa: E501
            tasks_per_core (int): Request the maximum ntasks be invoked on each core.. [optional]  # noqa: E501
            tasks_per_node (int): Request the maximum ntasks be invoked on each node.. [optional]  # noqa: E501
            tasks_per_socket (int): Request the maximum ntasks be invoked on each socket.. [optional]  # noqa: E501
            thread_specification (int): Count of specialized threads per node reserved by the job for system operations and not used by the application.. [optional]  # noqa: E501
            threads_per_core (int): Restrict node selection to nodes with at least the specified number of threads per core.. [optional]  # noqa: E501
            time_limit (int): Step time limit.. [optional]  # noqa: E501
            time_minimum (int): Minimum run time in minutes.. [optional]  # noqa: E501
            wait_all_nodes (bool): Do not begin execution until all nodes are ready for use.. [optional]  # noqa: E501
            wckey (str): Specify wckey to be used with job.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.environment = environment
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, environment, *args, **kwargs):  # noqa: E501
        """V0037JobProperties - a model defined in OpenAPI

        Args:
            environment ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Dictionary of environment entries.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            account (str): Charge resources used by this job to specified account.. [optional]  # noqa: E501
            account_gather_freqency (str): Define the job accounting and profiling sampling intervals.. [optional]  # noqa: E501
            argv ([str]): Arguments to the script.. [optional]  # noqa: E501
            array (str): Submit a job array, multiple jobs to be executed with identical parameters. The indexes specification identifies what array index values should be used.. [optional]  # noqa: E501
            batch_features (str): features required for batch script's node. [optional]  # noqa: E501
            begin_time (int): Submit the batch script to the Slurm controller immediately, like normal, but tell the controller to defer the allocation of the job until the specified time.. [optional]  # noqa: E501
            burst_buffer (str): Burst buffer specification.. [optional]  # noqa: E501
            cluster_constraints (str): Specifies features that a federated cluster must have to have a sibling job submitted to it.. [optional]  # noqa: E501
            comment (str): An arbitrary comment.. [optional]  # noqa: E501
            constraints (str): node features required by job.. [optional]  # noqa: E501
            core_specification (int): Count of specialized threads per node reserved by the job for system operations and not used by the application.. [optional]  # noqa: E501
            cores_per_socket (int): Restrict node selection to nodes with at least the specified number of cores per socket.. [optional]  # noqa: E501
            cpu_binding (str): Cpu binding. [optional]  # noqa: E501
            cpu_binding_hint (str): Cpu binding hint. [optional]  # noqa: E501
            cpu_frequency (str): Request that job steps initiated by srun commands inside this sbatch script be run at some requested frequency if possible, on the CPUs selected for the step on the compute node(s).. [optional]  # noqa: E501
            cpus_per_gpu (str): Number of CPUs requested per allocated GPU.. [optional]  # noqa: E501
            cpus_per_task (int): Advise the Slurm controller that ensuing job steps will require ncpus number of processors per task.. [optional]  # noqa: E501
            current_working_directory (str): Instruct Slurm to connect the batch script's standard output directly to the file name.. [optional]  # noqa: E501
            deadline (str): Remove the job if no ending is possible before this deadline (start > (deadline - time[-min])).. [optional]  # noqa: E501
            delay_boot (int): Do not reboot nodes in order to satisfied this job's feature specification if the job has been eligible to run for less than this time period.. [optional]  # noqa: E501
            dependency (str): Defer the start of this job until the specified dependencies have been satisfied completed.. [optional]  # noqa: E501
            distribution (str): Specify alternate distribution methods for remote processes.. [optional]  # noqa: E501
            exclusive (str): The job allocation can share nodes just other users with the \"user\" option or with the \"mcs\" option).. [optional]  # noqa: E501
            get_user_environment (bool): Load new login environment for user on job node.. [optional]  # noqa: E501
            gres (str): Specifies a comma delimited list of generic consumable resources.. [optional]  # noqa: E501
            gres_flags (str): Specify generic resource task binding options.. [optional]  # noqa: E501
            gpu_binding (str): Requested binding of tasks to GPU.. [optional]  # noqa: E501
            gpu_frequency (str): Requested GPU frequency.. [optional]  # noqa: E501
            gpus (str): GPUs per job.. [optional]  # noqa: E501
            gpus_per_node (str): GPUs per node.. [optional]  # noqa: E501
            gpus_per_socket (str): GPUs per socket.. [optional]  # noqa: E501
            gpus_per_task (str): GPUs per task.. [optional]  # noqa: E501
            hold (bool): Specify the job is to be submitted in a held state (priority of zero).. [optional]  # noqa: E501
            kill_on_invalid_dependency (bool): If a job has an invalid dependency, then Slurm is to terminate it.. [optional]  # noqa: E501
            licenses (str): Specification of licenses (or other resources available on all nodes of the cluster) which must be allocated to this job.. [optional]  # noqa: E501
            mail_type (str): Notify user by email when certain event types occur.. [optional]  # noqa: E501
            mail_user (str): User to receive email notification of state changes as defined by mail_type.. [optional]  # noqa: E501
            mcs_label (str): This parameter is a group among the groups of the user.. [optional]  # noqa: E501
            memory_binding (str): Bind tasks to memory.. [optional]  # noqa: E501
            memory_per_cpu (int): Minimum real memory per cpu (MB).. [optional]  # noqa: E501
            memory_per_gpu (int): Minimum memory required per allocated GPU.. [optional]  # noqa: E501
            memory_per_node (int): Minimum real memory per node (MB).. [optional]  # noqa: E501
            minimum_cpus_per_node (int): Minimum number of CPUs per node.. [optional]  # noqa: E501
            minimum_nodes (bool): If a range of node counts is given, prefer the smaller count.. [optional]  # noqa: E501
            name (str): Specify a name for the job allocation.. [optional]  # noqa: E501
            nice (str): Run the job with an adjusted scheduling priority within Slurm.. [optional]  # noqa: E501
            no_kill (bool): Do not automatically terminate a job if one of the nodes it has been allocated fails.. [optional]  # noqa: E501
            nodes ([int]): Request that a minimum of minnodes nodes and a maximum node count.. [optional]  # noqa: E501
            open_mode (str): Open the output and error files using append or truncate mode as specified.. [optional] if omitted the server will use the default value of "append"  # noqa: E501
            partition (str): Request a specific partition for the resource allocation.. [optional]  # noqa: E501
            priority (str): Request a specific job priority.. [optional]  # noqa: E501
            qos (str): Request a quality of service for the job.. [optional]  # noqa: E501
            requeue (bool): Specifies that the batch job should eligible to being requeue.. [optional]  # noqa: E501
            reservation (str): Allocate resources for the job from the named reservation.. [optional]  # noqa: E501
            signal (str): When a job is within sig_time seconds of its end time, send it the signal sig_num.. [optional]  # noqa: E501
            sockets_per_node (int): Restrict node selection to nodes with at least the specified number of sockets.. [optional]  # noqa: E501
            spread_job (bool): Spread the job allocation over as many nodes as possible and attempt to evenly distribute tasks across the allocated nodes.. [optional]  # noqa: E501
            standard_error (str): Instruct Slurm to connect the batch script's standard error directly to the file name.. [optional]  # noqa: E501
            standard_input (str): Instruct Slurm to connect the batch script's standard input directly to the file name specified.. [optional]  # noqa: E501
            standard_output (str): Instruct Slurm to connect the batch script's standard output directly to the file name.. [optional]  # noqa: E501
            tasks (int): Advises the Slurm controller that job steps run within the allocation will launch a maximum of number tasks and to provide for sufficient resources.. [optional]  # noqa: E501
            tasks_per_core (int): Request the maximum ntasks be invoked on each core.. [optional]  # noqa: E501
            tasks_per_node (int): Request the maximum ntasks be invoked on each node.. [optional]  # noqa: E501
            tasks_per_socket (int): Request the maximum ntasks be invoked on each socket.. [optional]  # noqa: E501
            thread_specification (int): Count of specialized threads per node reserved by the job for system operations and not used by the application.. [optional]  # noqa: E501
            threads_per_core (int): Restrict node selection to nodes with at least the specified number of threads per core.. [optional]  # noqa: E501
            time_limit (int): Step time limit.. [optional]  # noqa: E501
            time_minimum (int): Minimum run time in minutes.. [optional]  # noqa: E501
            wait_all_nodes (bool): Do not begin execution until all nodes are ready for use.. [optional]  # noqa: E501
            wckey (str): Specify wckey to be used with job.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.environment = environment
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
