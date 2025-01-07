import cv2
import time
import pyautogui
# import pydirectinput
# import win32api
# from win32con import *

account_list = []
account_1_park_coords = [
    ('instance_1_account#2.png', 0.9),
    ('instance_1_account#3.png', 0.9),
    ('instance_1_account#4.png', 0.9),
    ('instance_1_account#5.png', 0.9),
    ('instance_1_account#6.png', 0.9),
    ('instance_1_account#7.png', 0.9),
    ('instance_1_account#8.png', 0.9),
    ('instance_1_account#9.png', 0.9),
    ('instance_1_account#10.png', 0.9),
    ('instance_1_account#11.png', 0.9),
    ('instance_1_account#12.png', 0.9),
    ('instance_1_account#13.png', 0.9),
    ('instance_1_account#14.png', 0.9),
    ('instance_1_account#15.png', 0.9),
    ('instance_1_account#16.png', 0.9),
    ('instance_1_account#17.png', 0.9),
    ('instance_1_account#18.png', 0.9),
    ('instance_1_account#19.png', 0.9),
    ('instance_1_account#20.png', 0.9),
    ('instance_1_account#1.png', 0.9)
]

account_2_park_coords = [
    ('instance_2_account#2.png', 0.9),
    # ('instance_2_account#3.png', 0.9),
    ('instance_2_account#4.png', 0.9),
    ('instance_2_account#5.png', 0.9),
    ('instance_2_account#6.png', 0.9),
    ('instance_2_account#7.png', 0.9),
    ('instance_2_account#8.png', 0.9),
    ('instance_2_account#9.png', 0.9),
    ('instance_2_account#10.png', 0.9),
    ('instance_2_account#11.png', 0.9),
    ('instance_2_account#12.png', 0.9),
    ('instance_2_account#13.png', 0.9),
    ('instance_2_account#14.png', 0.9),
    ('instance_2_account#15.png', 0.9),
    ('instance_2_account#1.png', 0.9)
]


def get_mouse_position():
    while True:
        print(pyautogui.position())
        time.sleep(1)


def find_current_screen(filename='./Images/current_screen.png'):
    pyautogui.moveTo(1500, 750)
    pyautogui.screenshot(filename, region=(0, 160, 1334, 747))


def check_for_errors():
    time.sleep(1)
    try:
        if pyautogui.center(pyautogui.locateOnScreen('./Images/connection_error_message.png', confidence=0.9)):
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
            pass


def find_dv_account(filename, confidence_level=0.9, click_option=False):
    while True:
        try:
            park = pyautogui.center(pyautogui.locateOnScreen(filename, confidence=confidence_level))
            print(f"{filename} was located, resuming automation...")
            if click_option:
                time.sleep(3)
                pyautogui.click(park)
                print(f"{filename} was clicked, resuming automation...")
            else:
                pyautogui.moveTo(park)
                print(f"The cursor moved to {filename}'s position on the screen...")
            time.sleep(3)
            break
        except TypeError:
            check_for_errors()
            time.sleep(3)
            pyautogui.moveTo(669, 408)
            time.sleep(3)
            pyautogui.scroll(-15)
            time.sleep(3)
            try:
                deny_load_button = pyautogui.center(pyautogui.locateOnScreen('./Images/no_button.png'))
                time.sleep(3)
                pyautogui.click(deny_load_button)
                print(f"Stopped automated scrolling from loading wrong park...")
                time.sleep(3)
            except:
                check_for_errors()
                time.sleep(3)
                print(f"No miss click happened when scrolling for {filename}...")
                pass


def compare_image(image_1, image_2):
    minimum_commutative_image_diff = 0.05
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


def wait_until_element_appears(filename, confidence_level=0.9, click_option=False):
    if filename != './Images/free_gift_button.png' and filename != './Images/friends_button.png':
        find_current_screen('./Images/automation_start_screen.png')
    automation_status = True
    start_time = time.time()
    total_time = 0
    while automation_status is True:
        if total_time <= 30:
            try:
                element = pyautogui.center(pyautogui.locateOnScreen(filename, confidence=confidence_level))
                print(f"{filename} was located, resuming automation...")
                if click_option:
                    time.sleep(3)
                    pyautogui.moveTo(element)
                    time.sleep(3)
                    pyautogui.click()
                    print(f"{filename} was clicked, resuming automation...")
                    time.sleep(3)
                    if filename != './Images/free_gift_button.png' and filename != './Images/friends_button.png':
                        time.sleep(5)
                        find_current_screen()
                        if compare_image('./Images/automation_start_screen.png', 'current_screen.png'):
                            print("TRUE")
                            automation_status = True
                        else:
                            print("FALSE")
                            automation_status = False
                    else:
                        automation_status = False
                else:
                    pyautogui.moveTo(element)
                    print(f"The cursor moved to {filename}'s position on the screen...")
                    time.sleep(3)
                    break
            except TypeError:
                end_time = time.time()
                total_time = end_time - start_time
                check_for_errors()
                time.sleep(1)
        else:
            confidence_level -= 0.1
            start_time = time.time()
            total_time = 0


def wait_after_loading_screen():
    print("Checking if x_button is present or the Daily Rewards screen is...")
    while True:
        try:
            x_button = pyautogui.center(pyautogui.locateOnScreen('./Images/x_button.png', confidence=0.8))
            time.sleep(3)
            pyautogui.click(x_button)
            print("x_button has been clicked, resuming automation as the Daily Rewards screen is present...")
            break
        except:
            try:
                collect_button = pyautogui.center(pyautogui.locateOnScreen('./Images/collect_button.png'))
                time.sleep(3)
                pyautogui.moveTo(collect_button)
                print("The cursor moved to the collect_button's position on the Daily Rewards screen...")
                break
            except:
                check_for_errors()
                time.sleep(1)


def check_screen_after_loading_screen():
    wait_until_element_appears('./Images/market_button.png', click_option=False)
    try:
        time.sleep(10)
        if pyautogui.center(pyautogui.locateOnScreen('./Images/x_button.png', confidence=0.7)):
            time.sleep(3)
            x_button = pyautogui.center(pyautogui.locateOnScreen('./Images/x_button.png', confidence=0.7))
            print("1st X found...")
            time.sleep(3)
            pyautogui.click(x_button)
            time.sleep(10)
            if pyautogui.center(pyautogui.locateOnScreen('./Images/x_button.png', confidence=0.7)):
                time.sleep(3)
                x_button = pyautogui.center(pyautogui.locateOnScreen('./Images/x_button.png', confidence=0.7))
                print("2nd X found...")
                time.sleep(3)
                pyautogui.click(x_button)
    except:
        print("No messages popped up...")
        pass


def run_automation(dv_instance, threshold):
    wait_after_loading_screen()
    # ok_button = pyautogui.center(pyautogui.locateOnScreen('ok_button.png', confidence=0.9))
    # time.sleep(3)
    # pyautogui.click(ok_button)
    # time.sleep(5)
    wait_until_element_appears('./Images/multitasking_button.png', click_option=True)
    # multitasking_button = pyautogui.center(pyautogui.locateOnScreen('multitasking_button.png', confidence=0.9))
    # time.sleep(3)
    # pyautogui.click(multitasking_button)
    # time.sleep(5)
    wait_until_element_appears('./Images/clear_all_button.png', click_option=True)
    # clear_all_button = pyautogui.center(pyautogui.locateOnScreen('clear_all_button.png', confidence=0.9))
    # time.sleep(3)
    # pyautogui.click(clear_all_button)
    # time.sleep(3)
    wait_until_element_appears('./Images/game_icon.png', click_option=True)
    # game_icon = pyautogui.center(pyautogui.locateOnScreen('game_icon.png', confidence=0.9))
    # time.sleep(3)
    # pyautogui.click(game_icon)
    # wait_until_element_appears('loading_bar.png', 0.7)
    # time.sleep(60)
    check_screen_after_loading_screen()
    # wait_until_element_appears('x_button.png', click_option=True)
    # try:
    #     time.sleep(10)
    #     if pyautogui.center(pyautogui.locateOnScreen('x_button.png', confidence=0.7)):
    #         time.sleep(3)
    #         x_button = pyautogui.center(pyautogui.locateOnScreen('x_button.png', confidence=0.7))
    #         print("2nd X found...")
    #         time.sleep(3)
    #         pyautogui.click(x_button)
    # except:
    #     pass
    wait_until_element_appears('./Images/socials_button.png', click_option=True)
    # socials_button = pyautogui.center(pyautogui.locateOnScreen('socials_button.png', confidence=0.9))
    # time.sleep(3)
    # pyautogui.click(socials_button)
    # time.sleep(5)
    wait_until_element_appears('./Images/friends_button.png', click_option=True)
    # friends_button = pyautogui.center(pyautogui.locateOnScreen('friends_button.png', confidence=0.9))
    # time.sleep(3)
    # pyautogui.click(friends_button)
    # time.sleep(3)
    wait_until_element_appears('./Images/free_gift_button.png', click_option=True)
    # free_gift_button = pyautogui.locateOnScreen('free_gift_button.png', confidence=0.9)
    # time.sleep(3)
    # pyautogui.click(free_gift_button)
    # time.sleep(3)
    wait_until_element_appears('./Images/x_button.png', confidence_level=0.7, click_option=True)
    # x_button = pyautogui.center(pyautogui.locateOnScreen('x_button_1.png', confidence=0.5))
    # time.sleep(3)
    # pyautogui.click(x_button)
    # time.sleep(3)
    wait_until_element_appears('./Images/options_button.png', confidence_level=0.7, click_option=True)
    # options_button = pyautogui.center(pyautogui.locateOnScreen('options_button.png', confidence=0.9))
    # time.sleep(3)
    # pyautogui.click(options_button)
    # time.sleep(3)
    wait_until_element_appears('./Images/switch_park_button.png', click_option=True)
    # switch_park_button = pyautogui.center(pyautogui.locateOnScreen('switch_park_button.png', confidence=0.9))
    # time.sleep(3)
    # pyautogui.click(switch_park_button)
    # time.sleep(3)
    wait_until_element_appears("./Images/google_sign_in_button.png")
    find_dv_account(dv_instance, confidence_level=threshold, click_option=True)
    wait_until_element_appears('./Images/yes_button.png', click_option=True)


def gem_farm_account_1():
    print("Taking a screenshot of the desktop...")
    find_current_screen()
    while True:
        try:
            time.sleep(3)
            print("SEARCHING!")
            bluestacks_mi_opener = pyautogui.center(pyautogui.locateOnScreen('./Images/bluestacks_mi.png', confidence=0.9))
            pyautogui.doubleClick(bluestacks_mi_opener)
            break
        except:
            time.sleep(3)
            pyautogui.hotkey('win', 'd')
            pass
    print("Locating account...")
    wait_until_element_appears('./Images/start_button.png')
    for pos in pyautogui.locateAllOnScreen('./Images/start_button.png', confidence=0.9):
        account_list.append(pos)
    time.sleep(3)
    pyautogui.click(account_list[0])
    wait_until_element_appears('./Images/game_icon.png', click_option=True)
    for park_account, confidence_threshold in account_1_park_coords:
        run_automation(park_account, confidence_threshold)


def gem_farm_account_2():
    print("Closing the first instance gem farm...")
    wait_until_element_appears('./Images/close_instance_button.png', click_option=True)
    wait_until_element_appears('./Images/close_button.png', click_option=True)
    while True:
        try:
            time.sleep(3)
            print("SEARCHING!")
            bluestacks_mi_opener = pyautogui.center(pyautogui.locateOnScreen('./Images/bluestacks_mi.png', confidence=0.9))
            pyautogui.doubleClick(bluestacks_mi_opener)
            break
        except:
            time.sleep(3)
            pyautogui.hotkey('win', 'd')
            pass
    time.sleep(3)
    pyautogui.click(account_list[1])
    wait_until_element_appears('./Images/game_icon.png', click_option=True)
    for park_account, confidence_threshold in account_2_park_coords:
        run_automation(park_account, confidence_threshold)


# time.sleep(5)
# pyautogui.moveTo(889, 765)
# time.sleep(3)
# pyautogui.scroll(-100)
# time.sleep(3)
# wait_until_element_appears('instance_1_account#3.png', 1.00)
# time.sleep(3)
# prev_dv_account_1 = pyautogui.center(pyautogui.locateOnScreen('instance_1_account#4.png'))
# time.sleep(3)
# pyautogui.moveTo(prev_dv_account_1)
# time.sleep(3)
# pyautogui.scroll(-400)
# time.sleep(5)
# dv_account = pyautogui.center(pyautogui.locateOnScreen('instance_1_account#10.png'))
# time.sleep(3)
# prev_dv_account_1 = pyautogui.center(pyautogui.locateOnScreen('instance_1_account#5.png', confidence=0.8))
# time.sleep(3)
# pyautogui.moveTo(prev_dv_account_1)
# time.sleep(3)
# for park_account, confidence_threshold in account_1_park_coords:
#     find_dv_account(park_account, confidence_threshold)
# find_dv_account('instance_1_account#2.png', 0.9)
# get_mouse_position
# gem_farm_account_1()
# gem_farm_account_2()
# wait_until_element_appears('multitasking_button.png', click_option=True)
# screenshot_region = [(0, 160), (0, 907), (1334, 907), (1333, 160)]
# pyautogui.screenshot('test.png', region=(0, 160, 1334, 747))
# find_dv_account('instance_1_account#9.png', confidence_level=0.98)
gem_farm_account_1()
gem_farm_account_2()
