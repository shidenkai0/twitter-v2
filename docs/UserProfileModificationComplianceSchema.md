# UserProfileModificationComplianceSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_profile_modification** | [**UserProfileModificationObjectSchema**](UserProfileModificationObjectSchema.md) |  | 

## Example

```python
from twitter_v2.models.user_profile_modification_compliance_schema import UserProfileModificationComplianceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileModificationComplianceSchema from a JSON string
user_profile_modification_compliance_schema_instance = UserProfileModificationComplianceSchema.from_json(json)
# print the JSON string representation of the object
print UserProfileModificationComplianceSchema.to_json()

# convert the object into a dict
user_profile_modification_compliance_schema_dict = user_profile_modification_compliance_schema_instance.to_dict()
# create an instance of UserProfileModificationComplianceSchema from a dict
user_profile_modification_compliance_schema_form_dict = user_profile_modification_compliance_schema.from_dict(user_profile_modification_compliance_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


