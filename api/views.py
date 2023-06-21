from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from setfit import SetFitModel
import json

# Create your views here.

class Health_check(APIView):
    """Health check of the project"""

    def get(self, request):
        return Response({'detail': 'All is working fine'})


## Auxillary function
def load_model():
	""" Load pre-trained sentiment classifier """
	
	# Download from Hub and run inference
	model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
	return model

MODEL = load_model()

class PredictSentimentView(APIView):
	""" API endpoint to predict sentiment of text """

	def post(self, request):
		""" POST requests take in text and return sentiment"""
		labels = {
			1: "positive",
			0: "negative"
        }
		try:
			json_object = json.loads(request.body.decode("utf-8"))
			text = json_object['text']
		except Exception as e:
			return Response({"message": "json object does not contain 'text'"}, status=status.HTTP_400_BAD_REQUEST)

		if text!="":
			## Inference on loaded model
			pred = MODEL([text]).tolist()
			return Response({"sentiment": labels[pred[0]]}, status=status.HTTP_200_OK)
		else:
			return Response({"message": "Please enter text to analyze"}, status=status.HTTP_200_OK)