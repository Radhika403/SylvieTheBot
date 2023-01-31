### Sylvie - The Bot
![Alt](images/SylvieTheBot.jpeg)

Our witty bot “Sylvie” is designed to solve all the hackathon related queries and issues that a participant faces. 

It offers the users various functionalities like:
1) Seeking the hackathon details (details, schedule, prize, rules)
2) Handles the registration process (register,confirm and even cancel)
3) Provides resources to the user.
4) Sets a reminder for the user based on the custom date and time entered.
5) Chat feature which provides solutions to all the FAQ’s.

Some feature which acts as an icing on the cake are:
1) Cancel registration
2) Take feedback from the user if he/she cancels the registration.
3) Gives all the latest updates and announcements that the admin sends.
4) Engaging messages that use emojis.
5) Is able to understand any language that the user enters.

Along with all these functionalitites, it acts as a fun & motivating friend who is always there throughout the interaction.

![Alt](images/FlowChart.png)

### Tech Stacks
1. Python: python-telegram-bot (13.7), googletrans (3.1.0a0), emoji, datetime, time, csv, os/python-decouple
2. Replit: The deployment of this bot is done with the help of replit. The platform is used to host and share our bot.
3. NLP: Handles the /chat section of the bot. Uses the bag of words to identify the closest response.
4. Files as database: 
Csv files are used to store data of registered students. It is also used to fetch data for confirmation and cancellation. 
Text Files are also used to store feedback.

![Alt](images/WorkingBot.png)
