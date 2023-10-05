import requests
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken
from rest_framework.exceptions import ValidationError
import base64
from conf.settings import (
    DJANGO_BASE_URL,
    OAUTH_CLIENT_ID,
    OAUTH_CLIENT_SECRET
)


def _login(username,password):
    user = User.objects.get(username=username)
    access_token = AccessToken.objects.filter(user=user)

    if access_token.exists():
        return 
    
    url = f"{DJANGO_BASE_URL}/o/token/"
    auth_value = f"{OAUTH_CLIENT_ID}:{OAUTH_CLIENT_SECRET}"

    encoded_auth_value = base64.b64encode(auth_value.encode("utf-8")).decode(
        "utf-8"
    )

    payload = f"grant_type=password&username={username}&password={password}"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_auth_value}",
    }
    
    req = requests.request("POST", url, headers=headers, data=payload)
    if req.status_code != 200:
        raise ValidationError(f"{req.text}")

    return