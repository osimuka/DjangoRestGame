from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from game_api.models import GameDataModel
from game_api.serializer import GameDataSerializer


class GameUser(APIView):

    renderer_classes = (JSONRenderer, )

    def get_object(self, user):
        try:
            return GameDataModel.objects.get(unique_id=user)
        except GameDataModel.DoesNotExist:
            raise Http404

    def get(self, request, format=None, **kwargs):
        user_id = self.kwargs['user_id']
        queryset = self.get_object(user=user_id)
        serializer = GameDataSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, format=None, **kwargs):
        user_id = self.kwargs['user_id']
        queryset = self.get_object(user=user_id)
        serializer = GameDataSerializer(
            queryset,
            data={
                'unique_id': user_id,
                'game_data': request.data
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewGameUser(APIView):

    renderer_classes = (JSONRenderer, )

    def post(self, request, format=None):
        user_id = request.data["data"]["user_id"]
        serializer = GameDataSerializer(
            data={
                'unique_id': user_id,
                'game_data': request.data
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
