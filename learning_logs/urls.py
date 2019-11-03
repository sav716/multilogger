"""Def URL patterns for learning_logs"""
from . import views
from django.urls import path



app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # All Topics
    path('topics/', views.topics, name='topics'),

    # Detailed page for a single MultiLogger topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing existing logs
    path('edit_entry/<int:entry_id>/', views.edit_entry,
         name='edit_entry'),
]
 
