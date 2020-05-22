from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import PromptSession
from reflect.style import *
import os
from prompt_toolkit.shortcuts import clear



def get_menu(menu_items):
    message = []

    for k in menu_items:
        if "title" == k:
            message.append( ('class:title', menu_items[k]["text"]+"\n") )
            message.append(('class:separator',"="*20+"\n\n") )
            continue
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


def key_press_menu(menu_items, loop_display=""):
    bindings = KeyBindings()
    message = get_menu(menu_items)
    global key_pressed
    key_pressed = ""

    @bindings.add('c-m')
    @bindings.add('up')
    @bindings.add('escape')
    @bindings.add('down')
    @bindings.add('<any>')
    def _(event):
        event.app.exit()
        global key_pressed
        key_pressed=event.key_sequence[0].key

    session = PromptSession()
    loop = True
    current_key = 0
    key_positions = []
    for i, m in enumerate(message):
        if m[0]=="class:key":
            key_positions.append(i)

    while loop:
        print(loop_display)

        for k in key_positions:
            message[k]=('class:key', message[k][1])
            message[k+1]=('class:menu_item', message[k+1][1])
        message[key_positions[current_key]]=('class:current_key',message[key_positions[current_key]][1])
        message[key_positions[current_key]+1]=('class:current_key',message[key_positions[current_key]+1][1])

        session.prompt(message, style=style, key_bindings=bindings)
        if str(key_pressed)=="Keys.Up":
            if current_key>0:
                current_key=current_key-1
        if str(key_pressed)=="Keys.Down":
            if current_key<len(key_positions)-1:
                current_key=current_key+1

        if str(key_pressed)=="Keys.ControlM": # enter has been pressed
            key_pressed=message[key_positions[current_key]][1].split(")")[0][1:]

        if str(key_pressed)=="Keys.Escape": # enter has been pressed
            key_pressed="escape"
            loop=False
            return key_pressed

        if not key_pressed in menu_items:
            clear()
            continue
        else:
            loop=False
            break


    return key_pressed

def time_menu():
    items = {
        "title":{"text":"Which type of reflection do you want to do?"},
        "m":{"text":"Morning"},
        "e":{"text":"Evening"},
        "b":{"text":"Back"},
    }
    return items[key_press_menu(items)]["text"]

def menu_from_questions(questions, title, menu_generator=key_press_menu):
    items = {
        "title":{"text":title}
    }
    key_codes = [c for c in "123456789abcdefghijklmnoprstuvwxyz"]
    for i,q in enumerate(questions):
        items[key_codes[i]]={"text":q["text"]}
    items["--1"]={}
    items["q"]={"text":"Abort"}
    return menu_generator(items)



def browse_menu(day_string):
    items = {
        "title":{"text":"What do you want to do?"},
        "n":{"text":"Next day", "handler": quit},
        "p":{"text":"Previous day", "handler": quit },
        "g":{"text":"Goto day", "handler": quit },
        "b":{"text":"Back to main menu", "handler": quit },
    }
    return key_press_menu(items,day_string)
