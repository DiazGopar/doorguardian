""" Connecting with WeAppFit API Service
"""
import requests
import logging as log
import doorparameters as parameters


def getWebResponse(code, way):
	""" Send The client code and sense (True => IN, False => OUT)
	"""
	# data to be sent to api
	data = {
			'code': code,
			#'centre_code': parameters.CENTER_CODE, 03/01/2020 - Pedro me dice que lo elimine porque no hace falta
			'in_out': way,
			}
	#print("Web code to send %s"%code)
	num_retries = 3
	# sending post request and saving response as response object
	while num_retries > 0:
		#print(num_retries)
		num_retries -= 1
		try:
			r = requests.post(url = parameters.API_ENDPOINT, data = data, timeout = parameters.URL_TIMEOUT)
		except requests.Timeout:
			log.warning('Web Request Timeout')
			response = False
			pass
		except requests.ConnectionError:
			log.error('Web request Connection error')
			response = False
			pass
		else:
			num_retries = 0
			response = r.text

	# extracting response text
	#response = r.text
	log.debug("The Response is: %s"%response)
	if response != "true":
		response = False
	return response

#print(getWebResponse(3220, True))