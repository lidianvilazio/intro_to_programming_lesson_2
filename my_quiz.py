#!/usr/bin/python
# -*- coding: utf-8 -*-


parts_of_speech = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__",
                   "__7__", "__8__", "__9__", "__10__", "__11__", "__12__", "__13__"]
sample_easy = "Fill in the blanks with the proper tense or form of the verb given in the brackets.\n1. He  __1__ (win) a prize for standing first in the quiz competition.\n2. Have you  __2__ (carry out) my instructions?\n3.I  __3__ (wait) since morning.\n4.The box was so heavy that the boy  __4__ (can) not lift it.\n5. When I saw the child, he  __5__ (cry).\n6.I  __6__ (go) to my native place a week ago.\n7.We got our roof  __7__ (repair) before the rainy season set in.\n8.Not one of them dreamt of doing what he never  __8__ (attempt) to do.\n9. She  __9__ (reach) the railway station before the train came.\n10.I  __10__ (leave) school last year."
sample_medium = "Fill in the blanks with appropriate forms of the verb given in the brackets.\n1.We usually go to Singapore on a holiday, but this year we  __1__ (go) to Bangkok.\n2.Heat  __2__ (expand) and cold  __3__ (contract).\n3.A good player  __4__ (practice) every day.\n4.John usually  __5__ (drink) coffee in the morning, but today he  __6__ (drink) tea.\n5.The child  __7__ (suffer) from pneumonia since last week.\n6.He  __8__ (write) a novel since October last, and he is about to finish it.\n7.If he  __9__ (work) hard, he will pass.\n8.I  __10__ (help) you if I had had money.\n9.Time and tide  __11__ (wait) for no man.\n10.By this time next year he  __12__ (complete) the construction of his house.\n11.Whenever he is in London, my father  __13__ (stay) with a friend of his.\n12.He  __14__ (court) her for two years now, but he  __15__ (not propose) to her yet."
sample_hard = "Read the story given below and fill in the blanks with appropriate verb forms.\nOnce upon a time there __1__ (live) a man called Damocles.\nA friend of his eventually __2__ (become) the ruler of a small city.\nDamocles thought, ‘How lucky my friend __3__ (be).\nHe __3__ (be) now a ruler. He must __4__ (have) a great time.\n He __5__ have fine clothes, lots of money and a number of servants.\nI wish I __6__ (have) his luck’.He __7__ (decide) to visit his\nfriend to enjoy his hospitality.When he __8__ (reach) the palace,\n the king himself __9__ (receive) him with respect and affection.\nDamocles then __10__ (tell) the king that he __11__ (be) indeed\na lucky man. The king __12__ (smile).He __13__ (invite) his friend\nto have dinner with him."


answer_easy = ["Won", "Carried out", "Have been waiting", " Could",
               "Was crying", "Went", "Repaired", "Attempted", "Had reached", "Left"]
answer_medium = ["went", "expands", "contracts", "practices", "drinks", " drank", "has been suffering", "has been writing",
                 "works", "would have helped", "waits", "will have completed", "stays", "has been courting", "has not proposed"]
answer_hard = ["lived", "became", "is", "must be having", "must", "had",
               "decided", "reached", "received", "told""was", "smiled", "invited"]


def get_level():
    """get level from user"""
    level = None
    while level not in ["easy", "medium", "hard"]:
        level = raw_input("Possible choices include easy, medium, and hard: \n")
    return level


def choose():
    """start program"""
    """
    começando o jogo com o jogador escolhedo o nivel que ele prefere esses sendo entre fácil,medio e difícil.
     quando o jogador informar o nível de dificuldade ele será diretamente
     direcionado ao nível selecionado
     espero que goste do my quiz :)
    """
    print "Welcome to my Quiz!!!\nPlease select a game difficulty by typing it in!"
    while True:
        level = get_level()
        if level == "easy":
            print "\nYou choose easy!" + "\n\n" + sample_easy
            print play(sample_easy, answer_easy, parts_of_speech)
        elif level == "medium":
            print "\nYou choose medium!" + "\n\n" + sample_medium
            print play(sample_medium, answer_medium, parts_of_speech)
        elif level == "hard":
            print "\nYou choose hard!" + "\n\n" + sample_hard
            print play(sample_hard, answer_hard, parts_of_speech)


def play(string, answer, replacement):
    """
                com o nivel selecionado aqui que todo o jogo acontece ele terá no total de 4 tentativas
                 se ele acertar o primeiro blank ele passará para a próxima senão vai ficar no mesmo blank
                 até ele acertar ou as sua tentativas acabarem.
    """

    blank = 0
    tries = 4
    game_over = 0
    while blank != len(answer):
        user_input = raw_input("What is the answer to blank " + replacement[blank] + '?')
        if user_input != answer[blank]:
            tries -= 1
            if tries == game_over:
                print "Game Over"
                break
            print "Sorry!!! \nTry again you have %d try left!" % (tries)
        else:
            tries = 4
            string = string.replace(replacement[blank], answer[blank])
            print ":) \nCongratulations!\n\n\n\n" + string
            blank += 1
    return string


def main():
    choose()

if __name__ == '__main__':
    main()
