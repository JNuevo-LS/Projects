import random
import time
answers = ['It is most certainly so', 'Undeniably', 'Ask again later', 'I cannot say', 'My sources say no', 'My sources say yes',
           'Yes', 'No', 'Do not bother me with such trivial questions', 'It is a secret', 'False', 'True', 'Ask yourself',
            'I cannot tell for now', 'I must gather more information', 'Do not ask questions for which you know the answer',
            'Do not bother me', 'Of course', 'Possibly', 'Ask in 5 minutes', 'Leave me alone']

questions = 1

yes = ['yeah','yes', 'affirmative', 'true', 'one more', 'a few more', 'correct']
no = ['no', 'false', 'nah', 'no more questions', 'no more question', 'nope']

while questions >= 0:
    if questions > 0:
        question = input('What do you wish to know? ')
        if question != False:
            print('Thinking...')
            time.sleep(0.8)
            print(answers[random.randint(0, 19)])
            questions -= 1
    if questions == 0:
        question2 = input('Do you have any more questions? ').lower()
        if question2 in yes:
            questions = 1
        elif question2 in no:
            quit
        else:
            print('ANSWER ME!')
        