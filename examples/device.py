from automaton import Automaton, Key
from automaton.consts import LockState

# Remember to change to your device path.
app = Automaton.new(devices = ['/dev/input/event6', '/dev/input/event5'])

# Access keyboard like so
# Press the left shift key, but do not release it.
app.device.press(Key.LShift)
app.device.release(Key.LShift) # Release the left shift key, if its pressed.

# You can press, release, or tap multiple keys at the same time:
app.device.press(Key.LCtrl, Key.LShift)
app.device.release(Key.LCtrl, Key.LShift)

app.device.tap(Key.LCtrl, Key.LShift)


app.device.tap(Key.LShift) # Presses and releases the left shift key
# NOTE: This method works only on Gtk apps. Use type_ascii for a general one. But the latter
# doesn't support unicode.
app.device.type("Hello, World!") # Types a string. Can be any utf-8 value.

app.device.is_pressed(Key.LShift) # Returns True if left shift is pressed.
app.device.is_toggled(Key.CapsLock) # Returns LockState.On if capslock is toggled on
app.device.set_state(Key.CapsLock, LockState.On) # Toggles the capslock on.

app.device.move_rel(100, 100) # Moves 100px Left and 100px Right. 

app.run()