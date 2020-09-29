from post.models import GhostPost
from rest_framework import viewsets
from api.serializers import GhostPostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

class GhostPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows post to be viewed or edited.
    """
    basename = 'posts'
    name = 'posts'
    queryset = GhostPost.objects.all().order_by('-post_date')
    serializer_class = GhostPostSerializer

    @action(detail=False)
    def boast(self, request):
        boast = GhostPost.objects.filter(type_of_post=True).order_by('-post_date')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        roast = GhostPost.objects.filter(type_of_post=False).order_by('-post_date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def highest_score(self, request):
        highestscores = GhostPost.objects.all().order_by('-score')
        serializer = self.get_serializer(highestscores, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get','post'])
    def up_vote(self, request, pk=None):
        post = self.get_object()
        post.up_votes += 1
        post.save()
        return Response({'status': 'upvoted'})

    @action(detail=True, methods=['get','post'])
    def down_vote(self, request, pk=None):
        post = self.get_object()
        post.down_votes += 1
        post.save()
        return Response({'status': 'downvoted'})
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
    # @action(detail=True, methods=['get','delete'], name='Delete Post')
    # def delete_post(self, request, pk=id):
    #     current_post = GhostPost.objects.get(pk=pk)
    #     current_post.delete()
    #     return Response({'status': f'post {current_post.id} deleted'})
  


# class BoastViewSet(viewsets.ModelViewSet):
#     basename = 'boasts/'
#     name = 'boasts'
#     serializer_class = GhostPostSerializer
#     queryset = GhostPost.objects.filter(type_of_post=True)


# class RoastViewSet(viewsets.ModelViewSet):
#     basename = 'roasts/'
#     name = 'roasts'
#     serializer_class = GhostPostSerializer
#     queryset = GhostPost.objects.filter(type_of_post=False)

# class ScoreViewSet(viewsets.ModelViewSet):
#     basename = 'scores/'
#     name = 'scores'
#     serializer_class = GhostPostSerializer
#     queryset = GhostPost.objects.all().order_by('-score')