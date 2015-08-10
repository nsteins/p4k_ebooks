import re
import random

#generates nonsense genres and nonsense reviews using wordlists and mad-libs style substitution

def main():
    for x in range(1,10):
        text = generateDescription()
        print text
        print "length {0}".format(len(text))

def generateDescription():
    with open("./wordlists/4syllableadjectives.txt",'r') as adjf:
        adjs = adjf.readlines()
    with open("./wordlists/gerunds.txt",'r') as gerf:
        gers = gerf.readlines()
    with open("./wordlists/activeverbs.txt",'r') as verbf:
        verbs = verbf.readlines()
    with open("./wordlists/4syllableadverbs.txt",'r') as advf:
        advs = advf.readlines()
    with open("./wordlists/directobject.txt",'r') as dof:
        dos = dof.readlines()
    with open("./wordlists/emotions.txt",'r') as emof:
        emos = emof.readlines()
    
    genre = generateGenre()
    out = ""

    r= random.randint(1,6)
    if r==1:
        out += "The latest " + genre + " album "
    elif r==2:
        out += "This " + genre + " EP "
    elif r==3:
        out += "The " + genre + " record "
    elif r==4:
        out += "The new release from the " + genre + " legends "
    elif r==5:
        out += "The " + genre + " veterans' new work "
    elif r==6:
        out += "The " + genre + " band's sophomore album "

    r = random.randint(1,7)
    if r==1:
        out += "is like " + randel(gers) + " " + randel(advs) + " at a" + addn(randel(dos))
    elif r==2:
        out += "won't make you " + randel(verbs) + " but it just might make you " + randel(verbs)
    elif r==3:
        out += "is a love letter from a" + addn(randel(dos)) + " to a long lost " + randel(dos)
    elif r==4:
        out += "is a" + addn(randel(adjs)) + " album that will make you feel " + randel(emos)
    elif r==5:
        out += "tries to " + randel(verbs) + " " + randel(advs) + " but never hits the mark"
    elif r==6:
        out += "will have you nodding your head " + randel(advs)
    elif r==7:
        out += "starts out " + randel(gers) + " but never manages to " + randel(verbs)
    elif r==8:
        out += "ends with a" + addn(randel(adjs)) + " explosion of " + randel(dos)

    out += ". {:.1f}".format(random.random()*10)
    out = re.sub('\r?\n','',out)
    return out

def addn(word):
    if re.match("^[aeiou]",word):
        out = "n " + word
    else:
        out = " " + word
    return out


def randel(inlist):
	return inlist[random.randint(1,len(inlist))-1]

def generateGenre():
    with open("./wordlists/genres.txt","r") as genref:
            genres = genref.readlines()	
    with open("./wordlists/genreadj.txt","r") as adjf:
            adjs = adjf.readlines()
    out = "" 
    r = random.randint(1,6)
    if r == 1:
            gazes = ('blue','brew','chew','clue','glue','goo','jew','nu','shoo','screw','spew','who','sioux')
            gadj = ('bubble','power','flutter','chamber','gumbo','dream','fuzz','party')
            out += randel(gazes) + "gaze " + randel(gadj) + "-"
    elif r == 2:
            cores = ('thrash','skull','rattle','crumb','grum','battle','nickel','grumble','scatter','turtle','scum','number','shock','shot','bat','stoner')
            out += randel(adjs) + " " + randel(cores) + "core "
    elif r == 3:
            los = ('blow','bro','crow','dough','doe','flow','no','glow','go','grow','fro','ho','joe','lo','pro','sew','show','slow','snow','so','toe','throw','yo','woe','whoa')
            out += randel(los) + "-fi " + randel(adjs) + " "
    elif r == 4:
            waves = ('cry','grime','life','love','spazz','shine','mime','nice','twine','strike','bite','lie','grind','knife','cheer','brine')
            wadj = ('bluff','blunt','bud','bulge','bug','hush','dung','pus','mutt','gum','fudge','glum','fuss','dusk','crumb','crunch','clutch','scrub','putt','pump','puff','pluck','stun','shrug','sludge','snug')
            out += randel(waves) + "wave " + randel(wadj) + " "
    else:
            mods = ('post-','neo-','nu','psych-')
            out += randel(adjs) + ' ' + randel(adjs) + ' '+ randel(mods)	
    out += randel(genres) 
    return out.lower()

if __name__ == "__main__":
    main()
