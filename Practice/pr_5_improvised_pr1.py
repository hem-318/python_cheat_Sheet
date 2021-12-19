students = ["hem","dhyan","raj","aaisha","disha"]
name = str(input ("Enter your name ->"))
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
    # Python code to illustrate read() mode
    file = open("Practice/instructions.txt", "r")
    print (file.read())

    def percentage():
        p = ((maths+chemistry+physics+comps+english)/5)
        return p 
    percentage()
    if maths <= 33 or chemistry <= 33 or physics <= 33 or comps <= 33 or english <= 33:
        status = "Fail"
        grade = "Failed (E)"
        print ("You've failed since your total marks are less than passing marks in any 1 or more subjects")
    elif percentage() <=40:
        status = "Fail"
        grade = "Failed (E)"
        print ("you've failed since your overall percentage is less than 40%")
    else:
        result = True
        status = "Pass"
        if result == True and percentage() == 100:
            grade = "A+"
            print ("Congratulations, you've topped in exam")
        elif result == True and percentage() >=90:
            grade = "A+"
            print ("Congratulations, you've got A+ in exam")
        elif result == True and percentage() >=80:
            grade = "A"
            print ("Congratulations, you've got A in exam")
        elif result == True and percentage() >=70:
            grade = "B"
            print ("You've got B in exam, work harder next time!")
        elif result == True and percentage() >=60:
            grade = "C"
            print ("you've got C in exam, more efforts needed!")
        elif result == True and percentage() >=50:
            grade = "D"
            print ("you've got D in exam,Give your dad's number asap!")
# Saving result as individual text file


    file = open(f'Practice/result/{name}.txt','x+') 
    file.write("Name = ") , file.write(name) ,  file.write("\n") 

    file.write("Marks in maths = "),file.write(str(maths)) , file.write("\n")

    file.write("Marks in chemistry = "),file.write(str(chemistry)) , file.write("\n")

    file.write("Marks in physics = "),file.write(str(physics)) , file.write("\n")

    file.write("Marks in Cs= "),file.write(str(comps)) , file.write("\n")

    file.write("Marks in english = "),file.write(str(english)) , file.write("\n")

    file.write("Status = "),file.write(str(status)) , file.write("\n")

    file.write("Grade = "),file.write(str(grade))  , file.write("\n")

    file.write("Total percentage =  "),file.write(str(percentage())), file.write("%") , file.write("\n")
    print ("Your final result- \n \n")
    file.seek(0)
    print(file.read())
    file.close()



           