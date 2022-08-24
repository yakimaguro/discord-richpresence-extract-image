import requests

id = input('clientid: ')

assets = requests.get("https://discord.com/api/v9/oauth2/applications/" + id + "/assets")

jsonData = assets.json()

for jsonObj in jsonData:
    image = requests.get("https://cdn.discordapp.com/app-assets/" + id + "/" + jsonObj["id"] + ".png")
    with open(jsonObj["name"] + '.png', 'wb') as f:
        f.write(image.content)
