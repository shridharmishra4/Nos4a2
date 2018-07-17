from .swagger_api_view import SwaggerSchemaView

from .imagica_output_view import ImagicaOutputAPIView
from .imagica_specific_detailed_output import ImagicaSpecificOutputAPIView
from .imagica_detailed_output_api_view import ImagicaDetailedOutputAPIView
from .imagica_raw_output_api_view import ImagicaRawOutputAPIView

from .train_api_view import TrainAPIView
from .current_model_api_view import CurrentModelAPIView
from .is_initialized_api_view import IsInitializedAPIView
from .latest_status_api_view import LatestTrainingStatusAPIView
from .initialize_api_view import InitializeAPIView


__all__ = (
    'SwaggerSchemaView',

    'ImagicaOutputAPIView',
    'ImagicaSpecificOutputAPIView',
    'ImagicaRawOutputAPIView',
    'ImagicaDetailedOutputAPIView',

    'TrainAPIView',
    'IsInitializedAPIView',
    'InitializeAPIView',
    'CurrentModelAPIView',
    'LatestTrainingStatusAPIView'
)