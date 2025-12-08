import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

# ---------------------------
#  GPIO pins GP1–GP8
# ---------------------------
PINS = [
    board.D1,  # GP1 - Bottom Left  (Shift)
    board.D2,  # GP2 - Bottom Mid1  (A)
    board.D3,  # GP3 - Bottom Mid2  (S)
    board.D4,  # GP4 - Bottom Right (D)
    board.D5,  # GP5 - Top Left     (Ctrl)
    board.D6,  # GP6 - Top Mid1     (V)
    board.D7,  # GP7 - Top Mid2     (W)
    board.D8,  # GP8 - Top Right    (Z)
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# ---------------------------
#  Keymap (matches pin order)
# ---------------------------
keyboard.keymap = [
    [
        KC.LSHIFT,   # Bottom Left
        KC.A,        # Bottom Mid1
        KC.S,        # Bottom Mid2
        KC.D,        # Bottom Right

        KC.LCTRL,    # Top Left
        KC.V,        # Top Mid1
        KC.W,        # Top Mid2
        KC.Z,        # Top Right
    ]
]

if __name__ == '__main__':
    keyboard.go()
