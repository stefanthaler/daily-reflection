#!/usr/bin/python3


# https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, style_from_dict, Token, Separator, print_json, Separator
from examples import custom_style_2
from pprint import pprint
from tinydb import TinyDB, where, Query
from encrypted_json_storage import EncryptedJSONStorage
import sys
import os
import datetime
import uuid

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

def clear_screen():
    os.system('cls')
    os.system('clear')

pwd_questions = [
    {
        'type': 'password',
        'message': 'Enter your encryption key',
        'name': 'password'
    }
]


main_menu_questions = [
    {
        'type': 'rawlist',
        'name': 'mm_action',
        'message': 'What do you want to do?',
        'choices': [
            'Reflection',
            Separator(),
            'Add Questions',
            'Modify Questions',
            'Delete Questions',
            Separator(),
            'Quit'
        ]
    },
]
time_questions = [{
    'type': 'rawlist',
    'name': 'time',
    'message': 'Morning/Evening?',
    'choices': [
        'Morning',
        'Evening',
        'Back'
    ]
}]

# get password
clear_screen()
encryption_key = prompt(pwd_questions, style=custom_style_2)["password"]

try:
    db = TinyDB(encryption_key=encryption_key, path="./reflect.db", storage=EncryptedJSONStorage)
except:
    print("Error loading DB, probably wrong encryption key",sys.exc_info()[0], sys.exc_info()[1])
    sys.exit(0)

def today():
    return datetime.datetime.now().strftime("%Y%m%d")

def do_reflection(time, data_base):
    # load questions from database
    Questions = Query()
    questions = get_questions(time, data_base)
    # TODO check for empty questions
    if len(questions)==0:
        clear_screen()
        print("No questions for %s reflection. Add some questions.\n"%time )
        return

    #load answers for today if they are there
    Answers = Query()
    today = datetime.date.today().strftime("%Y%m%d")
    old_answers = data_base.search( (Answers.time == time) & (Answers.date==today) & (Answers.type=="reflection") )
    old_answers = (old_answers[0] if len(old_answers)>0 else {})

    # store answers for today in database
    ref_qs = []
    for i, q in enumerate(questions):
        ref_qs.append({
            'type': 'input',
            'name': q["id"],
            'default':  old_answers[q["id"]] if q["id"] in old_answers else "",#TODO load existing answers
            'message': q["text"].replace("?","") +  "?"
        })

    res = prompt(ref_qs)
    res["time"]=time
    res["type"]="reflection"
    res["date"]=today

    if len(old_answers)==0:
        data_base.insert(res)
    else:
        data_base.update(res, (Answers.time == time) & (Answers.date==today) & (Answers.type=="reflection") )
    print("%s-reflection stored.\n"%time)

def get_questions(time, data_base):
    Questions = Query()
    questions = data_base.search( Questions.time == time)
    if len(questions)==0:
        data_base.insert({'questions':questions, "time":time})
        questions=[]
    else:
        questions=[q for q in questions[0]["questions"] if not q["deleted"]]
    return questions


def add_questions(time, data_base):
    # load existing questions
    action=""
    while True:
        clear_screen()
        # get old questions
        questions=get_questions(time, data_base)
        print("Existing questions:")
        [print("\t"+q["text"]) for q in questions]
        print()

        # get new question
        add_question = [{
            'type': 'input',
            'name': 'new_question',
            'message': 'Which question do you want to add for your '+time+' reflection?'
        }]
        new_question_text=prompt(add_question)["new_question"]
        if not new_question_text[-1]=="?":
            new_question_text=new_question_text+"?"

        for q in questions:
            if new_question_text==q["text"]:
                clear_screen()
                print("Duplicate question '%s' not added."%new_question_text)
                return

        new_question={"text":new_question_text, "id":str(uuid.uuid4()), "deleted":False }
        questions += [ new_question ]
        #store new question
        Questions=Query()
        data_base.update({'questions':questions}, Questions.time == time)
        # prompt if you want to add more questions?
        continue_question = [{
            'type': 'rawlist',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': [
                'Add more questions',
                'Back'
            ]
        }]
        clear_screen()
        action = prompt(continue_question)["action"]
        if action=="Back":
            return

def delete_questions(time, data_base):
    # load existing questions
    action=""
    while True:
        clear_screen()
        # get old questions
        questions=get_questions(time, data_base)
        if (len(questions)==0):
            clear_screen()
            print("No questions for %s stored."%time )
            return
        # get new question
        delete_question = [{
            'type': 'rawlist',
            'name': 'action',
            'message': 'Which question do you want to delete from your '+time+' reflection?',
            'choices': [q["text"] for q in questions] + [
                Separator(),
                "Abort"
            ]
        }]
        delete_action=prompt(delete_question)["action"]

        if delete_action == "Abort":
            clear_screen()
            print("Aborted deleting.\n")
            return

        # delete data
        for q in questions:
            if q["text"] == delete_action:
                q["deleted"]=True

        Questions = Query()
        data_base.update({'questions':questions}, Questions.time == time)
        clear_screen()
        print("Question for %s reflection deleted .\n"%time)

        # prompt if you want to add more questions?
        continue_question = [{
            'type': 'rawlist',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': [
                'Delete more questions',
                'Back'
            ]
        }]
        action = prompt(continue_question)["action"]
        if action=="Back":
            return

def modify_questions(time, data_base):
    # load existing questions
    action=""
    while True:
        clear_screen()
        # get old questions
        Questions = Query()
        questions = get_questions(time, data_base)
        if (len(questions)==0):
            clear_screen()
            print("No questions for %s reflection stored."%time )
            return

        # get new question
        mod_question = [{
            'type': 'rawlist',
            'name': 'action',
            'message': 'Which question do you want to change in your '+time+' reflection?',
            'choices': [q["text"] for q in questions] + [
                Separator(),
                "Abort"
            ]
        }]
        mod_action=prompt(mod_question)["action"]

        if mod_action == "Abort":
            clear_screen()
            print("Aborted modification.\n")
            return

        # modify data
        # get new question
        mod_question = [{
            'type': 'input',
            'name': 'new_question',
            'message': 'New question:',
            'default':mod_action
        }]
        modified_question_text=prompt(mod_question)["new_question"]
        if not modified_question_text[-1]=="?":
            modified_question_text=modified_question_text+"?"

        for q in questions:
            if modified_question_text==q["text"]:
                clear_screen()
                print("Duplicate question, question not changed."%new_question_text)
                return

        for q in questions:
            if q["text"]==mod_action:
                q["text"]=modified_question_text

        data_base.update({'questions':questions}, Questions.time == time)
        clear_screen()
        #TODO proper messageb
        print("Question for %s reflection has been updated.\n"%time)

        # prompt if you want to add more questions?
        continue_question = [{
            'type': 'rawlist',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': [
                'Modify another question',
                'Back'
            ]
        }]
        action = prompt(continue_question)["action"]
        if action=="Back":
            return


action = ""
while True:
    action = prompt(main_menu_questions)["mm_action"]
    clear_screen()
    if action=="Quit": break

    time = prompt(time_questions)["time"]
    if time=="Back": continue

    if action=="Reflection":
        do_reflection(time, db)
    elif action=="Add Questions":
        add_questions(time, db)
    elif action=="Modify Questions":
        modify_questions(time, db)
    elif action=="Delete Questions":
        delete_questions(time, db)