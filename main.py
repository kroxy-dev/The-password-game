from prompt_toolkit import prompt 
from datetime import datetime 
from wordle_fetch import answer


#palindrome for rule 19
def palindrome(s):
    s=s.lower()
    for i in range (len(s)-2):
        pal=s[i:i+3]
        if pal== pal[::-1]:
            return True
    return False 
#All the game rules:
def all_rules():
    word=answer()
    return[
        ('Rule 0 : enter your password',lambda pw : len(pw)>0),
        ('Rule 1 : password must contain a number',lambda pw: any(c .isdigit() for c in pw)),
        ('Rule 2 : Password must contain an upper case letter', lambda pw : any(c.isupper() for c in pw)),
        ('Rule 3 : password must contain a symbol',lambda pw: any(c in"!@#$%^&*" for c in pw)),
        ('Rule 4 : password must include todays date in this format(Y-m-d)', lambda pw: datetime.today().strftime('%Y-%m-%d') in pw),
        ('Rule 5 : password must contain a roman number', lambda pw : any ( c in 'IVXLCDM' for c in pw )),
        ('Rule 6 : the number of digits in the password must be pair',lambda pw: sum(c.isdigit() for c in pw)%2==0),
        ('Rule 7 : password must include a country in europe', lambda pw : any (c in pw for c in [
        "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium",
        "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
        "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece",
        "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia",
        "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco",
        "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal",
        "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain",
        "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City"] )),

        ('Rule 8 : password must contain todays wordle answer (use apple if no internet)',lambda pw:word in pw),
        ('Rule 9 : the number of lower case letters must be equal to the number of upper case letters',lambda pw:sum(c.isupper() for c in pw )==sum(c.islower() for c in pw)),
        ('Rule 10 : your password must contain the current hour and minute in this format (hh-mm)', lambda pw:  datetime.now().strftime('%H-%M') in pw if not finalmode else True) ,
        ('Rule 11 : password must include the year Brazil hosted the FIFA World Cup',lambda pw: '2014' in pw),
        ('Rule 12 : An egg 🥚 has appeared! Make sure to keep it safe in your password',lambda pw : '🥚' in pw if not eggspawned else True),
        ('Rule 13 : the sum of the digits at odd positions must be divisible by 4 ',lambda pw: sum(int(c) for pos, c in enumerate(pw, 1) if c.isdigit() and pos % 2 == 1) % 4 == 0),
        ('Rule 14 : password must contain the name of the creator of this game(hint:kroxy)',lambda pw : 'kroxy' in pw),
        ('Rule 15 : the sum of the digits in your password must be divisible by 3', lambda pw : sum(int(c)for c in pw if c.isdigit())%3==0),
        ('Rule 16 : The egg has hatched! Say hi to Booger 🐣', lambda pw: '🐥' in pw if not finalmode else True),
        ('Rule 17 : You need to feed booger (worm) right next to it every attempt or he will die',lambda pw: ('🐥worm' in pw or 'worm🐥' in pw) if not finalmode else True ),
        ('Rule 18 : your password is not strong enough 🏋️ ',lambda pw : 'strong' in pw),
        ('Rule 19 : password must contain a palindrome substring that has 3 letters ',lambda pw: palindrome(pw)),        
        ]

eggspawned = False
eggactive = False
booger = False
finalmode=False #final rule is active
timer=True # for debugging
def main():
    i=1  #index of rules we unlocked so far
    rules=all_rules()
    unlocked_rules=[]
    global eggspawned, eggactive, booger,timer,finalmode
    pw=''
    final_rule = False
    final = ''
    print(rules[0][0])#prints the first rule when the game starts
    unlocked_rules.append(rules[0])

    while True :    
        #prompts password
        pw = prompt("Enter password: ", default=pw)

        # check all unlocked rules
        failed=[text for text,check in unlocked_rules if not check(pw)]

        #loses the game if the egg is deleted
        if eggactive and '🥚' not in pw:
            print('The egg died you lost the game')
            i=1
            pw=''
            eggactive=False
            timer=False
            eggspawned=False
            unlocked_rules=[]
            unlocked_rules.append(rules[0])
            print(rules[0][0])
            continue
        
        # loses if you don't feed booger or overfeed
        worm_count = pw.count('worm')
        if booger:
            if not ('🐥worm' in pw or 'worm🐥' in pw):#if booger isnt fed
                print('you forgot to feed booger')
                i = 1
                pw = ''
                booger = False  
                eggactive = False
                eggspawned=False
                timer=False
                unlocked_rules = []
                unlocked_rules.append(rules[0])
                print(rules[0][0])
                continue
            elif worm_count > 1: #if booger is over fed
                print('booger over ate')
                i = 1
                pw = ''
                booger = False
                eggactive = False
                eggspawned=False
                timer=False
                unlocked_rules = []
                unlocked_rules.append(rules[0])
                print(rules[0][0])
                continue
            else:
                pw=pw.replace('worm','')#feeds booger
        
        #unclock next rule if all previous ones are checked
        if not failed and i < len(rules):
            unlocked_rules.append(rules[i])
            i += 1
            # immediately show the new rule
            print(rules[i-1][0])

        #append final rule right after Rule 19
        elif i == 20 and not final_rule and not failed:
            print('Rule 20 FINAL RULE: YOU MUST RETYPE YOUR ENTIRE PASSWORD NOW')
            final = pw.replace('🐥','')
            finalmode=True
            booger=False
            pw = ''
            unlocked_rules.append(('Rule 20 FINAL RULE: YOU MUST RETYPE YOUR ENTIRE PASSWORD NOW(without booger and the food)', lambda pw_input, f=final: pw_input == f))
            rules=unlocked_rules
            #i += 1
            final_rule = True


        #win condition 
        if finalmode and pw==final:
            print('You won THE PASSWORD GAME, HERE IS A COOKIE 🍪 ')
            break
        else:
            for f in failed:
                print('-',f)
            print('try again \n')
        #spawns the egg if the egg rule is active 
        if len(unlocked_rules) == 13 and not(eggspawned ):
            pw+='🥚'
            eggactive=True
            eggspawned=True

        #disabling time rule for debugging   
        if len(unlocked_rules)==12:
            timer=True
        
        #hatches the egg
        if len(unlocked_rules) == 17 and not booger:
            pw=pw.replace('🥚', '🐥', 1)
            eggactive=False
            timer=False
        
        #triggers booger feeding
        if len(unlocked_rules) == 18:
            booger=True
        
        


                

#run game
if __name__ == "__main__":
    main()

            
