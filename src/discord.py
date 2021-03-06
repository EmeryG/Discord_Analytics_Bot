import requests

DISCORD_API = 'https://discord.com/api/v8'
BOT_ID = '907693823407312896'

with open('bot_secret.txt', 'r') as file:
    BOT_SECRET = file.read().rstrip()
    
with open('bot_token.txt', 'r') as file:
    BOT_TOKEN = file.read().rstrip()

headers = { 'authorization': f'Bot {BOT_TOKEN}' }

class Guild:
    def __init__(self, guild_id):
        self.guild_id = guild_id
    
    def post_req(self, extension, data, params={}):
        r = requests.post(DISCORD_API + extension, headers=headers, data=data, params=params)
        r.raise_for_status()
        return r.json()
    
    def get_req(self, extension, params={}):
        r = requests.get(DISCORD_API + extension, headers=headers, params=params)
        r.raise_for_status()
        return r.json()
    
    def get_users(self):
        return self.get_req(f'/guilds/{self.guild_id}/members', { 'limit': 1000 })

    def get_roles(self):
        return self.get_req(f'/guilds/{self.guild_id}/roles')
    
    def send_message(self, message):
        data = {
            'content': message,
            'tts': False
        }

        return self.post_req('/channels/908169250684960778/messages', data)
    
    def send_image(self, image):
        imageFile = open(image + ".png", "rb")
        
        multipart = {
            "file": (imageFile.name, imageFile.read(), "image/png")
        }
        
        data = {
            "content": ""
        }
        
        r2 = requests.post(DISCORD_API + '/channels/908169250684960778/messages', headers=headers, files=multipart, data=data)
        r2.raise_for_status()
        
with open('server_id.txt', 'r') as file:
    DEFAULT_GUILD = Guild(file.read().rstrip())