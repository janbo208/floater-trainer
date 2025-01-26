import constants as const
import streamlit as st
from tile_image import get_img

# Settings
with st.popover("Settings"):

    # Type
    if 'cs_type' not in st.session_state:
        st.session_state.cs_type = 0
    options = [const.TYPEPAIR19.label, const.TYPEPAIR28.label, const.TYPEPAIR37.label]

    def set_cs_type():
        match st.session_state.cs_type_input:
            case const.TYPEPAIR19.label:
                st.session_state.cs_type = const.TYPEPAIR19.order
            case const.TYPEPAIR28.label:
                st.session_state.cs_type = const.TYPEPAIR28.order
            case const.TYPEPAIR37.label:
                st.session_state.cs_type = const.TYPEPAIR37.order

    list_type = st.radio("Type",
                         options,
                         horizontal=True,
                         index=st.session_state.cs_type,
                         key="cs_type_input",
                         on_change=set_cs_type)
    type_first = 0
    type_second = 0
    match list_type:
        case const.TYPEPAIR19.label:
            type_first = const.TYPEPAIR19.first
            type_second = const.TYPEPAIR19.second
        case const.TYPEPAIR28.label:
            type_first = const.TYPEPAIR28.first
            type_second = const.TYPEPAIR28.second
        case const.TYPEPAIR37.label:
            type_first = const.TYPEPAIR37.first
            type_second = const.TYPEPAIR37.second

    # Suit
    if 'cs_suit' not in st.session_state:
        st.session_state.cs_suit = 0
    options = [const.Suits.man.short, const.Suits.pin.short, const.Suits.sou.short]

    def set_cs_suit():
        match st.session_state.cs_suit_input:
            case const.Suits.man.short:
                st.session_state.cs_suit = const.Suits.man.order
            case const.Suits.pin.short:
                st.session_state.cs_suit = const.Suits.pin.order
            case const.Suits.sou.short:
                st.session_state.cs_suit = const.Suits.sou.order

    tile_suit = st.radio("Suit",
                         options,
                         horizontal=True,
                         index=st.session_state.cs_suit,
                         key="cs_suit_input",
                         on_change=set_cs_suit)

    match tile_suit:
        case const.Suits.man.short:
            tile_suit = const.Suits.man.short
        case const.Suits.pin.short:
            tile_suit = const.Suits.pin.short
        case const.Suits.sou.short:
            tile_suit = const.Suits.sou.short

# Tile images
col1, col2 = st.columns(2)
with col1:
    tile_list = const.get_shape_list(type_first)
    for i in range(len(tile_list)):
        tile_img = get_img(type_first, tile_suit, i)
        st.image(tile_img.file_path_small)
with col2:
    tile_list = const.get_shape_list(type_second)
    for i in range(len(tile_list)):
        tile_img = get_img(type_second, tile_suit, i)
        st.image(tile_img.file_path_small)
