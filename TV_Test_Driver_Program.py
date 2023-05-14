# Delera, Aritz B.

# Exercise:
# Given: A UML Class Diagram below:
# Required: Create a Python Code for creating the Class named TV
# and a Test Driver program named TestTV that will create two objects from Class TV 
# and will produce the following output:

# PSEUDOCODE
# Create Class 
class TV:
    """A class representing a TV"""

    # Use Class Variable to initialize the values of channel and volume
    minimum_channel = 1
    maximum_channel = 120
    minimum_volume = 1
    maximum_volume = 7

    # Create Constructor
    def __init__(self, channel=1, volume=1, tv_is_on=False):
        """Constructor for creating a new TV object
        
        Parameters:
        channel (int): The starting value of the channel. The default value is 1.
        volume (int): The starting level of the volume. The default level is 1.
        tv_is_on (bool): The starting power state of the Televisiom. The default power state is false.

        """
    # Create Instances
        self.channel = channel
        self.volume = volume
        self.tv_is_on = tv_is_on

    # Turn on the TV
    def turnOn(self):
        """Turns on the TV"""
        tv_is_on = True
        
    # Turn off the TV
    def turnOff(self):
        """Turns off the TV"""
        tv_is_on = False

    # Get the Channel
    def getChannel(self):
        """Returns the channel that is currently being displayed on the TV"""
        return self.channel

    # Set the Channel
    def setChannel(self, channel):
        """Sets the TV channel to the given value, as long as it's within the valid range."""
        if self.minimum_channel <= channel <= self.maximum_channel:
            self.channel = channel

    # Get the Volume
    def getVolume(self):
        """Returns the volume level that is currently being displayed on the TV"""
        return self.volume

    # Set the Volume
    def setVolume(self, volume):
        """Sets the TV's volume level to the given value, as long as it's within the valid range."""
        if self.minimum_volume <= volume <= self.maximum_volume:
            self.volume = volume

    # Use channelUp to increment the channel by 1 if it is in a minimum value
    def channelUp(self):
        """Method for incrementing the current channel by 1 if it is less than the maximum allowed channel value.

        Args:
            None

        Returns:
            None
        """
        if self.channel < self.maximum_channel:
            self.channel += 1

    # Use channelDown to decrement the channel by 1 if it is in a maximum value
    def channelDown(self):
        """Method for decrementing the current channel by 1 if it is greater than the minimum allowed channel value.

        Args:
            None

        Returns:
            None
        """
        if self.channel > self.minimum_channel:
            self.channel -= 1

    # Use volumeUp to increment the volume by 1 if it is in a minimum value
    def volumeUp(self):
        """Method for incrementing the current volume by 1 if it is less than the maximum allowed volume value.

        Args:
            None

        Returns:
            None
        """
        if self.volume < self.maximum_volume:
            self.volume += 1

    # Use volumeDown to decrement the volume by 1 if it is in a maximum value
    def volumeDown(self):
        """Method for decrementing the current volume by 1 if it is greater than the minimum allowed volume value.

        Args:
            None

        Returns:
            None
        """
        if self.volume > self.maximum_volume:
            self.volume -= 1

# Create test driver program class named TestTV
class TestTV:

    # Create two instances; tv1 and tv2
    tv1 = TV('30', '3')
    tv2 = TV('3', '2')

    # Print the intances
    print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())