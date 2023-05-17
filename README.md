# CODED CREAM
Coded Cream is a program for an ice cream store. Salesmen can fill in the details of the order. Salesmen have just to follow the steps to fill in the details of the order.

![RUN PROGRAM](/assets/images/run-program.png)

## Flowchart
![FLOWCHART](/assets/images/flowchart.png)

## Features
I often go and look at Code Institute students' posts on LinkedIn to see their projects. This allows me to glean ideas and especially to better understand what to expect from a project on Python. It also allows me to start thinking about the project I would like to propose before I completely finish the lessons of the module.
I am impressed with the [My Sub My Way](https://github.com/shahid129/my-sub-my-way) from "shadid129". I really like this idea of offering a program that can record a command and still be relatively easy to use.
Moreover, the My Sub My Way project has a similar aspect with the Love Sandwiches project which is the fact of calling values stored in an Excel document and then recording the values filled in by the user. 
So I come up with a program that can offer to salesmen in an ice cream store. I am largely inspired by my own experience as a customer in the fabulous Berlin ice cream store Hockey Pockey. There are different options available, apart from simply choosing the ice cream flavor. The price to pay is just an addition of the different options chosen by the customer (type of cone, number of flavors chosen, addition of one or more toppings).  

![Order](/assets/images/complete-order.png)

However, my practice of Python is not yet up to my expectations. So I have to scale down my project and build something simpler. The "number 1" project that I have in mind at the beginning of my reflection will wait a little bit before seeing the day.

### Existing Features
The flow of the Coded Cream program is as follows: 
- The name of the customer is requested
- Validation of the entry
- A list of ice cream flavors is displayed
- Salesmen fill in the choosen flavor by indicating the corresponding number
- Validation of the entry
- Salesmen ask to the customer to say whether or not he/she would like to add a topping
- If the answer is no, the program goes directly to the calculation of the price to pay
- If the customer wants a topping, a list of different choices is displayed
- Vallidation of the entry
- The choice must be made by indicating the corresponding number
- Validation of the entry
- The price for an ice cream flavor and a topping is displayed

-__Global and Mutables Variables__
I know that using Global Variables is not a good practice. I just want to use local, global and mutable variables for this project to experiment with the different possibilities. 

-__Differents structures__
I choose to build differently my two parts of the code where the user has to choose a flavor and then a topping. For a real project, I would have chosen to build these two parts in a more or less identical way, keeping the same structure. Nevertheless for this project, I choose to multiply the structures in order to discover several ways of doing things. 

### Features Left to Implement
I have many ideas for this project. First, I need to practice Python a few more weeks, to better understand the logic, in order to realize them.

-__Several Selections__
First of all, I would like to be able to offer several selections of flavors and toppings. That the customer can order two or three flavors of ice cream and up to two toppings.

-__Discount condition__
I would like to offer a discount depending on whether the customer is a member of the loyalty program. If the customer is, a 15% discount will apply. If not, the customer has to fill in his email address in order to be subscribed to the newsletter and registered to the loyalty program.

-__Call data from Excel Document__
I would like, and this is the feature I am most interested in, to enter the values of the flavor choices, toppings and prices in an excel document. That way, if the flavors change or the prices fluctuate, the store staff can update this information directly, without my help and without having to "tweak the code". This could give them real autonomy.

-__Sava data order to Excel Document__
Moreover, I would like to record the values of the order (the name of the chosen flavors, the number of toppings, the email address, the price to pay...) in the same excel document filled previously, but in another sheet. This will allow the store manager or the sales manager to make statistics, studies on the details of the store sales.

-__Design__
Finally, as I am a visual person, I would like to propose a graphic interface.

This is the first flowchart I had in mind :
![FIRST-FLOWCHART](/assets/images/flowchart-first.jpg)

## Technology
This program is developed by the Python language.
It uses GitPod, GitHub and Heroku.

### Frameworks and packages
I install and import the Colorama module to have some colors in the code.

## Testing
| Problems                                                       | Actions                                                                 | Results                                                                                                                   |   |   |   |   |   |   |   |
|----------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---|---|---|---|---|---|---|
| ValueError                                                     | Add a try and except                                                    | If something with the wrong type is added, a sentence with explications is display                                        |   |   |   |   |   |   |   |
| IndexError                                                     | Change the structure and remplace by a else statement                   | The IndexError disappeared                                                                                                |   |   |   |   |   |   |   |
| Infinite loop in validate_flavor function when number too big  | Add a return False but it is not working or I use it in the wrong way. So I use a function call to come back to the first action with the flavor choice. I think it is not the good practice  | The Infinite loop is not running again, when the user adds a number too big, the program asks again for the flavor choice |   |   |   |   |   |   |   |
| "ModuleNotFoundError: No module named" on the deployed program | I install again the module, it was already done but I forgot to add the command "pip3 freeze > requirements.txt" to save the librairie                    | The error is gone on the deployed program and the user's inputs are green                                                 |   |   |   |   |   |   |   |
|                                                                |                                                                         |      



### Manual Testing
I do a lot of manual testing to see if the program responded correctly to each situation.
I test my input with symbols, letters instead of numbers for the choice of ingredients, or numbers instead of letters for the name.
For each type of error, I want an error message targeting exactly the error made so that the user could make a new action, this time correct.

### Validator Testing
I use the [CI Python Linter](https://pep8ci.herokuapp.com/) to check my Python code.

![PYTHON LINTER](/assets/images/python-linter.png)

### Unfixed Bugs
-__Both error messages__
In the differents_toppings() function, I want to have an error message adapted to each situation. A message that a number should be filled in if the user fills in a letter or a symbol. And a message that a number in the list of toppings choice must be filled in if the user fills in a number greater than 4. 

![BUG](/assets/images/bug.png)

I choose to put a "try" and "except". The latter welcoming the "ValueError" with the message corresponding to the wrong type of data filled in. However, my two error sentences mentioned above are launched. So it is not correct and confusing for the user. 
I remove the "try" and "except" by adding an "elif" with a "raise ValueError" with the corresponding message in my "if/else condition". 
Now it works correctly but the user is not offered a new input, so he has to start the program again from the beginning. I haven't found a solution for these both problems. I choose to display the correct message according to the error encountered. This is less confusing for the user but it is not perfect.

-__New entry not suggest again__
When the user enters a wrong character (letter or symbol) for the choice of the flavor, the program does not suggest a new entry. I try several things but I could not solve this problem.

![UNFIXED ERROR](/assets/images/unfixed-bug.png)  


## Resubmission  
Unfortunately the project doesn't pass the validation criterias. Indeed, I was unable to correct an error. When the user enters an invalid entry (number not present in the list, letter, symbol...) for the choice of the flavor, the choice to add or not a topping and the choice of the topping, it displays a message but stops the program. The user is then forced to restart his order from the beginning. The program displays an error message and asks the user to enter a new entry, which is the normal and usual procedure of the program, only for the customer's name. So I need to correct the rest of the program.  

I realize that I build my validations with two functions. When an erroneous number is entered, the program proposes a new entry, but it doesn't work with letters or others. One function, the if/else statement, works correctly but not the try/except. Moreover, for this last situation, two error messages follow one another, the message of the if/else function and the message of the try/except function.  

![TWO FUNCTIONS](/assets/images/two-functions.png)

So I need to combine the two functions into one. By wrapping the if/else function to validate if the number entered is correct in the try/except function which validates that the input is valid with a number.  
It is important to keep the try/except because without this function I can't handle invalid inputs, such as letters or symbols. So I remove the "raise ValueError" that I initially integrate to the differents_toppings function and that is not working properly.  
I build a little bit differently the functions choose_flavor and differents_toppings with the automatic conversion of the input to integer from the input and with a double validation if the input is indeed an integer and the number is less than or equal to 4.  

## Deployment
### Gitpod
I use Gitpod for this project. I use the [CI python essentials template](https://github.com/Code-Institute-Org/python-essentials-template) proposed by Code Institute in order to take advantage of the parameters already installed and predefined for Python.
I create a new repository of this template in order to save it in my workspace and to rename it. I launch Gitpod from this new repository.

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
I would like to thank my mentor Rory for all his precious advices, his help to better understand Python logic and his encouragement. And I would like to thank from the bottom of my heart my man, Stephane, who always has a word of encouragement and good vibes in the moments when I lose confidence in myself.