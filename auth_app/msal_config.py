import os
from dotenv import load_dotenv


load_dotenv()


MSAL_CONFIG = {
    "client_id": os.getenv("MSAL_CLIENT_ID"),
    "authority": "https://login.microsoftonline.com/common",
    "redirect_uri": os.getenv("MSAL_REDIRECT_URI"),
    "client_secret": os.getenv("MSAL_CLIENT_SECRET"),
    "scopes": ["User.Read"],
}
