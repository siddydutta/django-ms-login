import requests

from django.shortcuts import render, redirect
from django.contrib.auth import login
from msal import ConfidentialClientApplication

from auth_app.models import CustomUser
from auth_app.msal_config import MSAL_CONFIG

# Create a ConfidentialClientApplication instance
msal_app = ConfidentialClientApplication(
    client_id=MSAL_CONFIG["client_id"],
    client_credential=MSAL_CONFIG["client_secret"],
    authority=MSAL_CONFIG["authority"],
)

# Home page
def home(request):
    return render(request, "auth_app/home.html")

# Login route
def login_view(request):
    auth_url = msal_app.get_authorization_request_url(
        scopes=MSAL_CONFIG["scopes"],
        redirect_uri=MSAL_CONFIG["redirect_uri"],
    )
    return redirect(auth_url)

# Redirect route
def redirect_uri(request):
    code = request.GET.get("code")
    if code:
        result = msal_app.acquire_token_by_authorization_code(
            code=code,
            scopes=MSAL_CONFIG["scopes"],
            redirect_uri=MSAL_CONFIG["redirect_uri"],
        )
        if "access_token" in result:
            user_info_url = "https://graph.microsoft.com/v1.0/me"
            headers = {"Authorization": f"Bearer {result['access_token']}"}
            user_info_response = requests.get(user_info_url, headers=headers)
            user_info = user_info_response.json()

            email = user_info.get("mail") or user_info.get("userPrincipalName")
            first_name = user_info.get("givenName", "")
            last_name = user_info.get("surname", "")

            if email:
                # Check if user exists
                user, created = CustomUser.objects.get_or_create(
                    email=email,
                    defaults={
                        "first_name": first_name,
                        "last_name": last_name,
                    },
                )
                # Log in the user
                login(request, user)
            return render(request, "auth_app/home.html")
        else:
            return render(request, "auth_app/error.html", {"error": result.get("error_description")})
    return render(request, "auth_app/error.html", {"error": "Authorization code not received"})
