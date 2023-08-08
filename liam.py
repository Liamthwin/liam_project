import os
def Q_one():
    ask=input("Are u sure to answer?: ")
    if ask=="yes"or ask=="Yes":
        question1()
def question1():
    quest=input("What is 8+8?")
    if quest=="16":
        question2()
def question2():

    quest1=input("What is 9*2?")
    if quest1=="18":       
        question3()
def question3():
    quest2=input("What is 10-10?")
    if quest2=="0":
     question1()
def question4():
    quest3=input("What is 10-8?")
    if quest3=="2":
        question1()
Q_one()



    




