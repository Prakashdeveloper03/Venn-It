# Importing necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Setting page title and icon using set_page_config
st.set_page_config(page_title="Venn It", page_icon="🎯")

# Adding header and subheader using header and subheader methods
st.header("Venn It")
st.subheader("Input")

# Creating 3 columns
col1, col2, col3 = st.columns(3)

# Adding text area and sidebar input for each list in columns
with col1:
    list1 = st.text_area("List 1").split()
    list1_name = st.sidebar.text_input("List 1 name")
with col2:
    list2 = st.text_area("List 2").split()
    list2_name = st.sidebar.text_input("List 2 name")
with col3:
    list3 = st.text_area("List 3").split()
    list3_name = st.sidebar.text_input("List 3 name")

# Checking if all 3 lists have data and plotting venn diagram using venn3 method
if (list1 != []) and (list2 != []) and (list3 != []):
    st.subheader("Output")
    plt.figure(figsize=(4, 4))
    fig, ax = plt.subplots()
    venn3([set(list1), set(list2), set(list3)], (list1_name, list2_name, list3_name))
    st.pyplot(fig)
else:
    st.info("☝️ Enter data to proceed!")
