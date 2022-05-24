# Provide your unique API information below
API_KEY = ""
API_KEY_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
BEARER_TOKEN = ""

class TwitterSecrets:
    # holds API keys and other secret tokens
    def __init__(self):
        self.API_KEY = API_KEY
        self.API_KEY_SECRET = API_KEY_SECRET
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET
        self.BEARER_TOKEN = BEARER_TOKEN

        for key, secret in self.__dict__.items():
            assert secret != "", f"Please provide a valid secret for: {key}"

twitter_secrets = TwitterSecrets()