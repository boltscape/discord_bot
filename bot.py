from discord.ext.commands import Bot
import os
import requests

BOT_PREFIX = '!'
TOKEN = os.environ['BOT_TOKEN']
post_url = 'https://panel.freemc.host/api/client/servers/'+ os.environ['SERVER_ID'] +'/power'
get_url = 'https://panel.freemc.host/api/client/servers/'+ os.environ['SERVER_ID'] +'/utilization'
header = {"Accept": "Application/vnd.pterodactyl.v1+json",
          "Content-Type": "application/json",
          "Authorization": "Bearer " + Bearer os.environ['PTERO_TOKEN']
          }

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name="start", description="Starts Minecraft server", brief="Starts Minecraft server",
                pass_context=True)
async def startserver(ctx):
    params = {"signal": "start"}
    response = requests.post(post_url, json=params, headers=header)
    if response.status_code == 204:
        await ctx.send("Starting the server, " + ctx.author.mention + ", enjoy!")
    else:
        await ctx.send("Hmmmm. There seems to be an error, " + ctx.author.mention + ". Try again later?")


@client.command(name="stop", description="Stops Minecraft server", brief="Stops Minecraft server",
                pass_context=True)
async def stopserver(ctx):
    params = {"signal": "stop"}
    response = requests.post(post_url, json=params, headers=header)
    if response.status_code == 204:
        await ctx.send("Stopping the server, " + ctx.author.mention + ", hope you had a great time!")
    else:
        await ctx.send("Hmmmm. There seems to be an error, " + ctx.author.mention + ". Try again later?")


@client.command(name="status", description="Check if server is running", brief="Check if server is running",
                pass_context=True)
async def serverstatus(ctx):
    response = requests.get(get_url, headers=header)
    res = response.json()
    if res["attributes"]["state"] == "on":
        await ctx.send("Server is already on, " + ctx.author.mention + ", get on there!")
    elif res["attributes"]["state"] == "off":
        await ctx.send("Welp, server's off " + ctx.author.mention + ". Start it using the startserver command!")
    else:
        await ctx.send("Hmmmm. There seems to be an error, " + ctx.author.mention + ". Try again later?")


@client.command(description="Show the server address", brief="Show server address", pass_context=True)
async def address(ctx):
    await ctx.send("Hey " + ctx.author.mention + ", use " + os.environ['SERVER_ADDRESS'] + " to connect to the server!")


client.run(TOKEN)
