import state


class StateMachine:
    pass


# signal transitioned(state_name)

# export var initial_state := NodePath("/root/World/Player/ActionPlayer")
# onready var state: State = get_node(initial_state)

state: state.State


def _ready():
    yield (owner, "ready")

    for child in get_children():
        child.state_machine = self

    if state != None:
        state.enter()


def _input(event):
    state.input(event)


def _unhandled_input(event):
    state.unhandled_input(event)


def _unhandled_key_input(event):
    state.unhandled_key_input(event)


def _process(delta):
    state.process(delta)


def _physics_process(delta):
    state.physics_process(delta)


def transition_to(target_state_name: str, msg: dict = {}) -> None:
    if not has_node(target_state_name):
        return

    state.exit()
    state = get_node(target_state_name)
    state.enter(msg)
    emit_signal("transitioned", state.name)
