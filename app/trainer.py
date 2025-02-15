import time

import constants as const
import streamlit as st
from shape_image import get_answer_imgs
from streamlit_extras.keyboard_text import key, load_key_css
from streamlit_shortcuts import add_keyboard_shortcuts

if 'img_first' not in st.session_state:
    st.session_state.img_first = None
if 'img_second' not in st.session_state:
    st.session_state.img_second = None
if 'solved_count' not in st.session_state:
    st.session_state.solved_count = 0
if 'correct_count' not in st.session_state:
    st.session_state.correct_count = 0
if 'answer_chosen' not in st.session_state:
    st.session_state.answer_chosen = False
if 'correct_answer_chosen' not in st.session_state:
    st.session_state.correct_answer_chosen = False
if 'list_types' not in st.session_state:
    st.session_state.list_types = []
if 'started' not in st.session_state:
    st.session_state.started = False
if 'reset_button_label' not in st.session_state:
    st.session_state.reset_button_label = "Start"
if 'finished' not in st.session_state:
    st.session_state.finished = False


def reset_trainer():
    if st.session_state.list_types:
        get_answer_imgs(st.session_state.list_types)
        st.session_state.started = True
        st.session_state.solved_count = 0
        st.session_state.correct_count = 0
        st.session_state.answer_chosen = False
        st.session_state.correct_answer_chosen = False
        st.session_state.finished = False
        st.session_state.reset_button_label = "Reset"
    else:
        st.error("Select at least one type in the settings!", icon="❌")


# Sidebar
FIRST_LABEL = "Discard from A"
SECOND_LABEL = "Discard from B"
NEXT_LABEL = "Next"

with st.sidebar:
    st.write("Discard from the weaker shape")
    st.write("")
    st.markdown("Keyboard shortcuts")
    load_key_css()
    col1, col2, col3 = st.columns(3)
    with col1:
        key("←")
        st.write(FIRST_LABEL)
    with col2:
        key("↑")
        st.write(NEXT_LABEL)
    with col3:
        key("→")
        st.write(SECOND_LABEL)

col_settings, col_start = st.columns([1, 5])

# Settings


def set_finished():
    st.session_state.finished = st.session_state.solved_count >= st.session_state.question_count


with col_settings:
    with st.popover("Settings"):
        col1, col2 = st.columns(2)
        with col1:
            # Type
            options = [const.FLOATER_TYPE19.label,
                       const.FLOATER_TYPE28.label,
                       const.FLOATER_TYPE37.label]
            if 'question_types' not in st.session_state:
                st.session_state.question_types = options

            def set_type():
                st.session_state.question_types = st.session_state.types_input

            list_types = st.segmented_control(
                "Type", options, selection_mode="multi",
                default=st.session_state.question_types,
                key="types_input",
                on_change=set_type)
            st.session_state.list_types = list_types

            # Counter
            if 'show_counter' not in st.session_state:
                st.session_state.show_counter = False

            def toggle_counter():
                st.session_state.show_counter = st.session_state.toggle_counter

            st.checkbox("show counter",
                        value=st.session_state.show_counter,
                        key="toggle_counter",
                        on_change=toggle_counter)

            # Auto advance after correct answer
            if 'auto_advance' not in st.session_state:
                st.session_state.auto_advance = True

            def toggle_auto_advance():
                st.session_state.auto_advance = st.session_state.toggle_auto_advance

            st.checkbox("auto advance  \n (after correct answer)",
                        value=st.session_state.auto_advance,
                        key="toggle_auto_advance",
                        on_change=toggle_auto_advance)
        with col2:
            # Question count
            if 'question_count' not in st.session_state:
                st.session_state.question_count = 30

            def set_question_count():
                st.session_state.question_count = st.session_state.question_count_input

            st.number_input("Number of questions",
                            min_value=1,
                            step=10,
                            value=st.session_state.question_count,
                            key="question_count_input",
                            on_change=set_question_count)
            set_finished()

# Start/Reset button
with col_start:
    reset_button_label = st.session_state.reset_button_label
    st.button(reset_button_label, key="reset", on_click=reset_trainer)
    if not st.session_state.started:
        st.stop()

# Progress bar
progress_bar = st.progress(0)
progress = st.session_state.solved_count / st.session_state.question_count
if progress > 1.0:
    progress = 1.0
progress_bar.progress(progress)

# Shape images
if st.session_state.img_first:
    col1, col2, col3 = st.columns([1, 2.5, 2.5])

    with col1:
        correct = st.session_state.correct_count
        solved = st.session_state.solved_count
        counter_text = f"{correct}/{solved}"
        if st.session_state.show_counter:
            st.metric(label="counter", value=counter_text, label_visibility="collapsed")
    with col2:
        st.text("Shape A")
        file_path = st.session_state.img_first.file_path
        st.image(file_path)
    with col3:
        st.text("Shape B")
        file_path = st.session_state.img_second.file_path
        st.image(file_path)


# Answer buttons
col1, col2, col3 = st.columns([1, 2.5, 2.5])

# Answer feedback
answer_feedback = st.empty()
if st.session_state.answer_chosen:
    if st.session_state.correct_answer_chosen:
        with answer_feedback:
            st.success('Correct', icon="✅")
    else:
        with answer_feedback:
            st.error('Incorrect', icon="❌")

add_keyboard_shortcuts({"ArrowLeft": FIRST_LABEL,
                        "ArrowRight": SECOND_LABEL,
                        "ArrowUp": NEXT_LABEL,
                        })


def advance_question():
    st.session_state.answer_chosen = False
    st.session_state.correct_answer_chosen = False
    if not st.session_state.finished:
        get_answer_imgs(st.session_state.list_types)


def check_answer(answer_correct):
    if not st.session_state.answer_chosen:
        if answer_correct:
            with answer_feedback:
                st.success('Correct', icon="✅")
            st.session_state.correct_answer_chosen = True
            st.session_state.correct_count += 1
        else:
            with answer_feedback:
                st.error('Incorrect', icon="❌")
            st.session_state.correct_answer_chosen = False
        st.session_state.answer_chosen = True
        st.session_state.solved_count += 1
    if not st.session_state.finished:
        set_finished()
        if st.session_state.correct_answer_chosen and st.session_state.auto_advance:
            time.sleep(0.5)
            advance_question()
    if st.session_state.finished:
        time.sleep(1.0)

        @st.dialog("Result")
        def show_result():
            solved = st.session_state.solved_count
            correct = st.session_state.correct_count
            correct_pct = round(correct / solved * 100)
            st.write(f"Correct answers: {correct}/{solved}")
            st.write(f"{correct_pct}%")
        show_result()


disable_answer_button = st.session_state.finished or st.session_state.answer_chosen
with col2:
    answer_correct = st.session_state.img_first.order < st.session_state.img_second.order
    st.button(FIRST_LABEL, key="answer_first",
              use_container_width=True,
              disabled=disable_answer_button,
              on_click=check_answer,
              args=(answer_correct,))

with col3:
    answer_correct = st.session_state.img_second.order < st.session_state.img_first.order
    st.button(SECOND_LABEL, key="answer_second",
              use_container_width=True,
              disabled=disable_answer_button,
              on_click=check_answer,
              args=(answer_correct,))

with col1:
    button_disabled = not st.session_state.answer_chosen
    if st.session_state.finished:
        button_disabled = True
    st.button(NEXT_LABEL, key="next",
              use_container_width=True,
              on_click=advance_question,
              disabled=button_disabled)
