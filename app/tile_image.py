import random
from dataclasses import dataclass

import constants as const
import streamlit as st


@dataclass
class TileImage:

    tiles: str
    suit: str
    list_type: int

    def __init__(self, tiles, suit, list_type):
        self.tiles = tiles
        self.suit = suit
        self.list_type = list_type

    @property
    def order(self):
        tile_list = const.get_shape_list(self.list_type)
        index = tile_list.index(self.tiles)
        return index

    @property
    def file_path(self):
        filename = self.tiles + self.suit
        img_folder = "/png/regular/"
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
    def file_path_small(self):
        filename = self.tiles + self.suit
        img_folder = "/png/small/"
        match self.suit:
            case const.Suits.man.short:
                folder = img_folder + const.Suits.man.lower
            case const.Suits.pin.short:
                folder = img_folder + const.Suits.pin.lower
            case const.Suits.sou.short:
                folder = img_folder + const.Suits.sou.lower
        file_path_small = f"./{folder}/{filename}.png"
        return file_path_small


def randomize_list_order(list_types):
    order_list = []
    if const.TYPEPAIR19.label in list_types:
        order_list.append(const.TYPEPAIR19.order)
    if const.TYPEPAIR28.label in list_types:
        order_list.append(const.TYPEPAIR28.order)
    if const.TYPEPAIR37.label in list_types:
        order_list.append(const.TYPEPAIR37.order)
    return random.choice(order_list)


def ranomize_list_type(list_order):
    match list_order:
        case const.TYPEPAIR19.order:
            list_types = [const.TYPEPAIR19.first, const.TYPEPAIR19.second]
        case const.TYPEPAIR28.order:
            list_types = [const.TYPEPAIR28.first, const.TYPEPAIR28.second]
        case const.TYPEPAIR37.order:
            list_types = [const.TYPEPAIR37.first, const.TYPEPAIR37.second]
    list_type = random.choice(list_types)
    return list_type


def get_img(list_type, tile_suit="", tile_order=-1):
    tile_list = const.get_shape_list(list_type)
    if tile_order == -1:
        tile_order = random.randint(0, len(tile_list) - 1)
    if tile_suit == "":
        tile_suit = random.choice(const.Suits.short)
    tile_string = tile_list[tile_order]
    tile_img = TileImage(tile_string, tile_suit, list_type)
    return tile_img


def get_answer_imgs(list_types):
    list_order = randomize_list_order(list_types)
    list_type_first = ranomize_list_type(list_order)
    list_type_second = ranomize_list_type(list_order)
    st.session_state.img_first = get_img(list_type_first)
    st.session_state.img_second = get_img(list_type_second)
    if st.session_state.img_first.order == st.session_state.img_second.order:
        get_answer_imgs(list_types)
