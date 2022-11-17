class State:
	state_machine = None
	state_parent = None

	def _ready():
		yield (owner, "ready")
		state_parent = get_parent()
		assert state_parent != None, 'Hello'

	def input(_event) -> None:
		pass

	def unhandled_input(_event) -> None:
		pass

	def unhandled_key_input(_event) -> None:
		pass

	def process(_delta: float) -> None:
		pass

	def physics_process(_delta: float) -> None:
		pass

	# Called by the state machine upon changing the active state. The `msg` parameter
	# is a dictionary with arbitrary data the state can use to initialize itself.
	def enter(_msg: dict = {}) -> None:
		pass

	# Called by the state machine before changing the active state. Use this function
	# to clean up the state.
	def exit() -> None:
		pass
