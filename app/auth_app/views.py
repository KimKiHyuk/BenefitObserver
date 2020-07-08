from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Auth
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def register_token(request):
    auth = request.headers.get('Authorization')

    if auth is None:
        return JsonResponse({"message": "FCM Token is empty"}, status=401)

    # validate token

    try:
        Auth.obejcts.get_or_create(
            token=auth
        )
    except Exception as err:
        return JsonResponse({"message": "could not register FCM Token"}, status=404)

    return JsonResponse({"message": "OK"}, status=200)
