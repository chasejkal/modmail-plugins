import discord
from discord.ext import commands
import openai

# Set up your OpenAI API key
openai.api_key = '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'

# Set up your Discord bot
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def chat(ctx, *, user_input):
    # Use OpenAI to generate a response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_input,
        temperature=0.7,
        max_tokens=150,
        n=1,
    )
    
    # Send the response back to Discord
    await ctx.send(response.choices[0].text)

# Run your bot
bot.run('your_discord_bot_token')
