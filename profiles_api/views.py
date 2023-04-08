from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
	"""Test Api View""" 

	def get(self, request, format=None):
		'''Return list of API features'''
		an_apiview = [
			'Users HTTP methods (get, post, patch, put, delete)',
			'Is simililar to a traditional Django viwe',
			'Gives you the most control over your aplication logic',
			'Is mapped manually to URLs',
		]

		return Response({'message': ' Hello!', 'an_apiview': an_apiview})
