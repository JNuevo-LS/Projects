import requests
from google.cloud import translate_v2 as translate
import os
import smtplib
from email.message import EmailMessage
import ssl

client_id = 'X'
client_secret='X'
user_agent='X'

auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

login_data = {
    'grant_type' : 'password',
    'username' : 'X',
    'password' : 'X'
}

headers = { 'User-Agent' : 'X' }


response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=login_data, headers=headers)
response.json()

token = response.json()['access_token']

headers = {**headers, **{'Authorization':f'bearer {token}'}}

params = {'limit': 5}

AITAH_hot = requests.get('https://oauth.reddit.com/r/AmItheAsshole/hot', headers=headers, params=params)
postsAITAH = AITAH_hot.json()['data']['children']

AITA_hot = requests.get('https://oauth.reddit.com/r/AITA/hot', headers=headers, params=params)
postsAITA = AITA_hot.json()['data']['children']

list_of_posts = []
list_of_urls = []

for post in postsAITAH + postsAITA:
    list_of_posts.append(post['data']['selftext'])
    list_of_urls.append('\n https://www.reddit.com' + post['data']['permalink'])

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Key JSON Location'
 
translate_client = translate.Client()

translated_posts = []

for index, post in enumerate(list_of_posts):
    translated_posts.append((f'Post {index} ' + (translate_client.translate(post, target_language='es'))['translatedText']))



msg = EmailMessage()

email_b1 = '\n\n'.join(translated_posts)
email_b2 = '\n'.join(list_of_urls)

email_body = email_b1 + email_b2

msg.set_content(email_body)

msg['Subject'] = 'Test'
msg['From'] = 'X'
msg['To'] = 'X'

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', context=context) as server:
    server.login("X", "X")
    server.send_message(msg)
