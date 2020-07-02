import string
import random
import time

possiblecharac = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'


t = 'geek'

attempthis = ''.join(random.choice(possiblecharac) for i in range(len(t)))
attempnext = ''


iteration = 0
completed = False

while completed == False :
    print(attempthis)
    attempnext = ''
    completed = True

    for i in range(len(t)) :
        if attempthis[i] != t[i] :
            completed = False
            attempnext += random.choice(possiblecharac)
        else :
            attempnext += t[i]
    iteration += 1
    attempthis = attempnext

    if iteration == 100000 :
        completed = True

print('Target matched after',iteration,'iterations')
