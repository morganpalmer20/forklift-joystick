radio.onReceivedNumber(function (receivedNumber) {
    action = receivedNumber
})
let action = 0
joystickbit.initJoystickBit()
radio.setGroup(13)
basic.showIcon(IconNames.Ghost)
basic.forever(function () {
    if (joystickbit.getButton(joystickbit.JoystickBitPin.P12)) {
        radio.sendNumber(5)
    } else if (joystickbit.getButton(joystickbit.JoystickBitPin.P13)) {
        radio.sendNumber(6)
    } else {
    	
    }
})
basic.forever(function () {
    if (action == 5) {
        wuKong.setServoAngle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 60)
    }
    if (action == 6) {
        wuKong.setServoAngle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 0)
    }
})
