import responses

def returnSpeech(speech, endSession=True):
	return {
		"version": "1.0",
		"sessionAttributes": {},
		"response": {
		"outputSpeech": {
		"type": "PlainText",
		"text": speech
			},
			"shouldEndSession": endSession
		  }
	}

def lambda_handler(event, context):
	speech = responses.get_tweet()
	return returnSpeech(speech)

if __name__ == '__main__':
	pass
