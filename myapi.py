
import paralleldots
# Setting your API key
class API:
    def __init__(self):
        paralleldots.set_api_key('API')
    def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        return response

