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
        '''Shows boast post only'''
        boast = GhostPost.objects.filter(type_of_post='B').order_by('-post_date')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        '''Shows roast post only'''
        roast = GhostPost.objects.filter(type_of_post='R').order_by('-post_date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def highest_score(self, request):
        '''Shows post in order by score'''
        highestscores = GhostPost.objects.all().order_by('-score')
        serializer = self.get_serializer(highestscores, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get','post'])
    def up_vote(self, request, pk=None):
        '''Adds a up vote to certian post'''
        post = self.get_object()
        post.up_votes += 1
        post.save()
        return Response({'status': 'upvoted'})

    @action(detail=True, methods=['get','post'])
    def down_vote(self, request, pk=None):
        '''Adds a down vote to certian post'''
        post = self.get_object()
        post.down_votes += 1
        post.save()
        return Response({'status': 'downvoted'})

    def destroy(self, request, pk=id):
        '''To test run http://localhost:8000/api/posts/${id}/?secret=${secret} 
        with method of DELETE'''
        post = GhostPost.objects.get(id=pk)
        if post.secret == self.request.query_params['secret']:
            post.delete()
            return Response({'status': "Deleted!"})
        else:
            return Response({'status': "Didn't delete, bad secret ket."})
  


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