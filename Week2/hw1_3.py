################################
# Project: HW1_3               #
# Date: 20211009               #
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

# # reservation for enroll the class
reserve_1 = int(input())
reserve_2 = int(input())

# student id comparison (need to swap with dept)

if id_1 > id_2:
    id_temp = id_2
    dept_temp = dept_2
    id_2 = id_1
    dept_2 = dept_1
    id_1 = id_temp
    dept_1 = dept_temp

if id_2 > id_3:
    id_temp = id_3
    dept_temp = dept_3
    id_3 = id_2
    dept_3 = dept_2
    id_2 = id_temp
    dept_2 = dept_temp

if id_1 > id_2:
    id_temp = id_2
    dept_temp = dept_2
    id_2 = id_1
    dept_2 = dept_1
    id_1 = id_temp
    dept_1 = dept_temp
    
if reserve_1 == reserve_2:
    # dept are all different but 2 reserves are the same
    if reserve_1 == dept_1 and reserve_1 == dept_2 and reserve_1 == dept_3:
        print(id_1, id_2, id_3, sep=',')
        
    elif reserve_1 != dept_1 and reserve_1 == dept_2 and reserve_1 == dept_3:
        print(id_2, id_3, sep=',')
    elif reserve_1 == dept_1 and reserve_1 != dept_2 and reserve_1 == dept_3:
        print(id_1, id_3, sep=',')
    elif reserve_1 == dept_1 and reserve_1 == dept_2 and reserve_1 != dept_3:
        print(id_1, id_2, sep=',')
        
    elif reserve_1 == dept_1 and reserve_1 != dept_2 and reserve_1 != dept_3:
        print(id_1)    
    elif reserve_1 != dept_1 and reserve_1 == dept_2 and reserve_1 != dept_3:
        print(id_2) 
    elif reserve_1 != dept_1 and reserve_1 != dept_2 and reserve_1 == dept_3:
        print(id_3) 
    else:
        print("-1")

else:
    
    # dept are all different but 2 reserves are valid
    if reserve_1 == dept_1 and reserve_2 == dept_2 and (dept_3 != reserve_1 and dept_3 != reserve_2):
        print(id_1, id_2, sep=',')
    elif reserve_1 == dept_1 and reserve_2 == dept_3 and (dept_2 != reserve_1 and dept_2 != reserve_2):
        print(id_1, id_3, sep=',')
    elif reserve_1 == dept_2 and reserve_2 == dept_1 and (dept_3 != reserve_1 and dept_3 != reserve_2):
        print(id_1, id_2, sep=',')
    elif reserve_1 == dept_2 and reserve_2 == dept_3 and (dept_1 != reserve_1 and dept_1 != reserve_2):
        print(id_2, id_3, sep=',')
    elif reserve_1 == dept_3 and reserve_2 == dept_1 and (dept_2 != reserve_1 and dept_2 != reserve_2):
        print(id_1, id_3, sep=',')
    elif reserve_1 == dept_3 and reserve_2 == dept_2 and (dept_1 != reserve_1 and dept_1 != reserve_2):
        print(id_2, id_3, sep=',')
    
    # 2 dept are the same but 2 reserves are valid
    elif (dept_1 == dept_2) and (dept_1 != dept_3) and (dept_2 != dept_3):
        if reserve_1 == dept_1 and reserve_2 == dept_3:
            print(id_1, id_2, id_3, sep=',')
        elif reserve_1 != dept_1 and reserve_1 != dept_3 and reserve_2 == dept_3:
            print(id_3)
        elif reserve_1 != dept_1 and reserve_1 != dept_3 and reserve_2 == dept_1:
            print(id_1, id_2, sep=',')   
        elif reserve_1 == dept_1 and reserve_1 != dept_3 and reserve_2 != dept_3:
            print(id_1, id_2, sep=',')
        elif reserve_1 == dept_3 and reserve_2 == dept_1:
            print(id_1, id_2, id_3, sep=',')
        elif reserve_1 == dept_3 and reserve_2 != dept_1 and reserve_2 != dept_2:
            print(id_3)          
            
    elif (dept_1 == dept_3) and (dept_1 != dept_2) and (dept_2 != dept_3):
        if reserve_1 == dept_1 and reserve_2 == dept_2:
            print(id_1, id_2, id_3, sep=',')
        elif reserve_1 != dept_1 and reserve_1 != dept_2 and reserve_2 == dept_2:
            print(id_2)
        elif reserve_1 != dept_1 and reserve_1 != dept_2 and reserve_2 == dept_1:
            print(id_1, id_3, sep=',')        
        elif reserve_1 == dept_1 and reserve_1 != dept_2 and reserve_2 != dept_2:
            print(id_1, id_3, sep=',')
        elif reserve_1 == dept_2 and reserve_2 == dept_1:
            print(id_1, id_2, id_3, sep=',')
        elif reserve_1 == dept_2 and reserve_2 != dept_1 and reserve_2 != dept_3:
            print(id_2)
        else:
            print("-1")
            
    elif (dept_2 == dept_3) and (dept_2 != dept_1) and (dept_1 != dept_3):
        if reserve_1 == dept_2 and reserve_2 == dept_1:
            print(id_1, id_2, id_3, sep=',')
        elif reserve_1 != dept_2 and reserve_1 != dept_1 and reserve_2 == dept_2:
            print(id_2, id_3, sep=',')
        elif reserve_1 != dept_2 and reserve_1 != dept_1 and reserve_2 == dept_1:
            print(id_1)
        elif reserve_1 == dept_2 and reserve_1 != dept_1 and reserve_2 != dept_1:
            print(id_2, id_3, sep=',')
        elif reserve_1 == dept_1 and reserve_2 == dept_2:
            print(id_1, id_2, id_3, sep=',')
        elif reserve_1 == dept_1 and reserve_2 != dept_2 and reserve_2 != dept_3:
            print(id_1)    
        else:
            print("-1")
             
    # 3 dept are the same but 2 reserves are valid
    elif (dept_1 == dept_2) and (dept_2 == dept_3):
        if reserve_1 == dept_1 or reserve_2 == dept_1:
            print(id_1, id_2, id_3, sep=',')
        elif reserve_1 != dept_1 and reserve_2 != dept_1:
            print("-1")
            
    # dept are all different but just 1 reserves are valid
    elif reserve_1 == dept_1 and (dept_2 != reserve_1 or dept_2 != reserve_2) and (dept_3 != reserve_1 or dept_3 != reserve_2):
        print(id_1)
    elif reserve_1 == dept_2 and (dept_1 != reserve_1 or dept_1 != reserve_2) and (dept_3 != reserve_1 or dept_3 != reserve_2):
        print(id_2)
    elif reserve_1 == dept_3 and (dept_1 != reserve_1 or dept_1 != reserve_2) and (dept_2 != reserve_1 or dept_2 != reserve_2):
        print(id_3)
    elif reserve_2 == dept_1 and (dept_2 != reserve_1 or dept_2 != reserve_2) and (dept_3 != reserve_1 or dept_3 != reserve_2):
        print(id_1)
    elif reserve_2 == dept_2 and (dept_1 != reserve_1 or dept_1 != reserve_2) and (dept_3 != reserve_1 or dept_3 != reserve_2):
        print(id_2)
    elif reserve_2 == dept_3 and (dept_1 != reserve_1 or dept_1 != reserve_2) and (dept_2 != reserve_1 or dept_2 != reserve_2):
        print(id_3)
    else:
        print("-1")

