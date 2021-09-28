from random import *
from better_profanity import profanity
profanity.load_censor_words()


filter = []
def randomwords():
    c = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v = ["A","E","I","O","U","Y"]
    for x in range(0,2):
        cvcvc = choice(c)+ choice(v)+ choice(c)+ choice(v)+ choice(c)
        if cvcvc in filter:
            continue
    for amount in range(3):
        return cvcvc
        filter.append(cvcvc)


def randomwords1():
    c1 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v1 = ["A","E","I","O","U","Y"]

    for x1 in range(0,2):
        ccvvc = choice(c1)+ choice(c1)+ choice(v1)+ choice(v1)+ choice(c1)
        if ccvvc in filter:
            continue
    for amount in range(3):
        return ccvvc
        filter.append(ccvvc)


def randomwords2():
    c2 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v2 = ["A","E","I","O","U","Y"]

    for x2 in range(0,2):
        cvvcv = choice(c2)+ choice(v2)+ choice(v2)+ choice(c2)+ choice(v2)
        if cvvcv in filter:
            continue
    for amount in range(3):
        return cvvcv
        filter.append(cvvcv)



def randomwords3():
    c3 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v3 = ["A","E","I","O","U","Y"]

    for x3 in range(0,2):
        vccvc = choice(v3)+ choice(c3)+ choice(c3)+ choice(v3)+ choice(c3)
        if vccvc in filter:
            continue
    for amount in range(3):
        return vccvc
        filter.append(vccvc)



def randomwords4():
    c4 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v4 = ["A","E","I","O","U","Y"]

    for x4 in range(0,2):
        vvcvc = choice(v4)+ choice(v4)+ choice(c4)+ choice(v4)+ choice(c4)
        if vvcvc in filter:
            continue
    for amount in range(3):
        return vvcvc
        filter.append(vvcvc)


def randomwords5():
    c5 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v5 = ["A","E","I","O","U","Y"]

    for x5 in range(0,2):
        vcvcv = choice(v5)+ choice(c5)+ choice(v5)+ choice(c5)+ choice(v5)
        if vcvcv in filter:
            continue
    for amount in range(3):
        return vcvcv
        filter.append(vcvcv)



def randomwords6():
    c6 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v6 = ["A","E","I","O","U","Y"]

    for x6 in range(0,2):
        vvccv = choice(v6)+ choice(v6)+ choice(c6)+ choice(c6)+ choice(v6)
        if vvccv in filter:
            continue
    for amount in range(3):
        return vvccv
        filter.append(vvccv)



def randomwords7():
    c7 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v7 = ["A","E","I","O","U","Y"]

    for x7 in range(0,2):
        ccvcv = choice(c7)+ choice(c7)+ choice(v7)+ choice(c7)+ choice(v7)
        if ccvcv in filter:
            continue
    for amount in range(3):
        return ccvcv
        filter.append(ccvcv)


po = randomwords(),randomwords1(),randomwords2(),randomwords3(),randomwords4(),randomwords5(),randomwords6(),randomwords7()


wordlist = profanity.censor(po)
print(wordlist)
