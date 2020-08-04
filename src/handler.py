import json

def handler(event,context):
    print(event)
    headers = [i+':'+j for i,j in event['headers'].items()]
    return {'statusCode':200,'body':'\n'.join(headers)}
