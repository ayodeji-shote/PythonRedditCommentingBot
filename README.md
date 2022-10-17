# PythonRedditCommentingBot
This is a reddit bot that searches through a specific sub reddit and responds to a specific comment then prints the author of that comment in a separate file. It uses the python extension Praw, and also the reddit api 


The Requirments are 
Python
Praw
A Reddit Account

Prerequisites:
1 Go to reddit and navigate to the app page or click this link https://www.reddit.com/prefs/apps/ 
2 Click create an app and select the type script while putting in your app name
3 You dont need to put something for the description or the about url but for the redirect uri past this in http://localhost:8080 
Not the outputted client id and secret.(The secret is sent to the mail thats connected to your reddit account or it is displayed below the personal use script).

Important files
Details.py keep the names the same otherwise praw doesnt know what to search for.
username: The username of your reddit account 
password: your reddit password
client_id: The client id mentioned before 
client_secret: The secret mentioned before
