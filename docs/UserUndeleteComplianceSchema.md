# UserUndeleteComplianceSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_undelete** | [**UserComplianceSchema**](UserComplianceSchema.md) |  | 

## Example

```python
from twitter_api_v2.models.user_undelete_compliance_schema import UserUndeleteComplianceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserUndeleteComplianceSchema from a JSON string
user_undelete_compliance_schema_instance = UserUndeleteComplianceSchema.from_json(json)
# print the JSON string representation of the object
print UserUndeleteComplianceSchema.to_json()

# convert the object into a dict
user_undelete_compliance_schema_dict = user_undelete_compliance_schema_instance.to_dict()
# create an instance of UserUndeleteComplianceSchema from a dict
user_undelete_compliance_schema_form_dict = user_undelete_compliance_schema.from_dict(user_undelete_compliance_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


