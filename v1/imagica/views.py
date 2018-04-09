import datetime

from rest_framework.permissions import AllowAny
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers


class MySchemaGenerator(SchemaGenerator):
    title = "Imagica API"

    def get_link(self, path, method, view):
        link = super().get_link(path, method, view)
        link._fields += self.get_core_fields(view)
        return link

    def get_core_fields(self, view):
        return getattr(view, 'coreapi_fields', ())


class SwaggerSchemaView(APIView):
    _ignore_model_permissions = True
    exclude_from_schema = True
    permission_classes = [AllowAny]
    renderer_classes = [
        CoreJSONRenderer,
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = MySchemaGenerator()
        schema = generator.get_schema(request=request)
        return Response(schema)


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


class ImagicaOutputAPIView(APIView):
    def get(self, request, file_name):
        """
        Get deals data from Imagica service

        **Example Response**
                {
                  "FileName": "string",
                  "GeneratedAt": "datetime"
                  "Data":[
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


class ImagicaDetailedOutputAPIView(APIView):
    def get(self, file_name):
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
                    ]
                }

        """

        return Response({
            "FileName": file_name,
            "GeneratedAt": datetime.datetime.now(),
            "Data": [],
            "Error": "File Not Found"
        })


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


class IsInitializedAPIView(APIView):
    def get(self):
        """
        Checks whether the models are initialized

        **Example Response**

                {
                    "isInitialized": "bool"
                }

        """
        return Response({})


class TrainAPIView(APIView):
    def get(self):    
        """
        Trains the models for classification

        **Example Response**

                {
                    "isInitialized": "bool",
                    "Error": "string"     
                }

        """
        return Response({})


class CurrentModelAPIView(APIView):
    def get(self):
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


class LatestTrainingStatusAPIView(APIView):
    def get(self):
        """
        Gets the status of the last training status

        **Example Response**
                {
                    "ModelName": "string",
                    "CurrentFold": "int",
                    "NumFold": "int",
                    "Epoch": "int",
                    "TotalEpochs": "int",
                    "Status": "string",
                    "Time": "datetime",
                    "FinalRound": "string",
                    "TrainLoss": "float",
                    "TrainAccuracy": "float",
                    "TrainAccuracy": "float",
                    "ValidationLoss": "float"
                }
        """
        return Response({})