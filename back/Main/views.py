from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, filters, mixins
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse


def home(request):
    return render(request, 'index.html')

@api_view(['GET'])
def check_auth(request):
    """Check if user is authenticated and return user info"""
    if request.user.is_authenticated:
        return JsonResponse({
            "authenticated": True, 
            "username": request.user.username
        }, status=200)
    return JsonResponse({"authenticated": False}, status=401)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """Handle user login"""
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"message": "Login riuscito!"}, status=200)
    return JsonResponse({"error": "Credenziali non valide"}, status=400)

@api_view(['POST'])
def logout_view(request):
    """Handle user logout"""
    logout(request)
    return JsonResponse({"message": "Logout riuscito!"}, status=200)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """Handle user registration"""
    
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")
    
    if not username or not password or not email:
        return JsonResponse({"error": "Tutti i campi sono obbligatori!"}, status=400)
    
    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Il nome utente è già in uso!"}, status=400)
    
    if User.objects.filter(email=email).exists():
        return JsonResponse({"error": "Un account con questa email esiste già!"}, status=400)
    
    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        
        login(request, user)
        
        return JsonResponse({"message": "Registrazione riuscita!", "username": user.username}, status=201)
    except Exception as e:
        return JsonResponse({"error": f"Errore durante la registrazione: {str(e)}"}, status=500)
