# Odyssey346's Code
# This code is not protected under any licenses at all. Go wild!

import requests
import os 
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

ScamSiteLink = 'https://doublekill.fun/auth.php'
names = json.loads(open('C:/Users/Odyssey346/Desktop/revenge/names.json').read())

for name in names: 
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra
    spampass = ''.join(random.choice(chars) for i in range (8))

    requests.post(ScamSiteLink, allow_redirects=False, data={
        'login': username, 'password': spampass
    })

    print('Sending fake login details. Ladies and Gentlemen, we got em.', username, spampass) 