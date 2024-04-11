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
    
    
    


class GetUnreadMSG(APIView):
    def post(self, request):
        key = request.data.get('key')
        if key == 'abcdef': #db에서 user 키 발급
            user_id = request.data.get('data', {}).get('userid')
            if user_id:
                messages = Message.objects.filter(user_id=user_id)
                serializer = MessageSerializer(messages, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'Missing or invalid userid'}, status=400)
            
        return Response({'error': 'Missing or invalid userid'}, status=400)