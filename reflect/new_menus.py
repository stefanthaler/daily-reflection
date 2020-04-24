from prompt_toolkit import prompt
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

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
        session.prompt(key_bindings=bindings)






# colorise output
