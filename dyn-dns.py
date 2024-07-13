import base64,requests

token = ''
def getSHA():
    response = requests.get('https://api.github.com/repos/dyn-dns/dyn-dns.github.io/contents/index.html')
    response.raise_for_status()
    data = response.json()
    return data['sha']

def updateIP(ip:str):
    headers = {
        'Authorization':'Bearer ' + token,
        'X-GitHub-Api-Version':'2022-11-28'
    }

    data = {
        'message':'upd',
        'content':base64.b64encode(('<script>window.location.replace("http://%s")</script>' % ip).encode('utf-8')).decode('utf-8'),
        'sha':getSHA()
    }

    response = requests.put('https://api.github.com/repos/dyn-dns/dyn-dns.github.io/contents/index.html',headers=headers, json=data)
    response.raise_for_status()

updateIP('github.com')
