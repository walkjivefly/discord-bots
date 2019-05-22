import discord
import requests
import configparser

config = configparser.ConfigParser()
config.read_file(open("Bots.ini"))
private_token = config.get("GitlabUpdater", "private_token")
base_url = config.get("GitlabUpdater", "base_url")
bot_id = config.get("GitlabUpdater", "bot_id")
magic_string = config.get("GitlabUpdater", "magic_string")

client = discord.Client()

headers = {
    'PRIVATE-TOKEN': private_token,
}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(magic_string):
        print('Bot triggered in ' + str(message.channel) + ' by ' + str(message.author))
        if str(message.channel) != 'gitlab-updater':
            response = 'Bot is not enabled in this channel'
        else:
            everything = str(message.content)[2:].strip()
            elist = everything.split(' ',1)
            issue = elist[0]
            if not issue.isnumeric():
                response = 'Begin your comment with the issue number to update.'
            else:
                url = base_url + issue + '/notes'
                msg = 'From ' + str(message.author) + ': ' + elist[1]
                params = ( ('body', msg), )
                response = str(requests.post(url, headers=headers, params=params))
                if response == '<Response [404]>':
                    response = 'Issue not found.'
                elif response == '<Response [201]>':
                    response = 'Issue updated successfully.'
                else:
                    response = 'Unexpected: ' + response
        await message.channel.send(response)

client.run(bot_id)
