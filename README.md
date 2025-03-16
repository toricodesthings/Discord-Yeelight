# yeelight-discord
Discord Bot Utilizing Yeelight Python Library (Local Only)

This is an extremely simple WIP bot that utilizes the Yeelight Python Lib. The bot can be added any server of your choosing but preferably your own private server. However, you'll need to host this bot instance on a server/computer with LAN Access to the Yeelight Devices (if non-local access is warranted, consider setting up a private vpn on the network that Yeelight is connected to). Right now, it allows you control your lightbulb On/Off state when you set the bulb's IP properly.

Usage:
- Create a discord bot here -> https://discord.com/developers/applications and input your token in the env file. KEEP THIS TOKEN A SECRET! 
- Please enable LAN Control in the YeeLight App (Important)
- Be sure to have both dot-env and yeelight library installed. Please install both these libraries if you do not have it. **Check the "Links" section for the link to said libraries.**
- Do not forget to edit the user editable area in the .py file, changes will be made to this soon.

# Changelog

v0.1
- Base Code
- On/Off Feature
- (Much more will be added soon)

# Lib Links 
- https://yeelight.readthedocs.io/en/latest/
- https://pypi.org/project/python-dotenv/
