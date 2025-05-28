from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_code(request):
    username = request.data.get('username')
    code = request.data.get('code')
    try:
        user = User.objects.get(username=username)
        user.code = code
        user.save()
        return Response({'message': 'Code saved successfully'})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

@api_view(['GET'])
def get_code(request):
    username = request.query_params.get('username')
    password = request.query_params.get('password')
    try:
        user = User.objects.get(username=username, password=password)
        return Response({'code': user.code})
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=404)

@api_view(['PUT'])
def update_company(request):
    username = request.data.get('username')
    company = request.data.get('company')
    try:
        user = User.objects.get(username=username)
        user.company = company
        user.save()
        return Response({'message': 'Company updated'})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)
