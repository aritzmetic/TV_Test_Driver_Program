# Delera, Aritz B.

import time
import pyfiglet

opening = pyfiglet.figlet_format("= O.O.P =", font="starwars")
print(opening)

# Create an introduction
print("=" * 61)
print(" Welcome to AritzMetic's Television Tester! ".center(60, "+"))
print("=" * 61)

    # Ask the user for their name and make a greeting
name = input("\033[30mHi Smart Pipol! what is your name?: \033[0m")
print("\033[31mHi", name, "! AritzMetic is here to help you in navigating your TVs!!\033[0m")

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
    def test(self):
        # Create two instances; tv1 and tv2
        tv1 = TV('30', '3')
        tv2 = TV('3', '2')

        # Print the intances
        time.sleep(1)
        print(":" * 61)
        print("\033[33mProcessing...\033[0m" .center(70))
        print(":" * 61)
        time.sleep(3)
        print()
        print("<>" * 30)
        print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
        print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())
        print("<>" * 30)
        time.sleep(2)

        # use while loop
        while True:
            try:
                # Ask the user if they want to change the TVs
                tv_change = input(f"\nHi {name}! Do you want to change the settings on the TVs? (y/n) ")
                if tv_change.lower() != 'y' and tv_change.lower() != 'n':
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 'y' or 'n'.")

        # If the user wants to change the TVs, allow them to do so.
        if tv_change.lower() == "y":
            while True:
                # Ask the user which TV they want to change.
                while True:
                    try:
                        tv_num = int(input("Which TV do you want to change? (1 or 2) "))
                        if tv_num != 1 and tv_num != 2:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid input. Please enter 1 or 2.")

                # Ask the user what setting they want to change.
                while True:
                    tv_setting = input("What do you want to change? [channel or volume] ")
                    if tv_setting.lower() == "channel" or tv_setting.lower() == "volume":
                        break
                    else:
                        print("Invalid input. Please enter 'channel' or 'volume'.")

                # Ask the user what value they want to set the setting to.
                while True:
                    try:
                        value = int(input("What do you want to set the " + tv_setting + " to? "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                # Set the specified setting on the specified TV to the specified value.
                if tv_num == 1:
                    if tv_setting.lower() == "channel":
                        tv1.setChannel(value)
                    else:
                        tv1.setVolume(value)
                    print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
                else:
                    if tv_setting.lower() == "channel":
                        tv2.setChannel(value)
                    else:
                        tv2.setVolume(value)
                    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())

                # Ask the user if they want to change the TVs again.
                while True:
                    try:
                        change_tvs = input("\nDo you want to change the settings on the TVs again? (y/n) ")
                        if change_tvs.lower() != 'y' and change_tvs.lower() != 'n':
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid input. Please enter 'y' or 'n'.")

                if change_tvs.lower() == "n":
                    print("Thank You!")
                    break
        else:
            print("Thank You!")

test_tv = TestTV()
test_tv.test()


