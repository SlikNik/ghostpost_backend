
from rest_framework import serializers
from post.models import GhostPost

class GhostPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GhostPost
        fields = ['id', 'type_of_post', 'title', 'body', 'up_votes', 'down_votes', 'score', 'secret', 'post_date', 'last_update']
