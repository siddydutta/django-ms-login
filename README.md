# Quickstart with Microsoft Login

## Pre-Requisites for the Microsoft App

### Step 1: Register Your App on Microsoft Azure > App Registrations
![azure-app-registration](/images/azure-app-registration.png)

### Step 2: Update .env
These credentials are used in [msal_config.py](/auth_app/msal_config.py), to create a `MSAL_CONFIG` object.

In [views.py](/auth_app/views.py#L11), the actual `ConfidentialClientApplication` instance is created which is used to get the authorization request URL for the login flow, and the access token from the code in the redirect flow.

## Usual Django Stuff

### Step 1: Create Virtual Environment
```shell
python3.12 -m venv venv/
source venv/bin/activate
```

### Step 2: Install Dependencies
```shell
pip install -r requirements.txt
```

### Step 3: Run Migrations
```shell
python manage.py migrate
```

### Step 4: Run Server
```shell
python manage.py runserver
```

## Code to Look At

1. [CustomUser](/auth_app/models.py#L22) model.
2. [Handle Microsoft Redirect](/auth_app/views.py#L33)

## Sample Screenshots

### Home Page without Login
![no-auth-home](/images/no-auth-home.png)

### Home Page with Login
![user-home](/images/user-home.png)

### [For Debugging] Microsoft Graph Me API Response
![me-api-response](/images/me-api-response.png)
