import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', 'greetings'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how','are','you'])
    response('You\'re welcome!', ['thank', 'thanks','thankyou'], single_response=True)
    response('Thank you!', ['i', 'love', 'you'], required_words=['love', 'you'])
    response('Great to hear!',['fine','good','doing','well'],single_response = True)
    response('I am Sylvie-the bot! I am here to guide you through this journey',['who','are','you'],required_words = ['who','are','you'])
    # Longer responses
    response(long.q1, ['what','schedule','timeline'],required_words= ['schedule','timeline'] )
    response(long.q2,['maximum','team','size'],required_words = ['team','size'])
    response(long.q2_,['team','limit'],required_words = ['team','limit'])
    response(long.q3,['participate','team','can'],required_words = ['team','can'])
    response(long.q4,['do','requirements','hackathon'],required_words = ['requirements'])
    response(long.q5,['rules','hackathon'],required_words = ['rules'])
    response(long.q6,['prizes'],required_words = ['prizes'])
    response(long.q7_,['where','place','location'],required_words = ['location'])
    response(long.q7,['where','place'],required_words = ['place'])
    response(long.q8,['deadline','participate','registration','hackathon'],required_words = ['deadline'])
    response(long.q9,['prepare','resources','resource','material'],required_words = ['resources'])
    response(long.q10,['what','techstacks','tech','stacks'],required_words = ['tech','stacks'])
    response(long.q11,['technical','financial','assistance'],required_words = ['assistance'])
    response(long.q12,['set','give','reminders'],required_words = ['reminder','set'])
    response(long.q13,['confirm','registration'],required_words = ['confirm','registration'])
    response(long.q14, ['updates','update','changes','notice','notices','change','hackathon','hackathons'],required_words = ['updates'])
    response(long.q15_,['about','hackathon'],required_words = ['about','hackathon'])
    response(long.q15,['what','hackathon'],required_words = ['what','hackathon'])
    response(long.q16,['how','register','hackathon'],required_words = ['how','register'])
    response(long.q17,['talk','organizer','coordinator','contact'],required_words = ['talk'])
    response(long.q17_,['talk','contact'],required_words = ['contact'])
    response(long.q18,['provide', 'information', 'other' ,'events','hackathons','hackathon','event'],required_words = ['other','event'])
    response(long.q19,['what','for','me'],required_words = ['what','for','me'])
    response(long.q20,['ask','question'],required_words = ['ask','question'])
    response(long.q21,['why','participate','hackathon'],required_words = ['why','participate'])
    response(long.q22,['participate','alone','individually'],required_words = ['individually','participate'])
    response(long.q23,['intercollege','different','college','team'],required_words = ['intercollege','team'])
    response(long.q24_,['i','want','participate'],required_words = ['i','want','participate'])
    response(long.q24,['how','can','participate'],required_words = ['how','can','participate'])
    response(long.q25,['eligibility','criteria','what'],required_words = ['eligibility','criteria'])
    response(long.q25_,['who','participate','can'],required_words = ['who','can','participate'])
    response(long.q26,['dates','date','hackathon'],required_words = ['dates','hackathon'])
    response(long.q27,['submission','deadline'],required_words = ['submission','deadline'])
    response(long.q28_,['judging','criteria'],required_words = ['judging','criteria'])
    response(long.q28,['judgement','criteria'],required_words = ['judgement','criteria'])
    response(long.q29,['steps','register'],required_words = ['steps','register'])
    response(long.q30,['cancel','registeration'],required_words = ['cancel','registeration'])
    response(long.q31,['who','judge'],required_words = ['who','judge'])
    response(long.q32,['commands','functionalities','how'],required_words = ['commands'])
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    #print(response)
    return response