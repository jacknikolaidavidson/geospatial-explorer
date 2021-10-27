import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import pydeckapp,fractional_cover # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# st.title("Data Storyteller Application")

# Add all your applications (pages) here
app.add_page("Ground cover", pydeckapp.app)
app.add_page("Fractional cover", fractional_cover.app)


# The main app
app.run()