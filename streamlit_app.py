import streamlit
import pandas

streamlit.title("My Parents new healthy diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🐔 Rat droppings')
streamlit.text('🥣 Cockroach Soup')
streamlit.text('🥗 Fly-flakes')
streamlit.text('🥑🍞 Normal breakfast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# pick list
fruits_selected = streamlit.multiselect("pick some fruits:", list (my_fruit_list.index), ['Avocado', 'Strawberries'])
# display table
fruits_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_show)
