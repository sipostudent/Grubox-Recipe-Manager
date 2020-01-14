<h1 align="center">
<br>
  <img src="static/img/online-cookbook-sipo.herokuapp.com_(iPad Pro) (1).png" width="600">
  <br>
    <br>
  Grubox
  <br>
</h1>

<h3 align="center">Data Centric Development</h3>

<h4 align="center">A recipe manager, accessible online, which enables users to create, read, update and delete recipes</h4>

## Table of Contents

<!--ts-->

1. [About](#About)

    - [Goal](#Goal)
    - [Functionality (User Stories)](#Functionality-User-Stories)
    - [Initiation](#Initiation)

2. [UX](#UX)

    - [Layout Pro](#Layout-Pro-Boundless-Adaptability)
    - [Layout Con](#Layout-Con-Moderate-Speed-and-Execution)
    - [Tablet Display](#Tablet-Display)
    - [Mobile Display](#Mobile-Display)
    - [Additional Note](#Additional-Note)
    - [Colour Scheme](#Colour-Scheme)
    - [Font](#Font)
    - [Navigation](#Navigation)
    - [Database Structure](#Database-Structure)

3. [Technologies](#Technologies)

    - [Languages Frameworks Tools](#Languages-Frameworks-Tools)
    - [Other-Resources](#Other-Resources)

    - [Features](#Features)

    - [Existing Features](#Existing-Features)
    - [Features-Left-to-Implement](#Features-Left-to-Implement)

4. [Testing](#Testing)

    - [Tools-and-Methods-Used-for-Testing](#Tools-and-Methods-Used-for-Testing)
    - [Tested Sections 1 HTML & CSS](#Tested-Sections-1-HTML-&-CSS)
    - [Tested Sections 2 Python](#Tested-Sections-2-Python)
    - [Unresolved Bugs](#Unresolved-Bugs)

5. [Deployment](#Deployment)

    - [How the project got deployed to Heroku](#How-the-project-got-deployed-to-Heroku)
    - [Cloning the repository](#Cloning-the-repository)
    - [How to access the live application](#How-to-access-the-live-application)
    - [How to run things locally](#How-to-run-things-locally)

6. [Credits](#Credits)
7. [Content](#Content)
8. [Acknowledgements](#Acknowledgements)
    <!--te-->

## About

An **Online Cookbook** web application that allows users to store and easily access cooking recipes.


#### Goal

Create a web applications which enables users to create, read, update and delete (CRUD) their online cookbook. Users can fabricate their recipe database by collecting recipes on the web and utilising the apply features. The application can be used by non-enrolled users who can use the app for browsing or the individuals who sign up for an account which allows access to the majority of the CRUD highlights.

The core focus of this project is on functional app logic created with **Python** while utilising the **Flask** framework and **MongoDB** NoSQL database.

#### Functionality (User Stories)

1. Enrollment and login 

2. View every one of the plans 

3. Channel and sort plans 

4. Search through every one of the plans dependent on a catchphrase 

5. Various select menus that permit barring plans containing certain allergen/allergens 

6. Enlisted clients can include plans 

7. Enlisted clients approach their very own Cook Book. Where they can see, alter and erase their plans 

Recipes get added to the application by means of a dynamic structure, that permits to: 

- Include/erase fixings/steps. 
- Include an image for every recipe recipe 
- Checkboxes that match allergens that the recipe contains 
- Pick an eating diet or cuisine

#### Initiation

Research to understand what apps of similar scope were already doing in terms of functionality which provided me with a list of what I consider to be feasible options for functionality implementations to acknowledge and consider pre-production.

[**To top**](#Table-of-Contents)

## UX

#### Layout Pro (Boundless Adaptability)

- Choosing a **multiple page application (MPA)** takes into consideration the choice to make new content and spot it on new pages. Multi-page applications can incorporate as much data as required, for this situation, numerous tickets, name enrolment page, donations page, account profile, with no page confinements. To say it necessarily, because there is a fair amount of content and features included on the application, I feel that an **MPA** is the best decision.

#### Layout Con (Moderate Speed and Execution)

- Being as this is a multi-page application, a server needs to reload most assets, for example, HTML, CSS, and **Python** with each interaction. When loading another page, the browser completely reloads page information and downloads all assets once more, even rehashed segments throughout all pages (for example the header/navigation) which influences Speed and Execution.

#### Tablet Display

- Please note, except a slight difference in page/scale responsiveness, desktop applies the same UI.

<img src="static/img/online-cookbook-sipo.herokuapp.com_(iPad Pro) (1).png" width="600">


#### Mobile Display

- This image represents the standard UI across most modern mobile devices.

<img src="static/img/online-cookbook-sipo.herokuapp.com_ (1).png" width="600">

#### Template Style

I opted for the [Materialize](https://materializecss.com/ "Materialize Official Site") framework. As a tool, Bootstrap is excellent to get started, but I feel it cannot create a real quality UI without the need to write a considerable amount of custom CSS to get anywhere close to the look and feel of Materialize which looks great even out of the box.

#### Font

- Being as the website modelling is off a vegetarian theme, the Josefin Sans Font Family choice was selected. The typeface is geometric, elegant, and has a vintage feeling; thus, helping to emphasise a soft natural vibe to the displayed text content which I felt was appropiate for a food app; a subjective opinion, of course.

#### Navigation

- A navigation bar takes up space and a fixed one even more. That being the case, and that there is a lot of content to display in the form of recipes, etc., I deemed it not necessary to fix the navigation as there was no real advantage.

#### Database Structure

```console
recipes: {
_id: 5d433657ddab2ebc9620c441
allergens: Array
diet: ""
cuisine: ""
ingredients: Array
method: Array
author: "string"
recipe: "string"
image: "https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/r..."
email: "string"
views: 10
likes: 3
dislikes: 0
time: "string"
date: "string"
}

```

```console
users: {
_id: 5d2dff3f9398ee10830e15f7
name: "string"
email: "string"
password: "string"
}

```

[**To top**](#Table-of-Contents)

## Technologies

#### Languages, Libraries & Frameworks

- [HTML](https://www.w3.org/TR/html5/ "HTML5 Official Site")
is a semantic markup language utilised as the shell of the site.

- [CSS](https://www.w3.org/Style/CSS/ "Cascading Style Sheets Official Site") means Cascading Style Sheets and was used on the design of the site.

- [Python](www.python.org) was utilised to compose the game logic.

- [Flask](https://flask.palletsprojects.com/en/1.0.x/) is a Python web framework, library used for developing web applications.

- [MongoDB](https://www.mongodb.com/) is a NoSQL database program, to implement a data-store using JSON-like documents with schema. 

- [Jinja2](http://jinja.pocoo.org/docs/2.10/) was utilised to render HTML templates, imparting between front-end and back-end.

- [jQuery](http://jquery.com/ "jQuery Official Site") is used for HTML document traversal and manipulation, event handling.

- [javascript](https://www.javascript.com/ "Javascript Official Site") is used to create responsive, interactive elements for web pages, enhancing the user experience.

- [Materialize](https://materializecss.com/ "Materialize Official Site") is utilised for developing the entire UI and consistent throughout, also including Material Design Icons courtesy of Google.

- [Google Fonts](https://fonts.google.com/ "Google Fonts Official Site") provides the Josefin Sans and sans-serif fonts applied across the entire website

- [Font Awesome](https://fontawesome.com/ "Fontawesome Official Site") is the source for the social media icons.

  #### Other Resources

- [w3schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Slack](https://slack.com/)

[**To top**](#Table-of-Contents)


## Features

#### Existing Features

- Home Page

  - It is used to access the user registration page field, account page, recipes page, create/edit page, sign out link, sign in/sign up page.

- Sign Up

  - I have used for a user to register for an account so they can log in into the app.

- Sign In

  - Used for a user to login to the app so to access and utilise all available features.

- MongoDB (NoSQL Database)

  - Stores recipe and user objects.

- Create Page
  - It is applied for a user to create recipe data.

- Edit Page
  - For user to update and delete recipe data.

- View Page
  - It is for a user to update and delete recipe data.

- Recipe Page
  - Allows a  user to read all recipes within the app.

- Account Page
  - Allows a user to read all recipes created by themselves.

#### Features Left to Implement

- Upgrade current and add additional sifting features
- Include tags on the recipe view page which contains a word or two offering additional recipe related details.
- Add the likelihood to include more than one picture or give pictures to each progression. 
- Include remarks area plans 
- Add capacity to transfer user photographs 
- Add capacity to alter user profile, change the username, password or email.

## Testing

#### Tools and Methods Used for Testing

- HTML

  - [Freeformatter](https://www.freeformatter.com/)

  - [The W3C Markup Validation Service](https://validator.w3.org/)

- CSS

  - [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator)

- Python

  - [Python Formatter](https://pythoniter.appspot.com/)

- Phones

  - Galaxy Note 3 (simulation and actual device)
  - Galaxy Note 9
  - Galaxy S5
  - Galaxy S9/S9+
  - iPhone 5/SE
  - iPhone 6/7/8 (simulated and real device)
  - iPhone 6/7/8 Plus
  - iPhone X
  - LG Optimus L70
  - Microsoft Lumia 550
  - Microsoft Lumia 950
  - Nexus 5X
  - Nexus 6P
  - Nokia 8110 4G
  - Pixel 2
  - Pixel 2 XL

- Tablets
  - iPad (simulation and actual device)
  - iPad Mini
  - iPad Pro (10.5-inch)
  - iPad Pro (12.9-inch) (simulated and real device)
  - Kindle Fire HDX
  - Nexus 10
  - Nexus 7

* Laptops

  - MacBook Pro (simulated and real device)
  - Asus UX 305 (simulation and actual device)

* Televisions
  - 1080p Full HD Television (simulated and real device)

- Website responsiveness was also tested by resizing the window with every addition of a new code sequence.

#### Tested Sections 1 HTML & CSS

- External links to third party websites and code authors GitHub repository.

- Checked button sizes so, they were responsive and large enough to be clicked.

- Ensured individual section headers resized and appeared well when viewed on various device screens and added opacity to the navigation bar to allow for more visibility of section header area on smaller devices.

- Spell checked all text content.

- HTML and CSS validation via [w3.org](https://www.w3.org/ "W3C Official Site").

- Checked margins and padding of the container (sections) to ensure the content within it did not look disproportionate on various screen sizes, individually smaller devices.

#### Tested Sections 2 Python

Manual testing was embraced for this application and acceptably passed. An example of the tests directed are as per the following:

- Tested route catches and hyperlinks all through the page.
- Tested the rationale of the application by looking at expected conduct against the database record information.
- Tested the responsiveness of the application on various programs and after that utilising multiple gadgets.

[**To top**](#Table-of-Contents)

#### Unresolved Bugs

1. On occasion, when loading the production application in on Heroku, the app will appear to look already signed in as the navigation bar shows the sign-out option which is not, in fact, the case and users will need to create an account in order to save new recipes, but as of yet the bug remains unresolved.

2. The CSS stylesheet is cached, which causes modification problems. New changes to the stylesheet are not visible until the browser cache clears—that is until it deletes the saved version and fetches the stylesheet from scratch again. That could be hours or days, during which time all that is available is an outdated version of the site’s CSS rules. This issue has prevented a preference for wanting to amend some of the general typography to a darker shade Hex colour to accommodate light shade backgrounds.

## Deployment

#### How the project got deployed to Heroku

1. Make a `requirements.txt` file utilizing the terminal command 'pip freeze > `requirements.txt`

2. Make a `Procfile` with the terminal command `echo web: python app.py > Procfile`

3. `git add` and `git commit` the new prerequisites from the requirements.txt file and Procfile, then 'git push' the undertaking to GitHub. 

4. Go to [Heroku](https://dashboard.heroku.com/) website.

5. Make another application (app) on the [Heroku](https://dashboard.heroku.com/) website by tapping the "New" button on your dashboard. Name your app, followed by selecting Europe as your region. 

6. Select application

7. In the "Deployment Method" section, check to see if the application is already connected to GitHub. If not connected then click the relevant button to link the Heroku website to the dashboard.

8. Affirm the connecting of the Heroku application to the right GitHub repository. 

9. In the application dashboard, click on "Settings" > "Reveal Config Vars". 

10. Set the accompanying config vars: 

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@cluster0-0oagu.gcp.mongodb.net/recipebook?retryWrites=true`

PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To retrieve your MONGO_URI please reference the official MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

11. On the dashboard click "Deploy or alternatively in the "Automatic Deployment" section enable "Automatic Deploys" (optional).

12. In the "Manual Deploy" section, set the branch to "master" then click "Deploy Branch."



#### Cloning the repository

1. Open in terminal
2. Change the present working directory to the area where you wish to place the cloned directory.
3. Clone the repository or use the link below.

```console
git clone https://github.com/sipostudent/Milestone-Project-4.git
```

Deploy your changes, make some changes to the code you just cloned and deploy them to Heroku using Git.

#### How to access the live application

- A live demonstration is accessible by clicking [here](http://online-cookbook-sipo.herokuapp.com/ "Live Demonstration: Veggit - Online Cookbook").

#### How to run things locally


1. Download the project onto a PC and open with a source-code editor.

2. In the run.py file set the IP address and the PORT to the following:

```console
'IP', '127.0.0.1'
```

```console
'PORT', '5000'
```

3. Install all of the prerequisites shown in the requirements.txt file via opening a Command-line interface (CLI) and navigating to the project root or by opening an integrated terminal and entering the following command:

> Please Note: The CLI method for interacting with a computer may vary dependant upon the operating system in use.

```console
pip install -r requirements.txt
```

4. Initiate the app by entering the following command into a relevant terminal:

```console
python run.py
```

5. A message in your terminal will inform you that the project is now running with the following message:

```console
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

6. To display the project, open the above URL (localhost:5000) 

[**To top**](#Table-of-Contents)

## Credits

#### Content

- Except for the app (online cookbook) recipes, all written content is original and created by the code author (Sipo Charles).

#### Media

- The source of all recipes utilised in the development phase of the app is  [bbcgoodfood.com](bbcgoodfood.com/recipes).

#### Acknowledgements

- I received inspiration for this project from visiting [thecookbookapp.com](https://thecookbookapp.com/), but mostly from my interaction with other students on Code Institute's Full Stack Software Development Programme.

#### Disclaimer

This project is for educational purposes only.

[**To top**](#Table-of-Contents)