from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from .models import Message

class MessageView(APIView):
    def post(self, request):
        key = request.data.get('key')
        if key == 'abcdef': #db에서 user 키 발급
            serializer = MessageSerializer(data=request.data.get('data'))
            if serializer.is_valid():
                serializer.save()
                print("success")
                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Invalid API key."}, status=status.HTTP_403_FORBIDDEN)