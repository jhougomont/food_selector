import streamlit as st
import pygsheets
import pandas as pd

# Authorization
gc = pygsheets.authorize(service_file='creds.json')

# Open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('food')

# Select the first sheet
wks = sh.sheet1

# Make it a Pandas DF
cell_matrix = wks.get_as_df()

value_select = st.selectbox("Select Cuisine", cell_matrix["Type"].unique())
cost_select = st.selectbox("Select Price Range", cell_matrix["Cost"].unique())

selected = cell_matrix.loc[(cell_matrix["Type"] == value_select) & (cell_matrix["Cost"] == cost_select)]

try:
    st.dataframe(selected.sample())
except:
    st.write("No options for these selections...")


