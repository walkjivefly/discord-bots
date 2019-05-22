import discord
import requests

client = discord.Client()

headers = {
    'PRIVATE-TOKEN': 'kMAY2ToazuTYSpg_3YoE',
}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('##'):
        everything=str(message.content)[2:]
        elist=everything.split(' ',1)
        url='https://gitlab.crown.tech/api/v4/projects/54/issues/' + elist[0] + '/notes'
        msg='From ' + str(message.author) + ': ' + elist[1]
        params = ( ('body', msg), )
        response = requests.post(url, headers=headers, params=params)
        await message.channel.send(response)

client.run('NTgwMzk0NDI1MDI1Mjk4NDQy.XOQF4Q.hMOG6-yZ3wsUduIMK6dn1gGI38k')
