from django.urls import path

from .views import (
    UserActivityView,
    GetPosts,
    RefreshPost,
    CreatePost,
    PostVoteView,
    DeleteAllPosts,
    GetComments,
    CreateComment,
    CommentVoteView,
    EditComment,
    DeleteComment,
    DeletePost,
    EditPost,
    GetProfile,
    SearchPost,
)

urlpatterns = [
    path(
        'user-activity/<str:username>/',
        UserActivityView.as_view(),
        name='user-activity',
    ),
    path('posts/<int:post_id>/vote/', PostVoteView.as_view(), name='vote-on-post'),
    path('posts/delete/all/', DeleteAllPosts.as_view(), name='delete-all-posts'),
    path('post/create/', CreatePost.as_view(), name='create-post'),
    path('post/<int:post_id>/update/', EditPost.as_view(), name='post-update'),
    path('posts/', GetPosts.as_view(), name='get-posts'),
    path('posts/<int:pk>/', RefreshPost.as_view(), name='post-refresh'),
    path('comments/<int:pk>/', GetComments.as_view(), name='get-comments'),
    path(
        'comments/<int:post_id>/create/', CreateComment.as_view(), name='create-comment'
    ),
    path(
        'comments/<int:post_id>/<int:comment_id>/vote/',
        CommentVoteView.as_view(),
        name='vote-on-comment',
    ),
    path(
        'comments/<int:post_id>/update/<int:comment_id>/',
        EditComment.as_view(),
        name='edit-comment',
    ),
    path(
        'comments/<int:post_id>/delete/<int:comment_id>/',
        DeleteComment.as_view(),
        name='delete-comment',
    ),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='delete-post'),
    path('profile/<int:pk>', GetProfile.as_view(), name='get-profile'),
    path('search/', SearchPost.as_view(), name='search'),
]
