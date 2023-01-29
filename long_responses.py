import random

q1 = "The registration for the hackathon can be done by 18th february 2023. The problem statements will be released on 24th February and the hackathon is scheduled for 25-27th February 2023. Winners will be announced by 1st March."
q2 = "Maximum no of people in a team is 3."
q2_ = "Maximum no of people allowed is 3."
q3 = "Yes, you can participate individually and in teams upto 3 members."
q4 = "You'll be required to make a working telegram bot as per various problem statements taht will be shared on 24th Feb."
q5 = "1. You need to register yourself by entering your details latest by 18th Feb.\n2. You need to chose a problem statement out of the sets that will be released by 24th Feb. Develop a working prototype handling all test cases in the development period that starts from 25th Feb and lasts upto 27th Feb.\n3. Submission must be made by 27th Feb midnight.\n4. You can use open source libraries but do not copy the code.\n5. Your prototype must be your own, plagiarism in code is strictly prohibited.\n6. You must add a demo video to your submission alongside the repository containing your code.\nCAN'T WAIT TO MEET YOU AT THE HACKATHON!!"
q6 = "The winner will get a cash prize of Rs 10000/- along with certificates.\nThe top 3 submissions will get a cash prize of Rs 5000/- along with certificates.\nNext 10 teams will be given runner up certificates with a cash prize of Rs 1000/- each.\nAll participants will get a certificate of participation.\n ISN'T THAT AMAZING???"
q7 = "The hackathon will take place remotely. You can access the problem statements online, develop your prototypes and submit them by 27th Feb. The winners will be announced in an in-person event at IGDTUW on 1st March starting from 10:00 AM."
q7_ = "The hackathon will take place remotely. You can access the problem statements online, develop your prototypes and submit them by 27th Feb. The winners will be announced in an in-person event at IGDTUW on 1st March starting from 10:00 AM."
q8 = "The last date to fill out the registration form is 18th February, 2023."
q9 = "You can use the following resources : https://www.youtube.com/watch?v=PTAkiukJK7E.\nYou can also refer to the following sample projects - https://www.youtube.com/watch?v=CNkiPN_WZfA"
q10 = "You need to submit a working telergram bot. Programming language and deployment tech stacks can be chsoen by you according to your comfort."
q11 = "Sorry! I cannot provide you with any technical or financial assistance."
q12 = "Yes, you can use '/reminder' to set a reminder"
q13 = "Sure, to check your registeration deatils head to /registration -> /confirm."
q14 = "No the details remain the same -->The registration for the hackathon can be done by 18th february 2023. The problem statements will be released on 24th February and the hackathon is scheduled for 25-27th February 2023. Winners will be announced by 1st March. "
q15 = "Sure! 'Bots Around Us' hackathon is a student-led event that brings together students from different universities to work on innovative projects. It will take place on the weekend of 25-27th february 2023, and will be held at online."
q15_ = "'Bots Around Us' hackathon is a student-led event that brings together students from different universities to work on innovative projects. It will take place on the weekend of 25-27th february 2023, and will be held at online."
q16 = "You can register on our website by 18th Feb or you can register using the '/register' command here."
q17 = "Sure, you can use the '/contact' for getting the contact details of our organisers."
q17_ = "Sure, you can use the '/contact' for getting the contact details of our POCs."
q18 = "Unfortunately no. I have been designed to provide information about the 'Bots Around Us' hackathon only."
q19 = "You get to collaborate and compete with students from different universities and develop a telegram bot. You stand to win exciting cash prizes and certificates. It's an opoprtunity to learn, develop and present your protypes and seek feedback on the same."
q20 = "Yes, I'll be happy to answer that :)"
q21 = "Hmm there are a list of reason. I don't know where to start. There is a prize pool of Rs.10,0000. In addition to this, you will gain experience of participating and competing with India's top mind. Top winners will also get a chance to sit for interview round of some top notch companies like Microsoft ;)\nWHAT ARE YOU WAITING FOR?\n REGISTER NOW !!"
q22 = "Yes you can participate alone or in a team of upto 3 members"
q23 = "No, intercollege teams are not allowed"
q24 = "Even I want to see you there sugarcup!! Head to /register to register yourself for the hackathon."
q25 = "Anyone currently enrolled in a university is allowed to participate in this hackathon. Apart from that some important factors like excitement,zeal to learn etc. are also required.\nhehehehe"
q24_ = "Even I want to see you participate honeycup!! Head to /register to register yourself for the hackathon."
q25_ = "Anyone who is currently enrolled in a university is allowed to participate in this hackathon. Apart from that, some important factors like excitement,zeal to learn etc. are also required.\nhehehehe"
q26 = "Hackathon is scheduled for 25-27th February 2023. The registrations are open till 18th February."
q27 = "Submission deadline is 27th February 2023."
q28 = "Judgement Criteria: The bot that meets all the testcases and is most interactive and creative wins!!"
q28_ = "Judging Criteria: The bot that meets all the testcases and is most interactive and creative wins!!"
q29 = "Head to /registeration -> /register"
q30 = "Head to /registeration -> /cancel"
q31 = "Sorry! I am not allowed to disclose that. The Judge will be announced on the start day of Hackathon"
q32 = "You can use the /help option to see possible commands"
q33 = "Yes! I believe in you. You will get to learn so much from this hackathon and collaborate with other students. You should surely give this a chance. ou might just win as well."

def unknown():
    response = ["Could you please re-phrase that? ",
                "Hmm I'll work on understanding this, But till then please rephrase it :)",
                "I think you have misspelled it dear",
                "What does that mean?","Sorry! I am unable to understand it"][
        random.randrange(5)]
    return response