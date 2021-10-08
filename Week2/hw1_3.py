################################
# Project: HW1_3               #
# Date: 20211005               #
# Author: Ricky Hsien-Ming Liu #
# ID: R09323056                #
################################

########################
# Variable Declaration #
########################

# student id
id_1 = int(input())
id_2 = int(input())
id_3 = int(input())

# department id
dept_1 = int(input())
dept_2 = int(input())
dept_3 = int(input())

# reservation for enroll the class
reserve_1 = int(input())
reserve_2 = int(input())

###################
# Judge Statement #
###################

# Only one department can enroll into the class
if (reserve_1 == dept_1) and (reserve_2 == dept_1):
    print(str(id_1))
elif (reserve_1 == dept_2) and (reserve_2 == dept_2):
    print(str(id_2))
elif (reserve_1 == dept_3) and (reserve_2 == dept_3):
    print(str(id_3))

# Two depart ment can enroll into the class
elif (reserve_1 == dept_1) and (reserve_2 == dept_2):
    if dept_1 == dept_2:
        
    else:    
        if id_1 > id_2:
            print(str(id_1) + "," + str(id_2))
        else:
            print(str(id_2) + "," + str(id_1))
elif (reserve_1 == dept_1) and (reserve_2 == dept_3):
    if id_1 > id_3:
        print(str(id_1) + "," + str(id_3))
    else:
        print(str(id_3) + "," + str(id_1))
elif (reserve_1 == dept_2) and (reserve_2 == dept_1):
    if id_2 > id_1:
        print(str(id_2) + "," + str(id_1))
    else:
        print(str(id_1) + "," + str(id_2))
elif (reserve_1 == dept_2) and (reserve_2 == dept_3):
    if id_2 > id_3:
        print(str(id_2) + "," + str(id_3))
    else:
        print(str(id_3) + "," + str(id_2))
elif (reserve_1 == dept_3) and (reserve_2 == dept_1):
    if id_3 > id_1:
        print(str(id_3) + "," + str(id_1))
    else:
        print(str(id_1) + "," + str(id_3))
elif (reserve_1 == dept_3) and (reserve_2 == dept_2):
    if id_3 > id_2:
        print(str(id_3) + "," + str(id_2))
    else:
        print(str(id_2) + "," + str(id_3))

# No one has priority to enroll the class first
else:
    print(str(-1))