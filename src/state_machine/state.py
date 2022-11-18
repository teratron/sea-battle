class State:
    state_machine = None
    state_parent = None

    def __init__(self, state):
        # yield (owner, "ready")
        # state_parent = get_parent()
        # assert state_parent != None, 'Hello'
        pass

    def input(self, _event) -> None:
        return

    def unhandled_input(self, _event) -> None:
        return

    def unhandled_key_input(self, _event) -> None:
        return

    def process(self, _delta: float) -> None:
        return

    def physics_process(self, _delta: float) -> None:
        return

    # Called by the state machine upon changing the active state. The `msg` parameter
    # is a dictionary with arbitrary data the state can use to initialize itself.
    def enter(self, _msg: dict = {}) -> None:
        return

    # Called by the state machine before changing the active state. Use this function
    # to clean up the state.
    def exit(self) -> None:
        return
