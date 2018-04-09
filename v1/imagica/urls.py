from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from .views import TrainAPIView, CurrentModelAPIView, LatestTrainingStatusAPIView, ImagicaDetailedOutputAPIView, \
    ImagicaOutputAPIView, InitializeAPIView, IsInitializedAPIView, ImagicaRawOutputAPIView, SwaggerSchemaView

urlpatterns = [
    url(r'^$', SwaggerSchemaView.as_view()),
    url(r'^imagica/train/', TrainAPIView.as_view(), name="train"),
    url(r'^imagica/initialize/', InitializeAPIView.as_view(), name="initialize"),
    url(r'^imagica/isInitalized', IsInitializedAPIView.as_view(), name="isInitialized"),
    url(r'^imagica/currentModel/', CurrentModelAPIView.as_view(), name="currentModel"),
    url(r'^imagica/trainingStatus/', LatestTrainingStatusAPIView.as_view(), name="trainingStatus"),
    url(r'^imagica/rawOutput/FileName/(?P<file_name>[-\w]+)/', ImagicaRawOutputAPIView.as_view(), name="rawOutput"),
    url(r'^imagica/output/FileName/(?P<file_name>[-\w]+)/', ImagicaOutputAPIView.as_view(), name="output"),
    url(r'^imagica/detailedOutput/FileName/(?P<file_name>[-\w]+)/', ImagicaDetailedOutputAPIView.as_view(),
        name="detailedOutput")
]
