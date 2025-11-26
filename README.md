# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Czedrick Marcelino

## Assignment
Assignment 1: Classes - Classes, Encapsulation and Unit Testing. This assignment uses Module 1 to develop classes to support a larger system.
Assignment 2: Applying Object-Oriented Design
Assignment 3: Design Patterns
Assignment 4: Programming Paradigms
Assignment 5: Algorithms, Help Files and Distribution

## Encapsulation
First I'll explain how encapsulation works. So encapsulation is basically when you put attributes and methods that operate data into a single unit, so in this case it would be the BankAccount class. Encapsulation with the BankAccount class helps the editor see what the code is about and makes it easier for them to manage. We also made the init attributes private by adding the double underscore so that other programmers are restricted from direct access to the attributes and this promotes data integrity. A user can also access the get_balance method but they do not know how the balance is stored so encapsulation hides the internal mechanics of the code and only shows what the user needs.

## Polymorphism
So polymorphism for python, polymorphism only works through inheritance. Polymorphism can only work if you use duck typing. So in this assignment, we used polymorphism with our methods such as get service charges and implemented these in our superclasses. So to make sure polymorphism works through inheritance, you have to allow a subclass to inherit attributes and methods from a superclass and the subclass can add new attributes, methods, or override existing ones. You also need to do some method overriding which allows the subclass to customize or redfeine how that method works. Dynamic binding is the last step to make sure polymorphism is implemented so the method gets excuted at runtime based on the actual objects class. So in our case, we passed our method that we made in our superclass so that we can modify it depending on the conditions we need in our different subclasses. So service charge does different things in all of the subclasses we have.

## Strategy Pattern
So we used the pattern strategy in our chequing account, investment account and savings account. This makes it so that we can add new strategies without modifying the context, meaning that since we are inheriting the strategy method from the superclass, we can change the method to however we want in the subclasses to apply to certain accounts. So in this case, we have 3 methods of calculate_service_charges but each of these service charges have different conditions, parameters and arguments. This makes our program scalable since we can always just add another strategy when needed if a new bank account pops up.

## Observer Pattern
So we used the observer pattern in our client, savings and chequing accounts. So we attached the client to the savings and chequing account so that when we run our main, it will contain the ALERT message to the large transaction or the low balance warning message as well. Through this, we can accurately determine when this transaction happend and what specific time. We also used this pattern to notify the client whether or not they had a suspicious transaction and low balance warning through the attach, dettach and notify methods in our bank account.py. The subscribed observers which are the attached clients which we used in main.py, the simulated emails should be generated when the transaction drops or is below the minimum threshold, in our case is $50.00. These emails then are sent into our output file.

## Event-Driven Programming Paradigm
So in this assignment, we used event-driven programming. We had an event where a user interacts with a button using pyside6 widgets. We also had an event handler which is where we connect a event, so a button click to a function. In our case, we had a function called on_lookup_client where once a user clicks the button to look up the client, this function would run, iterating through the dictionary finding what client number the user is trying to look for. We also had signals, which is our balance updated signal to communicate with our slot to call this function when a balance has been updated. This would update our dictionary depending on the user depositing or withdrawing money on a certain client and would also update our csv data. We also had event loops but these were given to us as our base framework.

## Filtering
Filtering was used in this assignment with the method of on filter clicked. So we check in each row if the filter text the user as inputted is true, hide the rows that do not match this filter and keep the rows that do match this filter on there.
We iterated through the account table to find which filter meets our user's requirements and show them on our UI. For example, we want to filter out other accounts that is not an investment account to client number 1001. It would 
display only investment accounts owned by that client and not the other accounts he/she has.