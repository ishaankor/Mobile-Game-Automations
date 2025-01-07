# Mobile-Game-Automations

**DISCLAIMER: This script is provided for educational purposes only. Use it at your own risk. I am not liable for any consequences as I do not condone or encourage the violation of any game's Terms of Service or applicable laws.**

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
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

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ishaankor/Mobile-Game-Automations.git
    cd Mobile-Game-Automations
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Ensure the game is running and the screen resolution matches the images in the [Images](http://_vscodecontentref_/1) directory.
2. Run the script:
    ```sh
    python main.py
    ```
3. The script will start automating the tasks based on the images and confidence levels defined in the [automation_series](http://_vscodecontentref_/2) list.

## Functions
### [get_mouse_position()](http://_vscodecontentref_/3)
Prints the current mouse position every second. Useful for debugging and finding coordinates on the screen.

### [compare_image(image_1, image_2)](http://_vscodecontentref_/4)
Compares two images and returns `True` if they are similar based on a predefined threshold.

### [get_image_difference(image_1, image_2)](http://_vscodecontentref_/5)
Calculates the difference between two images using histogram comparison and template matching.

### [find_current_screen(filename='./Images/current_screen.png')](http://_vscodecontentref_/6)
Takes a screenshot of the current screen and saves it to the specified filename.

### [wait_after_loading_screen()](http://_vscodecontentref_/7)
Waits for the loading screen to disappear by checking for specific elements on the screen.

### [check_screen_after_loading_screen()](http://_vscodecontentref_/8)
Checks for additional pop-ups or messages after the loading screen and handles them.

### [wait_until_element_appears(filename, confidence_level=0.9, click_option=False)](http://_vscodecontentref_/9)
Waits until a specific element appears on the screen and optionally clicks it.

### [check_for_errors()](http://_vscodecontentref_/10)
Checks for common error messages and attempts to resolve them.

### [reposition_island()](http://_vscodecontentref_/11)
Repositions the game view to a known state.

### [get_tuple_index(current_file, file_confidence)](http://_vscodecontentref_/12)
Returns the index of a file in the [automation_series](http://_vscodecontentref_/13) list.

### [fix_automation(file, confidence)](http://_vscodecontentref_/14)
Attempts to fix the automation if it gets stuck on a specific file.

### [event_currency_automation()](http://_vscodecontentref_/15)
Main function that runs the automation loop.

### [calculate_proper_drag(current_x, current_y, found_island)](http://_vscodecontentref_/16)
Calculates the drag distance to reposition the game view.

## License
This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/17) file for details.