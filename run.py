import os
import math
import datetime
from flask import Flask
from flask import render_template, url_for, request, session, redirect, jsonify
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.secret_key = 'any random string'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)


@app.route('/')
def index():
    '''Retrieves four most viewed recipes in the recipes collection of database.
    Renders the template for the homepage and provides the recipe information for the template.'''

    recipes = list(mongo.db.recipes.find().sort(
        "views", pymongo.DESCENDING).limit(4))
    return render_template('index.html', title='Home | Grubox', recipes=recipes)


@app.route('/recipes/', methods=['GET', 'POST'])
@app.route('/recipes/<page>/<limit>', methods=['GET', 'POST'])
def recipes(page=1, limit=8):
    '''Limits the number of recipes shown on a page to a certain number. 
    Generates pagination dynamically based on the number of records in the database.'''
    limit = int(limit)

    if request.method == 'POST':
        limit = int(request.form['limit'])

    page = int(page)
    #print(page, limit)
    skip = page * limit - limit
    maximum = math.ceil((mongo.db.recipes.count_documents({})) / limit)

    recipes = list(mongo.db.recipes.find().sort(
        "$natural", pymongo.DESCENDING).skip(skip).limit(limit))
    return render_template(
        'recipes.html',
        title='Recipes | Grubox',
        recipes=recipes,
        page=page,
        pages=range(1, maximum + 1),
        maximum=maximum, limit=limit
    )


@app.route('/view/recipe_id?=<id>')
def view(id):
    '''Controls behavior of user-views increment operator.'''

    mongo.db.recipes.find_one_and_update(
        {"_id": ObjectId(id)}, {"$inc": {"views": 1}})
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    return render_template('view.html', title='View Recipe | Grubox', recipe=recipe)


@app.route('/like/recipe_id?=<id>')
def like(id):
    '''Controls behavior of user-like increment and decrements operator.
    Feature is dependant upon user interaction in the user-interface.'''

    mongo.db.recipes.find_one_and_update(
        {"_id": ObjectId(id)}, {"$inc": {"likes": 1}})
    return redirect(url_for('recipes'))


@app.route('/dislike/recipe_id?=<id>')
def dislike(id):
    '''Controls behavior of user-dislike increment and decrements operator.
    Feature is dependant upon user interaction in the user-interface.'''

    mongo.db.recipes.find_one_and_update(
        {"_id": ObjectId(id)}, {"$inc": {"dislikes": 1}})
    return redirect(url_for('recipes'))


@app.route('/create', methods=['GET', 'POST'])
def create():
    # check for logged in user
    email = session.get('email')
    inserted_id = 0
    if not email:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # get current date and time
        now = datetime.datetime.utcnow()
        current_date = datetime.datetime.strftime(now, '%b %d, %Y')
        current_time = now.strftime("%I:%M %p")

        recipe = request.get_json()

        if recipe:
            recipe.update(
                email=email,
                views=0,
                likes=0,
                dislikes=0,
                time=current_time,
                date=current_date
            )
            inserted_id = mongo.db.recipes.insert_one(recipe).inserted_id
        print(inserted_id)
        return redirect(url_for('recipes'))

    return render_template('create.html', title='Create Recipe | Grubox')


@app.route('/edit/recipe_id?=<id>', methods=['GET', 'POST'])
def edit(id):
    # check for logged in user
    email = session.get('email')
    if not email:
        return redirect(url_for('register'))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})

    if request.method == 'POST':
        update_recipe = request.get_json()

        if update_recipe:
            update_recipe.update(
                {
                    'email': email,
                    'views': recipe.get('views'),
                    'likes': recipe.get('likes'),
                    'dislikes': recipe.get('dislikes'),
                    'time': recipe.get('time'),
                    'date': recipe.get('date')
                }
            )

            mongo.db.recipes.replace_one({"_id": ObjectId(id)}, update_recipe)

        print(id)

        return redirect(url_for('view', id=id))

    return render_template('edit.html', title='Edit Recipe | Grubox', recipe=recipe)


@app.route('/login', methods=['POST', 'GET'])
def login():
    # check for logged in user
    email = session.get('email')
    if email:
        return redirect(url_for('register'))

    user = None
    if request.method == 'POST':
        email = request.form["email"]
        user = mongo.db.users.find_one({"email": email})

        try:
            assert(user["password"] == request.form["password"])
        except (AssertionError, TypeError):
            return render_template('login.html', title='Login | Grubox', user=None, error="incorrect_login")
        else:
            try:
                session['name'] = user['name']
            except KeyError:
                session['name'] = 'John Doe'
            session['email'] = email
            return redirect(url_for("index"))

    return render_template('login.html', title='Login | Grubox', user=user)


@app.route('/delete/recipe_id?=<id>')
def delete(id):
    # check for logged in user
    email = session.get('email')
    if not email:
        return redirect(url_for('register'))
    try:
        mongo.db.recipes.delete_one({"_id": ObjectId(id), 'email': email})
    except:
        return redirect(url_for('recipes'))
    return redirect(url_for('account'))


@app.route('/logout')
def logout():
    #  logout user and clear session
    session['email'] = None
    session['name'] = None
    # session.clear()
    return redirect(url_for('login'))


@app.route('/account/')
@app.route('/account/<page>')
def account(page=1):
    # check for logged in user
    email = session.get('email')
    if not email:
        return redirect(url_for('register'))

    limit = 8
    page = int(page)
    skip = page * limit - limit
    maximum = math.ceil(mongo.db.recipes.count_documents({"email": email}) / 8)
    count = mongo.db.recipes.find({"email": email}).count()
    recipes = list(mongo.db.recipes.find({"email": email}).sort(
        "$natural", pymongo.DESCENDING).skip(skip).limit(8))

    return render_template(
        'account.html',
        title='My Account | Grubox',
        recipes=recipes,
        page=page,
        pages=range(1, maximum + 1),
        maximum=maximum,
        count=count
    )


@app.route('/signup', methods=['POST', 'GET'])
def register():
    '''Accepts POST and GET requests.

    If the request is a GET request, checks for a session email.
    If session email is found, the homepage is rendered.
    If no session email is found, the register template is rendered.

    If the request is a POST request, form data is retrieved.
    A check is performed to verify that the user email doesn't already exist.
    If the user already exists, the register page is rendered with a user_exists error.

    If a user does not exist, the user is added to the database and the login page is rendered.'''

    # check for logged in user
    email = session.get('email')
    if email:
        return redirect(url_for('index'))

    user = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = {'name': name, 'email': email, 'password': password}

        if mongo.db.users.find_one({"email": email}):
            return render_template('register.html', title='Register | Grubox', error="user_exists")
        else:
            mongo.db.users.insert_one(user)
            return render_template('login.html', title='Login | Grubox', user=user, password=password)

    return render_template('register.html', title='Register | Grubox')


# Run App
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=os.environ.get('PORT', '5000'))
