from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import board
from .serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        boards_current_user = board.objects.all().filter(user = request.user)
        serializer = BoardSerializer(boards_current_user, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


