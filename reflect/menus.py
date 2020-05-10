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

def add_question_ary(time):
    return [{
        'type': 'input',
        'name': 'new_question',
        'message': 'Which question do you want to add for your '+time+' reflection?'
    }]

continue_add_question = [{
    'type': 'rawlist',
    'name': 'action',
    'message': 'What do you want to do?',
    'choices': [
        'Add more questions',
        'Back'
    ]
}]

def delete_questions_ary(time, questions):
    return [{
        'type': 'rawlist',
        'name': 'action',
        'message': 'Which question do you want to delete from your '+time+' reflection?',
        'choices': [q["text"] for q in questions] + [
            Separator(),
            "Abort"
        ]
    }]

continue_delete_question = [{
    'type': 'rawlist',
    'name': 'action',
    'message': 'What do you want to do?',
    'choices': [
        'Delete more questions',
        'Back'
    ]
}]

def move_question_from(questions):
    return [{
        'type': 'rawlist',
        'name': 'action',
        'message': 'Which question do you want to move?',
        'choices': [q["text"] for q in questions] + [
            Separator(),
            "Abort"
        ]
    }]

def move_question_to(questions):
    return [{
        'type': 'rawlist',
        'name': 'action',
        'message': 'To which position do you want to move your question to?',
        'choices': [q["text"] for q in questions] + [
            Separator(),
            "Abort"
        ]
    }]

def mod_question(time, questions):
    return [{
        'type': 'rawlist',
        'name': 'action',
        'message': 'Which question do you want to change in your '+time+' reflection?',
        'choices': [q["text"] for q in questions] + [
            Separator(),
            "Abort"
        ]
    }]


def mod_question_to(mod_action):
    return [{
        'type': 'input',
        'name': 'new_question',
        'message': 'New question:',
        'default':mod_action
    }]

continue_mod_question = [{
    'type': 'rawlist',
    'name': 'action',
    'message': 'What do you want to do?',
    'choices': [
        'Modify another question',
        'Back'
    ]
}]

browse_question = [
    {
        'type': 'list',
        'name': 'action',
        'message': 'What do you want to do?',
        'choices': [
            'Previous Day',
            'Next Day',
            'Goto Day',
            'Back'
        ]
    }

]

browse_question_day = [
    {
        'type': 'input',
        'name': 'browse_date',
        'message': 'Which day do you want to view (format: "YYYYMMDD")?',
    }

]
