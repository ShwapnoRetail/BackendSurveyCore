from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed
from utils.auth_utils import validate_shwapno_jwt
from utils.authentication import ShwapnoJWTAuthentication
from utils.permissions import IsJWTAuthenticated
import logging

logger = logging.getLogger(__name__)