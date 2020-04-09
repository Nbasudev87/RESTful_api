from django.urls import path,include
from .views import airticle_list,home,article_details,ArticleList,ArticleDetails,GenericArticleList,GenericArticleDetails,db_world,ArticleViewSet
from rest_framework.routers import DefaultRouter

# define routers
router=DefaultRouter()
router.register(r'article',ArticleViewSet,basename='article')

urlpatterns = [
    path('ArticleList/',ArticleList.as_view()),#class based view
    path('ArticleDetails/<int:pk>/',ArticleDetails.as_view()),#class based view
    path('GenericArticleList/',GenericArticleList.as_view()),
    path('GenericArticleDetails/<int:pk>/',GenericArticleDetails.as_view()),
    path('ArticleViewSet',ArticleViewSet),
    path('html_app/home',home),
    path('html_app/world',db_world),
    path('article_details/<int:pk>/',article_details),#function based view
    path('article_list/',airticle_list),#function based view
    path('viewset/',include(router.urls))
]