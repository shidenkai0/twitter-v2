# Get2ComplianceJobsIdResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ComplianceJob**](ComplianceJob.md) |  | [optional] 
**errors** | [**List[Problem]**](Problem.md) |  | [optional] 

## Example

```python
from twitter_api_v2.models.get2_compliance_jobs_id_response import Get2ComplianceJobsIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Get2ComplianceJobsIdResponse from a JSON string
get2_compliance_jobs_id_response_instance = Get2ComplianceJobsIdResponse.from_json(json)
# print the JSON string representation of the object
print Get2ComplianceJobsIdResponse.to_json()

# convert the object into a dict
get2_compliance_jobs_id_response_dict = get2_compliance_jobs_id_response_instance.to_dict()
# create an instance of Get2ComplianceJobsIdResponse from a dict
get2_compliance_jobs_id_response_form_dict = get2_compliance_jobs_id_response.from_dict(get2_compliance_jobs_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


