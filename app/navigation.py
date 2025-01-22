import streamlit as st

pages = {
    "Navigation": [
        st.Page("trainer.py", title="Floater Trainer"),
        st.Page("cheat_sheet.py", title="Cheat Sheet"),
        st.Page("about.py", title="About"),
    ],
}
pg = st.navigation(pages)
pg.run()
