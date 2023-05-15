# Delera, Aritz B.

import time
import pyfiglet
import random
import datetime
from termcolor import colored
from pyfiglet import Figlet
from TV import TV


f = Figlet(font='isometric2')
print(colored(f.renderText('OOP'), 'blue'))

# Create an introduction
print("=" * 61)
print("\033[32m Welcome to AritzMetic's Television Tester! \033[0m".center(60, "+"))
print("=" * 61)

    # Ask the user for their name and make a greeting
name = input("\033[30mHi Smart Pipol! what is your name?: \033[0m")
print("\033[31mHi", name, "! AritzMetic is here to help you in navigating your TVs!!\033[0m")

# Create test driver program class named TestTV
class TestTV:
    def test(self):
        # Create two instances; tv1 and tv2
        tv1 = TV('30', '3')
        tv2 = TV('3', '2')

        # Initialize the changes list
        changes = []

        # Print the intances
        time.sleep(1)
        print(":" * 61)
        print("\033[33mProcessing...\033[0m" .center(70))
        print(":" * 61)
        time.sleep(3)
        print()
        print()
        print("<>" * 30)
        print("\033[32m 📺 tv1's channel is", tv1.getChannel(), "and volume level is " + tv1.getVolume() + ".\033[0m")
        print("\033[32m 📺 tv2's channel is", tv2.getChannel(), "and volume level is " + tv2.getVolume() + ".\033[0m")
        print("<>" * 30)
        print()
        time.sleep(2)

        # use while loop
        while True:
            try:
                # Ask the user if they want to change the TVs
                tv_change = input(f"\033[30m\nHi {name}! Do you want to change the settings on the TVs? (y/n) \033[0m")
                if tv_change.lower() != 'y' and tv_change.lower() != 'n':
                    raise ValueError
                break
            except ValueError:
                print("\033[34mInvalid input. Please enter 'y' or 'n'.\033[0m")

        # If the user wants to change the TVs, allow them to do so.
        if tv_change.lower() == "y":
            while True:
                # Ask the user which TV they want to change.
                while True:
                    try:
                        tv_num = int(input("\033[30mWhich TV do you want to change? (1 or 2) \033[0m"))
                        if tv_num != 1 and tv_num != 2:
                            raise ValueError
                        break
                    except ValueError:
                        print("\033[34mInvalid input. Please enter 1 or 2.\033[0m")

                # Ask the user what setting they want to change.
                while True:
                    tv_setting = input("\033[30mWhat do you want to change? [channel or volume]\033[0m ")
                    if tv_setting.lower() == "channel" or tv_setting.lower() == "volume":
                        break
                    else:
                        print("\033[34mInvalid input. Please enter 'channel' or 'volume'.\033[0m")

                
                # Ask the user what value they want to set the setting to.
                while True:
                    try:
                        value = int(input("\033[30mWhat do you want to set the " + tv_setting + " to?\033[0m "))
                        break
                    except ValueError:
                        print("\033[34mInvalid input. Please enter a number.\033[0m")
                    
                # Store the changes made in a dictionary
                change = {
                    'tv': tv_num,
                    'setting': tv_setting,
                    'value': value
                }
                changes.append(change)

                # Set the specified setting on the specified TV to the specified value.
                if tv_num == 1:
                    if tv_setting.lower() == "channel":
                        tv1.setChannel(value)
                    else:
                        tv1.setVolume(value)
                    print("\033[45m📺 TV1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume(),".\033[0m")
                else:
                    if tv_setting.lower() == "channel":
                        tv2.setChannel(value)
                    else:
                        tv2.setVolume(value)
                    print("\033[45m📺 TV2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume(),".\033[0m")

                # Ask the user if they want to change the TVs again.
                while True:
                    try:
                        change_tvs = input("\033[30m\nDo you want to change the settings on the TVs again? (y/n) \033[0m")
                        if change_tvs.lower() != 'y' and change_tvs.lower() != 'n':
                            raise ValueError
                        break
                    except ValueError:
                        print("\033[34mInvalid input. Please enter 'y' or 'n'.\033[0m")

                if change_tvs.lower() == "n":

                    # Store the changes to a new file
                    filename = f"{name}_tv_changes.txt"
                    with open(filename, 'w') as file:
                        file.write("TV Changes:\n")
                        for change in changes:
                            file.write(f"TV {change['tv']} - {change['setting']}: {change['value']}\n")
                    
                    # Generate a report of the changes
                    now = datetime.datetime.now()
                    report_filename = f"{name}_tv_changes_report.txt"
                    with open(report_filename, 'w') as file:
                        file.write(f"TV Changes Report - {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
                        file.write("=" * 80 + "\n")
                        file.write(f"Name: {name}\n\n")
                        file.write("Changes:\n")
                        for change in changes:
                            file.write(f"TV {change['tv']} - {change['setting']}: {change['value']}\n")

                            print("=" * 61)
                            print("\033[35mYour changes have been saved to", filename, "successfully!\033[0m")
                            print("=" * 61)

                    goodbye_quotes = [
                        "Television is an invention that permits you to be entertained in your living room by people you wouldn't have in your home. - David Frost",
                        "Television is chewing gum for the eyes. - Frank Lloyd Wright",
                        "Television has brought back murder into the home - where it belongs. - Alfred Hitchcock",
                        "Television: a medium. So called because it's neither rare nor well done. - Ernie Kovacs"
                    ]
                    print()
                    print("\033[35mThank you for using AritzMetic's TV Tester! 📺💡\033[0m")
                    print("{}".format(random.choice(goodbye_quotes)))
                    f = Figlet(font='doom')
                    print(colored(f.renderText('=THE END='), 'green'))
                    break
        else:
            goodbye_quotes = [
                "Television is an invention that permits you to be entertained in your living room by people you wouldn't have in your home. - David Frost",
                "Television is chewing gum for the eyes. - Frank Lloyd Wright",
                "Television has brought back murder into the home - where it belongs. - Alfred Hitchcock",
                "Television: a medium. So called because it's neither rare nor well done. - Ernie Kovacs"
            ]

            print("\033[35mThank you for using AritzMetic's TV Tester! 📺💡\033[0m")
            print("{}".format(random.choice(goodbye_quotes)))
            f = Figlet(font='doom')
            print(colored(f.renderText('=THE END='), 'green'))


test_tv = TestTV()
test_tv.test()
