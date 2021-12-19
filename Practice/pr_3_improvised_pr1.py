students = ["hem","dhyan","raj","aaisha","disha"]
name = input ("Enter your name ->")
if name in students:
    eligible = True
else:
    eligible = False
    
if eligible == False:
    print ("You are not the student of the class!")
else:
    maths=int(input("Enter your total marks in Maths->"))
    chemistry=int(input("Enter your total marks in Chemistry->"))
    physics=int(input("Enter your total marks in Physics->"))
    comps=int(input("Enter your total marks in Cs->"))
    english=int(input("Enter your total marks in English->"))
    def percentage():
        p = ((maths+chemistry+physics+comps+english)/5)
        return p 
    percentage()
    if maths <= 33 or chemistry <= 33 or physics <= 33 or comps <= 33 or english <= 33:
        print ("You've failed since your total marks are less than passing marks in any 1 or more subjects")
    elif percentage() <=40:
        print ("you've failed since your overall percentage is less than 40%")
    else:
        result = True
        if result == True and percentage() == 100:
            print ("Congratulations, you've topped in exam")
        elif result == True and percentage() >=90:
            print ("Congratulations, you've got A+ in exam")
        elif result == True and percentage() >=80:
            print ("Congratulations, you've got A in exam")
        elif result == True and percentage() >=70:
            print ("You've got B in exam, work harder next time!")
        elif result == True and percentage() >=60:
            print ("you've got C in exam, more efforts needed!")
        elif result == True and percentage() >=50:
            print ("you've got D in exam,Give your dad's number asap!")
            

        
            