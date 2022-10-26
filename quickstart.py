import streamlit as st
import pandas as pd
from shillelagh.backends.apsw.db import connect, Cursor


connection = connect(":memory:")
cursor: Cursor = connection.cursor()

SQL = """
SELECT *
FROM "https://docs.google.com/spreadsheets/d/16z5ARs4CDX07Ps9Tf7Og6Dl79cvjY3A1iieJSDgM7Yk/edit#gid=0"
"""
item_list = list()
for row in cursor.execute(SQL):
    item_list.append(row)

cell_matrix = pd.DataFrame(item_list, columns=["Name", "Type", "Cost"])

# Create selection tools
create_list = st.number_input("How many choices do you want?", 1, 3)
value_select = st.selectbox("Select Cuisine", cell_matrix["Type"].unique())
cost_select = st.selectbox("Select Price Range", cell_matrix["Cost"].unique())

# Select values in dataset
selected = cell_matrix.loc[(cell_matrix["Type"] == value_select) & (cell_matrix["Cost"] == cost_select)]

# Display
try:
    st.dataframe(selected.sample(create_list))
except:
    st.write("No options for these selections...")


