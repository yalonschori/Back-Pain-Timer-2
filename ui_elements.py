import customtkinter as ctk
from CTkToolTip import *
from PIL import Image, ImageTk


class Custom_button(ctk.CTkButton):
    def __init__(
        self,
        color,
        hover_color,
        command,
        placement,
        text=" ",
        text_color="white",
        tooltip_text="",
    ):
        super().__init__(placement, text=text)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.command = command
        self.placement = placement
        self.text_color = text_color
        self.tooltip_opacity = 0 if tooltip_text == "" else 1
        self.button = ctk.CTkButton(
            self.placement,
            text=self.text,
            command=self.command,
            fg_color=self.color,
            hover_color=self.hover_color,
            text_color=self.text_color,
        )
        self.tooltip = CTkToolTip(
            self.button,
            message=tooltip_text,
            delay=0.1,
            alpha=self.tooltip_opacity,
            y_offset=30,
            x_offset=-125,
        )

    def pack_button(self):
        self.button.pack()

    def forget_button(self):
        self.button.pack_forget()

    def place_button(self, x, y):
        self.button.place(x=x, y=y)


class Icons(ctk.CTkButton):
    def __init__(
        self,
        placement,
        image,
        command,
        fg_color="transparent",
        hover_color="#ebebeb",
        tooltip_text="",
    ):
        super().__init__(placement)
        self.placement = placement
        self.image = image
        self.command = command
        self.fg_color = fg_color
        self.hover_color = hover_color
        self.tooltip_Text = tooltip_text
        self.tooltip_opacity = 0 if tooltip_text == "" else 1
        self.icon = ctk.CTkImage(Image.open(self.image), size=(26, 26))
        self.button = ctk.CTkButton(
            self.placement,
            image=self.icon,
            command=self.command,
            text="",
            fg_color=self.fg_color,
            hover_color=self.hover_color,
            width=27,
            height=23,
        )
        self.tooltip = CTkToolTip(
            self.button,
            message=tooltip_text,
            delay=0.1,
            alpha=self.tooltip_opacity,
        )

    def pack_button(self):
        self.button.pack()

    def config_this(self, path, hover_color):
        new_icon = ctk.CTkImage(Image.open(path), size=(26, 26))
        self.button.configure(image=new_icon, hover_color=hover_color)

    def place_button(self, x, y):
        self.button.place(x=x, y=y)
