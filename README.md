# Mobile-Game-Automations

**DISCLAIMER: This script is provided for educational purposes only. Use it at your own risk. I am not liable for any consequences as I do not condone or encourage the violation of any game's Terms of Service or applicable laws.**

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Manual Setup](#manual-setup)
- [Emulation](#emulation)
- [Repository Structure](#repository-structure)
- [Functions](#functions)
- [License](#license)

## Introduction
This project automates certain tasks in a mobile game using image recognition and mouse automation. The script is written in Python and utilizes libraries such as OpenCV and PyAutoGUI to perform actions based on the presence of specific images on the screen.

## Features
- Automates repetitive tasks in the game.
- Uses image recognition to identify elements on the screen.
- Can handle errors and reposition the game view if necessary.
- Logs actions and provides feedback on the automation status.

## Requirements
- Python 3.6 or higher
- OpenCV
- PyAutoGUI
- BlueStacks (or any other Android emulator)

## Manual Setup
1. Ensure BlueStacks (or your preferred Android emulator) is running and the screen resolution matches the images in the `Images` directory.
2. **Create Accounts Manually**: You will need to manually create the accounts in the game.
3. **Take Screenshots**: For each account, take screenshots of the relevant game elements and save them in the `Images` directory. Ensure the filenames match those specified in the `account_1_park_coords` and `account_2_park_coords` lists in `main.py`.
4. **Update Coordinates**: If necessary, update the coordinates and confidence levels in the `main.py` file to match your screenshots.

## Emulation
This project relies on BlueStacks, an Android emulator, to run the mobile game on a PC. Emulation is key to this automation as it allows the script to interact with the game as if it were running on a physical device. The script uses image recognition to identify elements on the screen and perform actions accordingly.

Two instances (or emulated devices) are being used to automate tasks for different accounts. This allows for parallel automation and increases efficiency. Ensure that both instances are properly set up and running before starting the script.

## Repository Structure
The repository is structured to separate the automation scripts for different accounts into branches. This allows for better organization and management of the automation scripts.

- `main` branch: Contains the main automation script and common functions.
- `gem-automation` branch: Contains the automation script specific to increasing gem count.
- `event-currency-automation` branch: Contains the automation script specific to increasing event currency count.

To switch between branches, use the following commands:
```sh
git checkout gem-automation
# or
git checkout event-currency-automation