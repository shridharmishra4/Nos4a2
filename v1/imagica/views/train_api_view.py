from rest_framework.response import Response
from rest_framework.views import APIView
from v1.imagica.core.model_trainer import ModelTrainer


class TrainAPIView(APIView):
    def get(self, request):
        """
        Trains the models for classification

        **Example Response**

                {
                    "isTrained": "bool",
                    "Error": "string"
                }

        """
        ModelTrainer().run()
        return Response({
            "isTrained": False,
            "Error": "Training code not written"

        })
