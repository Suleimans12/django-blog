from django.urls import path
from . views import (
	PostCreateView, 
	PostIndexView,
	PostDetailView,
	PostUpdateView
)

urlpatterns = [
	path('', PostIndexView.as_view(), name='index'),
	path('create/', PostCreateView.as_view(), name='create'),
	path('<int:pk>/', 	PostDetailView.as_view(), name='detail'),
	path('<int:pk>/update/', 	PostUpdateView.as_view(), name='update')
]
