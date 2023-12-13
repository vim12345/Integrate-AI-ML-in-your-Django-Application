import openai
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductDescriptionSerializer, ImageRecognitionSerializer
from .models import YourModel  # Import your model
from .serializers import YourModelSerializer  # Import your serializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = response.data['token']
        return Response({'token': token, 'user_id': request.user.id})

@api_view(['POST'])
@permission_classes([AllowAny])  
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Both username and password are required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username is already taken'}, status=400)

    new_user = User.objects.create_user(username=username, password=password)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id})
    else:
        return Response({'error': 'Unable to authenticate user'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_1(request):
    if request.method == 'GET':
        queryset = YourModel.objects.all()
        serializer = YourModelSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response({'message': 'API-1 endpoint'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_2(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Both username and password are required'}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id})
    else:
        return Response({'error': 'Invalid username or password'}, status=401)
    return Response({'message': 'API-2 endpoint'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_3(request):
    serializer = ProductDescriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer = ProductDescriptionSerializer(data=request.data)
    
    if serializer.is_valid():
        title = serializer.validated_data.get('title')

    
        openai.api_key = 'your_openai_api_key'

        def complete_text(title):
          prompt = f"Generate a product description based on the title: {title}. The product is a"

        response = openai.Completion.create(
          engine="text-davinci-002",  
          prompt=prompt,
          max_tokens=200, 
          n=1,  
          stop=None,  
        )

        completed_text = response['choices'][0]['text'].strip()

        return completed_text
        
        generated_description = complete_text(title)

        keywords = extract_keywords(generated_description)

        response_data = {
            'description': generated_description,
            'keywords': keywords,
        }

        return Response(response_data)

    return Response(serializer.errors, status=400)

def complete_text(title):
   
    completed_text = "Generated product description based on the title: " + title
    return completed_text

def extract_keywords(text):
   
    keywords = ['keyword1', 'keyword2']
    return keywords
    #     description = "Generated product descr,iption"
    #     keywords = ["keyword1", "keyword2"]
    #     return Response({'description': description, 'keywords': keywords})
    # return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_4(request):
    serializer = ImageRecognitionSerializer(data=request.data)
    if serializer.is_valid():
        keywords = ["keyword1", "keyword2"]
        return Response({'keywords': keywords})
    return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def crud_operations(request):
    if request.method == 'GET':
        queryset = YourModel.objects.all()
        serializer = YourModelSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)