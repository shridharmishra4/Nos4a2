from rest_framework.response import Response
from rest_framework.views import APIView


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