from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import board, list, card
from .serializers import BoardSerializer, ListSerializer, CardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        boards_current_user = board.objects.all().filter(user = request.user)
        serializer = BoardSerializer(boards_current_user, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class ListViewSet(viewsets.ModelViewSet):
    queryset = list.objects.all()
    serializer_class = ListSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        list_of_board = list.objects.all().filter(parent_board = request.GET['id'])
        serializer = ListSerializer(list_of_board, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class CardViewSet(viewsets.ModelViewSet):
    queryset = card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        card_of_lists = card.objects.all().filter(parent_list = request.GET['id'])
        serializer = CardSerializer(card_of_lists, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)




