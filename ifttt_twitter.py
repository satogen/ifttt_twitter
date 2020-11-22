import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TARGET_URL = os.environ.get("webhook_url")

default_twiit_value = '新規にデータが更新されました'

# IFTTT_Webhook


def ifttt_webhook(twiit_value=default_twiit_value):
    """
    Webhookを用いて、Twitterにデータを送信

    Parameters
    ----------
    twiit_value : str
        ツイートする内容
    """
    payload = {"value1": twiit_value}
    response = requests.post(TARGET_URL, data=payload)
    print(response)


# 起動時呼び出し
if __name__ == '__main__':
    print("IFTTT連携開始")
    # IFTTT_Webhook
    ifttt_webhook()
    print("IFTTT連携終了")
