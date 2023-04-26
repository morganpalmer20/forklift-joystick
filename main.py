def on_received_number(receivedNumber):
    global action
    action = receivedNumber
radio.on_received_number(on_received_number)

action = 0
joystickbit.init_joystick_bit()
radio.set_group(13)
basic.show_icon(IconNames.GHOST)

def on_forever():
    if joystickbit.get_button(joystickbit.JoystickBitPin.P12):
        radio.send_number(5)
    elif joystickbit.get_button(joystickbit.JoystickBitPin.P13):
        radio.send_number(6)
    else:
        pass
basic.forever(on_forever)

def on_forever2():
    if action == 5:
        wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 60)
    if action == 6:
        wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 0)
basic.forever(on_forever2)
