from rest_framework.response import Response
from rest_framework.views import APIView


class IsInitializedAPIView(APIView):
    def get(self):
        """
        Checks whether the models are initialized

        **Example Response**

                {
                    "isInitialized": "bool"
                }

        """
        return Response({
            "isInitialized": False
        })
