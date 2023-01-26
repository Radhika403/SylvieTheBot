import telegram.ext 
from decouple import config

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
    
def resources(update, context):
    update.message.reply_text("TESTTT We have various playlists and articles available!")

def hackathonDetails(update, context):
    update.message.reply_text("Details of the hackathon are as follows")

def registration(update, context):
    update.message.reply_text("Follow the given steps t register yourself for the hackathon")
    
def queries(update, context):
    update.message.reply_text("Please type your queries")
    
def reminders(update, context):
    update.message.reply_text("Welcome to reminders")
    
def contact(update, context):
    update.message.reply_text("You can contact on the official mail id")

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
# disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()