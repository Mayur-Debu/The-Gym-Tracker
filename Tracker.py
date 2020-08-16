import datetime

#FUNCTION FOR LOGGING INFORMATION INTO FILES


def user1_log():

    """THIS FUNCTION LOGS THE DIET AND EXERCISE INFORMATION FOR THE USER1 """

    print("\n ******************************************************************")
    print("What do you want to log?\n"
          "Please choose 1 for Diet and 2 for Exercise.")

    print("1: Diet")
    print("2: Exercise")

    f = int(input("Enter your choice: "))

    if  f==1:
        file = open("User1Diet.txt", "a")
        time=datetime.datetime.now()
        file.write("["+str(time)+"] : ")
        print("Please enter the diet followed with a \",\" and press ENTER to save file.\n")
        information=input()
        file.write(information+" \n")
        print("********** Diet Successfully Logged **********\n\n")
        file.close()
    elif f==2:
        file = open("User1Exercise.txt", "a")
        time = datetime.datetime.now()
        file.write("[" + str(time) + "] : ")
        print("Please enter the exercise followed with a \",\" and press ENTER to save file.\n")
        information = input()
        file.write(information + " \n")
        print("********** Exercise Successfully Logged **********\n\n")
        file.close()
    else:
        print("\n Their is no option ", f)
        user1_log()


def user2_log():

    """THIS FUNCTION LOGS THE DIET AND EXERCISE INFORMATION FOR THE USER2 """

    print("\n ******************************************************************")
    print("What do you want to log?\n"
          "Please choose 1 for Diet and 2 for Exercise.")

    print("1: Diet")
    print("2: Exercise")

    f = int(input("Enter your choice: "))

    if  f==1:
        file = open("User2Diet.txt", "a")
        time=datetime.datetime.now()
        file.write("["+str(time)+"] : ")
        print("Please enter the diet followed with a \",\" and press ENTER to save file.\n")
        information=input()
        file.write(information+" \n")
        print("********** Diet Successfully Logged **********\n\n")
        file.close()
    elif f==2:
        file = open("User2Exercise.txt", "a")
        time = datetime.datetime.now()
        file.write("[" + str(time) + "] : ")
        print("Please enter the exercise followed with a \",\" and press ENTER to save file.\n")
        information = input()
        file.write(information + " \n")
        print("********** Exercise Successfully Logged **********\n\n")
        file.close()
    else:
        print("\n Their is no option ", f)
        user2_log()


def user3_log():

    """THIS FUNCTION LOGS THE DIET AND EXERCISE INFORMATION FOR THE USER3  """

    print("\n ******************************************************************")
    print("What do you want to log?\n"
          "Please choose 1 for Diet and 2 for Exercise.")

    print("1: Diet")
    print("2: Exercise")

    f = int(input("Enter your choice: "))

    if  f==1:
        file = open("User3Diet.txt", "a")
        time=datetime.datetime.now()
        file.write("["+str(time)+"] : ")
        print("Please enter the diet followed with a \",\" and press ENTER to save file.\n")
        information=input()
        file.write(information+" \n")
        print("********** Diet Successfully Logged **********\n\n")
        file.close()
    elif f==2:
        file = open("User3Exercise.txt", "a")
        time = datetime.datetime.now()
        file.write("[" + str(time) + "] : ")
        print("Please enter the exercise followed with a \",\" and press ENTER to save file.\n")
        information = input()
        file.write(information + " \n")
        print("********** Exercise Successfully Logged **********\n\n")
        file.close()
    else:
        print("\n Their is no option ", f)
        user3_log()


#  FUNCTION FOR RETRIEVING INFORMATION FROM FILES


def user1_retrieve():
    """THIS FUNCTION RETRIEVE THE DIET AND EXERCISE INFORMATION FOR THE USER1 """

    print("\n ******************************************************************")
    print("What do you want to retrieve?\n"
          "Please choose 1 for Diet and 2 for Exercise.")

    print("1: Diet")
    print("2: Exercise")

    f = int(input("Enter your choice: "))

    if f == 1:
        file = open("User1Diet.txt", "r")
        print("\n")
        print(file.read())
        print("********** Diet Successfully Read **********\n\n")
        file.close()
    elif f == 2:
        file = open("User1Exercise.txt", "r")
        print("\n")
        print(file.read())
        print("********** Exercise Successfully Read **********\n\n")
        file.close()
    else:
        print("\n Their is no option ", f)
        user1_retrieve()


def user2_retrieve():
    """THIS FUNCTION RETRIEVE THE DIET AND EXERCISE INFORMATION FOR THE USER2 """

    print("\n ******************************************************************")
    print("What do you want to retrieve?\n"
          "Please choose 1 for Diet and 2 for Exercise.")

    print("1: Diet")
    print("2: Exercise")

    f = int(input("Enter your choice: "))

    if f == 1:
        file = open("User2Diet.txt", "r")
        print("\n")
        print(file.read())
        print("********** Diet Successfully Read **********\n\n")
        file.close()
    elif f == 2:
        file = open("User2Exercise.txt", "r")
        print("\n")
        print(file.read())
        print("********** Exercise Successfully Read **********\n\n")
        file.close()
    else:
        print("\n Their is no option ", f)
        user2_retrieve()


def user3_retrieve():
    """THIS FUNCTION RETRIEVE THE DIET AND EXERCISE INFORMATION FOR THE USER3 """

    print("\n ******************************************************************")
    print("What do you want to retrieve?\n"
          "Please choose 1 for Diet and 2 for Exercise.")

    print("1: Diet")
    print("2: Exercise")

    f = int(input("Enter your choice: "))

    if f == 1:
        file = open("User3Diet.txt", "r")
        print("\n")
        print(file.read())
        print("********** Diet Successfully Read **********\n\n")
        file.close()
    elif f == 2:
        file = open("User3Exercise.txt", "r")
        print("\n")
        print(file.read())
        print("********** Exercise Successfully Read **********\n\n")
        file.close()
    else:
        print("\n Their is no option ", f)
        user3_retrieve()



""" *********************************************************   MAIN PROGRAM STARTS FROM HERE   ***********************************************"""



print("********************* WELCOME TO THE EXERCISE AND DIET MANGEMENT SYSTEM *********************\n")
while(True):


 print("Select a option: ")
 print("1: Logging into to the file.")
 print("2: Retrieving the logged data.")
 print("3: Terminate the program.\n")
 ch = int(input("Enter Your Choice: "))

 if ch==1:                                                #logging data into the users's file
    print("Select a user: ")
    print("1: User_no1.")
    print("2: User_no2.")
    print("3: User_no3. \n")
    user = int(input("Enter User_no: "))

    if user==1:
        user1_log()
    elif user==2:
        user2_log()
    elif user==3:
        user3_log()
    else:
        print("TRY AGAIN :-( \n")

 elif ch==2:                                                #Retrieveing data from the user's file
    print("Select a user: ")
    print("1: User_no1.")
    print("2: User_no2.")
    print("3: User_no3. \n")
    user = int(input("Enter User_no: "))

    if user == 1:
        user1_retrieve()
    elif user == 2:
        user2_retrieve()
    elif user == 3:
        user3_retrieve()
    else:
        print("TRY AGAIN :-( \n")

 elif ch==3:
     print("Program Terminated ")
     print("*************************************************************************************************************")
     break

 else:
    print("\nTheir is no option ",ch)