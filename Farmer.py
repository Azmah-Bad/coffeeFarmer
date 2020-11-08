import pyautogui
import time
import sys

INPUT_BOX = (525, 755)
EMOJI = (1076, 662)
SELECT_EMOJI = (704, 478)
VOTE_EMOJI = (490, 684)

COMMANDS = {"prep": "$course", "ready": "$ready", "start": "$start"}


def write(cmd):
    """
    write command in the channel
    :param cmd:
    :return:
    """
    pyautogui.moveTo(*INPUT_BOX)
    pyautogui.click()

    pyautogui.write(COMMANDS[cmd])
    pyautogui.press(['enter'])


def selectEmoji():
    pyautogui.moveTo(*EMOJI)
    pyautogui.click()

    pyautogui.moveTo(*SELECT_EMOJI)
    pyautogui.click()


def vote():
    """
    vote for the first emoji
    :return:
    """
    pyautogui.moveTo(*VOTE_EMOJI)
    pyautogui.click()


def farm():
    """
    farm 50 tc-dollar
    :return:
    """
    write("prep")
    selectEmoji()
    time.sleep(3)

    write("ready")
    vote()
    time.sleep(3)

    write("start")


