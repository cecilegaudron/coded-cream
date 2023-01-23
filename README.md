# CODED CREAM
Coded Cream is a program for an ice cream store. Salesmen can fill in the details of the order. Salesmen have just to follow the steps to fill in the details of the order.

## Flowchart
![FLOWCHART](/assets/images/flowchart.png)

## Features
I often go and look at Code Institute students' posts on LinkedIn to see their projects. This allows me to glean ideas and especially to better understand what to expect from a project on Python. It also allows me to start thinking about the project I would like to propose before I completely finish the lessons of the module.
I was impressed with the [My Sub My Way](https://github.com/shahid129/my-sub-my-way) from "shadid129". I really liked this idea of offering a program that can record a command and still be relatively easy to use.
Moreover, the My Sub My Way project had a similar aspect with the Love Sandwiches project which was the fact of calling values stored in an Excel document and then recording the values filled in by the user. 
So I came up with a program that could be offered to salespeople in an ice cream store. I was largely inspired by my own experience as a customer in the fabulous Berlin ice cream store Hockey Pockey. There are different options available, apart from simply choosing the ice cream flavor. The price to pay is just an addition of the different options chosen by the customer (type of cone, number of flavors chosen, addition of one or more toppings).

However, my practice of Python is not yet up to my expectations. So I had to scale down my project and build something simpler. The "number 1" project that I had in mind at the beginning of my reflection will wait a little bit before seeing the day.

### Existing Features
The flow of the Coded Cream program is as follows: 
- The name of the customer is requested
- A list of ice cream flavors is displayed
- The customer is asked to fill in the chosen flavor by indicating the corresponding number
- The customer is asked to say whether or not he/she would like to add a topping
- If the answer is no, the program goes directly to the calculation of the price to pay
- If the customer wants a topping, a list of different choices is displayed
- The choice must be made by indicating the corresponding number
- The price for an ice cream flavor and a topping is displayed

### Features Left to Implement
I have many ideas for this project. First, I need to practice Python a few more weeks, to better understand the logic, in order to realize them.

- __Several Selections__
First of all, I would like to be able to offer several selections of flavors and toppings. That the customer can order two or three flavors of ice cream and up to two toppings.

- __Discount condition__
I would like to offer a discount depending on whether the customer is a member of the loyalty program. If they are, a 15% discount will apply. If not, the customer has to fill in his email address in order to be subscribed to the newsletter and registered to the loyalty program.

- __Call data from Excel Document__
I would like, and this is the feature I am most interested in, to enter the values of the perfume choices, toppings and prices in an excel document. That way, if the fragrances change or the prices fluctuate, the store staff can update this information directly, without my help and without having to "enter the code". This could give them real autonomy.

- __Sava data order to Excel Document__
Moreover, I would like to record the values of the order (the name of the chosen perfumes, the number of toppings, the choice of the booklet, the email address, the price to pay...) in the same excel document filled previously, but in another sheet. This will allow the store manager or the sales manager to make statistics, studies on the details of the store sales.

- __Design__
Finally, I am a visual person, I would like to propose a more graphic interface.

This is the first flowchart I had in mind :
![FIRST-FLOWCHART](/assets/images/flowchart-first.jpg)

## Technology
This program is developed by the Python language.
It uses GitPod, GitHub and Heroku.

### Frameworks and packages
I install and import the Colorama module to have some colors in the code. I use this 

## Testing
### Manual Testing
I do a lot of manual testing to see if the program responded correctly to each situation.
I test my input with symbols, letters instead of numbers for the choice of ingredients, or numbers instead of letters for the name.
For each type of error, I want an error message targeting exactly the error made so that the user could make a new action, this time correct.

### Validator Testing
I use the [CI Python Linter](https://pep8ci.herokuapp.com/) to check my Python code.

## Deployment

### Gitpod
I use Gitpod for this project. I use the [CI python essentials template](https://github.com/Code-Institute-Org/python-essentials-template) proposed by Code Institute in order to take advantage of the parameters already installed and predefined for Python.
I create a new repository of this template in order to save it in my workspace and to rename it. I then launched Gitpod from this new repository.

### Deployment on Heroku
- Create a list of requirements, the program needs it to run
- Go to requirements.txt and enter on the terminal : pip3 freeze > requirements.txt
- Save and push the code on Github
- We need an account on Heroku. It is possible to create a free account.
- Create a new app on the dashboard of Heroku and name the project (the name should be unique)
- On the Settings tab, it needs to add parameters to the Config Vars section. Create a cong var to add informations from the creds.json (connect the Heroku app with the settings about spreadsheet). And it needs to create another config var with the information PORT for keys and 8000 as value.

![Config Vars Settings on Heroku](/assets/images/heroku-config-vars.png)

- It needs to add some buildpacks : Python, node.js.
- On the Deploy tab, select on GitHub as the deployment method. To connect to GitHub, click on the Search button to see all repositories on GitHub. Click on the connect button to connect the project with the Heroku app.
- Select “Manuel deploy” and see the different packages be installed. 
- At the end of the deployment, click on the View button to see the app running. It is also possible to test the program. 
- Finally select the button “Enable Automatic Deploys”. This allows automatic deployment when the "add push" line is filled in the working document.

The site is live here : [Deployed Coded Cream project](https://coded-cream.herokuapp.com/)

## Credits
I got ideas and good explanations with examples from : 

- Love Sandwiches project
- [W3schools](https://www.w3schools.com/)
- [Universite Paris Diderot](https://python.sdv.univ-paris-diderot.fr/)
- [Sametmax2.com](https://sametmax2.com/)

### Acknowledgement
I would like to thank my mentor Rory for all his precious advice, his help to better understand Python logic and his encouragement.