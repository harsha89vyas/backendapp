#create settings class to store constants like api key
import os
OPENAI_API_KEY = str(os.environ.get("openai_api_key"))