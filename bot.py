import discord, asyncio, os, shutil, subprocess, json, time, sys, datetime
from discord.ext import commands

if not os.path.exists('config.json'):
    data = {
        'token': "",
        'prefix': "",
    }
    with open('config.json', 'w') as f:
        json.dump(data, f)

config = json.loads(open("config.json","r").read())
token = config['token']
prefix = config['prefix']

def getembed(text):
    embed = discord.Embed(
        description=text,
        color=0x2f3136
    )
    return embed

def checkConfig():
    if not token == "" and not prefix == "":
        return
    else: 
        if token == "":
            config['token'] = input('What is your token?\n')
        if prefix == "":
            config['prefix'] = input('Please choose a prefix for your commands e.g "+"\n')
        open('config.json','w+').write(json.dumps(config,indent=4,sort_keys=True))
        print('The program will now close so everything works correctly.')
        time.sleep(5)
        sys.exit()
        return

Client = discord.Client()
Client = commands.Bot(
    description='cnr selfbot',
    command_prefix=config['prefix'],
    self_bot=True
)
Client.remove_command('help') 

@Client.event
async def on_ready():
    
    os.system('cls')
    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print()
        print("[+] Made by cnr [+]".center(width))
        print()
        print(f"Current User: {Client.user}".center(width))
        print(f"User ID: {Client.user.id}".center(width))
        print()
        print(f"Prefix: {prefix}".center(width))
        print(f"Date: {datetime.date.today().strftime('%d, %B %Y')}".center(width))
        print()
        print("Commands:".center(width))
        print(f" {prefix}clear (clear messages in a single chat)".center(width))
        print(f" {prefix}cleardms (clear all messages in each dm)".center(width))
    ui()

    @Client.event
    async def on_message(message):
        if message.author == Client.user:
            if message.content == f'{prefix}clear':
                async for msg in message.channel.history(limit=None):
                    if msg.author == Client.user:
                        try:
                            print(f'Deleted msg {msg}')
                            await msg.delete()
                        except Exception as x:
                            pass
            if message.content == f'{prefix}cleardms':
                for channel in Client.private_channels:
                    if isinstance(channel, discord.DMChannel):
                        async for msg in message.channel.history(limit=None):
                            try:
                                if msg.author == Client.user:
                                    print(f'Deleted msg {msg}')
                                    await msg.delete()
                            except:
                                pass

checkConfig()
Client.run(config['token'], bot=False, reconnect=True)
