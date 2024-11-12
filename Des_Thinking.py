def Main_Menu():
    print("You are working at tech support for MicroApple^(tm), and you get a call, when you pick up, the and the client talk for a bit, and their computer is not turning on (if you press anything out of the options it will assume the last answer)")
    First_Empathize_Input = input("You come up with a few questions: (1) Is it getting to hot? (2) Are the fans overly loud? (3) Have you tried turning it on and off again? (4) Has this happened before? Chose 1, 2, 3, or 4 respectivly: ")
    Empathize_1(First_Empathize_Input, fail=0)

## first phase of Empathizeing, asking the player to chose out of the options, and giving a response based on that
def Empathize_1(First_Empathize, fail):
    ## differant options, some failing, some succesful
    if First_Empathize == "1":
        print("No, its ice cold")
        Second_Emphasize = input("You have a few more questions before you come up with ideas on the source of the problem: (1) When did you last use your computer? (2) How long have you had it? (3) Have you tried fixing it yourself? (4) What happened right before this started? Chose 1, 2, 3, or 4 respectivly: ")
        Empathize_2(Second_Emphasize, fail)
    elif First_Empathize == "2":
        print("They are quite a bit louder than normal, I'll get that checked out, and call back in 3-5 buisness days")
        Second_Emphasize = input("You have a few more questions before you come up with ideas on the source of the problem: (1) When did you last use your computer? (2) How long have you had it? (3) Have you tried fixing it yourself? (4) What happened right before this started? Chose 1, 2, 3, or 4 respectivly: ")
        Empathize_2(Second_Emphasize, fail)
    elif First_Empathize == "3":
        print("*Laughs bitterly* I just said I can't turn it on, please listen")
        fail = 1
        Second_Emphasize = input("You have a few more questions before you come up with ideas on the source of the problem: (1) When did you last use your computer? (2) How long have you had it? (3) Have you tried fixing it yourself? (4) What happened right before this started? Chose 1, 2, 3, or 4 respectivly: ")
        Empathize_2(Second_Emphasize, fail)
    else:
        print("Yes, it happened a few weeks ago in fact")
        Second_Emphasize = input("You have a few more questions before you come up with ideas on the source of the problem: (1) When did you last use your computer? (2) How long have you had it? (3) Have you tried fixing it yourself? (4) What happened right before this started? Chose 1, 2, 3, or 4 respectivly: ")
        Empathize_2(Second_Emphasize, fail)

## second phase of Empathizeing, asking the player to chose out of the options, and giving a response based on that again
def Empathize_2(Second_Empathize, fail):
    ## differant options, some failing, some succesful
    if Second_Empathize == "1":
        print("I last used my computer right before the power went out, about 2 hours ago. The power just got fixed")
        First_Define = input("You have a few more questions: (1) Are any other electronics on the same circuit breaker not working? (2) Are other people having this problem as well? (3) Have you tried fixing it yourself? Chose 1, 2, or 3 respectivly: ")
        Define_1(First_Define)
    elif Second_Empathize == "2":
        print("I got my computer 3 days ago, so its not just wear and tear")
        Second_Empathize = ("")
        Second_Emphasize = input("You have a few more questions before you come up with ideas on the source of the problem: (1) When did you last use your computer? (2) How long have you had it? (3) Have you tried fixing it yourself? (4) What happened right before this started? Chose 1, 2, 3, or 4 respectivly: ")
        Empathize_2(Second_Empathize, fail)
    elif Second_Empathize == "3" and fail == 1:
        print("Thats it, I'm shopping at GoogleSoft^(tm) (Please restart)")
    elif Second_Empathize == "3":
        print("Wow, please do your job, you're supposed to help")
        Second_Empathize = ("")
        Second_Emphasize = input("You have a few more questions before you come up with ideas on the source of the problem: (1) When did you last use your computer? (2) How long have you had it? (3) Have you tried fixing it yourself? (4) What happened right before this started? Chose 1, 2, 3, or 4 respectivly: ")
        Empathize_2(Second_Empathize, fail)
    else:
        print("The power went out, but it was fixed")
        First_Define = input("You have a few more questions: (1) Are any other electronics on the same circuit breaker not working? (2) Are other people having this problem as well? (3) Have you tried fixing it yourself? Chose 1, 2, or 3 respectivly: ")
        Define_1(First_Define)

## first stage of defining, finding the problem out of the options given
def Define_1(First_Define):
    ## differant options, some failing, some succesful
    if First_Define == "1":
        print("Yes, everything else on that circuit breaker is not working")
        First_Ideate = input("So, you believe that the problem is that the circuit breaker got overloaded, and can be fixed easily by the client: (1) The circuit breaker probably just got overloaded, do you know how to fix that? (2) The circuit breaker is overloaded, call an electrician: ")
        Ideate_1(First_Ideate)
    elif First_Define == "2":
        print("Nope, just me")
        First_Define = input("You have a few more questions: (1) Are any other electronics on the same circuit breaker not working? (2) Are other people having this problem as well? (3) Have you tried fixing it yourself? Chose 1, 2, or 3 respectivly: ")
        Define_1(First_Define)
    else:
        print("Thats it, I'm shopping at GoogleSoft^(tm) (Please restart)")

## the first stage of Ideating, making an idea on how to solve the problem
def Ideate_1(First_Ideate):
    ## differant options, some failing, some succesful
    if First_Ideate == "1":
        print("No, but I will look it up")
        print("...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...")
        First_Prototype = input("Ok, I am trying to fix it now, I will stay on the phone though. (1) Let them do it by them self (2)Lead the cliant through it: ")
        Prototype_1(First_Prototype)
    else:
        print("Ok, I will get back to you soon")
        print("...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...WAITINGNOISES...")
        print("WHAT why didn't you tell me I could fix it myself?!? I'm shopping at GoogleSoft^(tm) (Please restart)")

## prototype, testing if the idea works
def Prototype_1(First_Prototype):
    ## differant options, some failing, some succesful
    if First_Prototype == "1":
        print("It seemed to work, but the problem apeared again 3 days later (Please restart)")
    else:
        print("After a while, it worked! The circuit breaker was fixed, and it all worked out. YOU WON!!!! (CREDITS: Zach)")
Main_Menu()