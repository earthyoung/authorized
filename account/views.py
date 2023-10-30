import os, requests
from json.decoder import JSONDecodeError
from django.shortcuts import render, redirect
from rest_framework import viewsets, views, generics, mixins
from rest_framework.permissions import *
from rest_framework import status
from django.http.response import *
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from account.serializers import *
from account.models import *


# Create your views here.
class HealthViewSet(views.APIView):
    def get(self, request):
        return JsonResponse({"status": True})


BASE_URL = "http://localhost:8000/"
GOOGLE_CALLBACK_URI = BASE_URL + "accounts/google/callback"


class GoogleLoginView(views.APIView):
    def get(self, request):
        scope = "https://www.googleapis.com/auth/userinfo.email"
        client_id = os.environ.get("GOOGLE_CLIENT_ID")
        url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}"
        return redirect(url)


class GoogleCallbackView(views.APIView):
    def get(self, request):
        client_id = os.environ.get("GOOGLE_CLIENT_ID")
        client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")
        code = request.GET.get("code")
        state = os.environ.get("STATE")

        # get access token
        url = f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}"
        token_req = requests.post(url)
        token_req_json = token_req.json()
        error = token_req_json.get("error")
        if error is not None:
            raise Exception(error)
        access_token = token_req_json.get("access_token")

        # request email
        email_req = requests.get(
            f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}"
        )
        email_req_status = email_req.status_code
        if email_req_status != 200:
            return JsonResponse(
                {"err_msg": "failed to get email"}, status=status.HTTP_400_BAD_REQUEST
            )
        email = email_req.json().get("email")

        # signup or signin
        try:
            user = User.objects.get(email=email)

            # check if the user is google user
            social_user = SocialAccount.objects.get(user=user)
            if social_user is None:
                return JsonResponse(
                    {"err_msg": "email exists but not social user"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if social_user.provider != "google":
                return JsonResponse(
                    {"err_msg": "no matching social type"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # user is google user
            data = {"access_token": access_token, "code": code}
            accept = requests.post(
                f"{BASE_URL}accounts/google/login/finish/", data=data
            )
            accept_status = accept.status_code
            if accept_status != 200:
                return JsonResponse(
                    {"err_msg": "failed to signin"}, status=accept_status
                )
            accept_json = accept.json()
            accept_json.pop("user", None)
            return JsonResponse(accept_json)
        except User.DoesNotExist:
            data = {"access_token": access_token, "code": code}
            accept = requests.post(
                f"{BASE_URL}accounts/google/login/finish/", data=data
            )
            accept_status = accept.status_code
            if accept_status != 200:
                return JsonResponse(
                    {"err_msg": "failed to signup"}, status=accept_status
                )
            accept_json = accept.json()
            accept_json.pop("user", None)
            return JsonResponse(accept_json)


class GoogleLoginFinishView(SocialLoginView):
    adapter_class = google_view.OAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client


class UserViewSet(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin
):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()


class UserCreateViewSet(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class HouseViewSet(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return House.objects.all()


class OwnershipViewSet(viewsets.ModelViewSet):
    serializer_class = OwnershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ownership.objects.all()


class AuthorityViewSet(viewsets.ModelViewSet):
    serializer_class = AuthoritySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Authority.objects.all()


class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Record.objects.all()


class OwnershipRequestViewSet(viewsets.ModelViewSet):
    serializer_class = OwnershipRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OwnershipRequest.objects.all()


class AuthorityRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorityRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AuthorityRequest.objects.all()
