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
})

# message = [
#     ('class:username', 'johndo'),
#     ('class:at',       '@'),
# ]
def get_menu(menu_items):
    message = []
    for m in menu_items:
        message.append( ('class:key', "(%s) " %m["key"]) )
        message.append( ('class:menu_item'   , "%s \n"%m["text"]) )
    return message

global test
test = {}

def main_menu():
    bindings = KeyBindings()

    menu_items = [
        {"key":"r", "text":"Do reflection"},
        {"key":"a", "text":"Add Questions"},
        {"key":"q", "text":"Quit"}
    ]
    message = get_menu(menu_items)

    @bindings.add('<any>')
    def _(event):
        print("here",event)
        #key_pressed = event.key
        event.app.exit()
        global test
        test["event"]=event



    session = PromptSession()
    while True:
        session.prompt(message, style=style, key_bindings=bindings)
        print("here2",session.app)
        global test
        print(test)


main_menu()
