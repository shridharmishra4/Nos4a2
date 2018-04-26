import datetime

from rest_framework.views import APIView
from rest_framework.response import Response


class ImagicaDetailedOutputAPIView(APIView):
    def get(self, request, file_name):
        """
        Detailed report of Imagica extracted details from the PDF

        **Example Response**

                {
                    "FileName": "string",
                    "GeneratedAt": "datetime",
                    "Data":[
                        {
                            "RecordNumber": "int",
                            "Details":[
                                {
                                    "FieldName": "string",
                                    "FieldValue": "string",
                                    "FieldType": "string",
                                    "Top": "float",
                                    "Bottom": "float",
                                    "Left": "float",
                                    "Right": "float"
                                }
                            ]
                        }
                    ],
                    "Error": "string"
                }

        """

        return Response({
            "FileName": file_name,
            "GeneratedAt": datetime.datetime.now(),
            "Data": [],
            "Error": "File Not Found"
        })
