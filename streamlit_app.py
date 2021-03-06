import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#adding a function
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return (fruityvice_normalized)


#new section to display fruitvice API response
streamlit.header("🍌🥭 Fruityvice Fruit Advice!🥝🍇")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select fruit to get more info.")
  else: 
      back_from_function = get_fruityvice_data (fruit_choice) 
      # display as a dataframe
      streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

streamlit.header("🍌🥭 View our fruit list - Add your favorites!")

#adding a function
def get_fruit_load_list():
  with  my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

#button to load fruit list
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
 
#dont run
#streamlit.stop()

#adding a function
def insert_row(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('"+ new_fruit + "')")
    return "thanks for adding "+new_fruit

#allow end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like add?')
if streamlit.button('Add a new fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  backfromfunc= insert_row(add_my_fruit)
  my_cnx.close()
  streamlit.text (backfromfunc)
