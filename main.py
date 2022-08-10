import discord
import requests

#this makes an request to OS API and returns data


headers = {"Accept": "application/json"}

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
      #  print('Message from {0.author}: {0.content}'.format(message))
        command_content =  message.content.split(" ")
        second_command = command_content[1]
        if message.author == self.user:
            return
        url = f"https://api.opensea.io/api/v1/collection/{second_command}/stats"
        url_pic = f"https://api.opensea.io/api/v1/collection/{second_command}"
        if message.content.startswith('!floor'):
            
            response = requests.request("GET", url, headers=headers).json()
            response_irl = requests.request("GET", url_pic, headers=headers).json()
           
            image_url = response_irl["collection"]["primary_asset_contracts"][0]["image_url"]
            thumbnail_url = response_irl["collection"]["banner_image_url"]
            floor_price = str(response['stats']['floor_price'])
            embed = discord.Embed(
                title ="Collection Page", 
                url=f"https://opensea.io/collection/{second_command}",
                #description = floor_price + "ETH",
                colour = discord.Colour.red()
            )
            embed.set_footer(text="cokemethize's floor checker bot")
            embed.set_image(url=thumbnail_url)
            embed.set_thumbnail(url=image_url)
            #embed.set_author(name='Author Name', icon_url=image_url)
            embed.add_field(name="Floor Price", value=floor_price + " ETH", inline=False)
            #embed.add_field(name='Field Name', value='Field Value', inline=True)
            #embed.add_field(name='Field Name', value='Field Value', inline=True)

            await message.channel.send(embed=embed)

            #await message.channel.send(response['stats']['floor_price'])



client = MyClient()
client.run(SECRET_KEY)
    



