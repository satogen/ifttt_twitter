import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Webhook呼ぶためのURL
TARGET_URL = os.environ.get("webhook_url")
# デフォルトのツイートテキスト
default_tweet_value = '新規にデータが更新されました'


def ifttt_webhook(tweet_value=default_tweet_value):
    """
    Webhookを用いて、Twitterにデータを送信

    Parameters
    ----------
    tweet_value : str
        ツイートする内容
    """
    payload = {"value1": tweet_value}
    # Webhookでツイートするデータを送信
    response = requests.post(TARGET_URL, data=payload)
    print(response)


# 起動時呼び出し
if __name__ == '__main__':
    print("IFTTT連携開始")
    # ツイートを送信
    ifttt_webhook()
    print("IFTTT連携終了")
