# Class representing the television
class TV:
    # Initialize the TV object with default values for channel, volume, and is_on
    def __init__(self, channel=1, volume=1, is_on=False):
        self.channel = channel
        self.volume = volume
        self.is_on = is_on
        self.channels = list(range(1, 120))

    # Turn on the TV
    def turn_on(self):
        self.is_on = True

    # Turn off the TV
    def turn_off(self):
        self.is_on = False

    # Set the channel of the TV
    def set_channel(self, channel):
        if channel in self.channels:
            self.channel = channel

    # Set the volume of the TV
    def set_volume(self, volume):
        if 0 <= volume <= 7:
            self.volume = volume

    # Get the current channel of the TV
    def get_channel(self):
        return self.channel

    # Get the current volume of the TV
    def get_volume(self):
        return self.volume

    # Increase the channel by 1
    def channel_up(self):
        if self.channel < max(self.channels):
            self.channel += 1
        else:
            self.channel = min(self.channels)

    # Decrease the channel by 1
    def channel_down(self):
        if self.channel > min(self.channels):
            self.channel -= 1
        else:
            self.channel = max(self.channels)

    # Increase the volume by 1
    def volume_up(self):
        if self.volume < 7:
            self.volume += 1
        else:
            print("Maximum volume reached.")

    # Decrease the volume by 1
    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Minimum volume reached.")

# Create a new python file named 'test_tv' that will serve as the test driver.
