from PyKakao import Message
import os
from dotenv import load_dotenv
import requests

class KakaoManager:
    def __init__(self):
        load_dotenv()
        self.rest_api = os.environ.get("KAKAO_REST_API")
        self.refresh_token = os.environ.get("KAKAO_REFRESH_TOKEN")
        self.message = Message(self.rest_api)
        self.url = self.message.get_url_for_generating_code()

    """ get freshly updated access token """
    def get_access_token(self):
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "refresh_token",
            "client_id": self.rest_api,
            "refresh_token": self.refresh_token
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        tokens = response.json()
        return tokens["access_token"]

    def send_message(self, contents:str):
        access_token = self.get_access_token()

        self.message.set_access_token(access_token)
        self.message.send_message_to_me(
            message_type="text",
            text=contents,
            link={"web_url": "https://developers.kakao.com"},
            button_title="바로 확인"
        )
        print("success!")