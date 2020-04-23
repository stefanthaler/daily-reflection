from PyInquirer import  Separator

pwd_questions = [
    {
        'type': 'password',
        'message': 'Enter your encryption key',
        'name': 'password'
    }
]

new_pwd_questions = [
    {
        'type': 'password',
        'message': 'Enter your new encryption key',
        'name': 'password'
    }
]

repeat_new_pwd_questions = [
    {
        'type': 'password',
        'message': 'Repeat your new encryption key',
        'name': 'password'
    }
]

main_menu_questions = [
    {
        'message': 'What do you want to do?',
        'name': 'mm_action',
        'type': 'list',
        'default':'r',
        'choices': [
            {"key":"r","name":"Reflection", "value":"Reflection"},
            Separator(),
            {"key":"a","name":"Add Questions", "value":"Add Questions"},
            {"key":"m","name":"Modify Questions", "value":"Modify Questions"},
            {"key":"o","name":"Change Question Order", "value":"Change Question Order"},
            {"key":"d","name":"Delete Questions", "value":"Delete Questions"},
            Separator(),
            {"key":"c","name":"Change Password", "value":"Change Password"},
            {"key":"b","name":"Browse", "value":"Browse"},
            {"key":"e","name":"Export", "value":"Export"},
            Separator(),
            {"key":"q","name":"Quit", "value":"Quit"},
        ]
    },
]
time_questions = [{
    'type': 'list',
    'name': 'time',
    'message': 'Morning/Evening?',
    'choices': [
        'Morning', # TODO refactor to create enum
        'Evening',
        'Back'
    ]
}]

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
