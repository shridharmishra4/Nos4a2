from rest_framework.views import APIView
from rest_framework.response import Response


class ImagicaRawOutputAPIView(APIView):
    def get(self, request, file_name):
        """
        Generate token by token predicted tags

        **Example Response**

                {
                    "FileName": "string",
                    "GeneratedAt": "datetime",
                    "Tokens": [
                        {
                            "TokenIndex": "int",
                            "Text": "string",
                            "PredictedTag": "string"
                        }
                    ],
                    "Error": "string"
                }

        """
        return Response({
            "FileName": file_name
        })
