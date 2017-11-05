from matrix_bot_api.matrix_bot_api import MatrixBotAPI
from matrix_bot_api.mhandler import MHandler
import discord
import yaml

config = yaml.safe_load(open('config.yml'))

class DiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.run_matrix())

    async def on_ready(self):
        self.watching = self.get_channel(config.get('discord').get('channel_id'))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nDiscord client ready!")
        print(f"{self.user.name}#{self.user.discriminator}")
        print(f"Watching #{self.watching.name} in {self.watching.guild.name}")

    async def on_message(self, message):
        if not message.channel == self.watching: return
        if message.author == discord_client.user: return
        matrix_client.watching.send_text(f"{message.author.name}: {message.content}")

    async def run_matrix(self):
        matrix_client.add_handler(MHandler(return_true, matrix_on_message))
        matrix_client.start_polling()
        matrix_client.watching = matrix_client.client.rooms.get(config.get('matrix').get('room_id'))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nMatrix client ready!")
        print(matrix_client.client.user_id)
        print(f"Watching {matrix_client.watching.name} in {matrix_client.client.hs}")

def return_true(room, event):
    return True

def matrix_on_message(room, event):
    if event['sender'] == matrix_client.client.user_id: return
    discord_client.loop.create_task(discord_client.watching.send(f"{event['sender']}: {event['content']['body']}"))

matrix_client = MatrixBotAPI(config.get('matrix').get('username'), config.get('matrix').get('password'), config.get('matrix').get('homeserver'))

discord_client = DiscordClient()
discord_client.run(config.get('discord').get('token'))
