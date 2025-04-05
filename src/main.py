import streamlit as st
import langchain_helper

st.title("University list")

city = st.sidebar.selectbox("Select the city", ("New York", "New Jersey", "Austin", "Boston", "Chicago", "San Francisco"))


if city:
    response = langchain_helper.generate_description_city_and_univ(city)
    st.header(response['city_desc'].strip())
    univ_names = response['univ_names'].strip().split(",")
    st.write("**University List**")

    for item in univ_names:
        st.write('-', item)
