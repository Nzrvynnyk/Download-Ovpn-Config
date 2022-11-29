import os
import sys
from twocaptcha import TwoCaptcha


def solveRecaptcha(sitekey, url):
    api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR API_KEY')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)

    except Exception as e:
        print(e)

    else:
        return result
