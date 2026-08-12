import constants as const
import streamlit as st
from shape_image import get_img

# Settings
with st.popover("Settings"):

    # Type
    if 'cs_type' not in st.session_state:
        st.session_state.cs_type = 0
    options = const.TYPELABELS_LIST

    def set_cs_type():
        st.session_state.cs_type = const.TYPELABELS_LIST.index(st.session_state.cs_type_input)

    st.radio("Type",
             options,
             horizontal=True,
             index=st.session_state.cs_type,
             key="cs_type_input",
             on_change=set_cs_type)

    type_first = const.get_list_type_at(st.session_state.cs_type)
    type_second = const.get_list_type_at(st.session_state.cs_type, True)

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


@st.cache_data()
def display_shapes(type_first, shape_suit):
    shape_list = const.get_shape_list(type_first)
    for i in range(len(shape_list)):
        shape_img = get_img(type_first, shape_suit, i)
        st.image(shape_img.file_path_small)


with col1:
    display_shapes(type_first, shape_suit)
with col2:
    display_shapes(type_second, shape_suit)
