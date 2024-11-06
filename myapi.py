
import paralleldots
# Setting your API key
class API:
    def __init__(self):
        paralleldots.set_api_key('baLnjigzhEcLZdq8tmbQpaLPfB1Jrn2HmspltfOxnxI')
    def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        return response

