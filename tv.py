# Class representing the television
class TV:
    # Initialize the TV object with default values for channel, volume, and is_on
    def __init__(self, channel=1, volume=1, is_on=False):
        self.channel = channel
        self.volume = volume
        self.is_on = is_on
        self.channels = list(range(1, 31))

# Turn on the TV
# Turn off the TV
# Set the channel of the TV
# Set the volume of the TV
# Get the current channel of the TV
# Get the current volume of the TV
# Increase the channel by 1
# Decrease the channel by 1
# Increase the volume by 1
# Decrease the volume by 1
