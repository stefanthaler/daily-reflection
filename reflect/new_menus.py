from prompt_toolkit import prompt
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout


# colorise output
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style

style = Style.from_dict({
    # User input (default text).
    '':          '#ff0066',

    'key': '#FFC107', #material amber
    'menu_item':'#FFF',
    'separator': '#FFF',
})

# message = [
#     ('class:username', 'johndo'),
#     ('class:at',       '@'),
# ]
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


def quit():
    return False

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


no_enter_menu(menu_items=main_menu_items)
