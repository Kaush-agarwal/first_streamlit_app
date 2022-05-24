import streamlit
import pandas

streamlit.title("My new healthy diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🐔 Rat droppings')
streamlit.text('🥣 Cockroach Soup')
streamlit.text('🥗 Fly-flakes')
streamlit.text('🥑🍞 Normal breakfast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
