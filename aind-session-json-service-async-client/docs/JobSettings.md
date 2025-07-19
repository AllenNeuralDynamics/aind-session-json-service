# JobSettings

Data that needs to be input by user. Can be pulled from env vars with BERGAMO prefix or set explicitly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_settings_name** | **str** |  | [optional] [default to 'Bergamo']
**input_source** | [**InputSource**](InputSource.md) |  | [optional] 
**output_directory** | [**OutputDirectory**](OutputDirectory.md) |  | [optional] 
**user_settings_config_file** | [**UserSettingsConfigFile**](UserSettingsConfigFile.md) |  | [optional] 
**experimenter_full_name** | **List[str]** |  | 
**subject_id** | **str** |  | 
**imaging_laser_wavelength** | **int** |  | 
**fov_imaging_depth** | **int** |  | 
**fov_targeted_structure** | **str** |  | 
**notes** | **str** |  | 
**mouse_platform_name** | **str** |  | [optional] [default to 'Standard Mouse Tube']
**active_mouse_platform** | **bool** |  | [optional] [default to False]
**session_type** | **str** |  | [optional] [default to 'BCI']
**iacuc_protocol** | **str** |  | [optional] [default to '2109']
**rig_id** | **str** |  | [optional] [default to '442 Bergamo 2p photostim']
**behavior_camera_names** | **List[str]** |  | [optional] [default to [Side Face Camera, Bottom Face Camera]]
**ch1_filter_names** | **List[str]** |  | [optional] [default to [Green emission filter, Emission dichroic]]
**ch1_detector_name** | **str** |  | [optional] [default to 'Green PMT']
**ch1_daq_name** | **str** |  | [optional] [default to 'PXI']
**ch2_filter_names** | **List[str]** |  | [optional] [default to [Red emission filter, Emission dichroic]]
**ch2_detector_name** | **str** |  | [optional] [default to 'Red PMT']
**ch2_daq_name** | **str** |  | [optional] [default to 'PXI']
**imaging_laser_name** | **str** |  | [optional] [default to 'Chameleon Laser']
**photostim_laser_name** | **str** |  | [optional] [default to 'Monaco Laser']
**stimulus_device_names** | **List[str]** |  | [optional] [default to [speaker, lickport]]
**photostim_laser_wavelength** | **int** |  | [optional] [default to 1040]
**fov_coordinate_ml** | [**FovCoordinateMl**](FovCoordinateMl.md) |  | [optional] 
**fov_coordinate_ap** | **float** |  | [optional] [default to 1.5]
**fov_reference** | **str** |  | [optional] [default to 'Bregma']
**starting_lickport_position** | **List[float]** |  | [optional] [default to [0, -6, 0]]
**behavior_task_name** | **str** |  | [optional] [default to 'single neuron BCI conditioning']
**hit_rate_trials_0_10** | **float** |  | [optional] 
**hit_rate_trials_20_40** | **float** |  | [optional] 
**total_hits** | **float** |  | [optional] 
**average_hit_rate** | **float** |  | [optional] 
**trial_num** | **float** |  | [optional] 
**timezone** | **str** |  | [optional] [default to 'US/Pacific']

## Example

```python
from aind_session_json_service_async_client.models.job_settings import JobSettings

# TODO update the JSON string below
json = "{}"
# create an instance of JobSettings from a JSON string
job_settings_instance = JobSettings.from_json(json)
# print the JSON string representation of the object
print(JobSettings.to_json())

# convert the object into a dict
job_settings_dict = job_settings_instance.to_dict()
# create an instance of JobSettings from a dict
job_settings_from_dict = JobSettings.from_dict(job_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


