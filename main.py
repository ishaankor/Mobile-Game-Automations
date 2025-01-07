import cv2
import time
import pyautogui

automation_series = [
    ('./Images/breeding_cave.png', 0.5),
    ('./Images/retry_button.png', 0.7),
    ('./Images/breed_button.png', 0.8),
    ('./Images/heart_emoji.png', 0.78),
    ('./Images/place_in_nursery_button.png', 0.9),
    ('./Images/mythic_hall.png', 0.5),
    ('./Images/egg_nursery.png', 0.6),
    ('./Images/leaf_egg.png', 0.8),
    ('./Images/sell_button.png', 0.9),
    ('./Images/yes_button.png', 0.9),
    ('./Images/mythic_hall.png', 0.7)
]


def get_mouse_position():
    while True:
        print(pyautogui.position())
        time.sleep(1)


def compare_image(image_1, image_2):
    minimum_commutative_image_diff = 0.15
    image_1 = cv2.imread(image_1, 0)
    image_2 = cv2.imread(image_2, 0)
    commutative_image_diff = get_image_difference(image_1, image_2)
    if commutative_image_diff < minimum_commutative_image_diff:
        print(f"Matched with a commutative_image_diff of {commutative_image_diff}...")
        return True
    print(f"No match with a commutative_image_diff of {commutative_image_diff}...")
    return False


def get_image_difference(image_1, image_2):
    first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
    second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])
    img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
    img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
    img_template_diff = 1 - img_template_probability_match
    commutative_image_diff = (img_hist_diff / 10) + img_template_diff
    return commutative_image_diff


def find_current_screen(filename='./Images/current_screen.png'):
    pyautogui.moveTo(1500, 750)
    pyautogui.screenshot(filename, region=(0, 160, 1334, 747))


def wait_after_loading_screen():
    print("Checking if x_button is present or the Daily Rewards screen is...")
    while True:
        try:
            x_button = pyautogui.center(pyautogui.locateOnScreen('./Images/x_button.png', confidence=0.8))
            pyautogui.click(x_button)
            print("x_button has been clicked, resuming automation as the Daily Rewards screen is present...")
            break
        except:
            try:
                collect_button = pyautogui.center(pyautogui.locateOnScreen('./Images/collect_button.png'))
                pyautogui.click(collect_button)
                print("The cursor moved to the collect_button's position on the Daily Rewards screen...")
                return True
            except:
                time.sleep(1)


def check_screen_after_loading_screen():
    wait_until_element_appears('./Images/market_button.png', click_option=False)
    try:
        time.sleep(3)
        if pyautogui.center(pyautogui.locateOnScreen('./Images/x_button.png', confidence=0.7)):
            time.sleep(1)
            x_button = pyautogui.center(pyautogui.locateOnScreen('./Images/x_button.png', confidence=0.7))
            print("1st X found...")
            time.sleep(1)
            pyautogui.click(x_button)
            wait_after_loading_screen()
    except:
        print("No extra messages popped up...")
        pass


def wait_until_element_appears(filename, confidence_level=0.9, click_option=False):
    start_time = time.time()
    total_time = 0
    automation_status = True
    while automation_status is True:
        if total_time < 20:
            try:
                element = pyautogui.center(pyautogui.locateOnScreen(filename, confidence=confidence_level))
                print(f"{filename} was located, resuming automation...")
                if click_option:
                    pyautogui.moveTo(element)
                    time.sleep(0.5)
                    pyautogui.click(element)
                    print(f"{filename} was clicked, resuming automation...")
                    automation_status = False
                    time.sleep(1)
                else:
                    pyautogui.moveTo(element)
                    print(f"The cursor moved to {filename}'s position on the screen...")
                    automation_status = False
            except TypeError:
                end_time = time.time()
                total_time = end_time - start_time
                time.sleep(1)
        else:
            print("Automation is stuck; checking for errors...")
            error_status = check_for_errors()
            if not error_status:
                reposition_island()
                file_status = fix_automation(filename, confidence_level)
                if not file_status:
                    reposition_island()
            else:
                automation_status = False
            start_time = time.time()
            total_time = 0
            time.sleep(1)
            print(f"Looking for {filename} with a confidence of {confidence_level}...")


def check_for_errors():
    time.sleep(1)
    try:
        if pyautogui.center(pyautogui.locateOnScreen('connection_error.png', confidence=0.9)):
            print("Internet connection error detected!")
            time.sleep(1)
            try_again_button = pyautogui.center(pyautogui.locateOnScreen('./Images/try_again_button.png', confidence=0.9))
            time.sleep(1)
            pyautogui.moveTo(try_again_button)
            time.sleep(1)
            pyautogui.click()
    except:
        try:
            if pyautogui.center(pyautogui.locateOnScreen('./Images/apology_message.png', confidence=0.9)):
                print("Problem error detected!")
                time.sleep(1)
                continue_button = pyautogui.center(pyautogui.locateOnScreen('./Images/continue_button.png', confidence=0.9))
                time.sleep(1)
                pyautogui.moveTo(continue_button)
                time.sleep(1)
                pyautogui.click()
        except:
            return False
    check_screen_after_loading_screen()
    reposition_island()
    return True


def reposition_island():
    time.sleep(1)
    if pyautogui.locateOnScreen('./Images/mythic_hall.png', confidence=0.5):
        try:
            home_portal = pyautogui.center(pyautogui.locateOnScreen('./Images/mythic_hall.png', confidence=0.5))
            pyautogui.click(home_portal)
        except:
            pass
    else:
        while True:
            try:
                if pyautogui.locateOnScreen('./Images/breeding_island.png', confidence=0.5):
                    print("1")
                    breeding_island = pyautogui.center(pyautogui.locateOnScreen('./Images/breeding_island.png', confidence=0.3))
                    pyautogui.moveTo(breeding_island)
                    time.sleep(1)
                    calculate_proper_drag(breeding_island.x, breeding_island.y, True)
                    time.sleep(1)
                    pyautogui.keyDown('up')
                    time.sleep(0.6)
                    pyautogui.keyUp('up')
                    time.sleep(1)
                    mythic_hall = pyautogui.center(pyautogui.locateOnScreen('./Images/mythic_hall.png', confidence=0.5))
                    pyautogui.click(mythic_hall)
                    return True
                elif pyautogui.locateOnScreen('./Images/zoomed_out_breeding_island.png', confidence=0.7):
                    print("2")
                    zoomed_out_breeding_island = pyautogui.center(pyautogui.locateOnScreen('./Images/zoomed_out_breeding_island.png', confidence=0.5))
                    pyautogui.moveTo(zoomed_out_breeding_island)
                    time.sleep(1)
                    calculate_proper_drag(zoomed_out_breeding_island.x, zoomed_out_breeding_island.y, False)
                    time.sleep(1)
                    pyautogui.keyDown('up')
                    time.sleep(0.9)
                    pyautogui.keyUp('up')
                    time.sleep(1)
                    zoomed_out_mythic_hall = pyautogui.center(pyautogui.locateOnScreen('./Images/zoomed_out_mythic_hall.png', confidence=0.5))
                    pyautogui.click(zoomed_out_mythic_hall)
                    return True
                else:
                    print("3")
                    time.sleep(1)
                    pyautogui.keyDown('down')
                    time.sleep(0.2)
                    pyautogui.keyUp('down')
                    time.sleep(1)
            except:
                return False


def get_tuple_index(current_file, file_confidence):
    for index, file in enumerate(automation_series):
        if file[0] == current_file and file[1] == file_confidence:
            return index
        else:
            pass


def fix_automation(file, confidence):
    time.sleep(1)
    current_index = get_tuple_index(file, confidence)
    try:
        previous_file = automation_series[current_index - 1]
        previous_confidence = previous_file[1] - 0.1
        previous_element = pyautogui.center(pyautogui.locateOnScreen(previous_file[0], confidence=previous_confidence))
        print("Automation got stuck on previous file, fixing it...")
        pyautogui.moveTo(previous_element)
        time.sleep(0.5)
        pyautogui.click(previous_element)
        return True
    except TypeError:
        # for prior_file, prior_confidence in reversed(automation_series[:current_index - 2]):
        #     wait_until_element_appears(prior_file, prior_confidence, click_option=True)
        return False


def event_currency_automation():
    while True:
        for file, confidence in automation_series:
            wait_until_element_appears(file, confidence_level=confidence, click_option=True)


def calculate_proper_drag(current_x, current_y, found_island: bool):
    if found_island is True:
        island_center = (685, 475)
        # find_current_screen()
        x_difference = island_center[0] - current_x
        y_difference = island_center[1] - current_y
        pyautogui.drag(x_difference, y_difference, 3)
        pass
    else:
        zoomed_out_island_center = (595, 535)
        # find_current_screen()
        x_difference = zoomed_out_island_center[0] - current_x
        y_difference = zoomed_out_island_center[1] - current_y
        pyautogui.drag(x_difference, y_difference, 3)
        pass


if __name__ == "__main__":
    event_currency_automation()

