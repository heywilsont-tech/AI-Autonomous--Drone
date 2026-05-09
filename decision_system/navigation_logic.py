class NavigationLogic:
    def __init__(self):
        self.current_mode = 'IDLE'

    def update_mode(self, obstacle_detected):
        if obstacle_detected:
            self.current_mode = 'AVOIDANCE'
        else:
            self.current_mode = 'AUTONOMOUS_NAVIGATION'

    def get_navigation_command(self):
        if self.current_mode == 'AVOIDANCE':
            return 'CHANGE_PATH'

        if self.current_mode == 'AUTONOMOUS_NAVIGATION':
            return 'MOVE_FORWARD'

        return 'HOVER'

if __name__ == '__main__':
    nav = NavigationLogic()

    nav.update_mode(False)
    print(nav.get_navigation_command())

    nav.update_mode(True)
    print(nav.get_navigation_command())
