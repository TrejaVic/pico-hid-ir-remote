import pulseio
import board
import adafruit_irremote
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid


receiver = pulseio.PulseIn(board.GP15, maxlen=120, idle_state=True)


decoder = adafruit_irremote.GenericDecode()


keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
#To see your ir code just connect ir module, open serial and press buttons.
#Example of buttons (line 42)
w_code = (255, 0, 231, 24)#your ir code here
d_code = (255, 0, 165, 90)#your ir code here
a_code = (255, 0, 239, 16)#your ir code here
s_code = (255, 0, 181, 74)#your ir code here


#hold example (line 55)
shift_code = (255, 0, 199, 56)#your ir code here
shift_held = False

#shortcuts example/double button (line 87)
altf4_code = (255, 0, 87, 168)#your ir code here

while True:
    
    pulses = decoder.read_pulses(receiver)

    
    try:
        code = decoder.decode_bits(pulses)
        print("Received IR code: ", code)
        if code == w_code:
            keyboard.press(Keycode.W)
            keyboard.release(Keycode.W)
            # for release all buttons "keyboard.release_all()"
            
        elif code == d_code:
            keyboard.press(Keycode.D)
            keyboard.release(Keycode.D)
            
        elif code == a_code:
            keyboard.press(Keycode.A)
            keyboard.release(Keycode.A)
            
        elif code == s_code:
            keyboard.press(Keycode.S)
            keyboard.release(Keycode.S)
            
        elif code == shift_code:
            if shift_held:
                keyboard.release(Keycode.SHIFT)
                shift_held = False
            else:
                keyboard.press(Keycode.SHIFT)
                shift_held = True
                
        elif code == altf4_code:
            keyboard.press(Keycode.ALT, Keycode.F4)
            keyboard.release(Keycode.ALT, Keycode.F4)
        

    except adafruit_irremote.IRDecodeException:
        pass
