from sys import stdout
from SearchRecipes_Flask import app, forms
from flask import request, render_template

@app.route('/')
@app.route('/search',methods=["GET","POST"])
def search():
    search_form = forms.SearchForRecipes(request.form)

    if request.method == 'POST':
        """Assign to the following variables the input values by the user"""
        meal = request.form['meal']
        include = request.form['include']
        exclude = request.form['exclude']

        """Pass the variables above as arguments to the get_data function 
        and assign the return value to recipes"""
        recipes = forms.get_data(meal, include, exclude)

        #accessing the list available in the json:
        #print (recipes, file=stdout)
        
        for item in recipes[0]:
            print (item.items(), file=stdout)
            # now song is a dictionary
            #for attribute, value in item.items():
             #   print (attribute, value)
             #   recipes=recipes("V")
        
        print (recipes, file=stdout)
        exit(0)
        return render_template('recipes_results.html', form=search_form, meal=meal, include=include,
                               exclude=exclude, recipes=recipes)

    return render_template('recipes_search.html', form=search_form)