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

    # Prompt.
    'username': '#884444',
    'at':       '#00aa00',
    'colon':    '#0000aa',
    'pound':    '#00aa00',
    'host':     '#00ffff bg:#444400',
    'path':     'ansicyan underline',
})

message = [
    ('class:username', 'johndo'),
    ('class:at',       '@'),
]



if __name__ == "__main__":
    bindings = KeyBindings()

    # @Condition
    # def is_active():
    #     " Only activate key binding on the second half of each minute. "
    #     return datetime.datetime.now().second > 30

    @bindings.add('<any>')
    def _(event):
        print(event)
        pass
    # @bindings.add('c-m')
    # def _(event):
    #     print("Enter",event)
    #     pass
# wait for keypress
    session = PromptSession()
    while True:
        session.prompt(message, style=style, key_bindings=bindings)
