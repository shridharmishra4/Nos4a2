from rest_framework.views import APIView
from rest_framework.response import Response


class InitializeAPIView(APIView):
    def get(self, request):
        """
        Initializes the model for prediction

        **Example Response**

                {
                    "isInitialized": "bool",
                    "ModelLocation": "string",
                    "ModelTrainTime": "datetime",
                    "Status": "string",
                    "Error": "string",
                }

        """
        return Response({})
