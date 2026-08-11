import random
from dataclasses import dataclass

import constants as const
import streamlit as st


@dataclass
class ShapeImage:

    shape: str
    suit: str
    list_type: int

    def __init__(self, shape, suit, list_type):
        self.shape = shape
        self.suit = suit
        self.list_type = list_type

    def get_file_path(self, img_folder):
        filename = self.shape + self.suit
        match self.suit:
            case const.Suits.man.short:
                folder = img_folder + const.Suits.man.lower
            case const.Suits.pin.short:
                folder = img_folder + const.Suits.pin.lower
            case const.Suits.sou.short:
                folder = img_folder + const.Suits.sou.lower
        file_path = f"./{folder}/{filename}.png"
        return file_path

    @property
    def order(self):
        shape_list = const.get_shape_list(self.list_type)
        index = shape_list.index(self.shape)
        return index

    @property
    def file_path(self):
        img_folder = "/png/regular/"
        return self.get_file_path(img_folder)

    @property
    def file_path_small(self):
        img_folder = "/png/small/"
        return self.get_file_path(img_folder)


def randomize_list_order(list_types):
    order_list = [const.TYPELABELS_LIST.index(list_type) for list_type in list_types]
    return random.choice(order_list)


def ranomize_list_type(list_order):
    type_first = const.get_list_type_at(list_order)
    type_second = const.get_list_type_at(list_order, True)
    list_types = [type_first, type_second]
    list_type = random.choice(list_types)
    return list_type


def get_img(list_type, shape_suit="", shape_order=-1):
    shape_list = const.get_shape_list(list_type)
    if shape_order == -1:
        shape_order = random.randint(0, len(shape_list) - 1)
    if shape_suit == "":
        shape_suit = random.choice(const.Suits.short)
    shape = shape_list[shape_order]
    shape_img = ShapeImage(shape, shape_suit, list_type)
    return shape_img


def get_answer_imgs(list_types):
    list_order = randomize_list_order(list_types)
    list_type_first = ranomize_list_type(list_order)
    list_type_second = ranomize_list_type(list_order)
    st.session_state.img_first = get_img(list_type_first)
    st.session_state.img_second = get_img(list_type_second)
    if st.session_state.img_first.order == st.session_state.img_second.order:
        get_answer_imgs(list_types)
