from .tokens import *

general_styles = {}

label_styles = {
    "Label::h1": {
        "font_size": token_font_size_h1,
    },
    "Label::h2": {
        "font_size": token_font_size_h2,
    },
    "Label::h3": {
        "font_size": token_font_size_h3,
    },
    "Label::h4": {
        "font_size": token_font_size_h4,
    },
}

button_styles = {
    "Button": {
        "padding": token_button_padding,
        "border_radius": token_button_radius,
        "color": token_text_color_default,
    },
    "Button.Label": {
        "font_size": token_font_size_default,
        "color": token_text_color_default,
    },
    "Button.Label:hovered": {
        "color": token_text_color_default,
    },
    "Button.Label:disabled": {
        "color": token_text_color_isaac_disabled,
    },
}

button_primary_styles = {
    "Button::primary": {
        "background_color": token_buttons_primary_default,
    },
    "Button::primary:hovered": {
        "background_color": token_buttons_primary_hover,
    },
    "Button::primary:pressed": {
        "background_color": token_buttons_primary_pressed,
    },
    "Button.Label::primary": {
        "color": token_text_color_default,
    },
    "Button.Label::primary:disabled": {
        "color": token_text_color_custom_disabled,
    },
}

button_secondary_styles = {
    "Button::secondary": {
        "background_color": token_buttons_secondary_default,
    },
    "Button::secondary:hovered": {
        "background_color": token_buttons_secondary_hover,
    },
    "Button::secondary:pressed": {
        "background_color": token_buttons_secondary_pressed,
    },
    "Button.Label::secondary": {
        "color": token_text_color_default,
    },
}

button_danger_styles = {
    "Button::danger": {
        "background_color": token_buttons_danger_default,
    },
    "Button::danger:hovered": {
        "background_color": token_buttons_danger_hover,
    },
    "Button::danger:pressed": {
        "background_color": token_buttons_danger_pressed,
    },
    "Button.Label::danger": {
        "color": token_text_color_default,
    },
}

combobox_styles = {
    "ComboBox": {
        "padding": token_button_padding,
        "border_radius": token_button_radius,
        "color": token_text_color_default,
        "font_size": token_font_size_default,
    },
    "ComboBox:hovered": {
        "color": token_text_color_default,
    },
    "ComboBox:pressed": {
        "background_color": token_text_color_custom_pressed,
    },
    "ComboBox:disabled": {
        "color": token_text_color_isaac_disabled,
    },
}

styles = {
    **general_styles,
    **label_styles,
    **button_styles,
    **button_primary_styles,
    **button_secondary_styles,
    **button_danger_styles,
    **combobox_styles,
}
