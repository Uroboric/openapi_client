# ResetPassword

DTO model for user password reseting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | Login | [optional] 
**email** | **str** | Email | [optional] 

## Example

```python
from dm_api_account.models.reset_password import ResetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of ResetPassword from a JSON string
reset_password_instance = ResetPassword.from_json(json)
# print the JSON string representation of the object
print(ResetPassword.to_json())

# convert the object into a dict
reset_password_dict = reset_password_instance.to_dict()
# create an instance of ResetPassword from a dict
reset_password_from_dict = ResetPassword.from_dict(reset_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


