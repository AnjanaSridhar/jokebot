import boto3
import json
from botocore.vendored import requests

def lambda_handler(event, context):
    url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"

    querystring = {"contains":"C%2523","format":"json","blacklistFlags":"nsfw%2Cracist%2Csexist","idRange":"0-150","type":"single%2Ctwopart"}

    headers = {
        'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com",
        'x-rapidapi-key': "4ba0d14649mshcea34dc896dcaaap11a2f0jsna5e7e39959d6"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return {
        'statusCode': '200',
        'body': response 
    }