#!/usr/bin/python
# -*- coding: utf-8 -*-


parts_of_speech = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__",
                   "__7__", "__8__", "__9__", "__10__", "__11__", "__12__", "__13__"]
sample_easy = "who said english is easy ?\nfill this blanks with yes or No.....\n1. __1__ i don't have a brain.\n 2.__1__ I don't have sense.\n 3. __1__ i am stupid.\nTry to fill .\n All the best!!!"
sample_medium = "Decide whether you have to use much or many:\nWe saw __1__ animals at the zoo.\nHow __1__ oranges did you put in the box?\nThere isn’t __2__ sugar in my coffee.\nI don’t have __1__ friends.\nThe old man hasn’t got __2__ hair on his head.\nI’ve packed __1__ bottles of water.\nI didn’t get __2__ sleep last night.\nHow __2__ fruit do you eat in an average day? "
sample_hard = "Read the story given below and fill in the blankswith appropriate verb forms.\nOnce upon a time there __1__ (live) a man called Damocles.\nA friend of his eventually __2__ (become) the ruler of a small city.\nDamocles thought, ‘How lucky my friend __3__ (be).\nHe __3__ (be) now a ruler. He must __4__ (have) a great time.\n He __5__ have fine clothes, lots of money and a number of servants.\nI wish I __6__ (have) his luck’.He __7__ (decide) to visit his\nfriend to enjoy his hospitality.When he __8__ (reach) the palace,\n the king himself __9__ (receive) him with respect and affection.\nDamocles then __10__ (tell) the king that he __11__ (be) indeed\na lucky man. The king __12__ (smile).He __13__ (invite) his friend\nto have dinner with him."


answer_medium = ["many", "much"]
answer_hard = ["lived", "became", "is", "must be having", "must", "had",
               "decided", "reached", "received", "told""was", "smiled", "invited"]
answer_easy = ["no"]

# começando o jogo com o jogador escolhedo o nivel que ele prefere esses sendo entre fácil,medio e difícil.
# quando o jogador informar o nível de dificuldade ele será diretamente
# direcionado ao nível selecionado
# espero que goste do my quiz :)


def choose():
    print "Welcome to my Quiz!!!\nPlease select a game difficulty by typing it in!"
    level = raw_input("Possible choices include easy, medium, and hard: \n")
    while level not in ["easy", "medium", "hard"]:
        print "That's not a option!!!! \nPlease try it again!!!"
        return choose()
    if level == "easy":
        print "\nYou choose easy!" + "\n\n" + sample_easy
        print play(sample_easy, answer_easy, parts_of_speech)
    elif level == "medium":
        print "\nYou choose medium!" + "\n\n" + sample_medium
        print play(sample_medium, answer_medium, parts_of_speech)
    elif level == "hard":
        print "\nYou choose hard!" + "\n\n" + sample_hard
        print play(sample_hard, answer_hard, parts_of_speech)
    if __name__ == "__main__":
        try:
            choose()
        except SystemExit, e:
            print(e)

            # com o nivel selecionado aqui que todo o jogo acontece ele terá no total de 4 tentativas
            # se ele acertar o primeiro blank ele passará para a próxima senão vai ficar no mesmo blank
            # até ele acertar ou as sua tentativas acabarem.


def play(string, answer, replacement):
    i = 0
    tries = 4
    while i != len(answer):
        user_input = raw_input("What is the answer to blank " + replacement[i] + '?')
        if user_input != answer[i]:
            tries -= 1
            if tries == 0:
                print "Game Over"
                break
            print "Sorry!!! \nTry again you have %d try left!" % (tries)
        else:
            tries = 4
            string = string.replace(replacement[i], answer[i])
            print ":) \nCongratulations!\n\n\n\n" + string
            i += 1
    return string


choose()
