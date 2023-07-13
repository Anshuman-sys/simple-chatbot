import random

var1 = ['hi', 'hello']
var2 = ['how are you?', 'how are you doing?', 'how is your health?']
var3 = ['what is your name?', 'how do i call you?', 'your name please']
var4 = ['which programming language want do you learn?', 'what should i learn?']
var5 = ['what are your hobbies?', 'what do you do in your free time?']
var6 = ['good morning']
var7 = ['how was your day?']
var8 = ['can you speak english']
var9 = ['did you have fun at the party?']
var10 = ['see you later dinobot']
while(True):
    user_input = input("Anshuman said to bot :")

    if user_input.lower() in var1:
        bot_1 = ['Hello', 'Hi']
        print('Bot replied to Anshuman : ' + random.choice(bot_1)+'\n')

    elif user_input.lower() in var2:
        bot_2 = ['I am good', 'I am doing good', 'I am fine']
        print('Bot replied to Anshuman : '+random.choice(bot_2)+'\n')

    elif user_input.lower() in var3:
        bot_3 = ['MY name is Dinobot', 'You call me Dinobot', ' I am Dinobot']
        print('Bot replied to Anshuman : '+random.choice(bot_3)+'\n')

    elif user_input.lower() in var4:
        bot_4 = ['python', 'Python programming language']
        print('Bot replied to Anshuman : '+random.choice(bot_4)+'\n')

    elif user_input.lower() in var5:
        bot_5 = ['My hobbies is : Lerning new things day by day with programming language','Learn programming language i.e python']
        print('Bot replied to Anshuman : '+random.choice(bot_5)+'\n')

    elif user_input.lower() in var6:
        bot_6 = ['good morning sir -how may  can i help you?']
        print('Bot replied to Anshuman : '+random.choice(bot_6)+'\n')

    elif user_input.lower() in var7:
        bot_7 = ['Its been great,and yours?']
        print('Bot replied to Anshuman : '+random.choice(bot_7)+'\n')

    elif user_input.lower() in var8:
        bot_8 = ['Yes ,of course sir.']
        print('Bot replied to Anshuman : '+random.choice(bot_8)+'\n')

    elif user_input.lower() in var9:
        bot_9 = ['No, I did not.']
        print('Bot replied to Anshuman : '+random.choice(bot_9)+'\n')

    elif user_input.lower() in var10:
        bot_10 = ['Have a good day sir.']
        print('Bot replied to Anshuman : '+random.choice(bot_10)+'\n')

else:
        print('Bot replied to Anshuman :-Sorry what are you asking?\n')