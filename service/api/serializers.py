from rest_framework import serializers

from . import models


class TrackSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    moods = serializers.StringRelatedField(many=True)
    main_artists = serializers.StringRelatedField(many=True)
    featured_artists = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Track
        fields = [
            "id",
            "title",
            "length",
            "bpm",
            "genres",
            "moods",
            "main_artists",
            "featured_artists",
            "audio",
            "cover_art",
            "waveform",
            "spotify",
        ]




class GetmanyPlaylistNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Playlist
        fields = ['id', 'name']

class CreatePlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Playlist
        fields = '__all__'

class GetOnePlaylistSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = models.Playlist
        fields = '__all__'