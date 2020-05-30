from rest_framework import status
from rest_framework.response import Response

from profiles_api.constants import INTERNAL_SERVER_ERROR



class Utils(object):
	@staticmethod
	def dispatch_sucess(request, response, code=status.HTTP_200_OK, **kwargs):
		if response is None:
			data = {'ok': True, **kwargs}
		else:
			data = {'ok': True, 'result': response, **kwargs}
		return Response(data=data, status=code)
	
	@staticmethod
	def dispatch_failure(request, message, response=None, code=status.HTTP_400_BAD_REQUEST):
		if message == INTERNAL_SERVER_ERROR:
			code = status.HTTP_500_INTERNAL_SERVER_ERROR
		data = {'ok': False, 'message': message}
		if response is not None:
			data['errors'] = response
		return Response(data=data, status=code)


def logger_config():
	import logging
	return logging.getLogger(__name__)


logger = logger_config()