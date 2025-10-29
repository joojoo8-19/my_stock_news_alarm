from PyKakao import Message
import os
from dotenv import load_dotenv

class KakaoManager:
    def __init__(self):
        load_dotenv()
        self.rest_api = os.environ.get("KAKAO_REST_API")
        self.message = Message(self.rest_api)
        self.auth_url = self.message.get_url_for_generating_code()