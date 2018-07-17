from rest_framework.response import Response
from rest_framework.views import APIView


class CurrentModelAPIView(APIView):
    def get(self, request):
        """
        Returns the time at which the current model training was started

        **Example Response**

                {
                    "ModelLocation": "string",
                    "ModelTrainTime": "string",
                    "Status": "string"
                }

        """
        return Response({})
