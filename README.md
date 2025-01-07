# Mobile-Game-Automations

**DISCLAIMER: This script is provided for educational purposes only. Use it at your own risk. I am not liable for any consequences as I do not condone or encourage the violation of any game's Terms of Service or applicable laws.**

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Manual Setup](#manual-setup)
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
    git clone https://github.com/yourusername/Mobile-Game-Automations.git
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
3. The script will start automating the tasks based on the images and confidence levels defined in the `account_1_park_coords` and `account_2_park_coords` lists.

## Manual Setup
1. **Create Accounts Manually**: You will need to manually create the accounts in the game.
2. **Take Screenshots**: For each account, take screenshots of the relevant game elements and save them in the [Images](http://_vscodecontentref_/2) directory. Ensure the filenames match those specified in the `account_1_park_coords` and `account_2_park_coords` lists in [main.py](http://_vscodecontentref_/3).
3. **Update Coordinates**: If necessary, update the coordinates and confidence levels in the [main.py](http://_vscodecontentref_/4) file to match your screenshots.

## Functions
### `get_mouse_position()`
Prints the current mouse position every second. Useful for debugging and finding coordinates on the screen.

### `compare_image(image_1, image_2)`
Compares two images and returns `True` if they are similar based on a predefined threshold.

### `get_image_difference(image_1, image_2)`
Calculates the difference between two images using histogram comparison and template matching.

### `find_current_screen(filename='./Images/current_screen.png')`
Takes a screenshot of the current screen and saves it to the specified filename.

### `wait_after_loading_screen()`
Waits for the loading screen to disappear by checking for specific elements on the screen.

### `check_screen_after_loading_screen()`
Checks for additional pop-ups or messages after the loading screen and handles them.

### `wait_until_element_appears(filename, confidence_level=0.9, click_option=False)`
Waits until a specific element appears on the screen and optionally clicks it.

### `check_for_errors()`
Checks for common error messages and attempts to resolve them.

### `reposition_island()`
Repositions the game view to a known state.

### `get_tuple_index(current_file, file_confidence)`
Returns the index of a file in the `account_1_park_coords` or `account_2_park_coords` list.

### `fix_automation(file, confidence)`
Attempts to fix the automation if it gets stuck on a specific file.

### `run_automation(dv_instance, threshold)`
Main function that runs the automation loop.

### `calculate_proper_drag(current_x, current_y, found_island)`
Calculates the drag distance to reposition the game view.

## License
This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/5) file for details.