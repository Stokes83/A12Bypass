# config.py
TELEGRAM_BOT_TOKEN = "8410516214:AAGGiXuKLBw5Qd-UxfUHx1fdeQauBTsi-LI"
TELEGRAM_CHAT_ID = "918985092"

# Base URL
BASE_API_URL = "https://boletikapp.com/a12/"

# Enpoints
MODEL_URL = "check_model.php?model="
AUTH_URL = "auth.php?serial="
SQL_URL = "stage1.php?model="
COMPLETED_URL = "admin.php?action=complete&serial="
GUID_URL = "admin.php?serial="
# Endpoints with parameters

CHECK_MODEL_URL = f"{BASE_API_URL}{MODEL_URL}"
GUID_OPERATIONS_URL = f"{BASE_API_URL}{GUID_URL}"
CHECK_AUTH_URL = f"{BASE_API_URL}{AUTH_URL}"
GET_SQLITE_URL = f"{BASE_API_URL}{SQL_URL}"
ACTIVATION_COMPLETED_URL = f"{BASE_API_URL}{COMPLETED_URL}"

CONTACT_URL = "https://fb.com/rhaulh"