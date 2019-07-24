import  random  
def cows_n_bulls():
                c=''
                a=raw_input("wanna play cows and bulls y/n")
                s=0
                if a=='y':
                                for i in range(4):
                                                b=random.randint(0,9)
                                                s=s+(10**i)*b
                                c=str(s)
                print "welcome"                
                print "this is cows and bulls"
                print "each guess will be a 4 digit number"
                print "1 bull means there is a correct digit at the correct place"
                print "1 cow means there is a correct digit at the wrong place"
                print "you will get 10 chances to guess the whole number"
                e=0
                while True:
                                h=0
                                d=raw_input("enter the 4-digit guess")
                                f=d
                                g=c
                                bulls=0
                                cows=0
                                h=0
                                for j in range(len(f)):
                                    if f[j]==g[j] and bulls+cows<=4:
                                                bulls=bulls+1               
                                    elif f[j] in g and bulls+cows<=4:
                                                cows=cows+1
                                    elif f[j] not in g:
                                                h=1
                                e=e+1
                                print e
                                print bulls,"bulls"
                                print cows,"cows"
                                print 10-e,"chances left"
                                if e==10:
                                                print "game over, you lost the game"
                                                print "the number was",c
                                                break
                                if d==c:
                                               print "congoooooooooooooooooo"
                                               print "you won the game"
                                               break

cows_n_bulls()
