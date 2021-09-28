from random import *
from better_profanity import profanity
profanity.load_censor_words()


filter = []


def randomwords():
    c = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v = ["A","E","I","O","U","Y"]
    for x in range(0,2):
        cvcvcvc = choice(c)+ choice(v)+ choice(c)+ choice(v)+ choice(c)+ choice(v)+ choice(c)
        if cvcvcvc in filter:
            continue
    for amount in range(3):
        return cvcvcvc
        filter.append(cvcvcvc)

def randomwords1():
    c1 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v1 = ["A","E","I","O","U","Y"]

    for x1 in range(0,2):

        ccvvcvv = choice(c1)+ choice(c1)+ choice(v1)+ choice(v1)+ choice(c1)+ choice(v1)+ choice(v1)
        if ccvvcvv in filter:
            continue
    for amount in range(3):
        return ccvvcvv
        filter.append(ccvvcvv)

def randomwords2():
    c2 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v2 = ["A","E","I","O","U","Y"]

    for x2 in range(0,2):

        cvvcvcv = choice(c2)+ choice(v2)+ choice(v2)+ choice(c2)+ choice(v2)+ choice(c2)+ choice(v2)
        if cvvcvcv in filter:
            continue
    for amount in range(3):
        return cvvcvcv
        filter.append(cvvcvcv)


def randomwords3():
    c3 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v3 = ["A","E","I","O","U","Y"]

    for x3 in range(0,2):

        vccvcvc = choice(v3)+ choice(c3)+ choice(c3)+ choice(v3)+ choice(c3)+ choice(v3)+ choice(c3)
        if vccvcvc in filter:
            continue
    for amount in range(3):
        return vccvcvc
        filter.append(vccvcvc)


def randomwords4():
    c4 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v4 = ["A","E","I","O","U","Y"]

    for x4 in range(0,2):

        vvcvcvc = choice(v4)+ choice(v4)+ choice(c4)+ choice(v4)+ choice(c4)+ choice(v4)+ choice(c4)
        if vvcvcvc in filter:
            continue
    for amount in range(3):
        return vvcvcvc
        filter.append(vvcvcvc)


def randomwords5():
    c5 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v5 = ["A","E","I","O","U","Y"]

    for x5 in range(0,2):

        vcvcvcv = choice(v5)+ choice(c5)+ choice(v5)+ choice(c5)+ choice(v5)+ choice(c5)+ choice(v5)
        if vcvcvcv in filter:
            continue
    for amount in range(3):
        return vcvcvcv
        filter.append(vcvcvcv)



def randomwords6():
    c6 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v6 = ["A","E","I","O","U","Y"]

    for x6 in range(0,2):

        vvccvcv = choice(v6)+ choice(v6)+ choice(c6)+ choice(c6)+ choice(v6)+ choice(c6)+ choice(v6)
        if vvccvcv in filter:
            continue
    for amount in range(3):
        return vvccvcv
        filter.append(vvccvcv)



def randomwords7():
    c7 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    v7 = ["A","E","I","O","U","Y"]

    for x7 in range(0,2):

        ccvcvvc = choice(c7)+ choice(c7)+ choice(v7)+ choice(c7)+ choice(v7)+ choice(v7)+ choice(c7)
        if ccvcvvc in filter:
            continue
    for amount in range(3):
        return ccvcvvc
        filter.append(ccvcvvc)


po = randomwords(),randomwords1(),randomwords2(),randomwords3(),randomwords4(),randomwords5(),randomwords6(),randomwords7()


wordlist2 = profanity.censor(po)
print(wordlist2)
