import os
import discord
from dotenv import load_dotenv
from yeelight import Bulb, discover_bulbs, LightType

# Load environment variables and get Discord token
load_dotenv()
botToken = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# Global variables
botprefix = "yeelight"
botactivity = "Lights"
# Start with a default bulb IP (change as needed)
default_bulb_ip = "192.168.0.19"
bulb = Bulb(default_bulb_ip)
# Global variable to store the last discovered bulbs list
last_discovered_bulbs = []

@client.event
async def on_ready():
    print(f'{client.user} is connected to the following guilds:')
    for guild in client.guilds:
        print(f'{guild.name} (id: {guild.id})')
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(type=discord.ActivityType.watching, name=botactivity)
    )

@client.event
async def on_message(message):
    global bulb, last_discovered_bulbs

    if message.author == client.user or message.author.bot:
        return

    if message.content.lower().startswith(botprefix):
        tokens = message.content.split()
        if len(tokens) < 2:
            return
        # Command is the second word; remaining tokens are arguments.
        command = tokens[1].lower()
        args = tokens[2:]

        # HELP COMMAND: Display an embed with all command usages.
        if command == "help":
            embed = discord.Embed(
                title="Yeelight Bot Commands Help",
                description="Here are the available commands:",
                color=0x3498db
            )
            embed.add_field(name="help", value="Show this help message.", inline=False)
            embed.add_field(name="discover", value="Discover bulbs on the network.", inline=False)
            embed.add_field(name="setbulb <number>", value="Set active bulb from the discovered list.", inline=False)
            embed.add_field(name="setip <IP>", value="Manually set the active bulb IP.", inline=False)
            embed.add_field(name="on", value="Turn the bulb on.", inline=False)
            embed.add_field(name="off", value="Turn the bulb off.", inline=False)
            embed.add_field(name="toggle", value="Toggle the bulb power.", inline=False)
            embed.add_field(name="brightness <value>", value="Set brightness (1-100).", inline=False)
            embed.add_field(name="ambient <value>", value="Set ambient brightness (1-100) if supported.", inline=False)
            embed.add_field(name="rgb <R> <G> <B>", value="Set the RGB color.", inline=False)
            embed.add_field(name="hsv <H> <S> [V]", value="Set HSV color (V is optional).", inline=False)
            embed.add_field(name="ct <temperature>", value="Set color temperature (e.g., 2700-6500).", inline=False)
            embed.add_field(name="startcf", value="Start a default color flow.", inline=False)
            embed.add_field(name="stopcf", value="Stop any running color flow.", inline=False)
            embed.add_field(name="adjust <smooth/sudden>", value="Set the adjustment mode.", inline=False)
            embed.add_field(name="music <on/off>", value="Toggle music mode.", inline=False)
            embed.add_field(name="name <new name>", value="Rename the bulb.", inline=False)
            await message.channel.send(embed=embed)

        # DISCOVER: Scan for bulbs and display choices in an embed.
        elif command == "discover":
            bulbs = discover_bulbs()
            last_discovered_bulbs = bulbs
            if not bulbs:
                await message.channel.send("No bulbs found.")
            else:
                embed = discord.Embed(
                    title="Discovered Yeelight Bulbs",
                    description="Select a bulb using `yeelight setbulb <number>`.",
                    color=0x00ff00
                )
                for idx, b in enumerate(bulbs, start=1):
                    cap = b.get("capabilities", {})
                    name = cap.get("name", f"Bulb {idx}")
                    model = cap.get("model", "N/A")
                    power = cap.get("power", "N/A")
                    bright = cap.get("bright", "N/A")
                    ip = b.get("ip", "N/A")
                    embed.add_field(
                        name=f"{idx}: {name}",
                        value=f"**IP:** {ip}\n**Model:** {model}\n**Power:** {power}\n**Brightness:** {bright}",
                        inline=False
                    )
                await message.channel.send(embed=embed)

        # SETBULB: Set the active bulb from the discovered list.
        elif command == "setbulb":
            if len(args) < 1:
                await message.channel.send("Please specify the bulb number. Example: `yeelight setbulb 1`")
            else:
                try:
                    index = int(args[0]) - 1
                    if index < 0 or index >= len(last_discovered_bulbs):
                        await message.channel.send("Invalid bulb number.")
                    else:
                        selected = last_discovered_bulbs[index]
                        ip = selected.get("ip")
                        bulb = Bulb(ip)
                        await message.channel.send(f"Active bulb set to IP: {ip}")
                except Exception as e:
                    await message.channel.send(f"Error setting bulb: {e}")

        # SETIP: Manually set the active bulb IP.
        elif command == "setip":
            if len(args) < 1:
                await message.channel.send("Please provide an IP address. Example: `yeelight setip 192.168.0.19`")
            else:
                ip = args[0]
                try:
                    bulb = Bulb(ip)
                    await message.channel.send(f"Active bulb set to IP: {ip}")
                except Exception as e:
                    await message.channel.send(f"Error setting bulb IP: {e}")

        # Turn the bulb on.
        elif command == "on":
            try:
                bulb.turn_on()
                await message.channel.send("Bulb turned on successfully.")
            except Exception as e:
                await message.channel.send(f"Error turning on bulb: {e}")

        # Turn the bulb off.
        elif command == "off":
            try:
                bulb.turn_off()
                await message.channel.send("Bulb turned off successfully.")
            except Exception as e:
                await message.channel.send(f"Error turning off bulb: {e}")

        # Toggle bulb power.
        elif command == "toggle":
            try:
                bulb.toggle()
                await message.channel.send("Bulb toggled successfully.")
            except Exception as e:
                await message.channel.send(f"Error toggling bulb: {e}")

        # Set brightness.
        elif command == "brightness":
            if len(args) < 1:
                await message.channel.send("Please provide a brightness value (1-100).")
            else:
                try:
                    value = int(args[0])
                    bulb.set_brightness(value)
                    await message.channel.send(f"Brightness set to {value}%.")
                except Exception as e:
                    await message.channel.send(f"Error setting brightness: {e}")

        # Set ambient brightness.
        elif command == "ambient":
            if len(args) < 1:
                await message.channel.send("Please provide an ambient brightness value (1-100).")
            else:
                try:
                    value = int(args[0])
                    bulb.set_brightness(value, light_type=LightType.Ambient)
                    await message.channel.send(f"Ambient brightness set to {value}%.")
                except Exception as e:
                    await message.channel.send(f"Error setting ambient brightness: {e}")

        # Set RGB color.
        elif command == "rgb":
            if len(args) < 3:
                await message.channel.send("Please provide RGB values: R G B")
            else:
                try:
                    r = int(args[0])
                    g = int(args[1])
                    b_val = int(args[2])
                    bulb.set_rgb(r, g, b_val)
                    await message.channel.send(f"RGB set to ({r}, {g}, {b_val}).")
                except Exception as e:
                    await message.channel.send(f"Error setting RGB: {e}")

        # Set HSV color.
        elif command == "hsv":
            if len(args) < 2:
                await message.channel.send("Please provide at least HSV values: H S [V]")
            else:
                try:
                    h = int(args[0])
                    s = int(args[1])
                    if len(args) >= 3:
                        v = int(args[2])
                        bulb.set_hsv(h, s, v)
                        await message.channel.send(f"HSV set to ({h}, {s}, {v}).")
                    else:
                        bulb.set_hsv(h, s)
                        await message.channel.send(f"HSV set to ({h}, {s}).")
                except Exception as e:
                    await message.channel.send(f"Error setting HSV: {e}")

        # Set color temperature.
        elif command in ["ct", "color_temp"]:
            if len(args) < 1:
                await message.channel.send("Please provide a color temperature value (e.g., 2700-6500).")
            else:
                try:
                    temp = int(args[0])
                    bulb.set_color_temp(temp)
                    await message.channel.send(f"Color temperature set to {temp}K.")
                except Exception as e:
                    await message.channel.send(f"Error setting color temperature: {e}")

        # Start a default color flow.
        elif command == "startcf":
            try:
                # Default color flow: red, green, blue sequence.
                default_flow = [
                    (500, 1, 16711680, 100),  # red
                    (500, 1, 65280, 100),     # green
                    (500, 1, 255, 100)        # blue
                ]
                bulb.start_cf(count=3, flow=default_flow)
                await message.channel.send("Color flow started with default pattern.")
            except Exception as e:
                await message.channel.send(f"Error starting color flow: {e}")

        # Stop any running color flow.
        elif command == "stopcf":
            try:
                bulb.stop_cf()
                await message.channel.send("Color flow stopped.")
            except Exception as e:
                await message.channel.send(f"Error stopping color flow: {e}")

        # Set adjustment mode.
        elif command == "adjust":
            if len(args) < 1:
                await message.channel.send("Usage: yeelight adjust <smooth/sudden>")
            else:
                try:
                    mode = args[0].lower()
                    bulb.set_adjust(mode)
                    await message.channel.send(f"Adjustment mode set to {mode}.")
                except Exception as e:
                    await message.channel.send(f"Error setting adjustment mode: {e}")

        # Toggle music mode.
        elif command == "music":
            if len(args) < 1:
                await message.channel.send("Usage: yeelight music <on/off>")
            else:
                try:
                    state = args[0].lower()
                    if state == "on":
                        bulb.set_music(True)
                        await message.channel.send("Music mode enabled.")
                    elif state == "off":
                        # Disabling music mode might not be supported.
                        await message.channel.send("Disabling music mode is not supported via this command.")
                    else:
                        await message.channel.send("Invalid parameter. Use 'on' or 'off'.")
                except Exception as e:
                    await message.channel.send(f"Error setting music mode: {e}")

        # Rename the bulb.
        elif command == "name":
            if len(args) < 1:
                await message.channel.send("Usage: yeelight name <new name>")
            else:
                try:
                    new_name = " ".join(args)
                    bulb.set_name(new_name)
                    await message.channel.send(f"Bulb name set to {new_name}.")
                except Exception as e:
                    await message.channel.send(f"Error setting bulb name: {e}")

        else:
            await message.channel.send("Unknown command. Type `yeelight help` for a list of commands.")

client.run(botToken)
