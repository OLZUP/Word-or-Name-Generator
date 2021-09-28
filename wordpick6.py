from random import *
from better_profanity import profanity
profanity.load_censor_words()


filter = []

def randomwords():
    c = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v = ["A","E","I","O","U","Y"]
    for x in range(0,2):
        cvcvcv = choice(c)+ choice(v)+ choice(c)+ choice(v)+ choice(c)+ choice(v)
        if cvcvcv in filter:
            continue
    for amount in range(3):
        return cvcvcv
        filter.append(cvcvcv)

def randomwords1():
    c1 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v1 = ["A","E","I","O","U","Y"]

    for x1 in range(0,2):
        ccvvcv = choice(c1)+ choice(c1)+ choice(v1)+ choice(v1)+ choice(c1)+ choice(v1)
        if ccvvcv in filter:
            continue
    for amount in range(3):
        return ccvvcv
        filter.append(ccvvcv)

def randomwords2():
    c2 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v2 = ["A","E","I","O","U","Y"]

    for x2 in range(0,2):
        cvvcvc = choice(c2)+ choice(v2)+ choice(v2)+ choice(c2)+ choice(v2)+ choice(c2)
        if cvvcvc in filter:
            continue
    for amount in range(3):
        return cvvcvc
        filter.append(cvvcvc)


def randomwords3():
    c3 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v3 = ["A","E","I","O","U","Y"]

    for x3 in range(0,2):

        vccvcv = choice(v3)+ choice(c3)+ choice(c3)+ choice(v3)+ choice(c3)+ choice(v3)
        if vccvcv in filter:
            continue
    for amount in range(3):
        return vccvcv
        filter.append(vccvcv)


def randomwords4():
    c4 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v4 = ["A","E","I","O","U","Y"]

    for x4 in range(0,2):

        vvcvcv = choice(v4)+ choice(v4)+ choice(c4)+ choice(v4)+ choice(c4)+ choice(v4)
        if vvcvcv in filter:
            continue
    for amount in range(3):
        return vvcvcv
        filter.append(vvcvcv)


def randomwords5():
    c5 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v5 = ["A","E","I","O","U","Y"]

    for x5 in range(0,2):

        vcvcvc = choice(v5)+ choice(c5)+ choice(v5)+ choice(c5)+ choice(v5)+ choice(c5)
        if vcvcvc in filter:
            continue
    for amount in range(3):
        return vcvcvc
        filter.append(vcvcvc)


def randomwords6():
    c6 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v6 = ["A","E","I","O","U","Y"]

    for x6 in range(0,2):

        vvccvc = choice(v6)+ choice(v6)+ choice(c6)+ choice(c6)+ choice(v6)+ choice(c6)
        if vvccvc in filter:
            continue
    for amount in range(3):
        return vvccvc
        filter.append(vvccvc)



def randomwords7():
    c7 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v7 = ["A","E","I","O","U","Y"]

    for x7 in range(0,2):

        ccvcvv = choice(c7)+ choice(c7)+ choice(v7)+ choice(c7)+ choice(v7)+ choice(v7)
        if ccvcvv in filter:
            continue
    for amount in range(3):
        return ccvcvv
        filter.append(ccvcvv)

po = randomwords(),randomwords1(),randomwords2(),randomwords3(),randomwords4(),randomwords5(),randomwords6(),randomwords7()


wordlist1 = profanity.censor(po)
print(wordlist1)
