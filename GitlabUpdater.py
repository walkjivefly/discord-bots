import discord
import requests
import configparser
from datetime import datetime

# Read the config
config = configparser.ConfigParser()
config.read_file(open("Bots.ini"))
private_token = config.get("GitlabUpdater", "private_token")
base_url = config.get("GitlabUpdater", "base_url")
bot_id = config.get("GitlabUpdater", "bot_id")
magic_string = config.get("GitlabUpdater", "magic_string")
allowed_guild = config.get("GitlabUpdater", "guild")
allowed_channel = config.get("GitlabUpdater", "channel")

# Instantiate Discord interface
client = discord.Client()

# Build Gitlab request header
headers = {
    'PRIVATE-TOKEN': private_token,
}

# Register events and our reactions

# 1. Let the operator know we're logged in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# 2. What we're here for
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(magic_string):
        print(datetime.now().strftime('\n%Y-%m-%d %H:%M:%S ') + \
              str(message.author) + ' in ' + \
              str(message.guild) + '/' + str(message.channel))
        if str(message.guild) != allowed_guild and \
           str(message.channel) != allowed_channel:
            #response = 'Bot is not enabled in this server/channel.'
            return
        else:
            everything = str(message.content)[2:].strip()
            #print('<< ' + everything)
            elist = everything.split(' ',1)
            issue = elist[0]
            if not issue.isnumeric():
                response = 'Begin your comment with ' + magic_string + \
                           ' followed by the issue number to update.'
            elif len(elist) != 2:
                response = 'Missing comment for issue #' + issue
            else:
                url = base_url + issue + '/notes'
                msg = 'From ' + str(message.author) + ': ' + elist[1]
                params = ( ('body', msg), )
                response = str(requests.post(url, headers=headers, 
                                             params=params))
                if response == '<Response [404]>':
                    response = 'Issue #' + issue + ' not found.'
                elif response == '<Response [201]>':
                    response = 'Issue #' + issue + ' updated successfully.'
                else:
                    response = 'Unexpected: ' + response + \
                               ' - please report this.'
        await message.channel.send(response)
        print('>> ' + response)

# Actually do it
client.run(bot_id)
