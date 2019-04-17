from rest_framework import serializers

from game_api.models import GameDataModel


class GameDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDataModel
        fields = ('unique_id', 'game_data')
        read_only_fields = ('id', 'created', 'updated')

    def create(self, validated_data):
        """
        Create and return a new instance, given the validated data.
        """
        return GameDataModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `FishyRunModel` instance,
        given the validated data.
        """
        instance.game_data = validated_data.get(
            'game_data', instance.game_data)
        instance.save()
        return instance
