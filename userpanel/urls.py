from django.urls import path, include
from userpanel.views import *
from rest_framework import routers
from userpanel.views import *
router = routers.DefaultRouter()
router.register(r'submit-preverified-question',SubmitPreVerifiedQuestionView, basename='submit-nad')
router.register(r'submit-file-question',SubmitFileQuestionView, basename='submit-file-question')
router.register(r'submit-text-question',SubmitTextQuestionView, basename='submit-file-question')
router.register(r'upload', UploadDocumentViewset, basename='upload')

urlpatterns = [
    path('custom-document/', CustomDocumentView.as_view(), name="custom-document"),
    path('profile-documents/',ProfileDocumentView.as_view(), name= "profile-documents"),
    path('recent-upload/', RecentUpload.as_view(), name= "recent-upload"),
    path('retrieve', RetrieveDocument.as_view(), name= "retrieve"),
    path('', include(router.urls))
    # path('profile-documents/<int:pk>',ProfileDocumentView.as_view(), name= "profile-documents"),
]

urlpatterns += router.urls