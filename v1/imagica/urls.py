from django.conf.urls import url
from .views import TrainAPIView, CurrentModelAPIView, LatestTrainingStatusAPIView, InitializeAPIView, \
    IsInitializedAPIView
from .views import ImagicaDetailedOutputAPIView, ImagicaOutputAPIView, ImagicaRawOutputAPIView, \
    ImagicaSpecificOutputAPIView
from .views import SwaggerSchemaView


urlpatterns = [
    url(r'^$', SwaggerSchemaView.as_view()),
    url(r'^imagica/train/', TrainAPIView.as_view(), name="train"),
    url(r'^imagica/initialize/', InitializeAPIView.as_view(), name="initialize"),
    url(r'^imagica/isInitialized', IsInitializedAPIView.as_view(), name="isInitialized"),
    url(r'^imagica/currentModel/', CurrentModelAPIView.as_view(), name="currentModel"),
    url(r'^imagica/trainingStatus/', LatestTrainingStatusAPIView.as_view(), name="trainingStatus"),
    url(r'^imagica/rawOutput/FileName/(?P<file_name>[-\w]+)/', ImagicaRawOutputAPIView.as_view(), name="rawOutput"),
    # url(r'^imagica/rawOutput/FileName/(?P<file_name>[-\w]+)/'
    #     r'NormalizationVersion/(?P<normalization_version>[-\w]+)/'
    #     r'ModelVersion/(?P<model_version>[-\w]+)/',
    #  ImagicaSpecificRawOutputAPIView.as_view(), name="specificRawOutput"),
    url(r'^imagica/output/FileName/(?P<file_name>[-\w]+)/',
        ImagicaOutputAPIView.as_view(), name="output"),
    url(r'^imagica/output/FileName/(?P<file_name>[-\w]+)/'
        r'NormalizationVersion/(?P<normalization_version>[-\w]+)/'
        r'ModelVersion/(?P<model_version>[-\w]+)/'
        r'PostProcessingVersion/(?P<post_processing_version>[-\w]+)/',
        ImagicaSpecificOutputAPIView.as_view(), name="specificOutput"),
    url(r'^imagica/detailedOutput/FileName/(?P<file_name>[-\w]+)/',
        ImagicaDetailedOutputAPIView.as_view(), name="detailedOutput"),
    # url(r'^imagica/detailedOutput/FileName/(?P<file_name>[-\w]+)/'
    #     r'NormalizationVersion/{normalization_version}/'
    #     r'ModelVersion/{model_version}/', ImagicaSpecificDetailedOutputAPIView.as_view(), name="specificDetailedOutput")
]
