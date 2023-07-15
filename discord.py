import discord
import random

# Create a Discord client
client = discord.Client()

# Dictionary to store user balances
user_balances = {}

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/stocks'):
        # Generate a random number between -1000 and 1000
        stock_value = random.randint(-1000, 1000)

        # Calculate the gain or loss for the user
        user_gain_loss = stock_value

        # Get the user's balance or initialize it if not present
        user_id = str(message.author.id)
        if user_id not in user_balances:
            user_balances[user_id] = 0

        # Update the user's balance
        user_balances[user_id] += user_gain_loss

        # Format the gain/loss message
        if user_gain_loss >= 0:
            gain_loss_message = f"You gained ${user_gain_loss}!"
        else:
            gain_loss_message = f"You lost ${abs(user_gain_loss)}."

        # Send the gain/loss message to the user
        await message.channel.send(gain_loss_message)

    elif message.content.startswith('/leaderboard'):
        # Sort users by balance in descending order
        sorted_users = sorted(user_balances.items(), key=lambda x: x[1], reverse=True)

        # Get the top 5 users
        top_users = sorted_users[:5]

        # Format the leaderboard message
        leaderboard_message = "Top 5 Users:\n"
        for rank, (user_id, balance) in enumerate(top_users, start=1):
            user = client.get_user(int(user_id))
            leaderboard_message += f"{rank}. {user.name}: ${balance}\n"

        # Send the leaderboard message to the channel
        await message.channel.send(leaderboard_message)

    elif message.content.startswith('/loserboard'):
        # Sort users by balance in ascending order
        sorted_users = sorted(user_balances.items(), key=lambda x: x[1])

        # Get the lowest 5 users
        lowest_users = sorted_users[:5]

        # Format the loserboard message
        loserboard_message = "Lowest 5 Users:\n"
        for rank, (user_id, balance) in enumerate(lowest_users, start=1):
            user = client.get_user(int(user_id))
            loserboard_message += f"{rank}. {user.name}: ${balance}\n"

        # Send the loserboard message to the channel
        await message.channel.send(loserboard_message)

# Replace 'YOUR_TOKEN' with your actual bot token
client.run(1129732663075426357)
