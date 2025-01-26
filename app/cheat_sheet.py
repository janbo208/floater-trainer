import constants as const
import streamlit as st
from shape_image import get_img

# Settings
with st.popover("Settings"):

    # Type
    if 'cs_type' not in st.session_state:
        st.session_state.cs_type = 0
    options = [const.FLOATER_TYPE19.label, const.FLOATER_TYPE28.label, const.FLOATER_TYPE37.label]

    def set_cs_type():
        match st.session_state.cs_type_input:
            case const.FLOATER_TYPE19.label:
                st.session_state.cs_type = const.FLOATER_TYPE19.order
            case const.FLOATER_TYPE28.label:
                st.session_state.cs_type = const.FLOATER_TYPE28.order
            case const.FLOATER_TYPE37.label:
                st.session_state.cs_type = const.FLOATER_TYPE37.order

    list_type = st.radio("Type",
                         options,
                         horizontal=True,
                         index=st.session_state.cs_type,
                         key="cs_type_input",
                         on_change=set_cs_type)
    type_first = 0
    type_second = 0
    match list_type:
        case const.FLOATER_TYPE19.label:
            type_first = const.FLOATER_TYPE19.first
            type_second = const.FLOATER_TYPE19.second
        case const.FLOATER_TYPE28.label:
            type_first = const.FLOATER_TYPE28.first
            type_second = const.FLOATER_TYPE28.second
        case const.FLOATER_TYPE37.label:
            type_first = const.FLOATER_TYPE37.first
            type_second = const.FLOATER_TYPE37.second

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

    shape_suit = st.radio("Suit",
                          options,
                          horizontal=True,
                          index=st.session_state.cs_suit,
                          key="cs_suit_input",
                          on_change=set_cs_suit)

    match shape_suit:
        case const.Suits.man.short:
            shape_suit = const.Suits.man.short
        case const.Suits.pin.short:
            shape_suit = const.Suits.pin.short
        case const.Suits.sou.short:
            shape_suit = const.Suits.sou.short

# Shape images
col1, col2 = st.columns(2)
with col1:
    shape_list = const.get_shape_list(type_first)
    for i in range(len(shape_list)):
        shape_img = get_img(type_first, shape_suit, i)
        st.image(shape_img.file_path_small)
with col2:
    shape_list = const.get_shape_list(type_second)
    for i in range(len(shape_list)):
        shape_img = get_img(type_second, shape_suit, i)
        st.image(shape_img.file_path_small)
