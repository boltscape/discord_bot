from discord.ext.commands import Bot
from pydactyl import PterodactylClient
from discord import Game
import requests
import os


BOT_PREFIX = ('!')
TOKEN = os.environ['BOT_TOKEN']
srv_id = os.environ['SERVER_ID']

client = Bot(command_prefix=BOT_PREFIX)
panel_client = PterodactylClient('https://panel.gamehosting.gg', os.environ['PTERO_TOKEN'])

@client.command(name="start", description="Starts Minecraft server", brief="Starts Minecraft server", pass_context=True)
async def startserver(ctx):
    response = panel_client.client.send_power_action(srv_id, 'start')
    if response.status_code == 204:
        await ctx.send("Starting the server, "+ ctx.author.mention + ", enjoy!")

@client.command(name="stop", description="Stops Minecraft server", brief="Stops Minecraft server", pass_context=True)
async def stopserver(ctx):
    response = panel_client.client.send_power_action(srv_id, 'stop')
    if response.status_code == 204:
        await ctx.send("Stopping the server, "+ ctx.author.mention + ", hope you had a great time!")

@client.command(name="status", description="Check if server is running", brief="Check if server is running", pass_context=True)
async def serverstatus(ctx):
    res = panel_client.client.get_server_utilization('61955f87')
    if res['state'] == "on":
        await ctx.send("Server is already on, "+ ctx.author.mention + ", get on there!")
    elif res['state'] == "off":
        await ctx.send("Welp, server's off "+ ctx.author.mention + ". Start it using the start command!")
    else:
        await ctx.send("Hmmmm. The server is either starting or stopping right now, "+ ctx.author.mention)

@client.command(description="Show the server address", brief="Show server address", pass_context=True)
async def address(ctx):
    await ctx.send("Hey "+ ctx.author.mention + ", use " + os.environ['SERVER_ADDRESS'] + " to connect to the server!")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Minecraft"))

                                 
client.run(TOKEN)
