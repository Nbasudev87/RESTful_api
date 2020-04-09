from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from .models import Article,Customer,Vehicle
from .serializer import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
import json
from .database_world import records
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


#create class based view

#...........................................Viewset...............................................
class ArticleViewSet(viewsets.ViewSet):
    def list(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk):
        queryset = Article.objects.all()
        articles=get_object_or_404(queryset,pk)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)





#..........................................Generic view..........................................
class GenericArticleList(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    def get(self,request,id=None):
        if id:
            return self.retrive(request,id)
        else:
            return self.list(request)
    try:
        def post(self,request):
             return self.create(self,request)
    except Exception as e:
        print(e)

class GenericArticleDetails(generics.GenericAPIView,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    def get(self,request,id=None):
        if id:
            return self.retrive(request, id)
        else:
            return self.list(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id=None):
        return self.destroy(request, id)

#..............................................Generic class based view..............................




#.........................................class base view.......................................
class ArticleList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist():
            raise Http404
    def get(self,request,pk,format=None):
        article=self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        article=self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        article=self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#................................................function based view.............................................
# Create function based views here.
@api_view(['GET','POST'])
def airticle_list(request):
    if request.method=='GET':
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        #data= JSONParser().parse(request)
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#......................................................................................................
def home(request):
    contex=Customer.objects.all()
    info={"customer":contex}
    return render(request,'html_app/index.html',info)
def db_world(request):
    city=records
    city_info={'city':city}
    return render(request,'html_app/worldinfo.html',city_info)
#...............................................................................................................
#@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def article_details(request,pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method=='PUT':
        #data = JSONParser().parse(request)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.H)
    elif request.method=='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





