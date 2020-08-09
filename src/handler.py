import json

def handler(event,context):
    headers = ['<html>']
    headers.extend([i+':'+j+'<br/>' for i,j in event['headers'].items() if i.startswith('CloudFront')])
    headers.append("<a href=\"https://blog.owen.dev\">Blog</a>")
    headers.append("<a href=\"https://owen.dev\">Site</a>")
    headers.append('</html>')
    return {'statusCode':200,'body':'\n'.join(headers),'headers':{'Content-Type':'text/html'}}
