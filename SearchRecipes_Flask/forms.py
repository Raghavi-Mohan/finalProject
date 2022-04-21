from SearchRecipes_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import StringField

class SearchForRecipes (FlaskForm):
    meal = StringField('Meal')
    include = StringField('Include')
    exclude = StringField("Exclude")

def get_data(meal, include, exclude):

    api_key_dict=main_functions.read_from_file('SearchRecipes_Flask/JSON_Files/api_key.json')
    api_key = api_key_dict["api_key"]

    url = "https://api.spoonacular.com/food/videos/search?query=" + meal + "&excludeIngredients="+ exclude + "&includeIngredients=" + include + "&apiKey=" + api_key
    payload={}
    headers = {}
    """Make the api request using requests and .get method"""
    response = requests.request("GET", url, headers=headers, data=payload)


    """ Save the response as a json file on the project"""
    #hint: use main_functions

    """Read the JSON file and save it to variable"""
    # hint: use main_functions
    responseRecipes =main_functions.save_to_file(response.text,'trial1')

    recipes =main_functions.read_from_file('trial1')

    return recipes
