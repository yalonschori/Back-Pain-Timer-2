# Main Module (UI and Controller)

from app_timer import Timer
import customtkinter as ctk
from ui_elements import Custom_button, Icons
from CTkMessagebox import CTkMessagebox
import pygame


pygame.mixer.init()
sound_file_path = "sounds/original_notification.mp3"
main_sound = pygame.mixer.Sound(sound_file_path)
sound_volume = 0.2
main_sound.set_volume(sound_volume)


sound_library_options = {
    "Original": pygame.mixer.Sound("sounds/original_notification.mp3"),
    "Deep Woosh": pygame.mixer.Sound("sounds/deep_woosh_notification.mp3"),
    "Positive Bells": pygame.mixer.Sound("sounds/positive_bells.mp3"),
    "Smartphone": pygame.mixer.Sound("sounds/smartphone_notification.mp3"),
    "Tech": pygame.mixer.Sound("sounds/tech_notification.mp3"),
}


remaining_time = 15 * 60 + 1
should_start = False
minutes = remaining_time // 60
seconds = remaining_time % 60 - 1
show_pop_ups = True


def start_timer_change_ui():
    global remaining_time
    ui_timer.start_timer(remaining_time)
    start_button.forget_button()
    stop_button.pack_button()


def stop_timer_change_ui():
    global remaining_time
    ui_timer.stop_timer(remaining_time)
    stop_button.forget_button()
    start_button.pack_button()


def reset_button_command():
    stop_button.forget_button()
    start_button.pack_button()


def show_message(boolean: bool):
    main_sound.play()
    if show_pop_ups:
        if not boolean:
            CTkMessagebox(
                title="Back Pain Timer 2",
                message="Please Change Your Sitting Position",
                icon="info",
            )
        if boolean:
            CTkMessagebox(
                title="Back Pain Timer 2",
                message="Please Take A Break To Walk And Look At Objects In The Distance",
                icon="warning",
            )
    else:
        return


def activate_gaming_mode():
    global show_pop_ups
    ctk.set_appearance_mode("dark")
    gaming_mode_button.forget_button()
    work_mode_button.pack_button()
    root.title("Back Pain Timer 2 (Gaming Mode)")
    show_pop_ups = False
    """notification_sound_picker.config_this(
        path="icons/music_library_white.png", hover_color="#242424"
    )"""


def activate_work_mode():
    global show_pop_ups
    ctk.set_appearance_mode("light")
    work_mode_button.forget_button()
    gaming_mode_button.pack_button()
    root.title("Back Pain Timer 2 (Work Mode)")
    show_pop_ups = True
    """notification_sound_picker.config_this(
        path="icons/music_library.png", hover_color="#ebebeb"
    )"""


def play_sound_preview(sound):
    global sound_volume
    if not sound_var.get():
        pass
    else:
        pygame.mixer.Sound.play(sound_library_options[sound]).set_volume(sound_volume)


def save_sound(sound):
    global sound_volume
    global main_sound
    if not sound_var.get():
        pass
    else:
        main_sound = sound_library_options[sound]
        main_sound.set_volume(sound_volume)
        CTkMessagebox(title="Back Pain Timer 2", message="Saved!", icon="info")
        main_sound.play()


def change_volume(value):
    main_sound.set_volume(value)


root = ctk.CTk()
root.geometry("400x500")
root.title("Back Pain Timer 2 (Work Mode)")
ctk.set_appearance_mode("light")
root.resizable(False, False)

frame1 = ctk.CTkFrame(root)
frame2 = ctk.CTkFrame(root, fg_color="transparent")
time_left_label = ctk.CTkLabel(frame1, text=f"{minutes:02d} : {seconds:02d}")
ui_timer = Timer(
    root,
    time_left_label,
    should_start,
    show_message,
    reset_button_command,
)
start_button = Custom_button(
    placement=frame1,
    text="Start Timer",
    command=start_timer_change_ui,
    color="#1AA6B7",
    hover_color="#004D61",
)
stop_button = Custom_button(
    placement=frame1,
    text="Stop Timer",
    command=stop_timer_change_ui,
    color="#FF414D",
    hover_color="#F56A79",
)

gaming_mode_button = Custom_button(
    placement=frame2,
    text="Switch To Gaming Mode",
    command=activate_gaming_mode,
    color="#233142",
    hover_color="#21243D",
    tooltip_text="Activates Dark Mode and Disables Pop Ups",
)


work_mode_button = Custom_button(
    placement=frame2,
    text="Switch To Work Mode",
    command=activate_work_mode,
    color="#FEFBF3",
    hover_color="#F8F0DF",
    text_color="black",
    tooltip_text="Activates Light Mode and Activates Pop Ups",
)


sound_var = ctk.StringVar()
drop_down_sound_menu = ctk.CTkOptionMenu(
    root,
    fg_color="#1AA6B7",
    variable=sound_var,
    values=list(sound_library_options.keys()),
)


preview_sound_button = Icons(
    placement=root,
    image="icons/play_arrow_white.png",
    hover_color="#004D61",
    fg_color="#1AA6B7",
    command=lambda: play_sound_preview(sound_var.get()),
    tooltip_text="Preview a sound",
)

save_sound_icon = Icons(
    placement=root,
    image="icons/save_icon_white.png",
    hover_color="#004D61",
    fg_color="#1AA6B7",
    command=lambda: save_sound(sound_var.get()),
    tooltip_text="Save preference",
)

slider_label = ctk.CTkLabel(root, text="Volume Control")
slider_var = ctk.DoubleVar()
slider = ctk.CTkSlider(
    root,
    orientation="horizontal",
    variable=slider_var,
    width=130,
    height=20,
    from_=0.1,
    to=1,
    command=change_volume,
)


frame1.pack(pady=100)
frame2.pack()
time_left_label.pack()
start_button.pack_button()
gaming_mode_button.pack_button()
# notification_sound_picker.place_button(5, 420)
drop_down_sound_menu.place(x=105, y=463)
preview_sound_button.place_button(x=55, y=460)
save_sound_icon.place_button(x=5, y=460)
slider.place(x=260, y=468)
slider_label.place(x=280, y=440)

root.mainloop()

pygame.mixer.quit()
