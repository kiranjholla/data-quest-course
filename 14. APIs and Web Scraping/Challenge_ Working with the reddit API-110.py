## 2. Authenticating with the API ##

params = { "t": "day" }
headers = { "Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0" }
python_top = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params).json()


print(python_top)

## 3. Getting the Most Upvoted Post ##

#print(python_top['data']['children'])

most_upvotes = 0
most_upvoted = ''
for rec in python_top['data']['children']:
    if 'ups' in rec['data'] and rec['data']['ups'] > most_upvotes:
        most_upvoted = rec['data']['id']
        most_upvotes = rec['data']['ups']
        
print(most_upvoted)

## 4. Getting Post Comments ##

comments = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers).json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]['data']['children']

most_upvoted_comment = ''
most_upvotes_comment = 0

for com in comments_list:
    if com['data']['ups'] > most_upvotes_comment:
        most_upvotes_comment = com['data']['ups']
        most_upvoted_comment = com['data']['id']

## 6. Upvoting a Comment ##

status = requests.post("https://oauth.reddit.com/api/vote", headers=headers, json={ "dir": 1, "id": "d16y4ry" }).status_code