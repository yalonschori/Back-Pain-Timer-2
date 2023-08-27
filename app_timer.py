class Timer:
    def __init__(
        self,
        root,
        displaying_widget,
        should_start,
        message_command,
        reset_button_command,
    ):
        self.root = root
        self.displaying_widget = displaying_widget
        self.should_start = should_start
        self.message_command = message_command
        self.reset_button_comand = reset_button_command
        self.message_tracker = 0

    def start_timer(self, remaining_time):
        self.should_start = True
        self.update_timer(remaining_time)

    def stop_timer(self, remaining_time):
        self.should_start = False
        minutes = remaining_time // 60
        seconds = remaining_time % 60 - 1
        self.displaying_widget.configure(text=f"{minutes:02d} : {seconds:02d}")

    def update_timer(self, remaining_time):
        if self.should_start:
            if remaining_time > 0:
                remaining_time -= 1
                minutes = remaining_time // 60
                seconds = remaining_time % 60
                self.displaying_widget.configure(text=f"{minutes:02d} : {seconds:02d}")
                self.root.after(1000, lambda: self.update_timer(remaining_time))
            else:
                self.reset_button_comand()
                if self.message_tracker == 0:
                    self.message_command(False)
                    self.message_tracker += 1
                else:
                    self.message_command(True)
                    self.message_tracker -= 1

        else:
            return
