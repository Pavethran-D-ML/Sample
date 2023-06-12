import pandas as pd
import random

def getExcel():
    excel_file = 'https://raw.githubusercontent.com/Pavethran-D-ML/Sample/master/questions.xlsx'
    return pd.read_excel(excel_file)

def getTopic():
    print('''
    Enter the Topic:
    1. Python
    2.Java
    3.C++''')
    topic_code = int(input("Enter the topic: "))

    topic_dict = {1: 'python', 2: 'java', 3: 'c++'}
    return topic_dict.get(topic_code, 'python')

def getTopicQuestions(df,topic):
    return df[df['topic'] == topic].values

def askQuestion(df_selected,score):
    while True:
        question = random.choice(df_selected)
        print(question[1])
        answer = input('Enter the answer : ')
        if str(answer) == str(question[2]):
            print('Your answer is correct....')
            score =  score + 1
        else:
            print('Your answer is wrong')
        print('Did You Like to Continue...? Y/N :')
        flag = input('Enter:')
        if flag in {'N', 'n'}:
            print('Total Score:',score)
            break
        print('score is ',score)

if __name__ == "__main__":
    score = 0
    df = getExcel()
    topic = getTopic()
    df_selected = getTopicQuestions(df,topic)
    score = askQuestion(df_selected=df_selected,score=score)
    