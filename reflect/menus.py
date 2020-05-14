from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import PromptSession
from reflect.style import *

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


def key_press_menu(menu_items):
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
        if not key_pressed in menu_items:
            clear_screen()
            continue
        else:
            loop=False

    return key_pressed

def time_menu():
    items = {
        "title":{"text":"Which type of reflection do you want to do?"},
        "m":{"text":"Morning", "handler": quit},
        "e":{"text":"Evening", "handler": quit },
        "b":{"text":"Back", "handler": quit },
    }
    return items[key_press_menu(items)]["text"]

def browse_menu():
    items = {
        "title":{"text":"What do you want to do?"},
        "n":{"text":"Next day", "handler": quit},
        "p":{"text":"Previous day", "handler": quit },
        "g":{"text":"Goto day", "handler": quit },
        "b":{"text":"Back to main menu", "handler": quit },
    }
    return key_press_menu(items)
