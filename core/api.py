from urllib.parse import quote
from config import BASE_API_URL, CHECK_MODEL_URL, CHECK_AUTH_URL,ACTIVATION_COMPLETED_URL,GUID_OPERATIONS_URL
class Api:
    # For model checking
    def get_api_url(model):
            return f"{CHECK_MODEL_URL}{model}"
    # For authorization check
    def get_authorization_url(model, serial):
        encoded_model = quote(model)
        return f"{CHECK_AUTH_URL}{encoded_model}&serial={serial}"

    # For GUID submission
#     STORE_GUID_URL
    def get_guid_api_url(serial):
        return f"{GUID_OPERATIONS_URL}{serial}&action=get_guid"
    def get_store_guid_url(serial,guid):
        return f"{GUID_OPERATIONS_URL}{serial}&guid={guid}&action=store_guid"
     # For GUID submission
    def get_completed_api_url(serial):
        return f"{ACTIVATION_COMPLETED_URL}{serial}"
    # For Compatible device folder URL
    def get_device_folder_url(model):
        return f"{BASE_API_URL}devices/{model}/"