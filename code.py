import pulseio
import board
import adafruit_irremote
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid


receiver = pulseio.PulseIn(board.GP0, maxlen=240, idle_state=True)


decoder = adafruit_irremote.GenericDecode()


keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)


target_code_1 = (255, 0, 93, 162)
target_code_2 = (255, 0, 157, 98)
target_code_3 = (255, 0, 103, 152)
target_code_4 = (255, 0, 151, 104)
target_code_5 = (255, 0, 79, 176)
target_code_6 = (255, 0, 29, 226)
w_code = (255, 0, 231, 24)
d_code = (255, 0, 165, 90)
a_code = (255, 0, 239, 16)
s_code = (255, 0, 181, 74)
z_button = (255, 0, 199, 56)
shift_held = False 
ctrl_held = False
w_held = False
d_held = False
a_held = False
s_held = False

while True:
    
    pulses = decoder.read_pulses(receiver)

    
    try:
        code = decoder.decode_bits(pulses)
        print("Alınan IR kodu:", code)  
        if code == target_code_1:
            keyboard.press(Keycode.SPACE)
            keyboard.release(Keycode.SPACE)
            time.sleep(0.1) 
        elif code == target_code_2:
            if shift_held:
                keyboard.release(Keycode.SHIFT)
                shift_held = False
            else:
                keyboard.press(Keycode.SHIFT)
                shift_held = True
        elif code == target_code_3:
            keyboard.press(Keycode.ALT, Keycode.F4)
            keyboard.release_all()
        elif code == target_code_4:
            keyboard.press(Keycode.ENTER)
            keyboard.release(Keycode.ENTER)
            keyboard.press(Keycode.S, Keycode.A)
            keyboard.release_all()
            keyboard.press(Keycode.ENTER)
            keyboard.release_all()
        elif code == target_code_5:
            keyboard.release_all()
        elif code == target_code_6:
            if ctrl_held:
                keyboard.release(Keycode.LEFT_CONTROL)
                ctrl_held = False
            else:
                keyboard.press(Keycode.LEFT_CONTROL)
                ctrl_held = True
        elif code == w_code:
            if w_held:
                keyboard.release(Keycode.W)
                w_held = False
            else:
                keyboard.press(Keycode.W)
                w_held = True

        elif code == a_code:
            if a_held:
                keyboard.release(Keycode.A)
                a_held = False
            else:
                keyboard.press(Keycode.A)
                a_held = True
        elif code == d_code:
            if d_held:
                keyboard.release(Keycode.D)
                d_held = False
            else:
                keyboard.press(Keycode.D)
                d_held = True
        elif code == s_code:
            if s_held:
                keyboard.release(Keycode.S)
                s_held = False
            else:
                keyboard.press(Keycode.S)
                s_held = True
        elif code == z_button:
            keyboard.press(Keycode.Z)
            keyboard.release(Keycode.Z)

    except adafruit_irremote.IRDecodeException:
        pass
