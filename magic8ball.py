import random
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
print('Hello World, I am the Magic 8 Ball, What is your name?')
name = input()
print('Hello ' + name)


def Magic8Ball():
    print('')
    print('Ask me a question.')
    input()
    print('')
    print (answers[random.randint(0, len(answers)-1)] )
    print('')
    print('I hope that helped!')
    Replay()
    

def Replay():
    print('')
    print ('Do you have another question? [Y/N] ')
    reply = input()
    if reply == 'Y':
        Magic8Ball()
    elif reply == 'N':
        exit()
    else:
        print('I apologize, I did not catch that. Please repeat.')
        Replay()

		
Magic8Ball()
