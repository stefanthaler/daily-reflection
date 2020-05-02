#!/usr/bin/python3


# https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df

from __future__ import print_function, unicode_literals
from pprint import pprint
from tinydb import TinyDB, where, Query
import tinydb_encrypted_jsonstorage as tae
from reflect.menus import *
from reflect.actions import *
import sys
import os
import datetime
import uuid # creating unique id's for storage
from pathlib import Path # for finding user's home
# colorise output
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style

from prompt_toolkit import prompt
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

VERSION="0.2.0"

def get_menu(menu_items):
    message = []
    for k in menu_items:
        if "==" in k:
            message.append( ('class:separator', "="*20+"\n" ) )
            continue

        if "--" in k:
            message.append( ('class:separator', "-"*20+"\n"  ) )
            continue


        m=menu_items[k]
        message.append( ('class:key', "(%s) " %k) )
        message.append( ('class:menu_item'   , "%s \n"%m["text"]) )
    return message


def no_enter_menu(menu_items):
    bindings = KeyBindings()
    message = get_menu(menu_items)
    global key_pressed
    key_pressed = ""

    @bindings.add('<any>')
    def _(event):
        event.app.exit()
        global key_pressed
        key_pressed=event.key_sequence[0].data

    session = PromptSession()
    loop = True
    while loop:
        session.prompt(message, style=style, key_bindings=bindings)
        loop = menu_items[key_pressed]["handler"]()

style = Style.from_dict({
    # User input (default text).
    '':          '#ff0066',

    'key': '#FFC107', #material amber
    'menu_item':'#FFF',
    'separator': '#FFF',
})

from prompt_toolkit import prompt
import getpass




# get password
clear_screen()
print("Daily Reflection, v%s"%VERSION)

# TODO password prompt
encryption_key = prompt('Enter password: ', is_password=True)

try:
    from os.path import join as join_path
    db = TinyDB(encryption_key=encryption_key, path=join_path(str(Path.home()),".reflect.db"), storage=tae.EncryptedJSONStorage)
except:
    print("Error loading DB, probably wrong encryption key",sys.exc_info()[0], sys.exc_info()[1])
    sys.exit(0)





def quit():
    return False

def reflection_menu():
    main_menu_items = {
        "r":{"text":"Do reflection", "handler": quit  },
        "--1":{},
        "a":{"text":"Add questions", "handler": quit },
        "m":{"text":"Modify questions", "handler": quit },
        "o":{"text":"Change questions order", "handler": quit },
        "d":{"text":"Delete questions", "handler": quit },
        "--2":{},
        "p":{"text":"Change password", "handler": quit },
        "b":{"text":"Browse questions", "handler": quit },
        "e":{"text":"Export reflections", "handler": quit },
        "--3":{},
        "q":{"text":"Quit", "handler": quit }
    }
    no_enter_menu(menu_items=main_menu_items)




# def reflection_menu():
#     action = "" # action has to be the same as the name of the action TODO refactor
#     while True:
#         action = prompt(main_menu_questions, style=custom_style_2)["mm_action"]
#         view_day(today(), db)
#         clear_screen()
#         if action=="Quit": break
#         if action=="Change Password":
#             change_password(db)
#             continue
#         if action== "Export":
#             export(db)
#             continue
#         if action== "Browse":
#             browse( today(), db )
#             continue
#
#
#         # Time based questions
#         time = prompt(time_questions)["time"]
#         if time=="Back":
#             continue
#
#         if action=="Reflection":
#             do_reflection(time, db)
#         elif action=="Add Questions":
#             add_questions(time, db)
#         elif action=="Modify Questions":
#             modify_questions(time, db)
#         elif action=="Change Question Order":
#             change_order(time, db)
#         elif action=="Delete Questions":
#             delete_questions(time, db)
