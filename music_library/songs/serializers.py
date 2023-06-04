from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    model = Song
    fields = ['title','artist','album','release_date','genre']
    depth = 1

