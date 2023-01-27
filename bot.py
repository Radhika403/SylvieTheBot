import telegram.ext 
from decouple import config
from datetime import date
import csv
import time

USERNAME = config('USERNAME')
TOKEN = config('TOKEN')

def start(update, context):
    update.message.reply_text("""Hello!
    Type /help to see the available commands 
    """)
    
def help(update,context):
    update.message.reply_text("""
    The following commands are avilable:
    
    /help -> This message
    /hackathonDetails  -> Get all the details about the Hackathon!!
    /registration -> Register yourself for the hackathon here
    /resources -> Dive in to explore the resources
    /queries -> Post your queries here
    /reminders -> Set a reminder here
    /contact -> contact information 
    """)
    
def hackathonDetails(update, context):
    update.message.reply_text("Details of the hackathon are as follows")

def resources(update, context):
    update.message.reply_text("""You can refer to the following resources -
    https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e
    https://medium.com/spidernitt/how-to-create-your-own-telegram-bot-63d1097999b6

    These sample projects can also 
    """)

# def record_details(details):
#     f = open

def record_details(details):
    file = open('resgitrationDetails.csv', 'a+', newline ='')
 
    with file:   
        write = csv.writer(file)
        write.writerow(details)

def is_invalid(number):
    if len(number) != 10:
        return True
    
    digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in number:
        if int(i) not in digits:
            return True
    return False

def register(update, context):
    update.message.reply_text("""Welcome to the registration portal. Please provide the following details""")
    update.message.reply_text("No of team Members")
    members = update.message.text
    print(members)
    update.message.reply_text("Team Name")
    time.sleep(5)
    team_name = update.message.text
    member_details = [members, team_name]
    # for i in range(1, members + 1):
    #     update.message.reply_text("Full Name for member " + i)
    #     name = update.message.text
    #     update.message.reply_text("Email Address for member " + i)
    #     email = update.message.text
    #     while '@' not in email or "." not in email:
    #         update.message.reply_text("Please Enter valid email")
    #         email = update.message.text
    #     update.message.reply_text("Mobile Number for member " + i)
    #     number = update.message.text
    #     while is_invalid(number):
    #         update.message.reply_text("Please Enter valid 10 digit mobil number")
    #         number = update.message.text
    #     now = date.today()
    #     member_details.extend([name, email, number, now])
        # print(member_details)
        # record_details(member_details)  

def registration(update, context):
    update.message.reply_text("""The following commands are avilable:
    
    /register -> Register yourself for the hackathon
    /confirm  -> Confirm your registration
    /cancel -> Cancel your registration""")
    
    # user_input = update.message.text

    
def queries(update, context):
    update.message.reply_text("Please type your queries")
    
def reminders(update, context):
    update.message.reply_text("Welcome to reminders")
    
def contact(update, context):
    update.message.reply_text("You can contact on the official mailID - ")

# def handle_message(update, context):
#     update.message.reply_text(f"You said {update.message.text}, use the commands using /")


# Token = (" ")
#print(bot.get_me())
updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
disp.add_handler(telegram.ext.CommandHandler('hackathonDetails',hackathonDetails))
disp.add_handler(telegram.ext.CommandHandler('registration',registration))
disp.add_handler(telegram.ext.CommandHandler('resources',resources))
disp.add_handler(telegram.ext.CommandHandler('queries',queries))
disp.add_handler(telegram.ext.CommandHandler('reminders',reminders))
disp.add_handler(telegram.ext.CommandHandler('contact',contact))
disp.add_handler(telegram.ext.CommandHandler('register',register))
# disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()