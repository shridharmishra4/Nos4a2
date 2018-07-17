import datetime

from rest_framework.views import APIView
from rest_framework.response import Response


class ImagicaSpecificOutputAPIView(APIView):
    def get(self, request, file_name, normalization_version, model_version, post_processing_version):
        """
        Get deals data from Imagica service

        **Example Response**

                {
                    "FileName": "string",
                    "GeneratedAt": "datetime",
                    "DocumentCreatedAt": "datetime",
                    "NormalizationVersion": "string",
                    "PostProcessingVersion": "string",
                    "ModelVersion": "string",
                    "Data": [
                        {
                            "ImagicaDealNumber": "int",
                            "TRADE_DATE": "string",
                            "UNDERLYING_NAME": "string",
                            "CURRENCY": "string",
                            "INSTRUMENT_NAME": "string",
                            "EXERCISE_TYPE": "string",
                            "OPTION_TYPE": "string",
                            "BUY/SELL": "string",
                            "PRODUCT_PRICE": "float",
                            "PRODUCT_QUANTITY": "float",
                            "STRIKE": "float",
                            "MATURITY_DATE": "string",
                            "BROKER_FEES": "float",
                            "BROKER_FEES_CCY": "string",
                            "CONTRACT": "string",
                            "MARKET": "string"
                        }
                    ],
                    "Error": "string"
                }
        """
        return Response({
            "FileName": file_name,
            "GeneratedAt": datetime.datetime.now(),
            "DocumentCreatedAt": datetime.datetime.now(),
            "NormalizationVersion": normalization_version,
            "ModelVersion": model_version,
            "PostProcessingVersion": post_processing_version,
            "Data": [],
            "Error": "File Not Found"
        })
