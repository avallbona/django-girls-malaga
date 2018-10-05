# -*- encoding: utf-8 -*-


import requests
my_domain = 'avallbona.pythonanywhere.com'
username = 'avallbona'
token = 'a5fd765153220b3b6241b575b95e7a403def56bb'

response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
        username=username, domain=my_domain
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('All OK')
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))