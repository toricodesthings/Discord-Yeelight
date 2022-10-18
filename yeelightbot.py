from dotenv import load_dotenv
from yeelight import Bulb
from yeelight import discover_bulbs

# Get Discord Token from .env file
load_dotenv()
botToken = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# User Changeable Info #
botprefix = "yeelight"
botactivity = "Lights"
bulb = Bulb("192.168.x.x")
# ======================= #

# Start Code, sets activity and online status and outputs list of guild
@client.event
async def on_ready():
    print(f'{client.user} is connected to the following guilds:')
    for guild in client.guilds:
        print(f'{guild.name}(id: {guild.id})')
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(type=discord.ActivityType.watching,
                                                           name="Lights"))
    
# Main Code
@client.event    
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    authorid = message.author.id
    authorname = message.author.name
    checkymsg = message.content.lower()
    
    if checkymsg.startswith(botprefix):
        sm = checkymsg.split()
        if "bulb discover" in checkymsg:
            discover_bulbs()
            await message.channel.send("Please check command console for light IP!")
        elif "bulb on" in checkymsg:
            bulb.turn_on()
            await message.channel.send("Successfully turned on light bulb")
        elif "bulb off" in checkymsg:
            bulb.turn_off()
            await message.channel.send("Successfully turned off light bulb")

# More Features added soon

# Runs the client
client.run(botToken)
