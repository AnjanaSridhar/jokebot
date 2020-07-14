import boto3
import json
from botocore.vendored import requests

def lambda_handler(event, context):
    url = "https://jokeapi-v2.p.rapidapi.com/joke/Any?ormat=json&blacklistFlags=racist,nsfw,sexist"

    querystring = {"contains":"C%2523","format":"json","blacklistFlags":"nsfw%2Cracist%2Csexist","idRange":"0-150","type":"single%2Ctwopart"}

    headers = {
        'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com",
        'x-rapidapi-key': "xxx"
        }

    response = requests.get(url, headers=headers).json()
    print(response)
    if('joke' in response):
        return {
            'statusCode': '200',
            'body': response['joke']
        }
    else:
        return {
            'statusCode': '200',
            'body': response['setup'] + '\n' + response['delivery'] + ' :wink:'
        }
