from prompt_toolkit import prompt
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings


if __name__ == "__main__":
    bindings = KeyBindings()

    # @Condition
    # def is_active():
    #     " Only activate key binding on the second half of each minute. "
    #     return datetime.datetime.now().second > 30

    @bindings.add('c')
    def _(event):
        print(event)
        pass

    prompt('> ', key_bindings=bindings)
