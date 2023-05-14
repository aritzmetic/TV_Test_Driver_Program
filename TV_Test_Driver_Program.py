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
    def __init__(self, channel=1, volume=1, tv_is_on=False)
    """Constructor for creating a new TV object"""
    # Create Instances
    self.channel = channel
    self.volume = volume
    self.tv_is_on = tv_is_on

# Turn on the TV
# Turn off the TV
# Get the Channel
# Set the Channel
# Get the Volume
# Set the Volume
# Use channelUp to increment the channel by 1 if it is in a minimum value
# Use channelDown to decrement the channel by 1 if it is in a maximum value
# Use volumeUp to increment the volume by 1 if it is in a minimum value
# Use volumeDown to decrement the volume by 1 if it is in a maximum value

# Create test driver program class named TestTV
# Create two instances; tv1 and tv2
# Print the intances