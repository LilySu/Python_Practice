# waits for the user input. The user can press get number, where number is a floor where the passenger is located.

# one of the command line arguments is floor (the maximum number of floors in building).

# When the passenger is in the elevator he can push one or more buttons and the elevator should go to the nearest floor and so on.

# speed - the speed of the elevator
# doors - doors opening and closing speed
# floor_height - height of the floor
import argparse

parser = argparse.ArgumentParser(description='Run Elevator')
parser.add_argument('-e','--entered_floor', help='Floor coming from', type=int, metavar='', required=False)
parser.add_argument('-f','--floor', help='Floor to go to', type=int, metavar='', required=False)
args = parser.parse_args()

class Elevator:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor

    def hardware_functions(self):
        return "door open | sensor does not sense anything blocking door | door close"

    def elevator_movement(self, enter_floor, button_press):
        if enter_floor is None:
            enter_floor = self.current_floor
        led_display_panel = []
        for floor in range(enter_floor, button_press + 1):
            led_display_panel.append('ding ' + str(floor))
        return led_display_panel

    def go_to(self, enter_floor = 0 , button_press = 0):
        result = []
        hardware_response_start = self.hardware_functions()
        sound = self.elevator_movement(enter_floor, button_press)
        hardware_response_end = self.hardware_functions()
        result.append(hardware_response_start)
        result.append(sound)
        result.append(hardware_response_end)
        return result

if __name__ == '__main__':
    e = Elevator()
    print(e.go_to(args.entered_floor, args.floor))