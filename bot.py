import time
import d
from random import randint
from pynput.keyboard import Key, Controller
import keyboard
import main
from math import floor

print()

kb = Controller()
count = -1
hold_i_cs = -1

def send_message():
    global count
    global iterations
    global hold_i_cs
    if (count == iterations or count == -1):
        index_cs = randint(0, len(d.cs) - 1)
        index_d = randint(0, len(d.descriptors) - 1)
        index_t = randint(0, len(d.topics) - 1)

        if (hold_i_cs == index_cs): 
            send_message()
            return

        kb.type(d.cs[index_cs].format(d=d.descriptors[index_d], t=d.topics[index_t]))

        kb.press(Key.enter)
        kb.release(Key.enter)

        if count == -1: count = 1
        else: count = 0

        hold_i_cs = index_cs

    else: count += 1

def begin():
    global count
    global iterations

    time.sleep(seconds_until_start)

    while (keyboard.is_pressed('`') == False):
        send_message()
        print("\033[F\033[2K0{0} min : {1} sec".format(floor(((iterations-count)/10)/60), floor(((iterations-count)/10)%60)))
        time.sleep(0.1)

    time.sleep(2)

def begin_faster():
    global count
    time.sleep(seconds_until_start)

    while (keyboard.is_pressed('`') == False):
        send_message()

    time.sleep(2)

seconds_until_start = main.seconds_until_start

iterations = main.iterations
if (iterations == -1): iterations = (2 + (randint(0, 10) * 0.1)) * 600

#begin()
begin_faster()

print("\033[F\033[2KDone!")