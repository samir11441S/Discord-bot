import discord
from discord.ext import commands
from discord.ui import Button, View

# Define intents and create bot instance
intents = discord.Intents.default()
intents.members = True  # Make sure the bot can access member updates

bot = commands.Bot(command_prefix='!', intents=intents)

# Define your channel IDs and role ID
WELCOME_CHANNEL_ID = 1267411121443442689  # Replace with your actual welcome channel ID
GOODBYE_CHANNEL_ID = 1274115352032186398  # Replace with your actual goodbye channel ID
ROLE_ID = 1275821445431165000  # Replace with your actual role ID

# URL of the animated GIF you want to use
ANIMATED_GIF_URL = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjJva2g2b3owcHQ4OWIzdzZxcm9hNWZkeTg1ZGF0djlhY2R3b2ZqOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JUk5OvdAM8fD7BVvJE/giphy.gif"  # Replace with your actual GIF URL

# URL of a default image to use if the user has no avatar
DEFAULT_AVATAR_URL = "https://i.imgur.com/0F1pDSS.png"  # Replace with your default image URL

# Class for the welcome view with buttons
class WelcomeView(View):
    def __init__(self):
        super().__init__()
        # Add buttons with links
        self.add_item(Button(label="Join Our Discord", url="https://discord.gg/8mwaFhxWES", style=discord.ButtonStyle.link))
        self.add_item(Button(label="Visit Our Telegram", url="https://t.me/blackmamba5043", style=discord.ButtonStyle.link))
        self.add_item(Button(label="Visit Our Youtube", url="https://www.youtube.com/@MAMBAGAMRES", style=discord.ButtonStyle.link))

# Event that triggers when the bot has connected to the server
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event that triggers when a new member joins the server
@bot.event
async def on_member_join(member):
    try:
        # Get the welcome channel using the ID
        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            # Determine the avatar URL or use default if not available
            avatar_url = member.avatar.url if member.avatar else DEFAULT_AVATAR_URL
            
            embed = discord.Embed(
                title="Welcome to Mamba Gamers Zone!",
                description=(
                    f"𝙃𝙀𝙔 🎀{member.mention}🎀\n\n"
                    "🎉 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊  𝙈𝙔 𝙎𝙀𝙍𝙑𝙀𝙍  𝙏𝙃𝘼𝙉𝙆𝙎 𝙁𝙊𝙍 𝙅𝙊𝙄𝙉𝙄𝙉𝙂! 🎉\n\n"
                    "────────────────────────────────\n\n"
                    "➡️ 。゜✿ 📢┆𝐀𝐍𝐍𝐎𝐂𝐔𝐍𝐂𝐄𝐌𝐄𝐍𝐓 ✿゜[。゜𝘾𝙇𝙄𝘾𝙆 ゜。](https://ptb.discord.com/channels/1267380242784190588/1268058470142447669) ⬅️\n\n"
                    "➡️ 。゜✿ 📌┆𝐑𝐔𝐋𝐄𝐒 ✿゜[。゜𝘾𝙇𝙄𝘾𝙆 ゜。](https://ptb.discord.com/channels/11267380242784190588/1267598097450668056) ⬅️\n\n"
                    "➡️ 。゜✿ ☎┆𝐂𝐎𝐍𝐓𝐑𝐒𝐂𝐓  ✿゜[。゜𝘾𝙇𝙄𝘾𝙆 ゜。](https://discord.gg/KmphMRQUzQ) ⬅️\n\n"
                    "➡️ 。゜✿ 📸┆ᴡᴡᴄᴅ ✿゜[。゜𝘾𝙇𝙄𝘾𝙆 ゜。](https://ptb.discord.com/channels/1267380242784190588/1269493829841588428) ⬅️\n\n"
                    "➡️ 。゜✿ 💬┆𝐏𝐔𝐁𝐋𝐈𝐂-𝐂𝐇𝐀𝐓┆-✿゜[。゜𝘾𝙇𝙄𝘾𝙆 ゜。](https://ptb.discord.com/channels/1267380242784190588/1267384229847765052) ⬅️\n\n"
                    "────────────────────────────────\n\n"
                ),
                color=discord.Color.blue()
            )
            embed.set_author(name=member.display_name, icon_url=avatar_url)  # Use avatar URL or default
            embed.set_image(url=ANIMATED_GIF_URL)  # Set your GIF as the image in the embed

            view = WelcomeView()
            await channel.send(embed=embed, view=view)

        # Assign role to the new member
        role = discord.utils.get(member.guild.roles, id=ROLE_ID)
        if role:
            await member.add_roles(role)
            print(f'Assigned role {role.name} to {member.name}')
        else:
            print(f'Role with ID {ROLE_ID} not found.')

    except Exception as e:
        print(f"Error sending welcome message or assigning role: {e}")

# Event that triggers when a member leaves the server
@bot.event
async def on_member_remove(member):
    try:
        # Get the goodbye channel using the ID
        channel = bot.get_channel(GOODBYE_CHANNEL_ID)
        if channel:
            await channel.send(f'Goodbye, {member.name}. We hope to see you again soon. Have a great day!')
    except Exception as e:
        print(f"Error sending goodbye message: {e}")

# Run the bot with your token directly (not recommended for production)
bot.run('')
