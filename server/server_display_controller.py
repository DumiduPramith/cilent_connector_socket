main_options = {
    1 : "Show Connected Devices",
    0 : "Exit"
}

class MainCommandLineTool:
    global main_options

    def show_main_options(self):
        for option in main_options:
            print(f'{option}: {main_options.get(option)}')
        val = self.get_input()
        if val == 1:
            pass
    def show_connected_devices(self):
        pass

    def get_input(self):
        val = input(": ")
        return val

    def run(self):
        self.show_main_options()

x = MainCommandLineTool()
x.run()
exit = False

