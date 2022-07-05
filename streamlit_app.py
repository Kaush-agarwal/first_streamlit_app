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

#new section to display fruitvice API response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
#streamlit.text(fruityvice_response.json())
# normalise json response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display as a dataframe
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_row)
