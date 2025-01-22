import constants as const
import streamlit as st
from tile_image import get_img

# Settings
with st.popover("Settings"):

    # Type
    if 'cs_type' not in st.session_state:
        st.session_state.cs_type = 0
    options = [const.TILEPAIR19.label, const.TILEPAIR28.label, const.TILEPAIR37.label]

    def set_cs_type():
        match st.session_state.cs_type_input:
            case const.TILEPAIR19.label:
                st.session_state.cs_type = const.TILEPAIR19.order
            case const.TILEPAIR28.label:
                st.session_state.cs_type = const.TILEPAIR28.order
            case const.TILEPAIR37.label:
                st.session_state.cs_type = const.TILEPAIR37.order

    list_type = st.radio("Type",
                         options,
                         horizontal=True,
                         index=st.session_state.cs_type,
                         key="cs_type_input",
                         on_change=set_cs_type)
    type_first = 0
    type_second = 0
    match list_type:
        case const.TILEPAIR19.label:
            type_first = const.TILEPAIR19.first
            type_second = const.TILEPAIR19.second
        case const.TILEPAIR28.label:
            type_first = const.TILEPAIR28.first
            type_second = const.TILEPAIR28.second
        case const.TILEPAIR37.label:
            type_first = const.TILEPAIR37.first
            type_second = const.TILEPAIR37.second

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
    tile_list = const.get_tile_list(type_first)
    for i in range(len(tile_list)):
        tile_img = get_img(type_first, tile_suit, i)
        st.image(tile_img.file_path_small)
with col2:
    tile_list = const.get_tile_list(type_second)
    for i in range(len(tile_list)):
        tile_img = get_img(type_second, tile_suit, i)
        st.image(tile_img.file_path_small)
