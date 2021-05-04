# catFacts

A Simple Python App to send people cat facts. 

Utilises https://catfact.ninja/ API to pull facts then sends via a Twilio Account to your recipient.

###### Requirements(Python Modules):
* Requests - To make the requests
* Twilio - For the SMS functions
* Api - API functions
* Tkinter - UI
* Traceback - For the stack traces

###### Notes:
Currently In progress. 

The app can (currently) send multiple SMS messages to a single number. You can set the number of messages to send. 
Don't do too many (I've gone up to 500).

###### Roadmap:

The plan for the future is to add the ability to send the SMS to multiple numbers at once by adding an 'Add Number' 
function that is dynamically added when a user clicks the 'Add Number button'. It will pop up a new number entry field.

Additionally I'll be adding the ability to set your own delay, and also schedule these to go out at dates/times 
of the user's choosing.

Next big thing is to package it for installation as a standalone.

Long term, I'm planning to redo the ui with Electron to be available on Mobile/Desktop and look nicer.
###### Roadmap Summary:

* Update UI with Electron
* Package for standalone install
* Add configurable Delay
* Add Scheduling
* Add Multi-Number SMS sending


4/24: 
Fixed - 
* Send Button
* Added Popup
* Added Random frequency triggered by send

5/4: Increased random delay to 60 seconds rather than 5. For more fun.