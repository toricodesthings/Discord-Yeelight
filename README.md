# Yeelight Discord Bot

## Introduction

Yeelight Discord Bot is a simple yet powerful bot utilizing the Yeelight Python Library for local device control. It's a fun bot, and SHOULD be used for private servers. The bot instance must be hosted on a server or computer with LAN access to your Yeelight devices. For remote usage, consider setting up a private VPN on the network hosting your Yeelight devices. Currently, it allows comprehensive control of your bulbs and lightstrips, including power control, brightness, color customization, and more.

### Features

- **Device Discovery**: Automatically discover Yeelight bulbs on your local network.
- **Direct IP Management**: Manually set active bulb IP addresses.
- **Power Control**: Toggle bulbs on/off or switch power state easily.
- **Brightness Control**: Adjust brightness levels smoothly (1-100).
- **Ambient Brightness**: Control ambient brightness (if your bulb supports it).
- **Color Customization**:
  - RGB color adjustment.
  - HSV (Hue, Saturation, Value) adjustments.
  - Color temperature settings (range 2700K - 6500K).
- **Color Flow**: Initiate and stop dynamic color flows.
- **Adjustment Modes**: Choose between smooth transitions or sudden changes.
- **Music Mode**: Toggle music synchronization mode for enhanced effects.
- **Device Renaming**: Rename your bulbs directly via Discord commands.

## Installation

### Requirements:
- Python 3.7+
- Discord bot token ([create one here](https://discord.com/developers/applications))
- Yeelight Python library
- python-dotenv library

### Setup Steps:

1. **Clone the Repository:**
   ```bash
   git clone [your-repo-url]
   cd yeelight-discord
   ```

2. **Install Dependencies:**
   ```bash
   pip install yeelight python-dotenv discord.py
   ```

3. **Configuration:**
   - Rename `.env.example` to `.env` and input your Discord bot token.
   - Enable LAN Control in your Yeelight app (critical step).
   - Modify any necessary settings in the user-editable section within the Python script.

4. **Launch the Bot:**
   ```bash
   python yeelight_bot.py
   ```

---

## Command Usage

- `help`: Show the help message with all available commands.
- `discover`: Discover all Yeelight bulbs on the network.
- `setbulb <number>`: Select an active bulb from the discovered list.
- `setip <IP>`: Manually set the active bulb IP.
- `on`: Turn the bulb on.
- `off`: Turn the bulb off.
- `toggle`: Toggle the bulb's power state.
- `brightness <value>`: Set bulb brightness (1-100).
- `ambient <value>`: Set ambient brightness if supported (1-100).
- `rgb <R> <G> <B>`: Set the RGB color.
- `hsv <H> <S> [V]`: Set the HSV color (Value is optional).
- `ct <temperature>`: Set color temperature (2700-6500).
- `startcf`: Begin a default color flow sequence.
- `stopcf`: Stop any running color flow sequence.
- `adjust <smooth/sudden>`: Set bulb adjustment mode.
- `music <on/off>`: Toggle music synchronization mode.
- `name <new name>`: Rename the current bulb.

## Changelog

### v1.0
- Added comprehensive control (brightness, color, color flow, etc.).
- Device discovery and IP management.
- Enhanced stability and response.

### v0.1
- Initial base code implementation.
- Basic on/off functionality.

## Helpful Links
- [Yeelight Python Documentation](https://yeelight.readthedocs.io/en/latest/)
- [python-dotenv on PyPI](https://pypi.org/project/python-dotenv/)
- [discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

## Security & Privacy

Always keep your Discord bot token private. Never share this token publicly or commit it to public repositories.

## License

This project is open-source under the [MIT License](LICENSE).

