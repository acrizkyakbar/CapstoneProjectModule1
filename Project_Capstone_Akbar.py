# ============================================================================================================================================================
# INITIAL DATABASE
allList = {
            1:{'Student_ID':1, 'First_Name': 'Allisa', 'Last_Name':'Martinez', 'Mid_Term': '78', 'Final_Exam': '80'},
            2:{'Student_ID':2, 'First_Name': 'Clyde', 'Last_Name':'Williams', 'Mid_Term': '72', 'Final_Exam': '85'},
            3:{'Student_ID':3, 'First_Name': 'Theresa', 'Last_Name':'Frederick', 'Mid_Term': '76', 'Final_Exam': '78'},
            4:{'Student_ID':4, 'First_Name': 'Priya', 'Last_Name':'Koch', 'Mid_Term': '90', 'Final_Exam': '70'},
            5:{'Student_ID':5, 'First_Name': 'Shauna', 'Last_Name':'Ingram', 'Mid_Term': '65', 'Final_Exam': '94'}
            }

# PASSWORD
def passChecker():
    while True:
        print()
        inputPass = input('Enter password: ')
        if inputPass == 'admin1':
            print()
            print('access granted')
            break
        else:
            print()
            print('access denied')
            break
# ============================================================================================================================================================
# MAIN MENU:
def mainUI():
    print()
    print('============================')
    print('CAPSTONE PROJECT')
    print('============================')
    print('[1] Read')
    print('[2] Create')
    print('[3] Update')
    print('[4] Delete')
    print('[0] Exit')
    print('============================')
# ============================================================================================================================================================
# READ
def readMenu():
    print()
    print('============================')
    print('READ')
    print('============================')
    print('[1] Show All Data')
    print('[2] Find Data')
    print('[0] Back to Main Menu')
    print('============================')

def allData():
    print()
    print('============================')
    print('All Data')
    print('============================')
    print('All Data is here')
    print('[0] Back to previous menu')
    print('============================')


def tableHeader():
    header = ['Student_ID', 'First_Name', 'Last_Name', 'Mid_Term', 'Final_Exam']
    print('==========================================================================================')
    for i in range(len(header)):
        print(f'{header[i]:<16} |', end = '')
    print()
    print('==========================================================================================')


def findFooter():
    print('==========================================================================================')
    print('[1] Find data                                                                            |')
    print('[0] Back to previous menu                                                                |')
    print('==========================================================================================')

def initialTable():
    allList = {
        1:{'Student ID':1, 'First Name': 'Allisa', 'Last Name':'Martinez', 'Mid Term': 78, 'Final Exam': 80},
        2:{'Student ID':2, 'First Name': 'Clyde', 'Last Name':'Williams', 'Mid Term': 72, 'Final Exam': 85},
        3:{'Student ID':3, 'First Name': 'Theresa', 'Last Name':'Frederick', 'Mid Term': 76, 'Final Exam': 78},
        4:{'Student ID':4, 'First Name': 'Priya', 'Last Name':'Koch', 'Mid Term': 90, 'Final Exam': 70},
        5:{'Student ID':5, 'First Name': 'Shauna', 'Last Name':'Ingram', 'Mid Term': 65, 'Final Exam': 94}
    }

    tableHeader = list(allList[1].keys())

    print('==========================================================================================')
    for i in range(len(tableHeader)):
        print(f'{tableHeader[i]:<16} |', end = '')
    print()
    print('==========================================================================================')

    for i in range(len(allList)):
        i += 1
        print(f''' {i:<15} |{allList[i]['First Name']:<17}| {allList[i]['Last Name']:<15} | {allList[i]['Mid Term']:<15} | {allList[i]['Final Exam']:<15} |
        ''')
    print('==========================================================================================')
    print('[0] Back to previous menu')
    print('==========================================================================================')

# ============================================================================================================================================================
# CREATE

def createMenu():
    print()
    print('============================')
    print('CREATE')
    print('============================')
    print('[1] Add new data')
    print('[0] Back to Main Menu')
    print('============================')

# ============================================================================================================================================================
# UPDATE

def updateMenu():
    print()
    print('============================')
    print('UPDATE')
    print('============================')
    print('[1] Update existing data')
    print('[0] Back to Main Menu')
    print('============================')

def updateBased():
    print('============================')
    print('UPDATE BASED ON')
    print('============================')
    print('[1] First_Name')
    print('[2] Last_Name')
    print('[3] Mid_Term')
    print('[4] Final_Exam')
    print('[0] Back to Previous Menu')
    print('============================')
# ============================================================================================================================================================
# DELETE

def deleteMenu():
    print()
    print('============================')
    print('DELETE')
    print('============================')
    print('[1] Delete existing data')
    print('[0] Back to Main Menu')
    print('============================')

# ============================================================================================================================================================
while True:
    mainUI()
    chooseOption = (input('Input Option: '))
    if chooseOption.isnumeric(): #---------------------------------------------------Cek apakah input sebuah numerik
        # MENU 1: READ
        if int(chooseOption) == 1:
            while True:
                readMenu()
                chooseOption = (input('Input Option: '))
                if chooseOption.isnumeric():
                    # MENU 1.1: SHOW DATA
                    if int(chooseOption) == 1:
                        while True:
                            print()
                            tableHeader()
                            for i in range(1, len(allList)+2):
                                if i in list(allList.keys()):
                                    print(f''' {i:<15} |{allList[i]['First_Name']:<17}| {allList[i]['Last_Name']:<15} | {allList[i]['Mid_Term']:<15} | {allList[i]['Final_Exam']:<15} |
                                    ''')
                                else:
                                    continue
                            print('==========================================================================================')
                            print('[0] Back to previous menu                                                                |')
                            print('==========================================================================================')
                            chooseOption = (input('Input Option: '))
                            if chooseOption.isnumeric():
                                if int(chooseOption) == 0:
                                    print()
                                    print('Back to previous menu')
                                    break
                                else:
                                    print()
                                    print('Invalid option')
                                    continue
                            else:
                                print()
                                print('Invalid input')
                                continue    
                        continue
                    # MENU 1.2: FIND DATA
                    elif int(chooseOption) == 2:
                        while True:
                            print()
                            findFooter()
                            chooseOption = (input('Input Option: '))
                            if chooseOption.isnumeric():
                                if int(chooseOption) == 1:
                                    print()
                                    inputID = (input('Input Student ID: '))
                                    if inputID.isnumeric():
                                        while True:
                                            inputID = int(inputID)
                                            if inputID in allList:
                                                tableHeader()
                                                print(f''' {inputID:<15} |{allList[inputID]['First_Name']:<17}| {allList[inputID]['Last_Name']:<15} | {allList[inputID]['Mid_Term']:<15} | {allList[inputID]['Final_Exam']:<15} |
                                                ''')
                                                break
                                            else:
                                                print()
                                                print('ID is not found')
                                                break
                                    else:
                                        print()
                                        print('Invalid input')
                                elif int(chooseOption) == 0:
                                    print()
                                    print('Previous menu')
                                    break
                                else:
                                    print()
                                    print('Invalid option')
                                    continue
                            else:
                                print()
                                print("Invalid input")
                    elif int(chooseOption) == 0:
                        print()
                        print('Back to main menu')
                        break
                    else:
                        print()
                        print('Invalid option')
                        continue
                else:
                    print()
                    print('invalid input')
                    pass
        # MENU 2: CREATE
        elif int(chooseOption) == 2:
            print()
            inputPass = input('Enter password: ')
            if inputPass == 'admin1':
                print()
                print('access granted')
                while True:
                    createMenu()
                    chooseOption = (input('Input Option: '))
                    if chooseOption.isnumeric():
                        if int(chooseOption) == 1:
                            print()
                            print('Student_ID is automatically created')
                            print()
                            firstName   = input('Insert First_Name  : ')
                            lastName    = input('Insert Last_Name   : ')
                            midTerm     = input('Insert Mid_Term    : ')
                            finalExam   = input('Insert Final_Exam  : ')
                            while True:
                                print('Create new data?')
                                confirmation = input('[Y]/[N]: ')
                                if confirmation == 'Y' or confirmation == 'y':
                                    allList.update({len(allList)+1:{'Student_ID'    : len(allList)+1,
                                                                    'First_Name'    : firstName,
                                                                    'Last_Name'     : lastName,
                                                                    'Mid_Term'      : midTerm,
                                                                    'Final_Exam'    : finalExam
                                                                    }})
                                    print()
                                    print('Data has been added')
                                    break
                                elif confirmation == 'N' or confirmation == 'n':
                                    print()
                                    print('Data is not added')
                                    pass
                                else:
                                    print('Invalid input')
                                    continue
                                break
                            continue
                        elif int(chooseOption) == 0:
                            break
                        else:
                            print()
                            print('Invalid option')
                            continue
                    else:
                        print()
                        print("Invalid input")
                        continue
            else:
                print()
                print('Access denied')
                pass
        # MENU 3: UPDATE
        elif int(chooseOption) == 3:
            print()
            inputPass = input('Enter password: ')
            if inputPass == 'admin1':
                print()
                print('access granted') 
                while True:
                    updateMenu()
                    chooseOption = (input('Input Option: '))
                    if chooseOption.isnumeric():
                        if int(chooseOption) == 1:
                            inputID = (input('Input Student ID: '))
                            if inputID.isnumeric():
                                while True:
                                    inputID = int(inputID)
                                    if inputID in allList:
                                        while True:
                                            tableHeader()
                                            print(f''' {inputID:<15} |{allList[inputID]['First_Name']:<17}| {allList[inputID]['Last_Name']:<15} | {allList[inputID]['Mid_Term']:<15} | {allList[inputID]['Final_Exam']:<15} |
                                            ''')
                                            print('==========================================================================================')
                                            confirmation = input('Update data? [Y]/[N]: ')
                                            if confirmation == 'Y' or confirmation == 'y':
                                                while True:
                                                    updateBased()
                                                    chooseOption = (input('Input Option: '))
                                                    if chooseOption.isnumeric():
                                                        if int(chooseOption) == 1:
                                                            print()
                                                            updateFirstName = input('Update First_Name: ')
                                                            confirmation = input('[Y]/[N]: ')
                                                            print('Update Data?')
                                                            if confirmation == 'Y' or confirmation == 'y':
                                                                allList[inputID]['First_Name'] = updateFirstName
                                                                print()
                                                                print('Data has been updated')
                                                                break
                                                            elif confirmation == 'N' or confirmation == 'n':
                                                                print()
                                                                print('Data is not updated')
                                                                break
                                                            else:
                                                                print()
                                                                print('Invalid input')
                                                                print()
                                                                pass   
                                                        elif int(chooseOption)  == 2:
                                                            print()
                                                            updateLastName = input('Update Last_Name: ')
                                                            confirmation = input('[Y]/[N]: ')
                                                            print('Update Data?')
                                                            if confirmation == 'Y' or confirmation == 'y':
                                                                allList[inputID]['Last_Name'] = updateLastName
                                                                print()
                                                                print('Data has been updated')
                                                                break
                                                            elif confirmation == 'N' or confirmation == 'n':
                                                                print()
                                                                print('Data is not updated')
                                                                break
                                                            else:
                                                                print()
                                                                print('Invalid input')
                                                                print()
                                                                pass
                                                        elif int(chooseOption)  == 3:
                                                            print()
                                                            updateMidTerm = input('Update Mid_Term: ')
                                                            confirmation = input('[Y]/[N]: ')
                                                            print('Update Data?')
                                                            if confirmation == 'Y' or confirmation == 'y':
                                                                allList[inputID]['Mid_Term'] = updateMidTerm
                                                                print()
                                                                print('Data has been updated')
                                                                break
                                                            elif confirmation == 'N' or confirmation == 'n':
                                                                print()
                                                                print('Data is not updated')
                                                                print()
                                                                break
                                                            else:
                                                                print()
                                                                print('Invalid input')
                                                                print()
                                                                pass
                                                        elif int(chooseOption)  == 4:
                                                            print()
                                                            updateFinalExam = input('Update Final_Exam: ')
                                                            confirmation = input('[Y]/[N]: ')
                                                            print('Update Data?')
                                                            if confirmation == 'Y' or confirmation == 'y':
                                                                allList[inputID]['Mid_Term'] = updateFinalExam
                                                                print()
                                                                print('Data has been updated')
                                                                break
                                                            elif confirmation == 'N' or confirmation == 'n':
                                                                print()
                                                                print('Data is not updated')
                                                                print()
                                                                break
                                                            else:
                                                                print()
                                                                print('Invalid input')
                                                                print()
                                                                pass
                                                        elif int(chooseOption)  == 0:
                                                            break
                                                        else:
                                                            print()
                                                            print('Invalid option')
                                                            print()
                                                            continue   
                                                    else:
                                                        print()
                                                        print("Invalid input")
                                                        print()
                                                break
                                            elif confirmation == 'N' or confirmation == 'n':
                                                print()
                                                print('Data is not updated')
                                                break
                                            else:
                                                print()
                                                print('Invalid input')
                                                print()
                                                continue
                                        break
                                    else:
                                        print()
                                        print('ID is not found')
                                        break
                            else:
                                print()
                                print('Invalid input')
                                pass
                            continue
                        elif int(chooseOption) == 0:
                            print()
                            print('Back to Main Menu')
                            break
                        else:
                            print()
                            print('Invalid option')
                            continue
                    else:
                        print()
                        print("Invalid input")
                        continue
            else:
                print()
                print('Access denied')
                pass
        # MENU 4: DELETE
        elif int(chooseOption) == 4:
            print()
            inputPass = input('Enter password: ')
            if inputPass == 'admin1':
                print()
                print('access granted')         
                while True:
                    deleteMenu()
                    chooseOption = (input('Input Option: '))
                    if chooseOption.isnumeric():
                        if int(chooseOption) == 1:
                            print()
                            inputID = (input('Input Student ID: '))
                            if inputID.isnumeric():
                                while True:
                                    inputID = int(inputID)
                                    if inputID in allList:
                                        tableHeader()
                                        print(f''' {inputID:<15} |{allList[inputID]['First_Name']:<17}| {allList[inputID]['Last_Name']:<15} | {allList[inputID]['Mid_Term']:<15} | {allList[inputID]['Final_Exam']:<15} |
                                        ''')
                                        confirmation = input('Delete Data? [Y]/[N]: ')
                                        if confirmation == 'Y' or confirmation == 'y':
                                            del allList[inputID]
                                            print('Data has been deleted')
                                            break
                                        elif confirmation == 'N' or confirmation == 'n':
                                            print()
                                            print('Data is not deleted')
                                            break
                                        else:
                                            print()
                                            print('Invalid input')
                                            print()
                                            pass   
                                    else:
                                        print()
                                        print('ID is not found')
                                        break
                            else:
                                print()
                                print('Invalid input')
                        elif int(chooseOption) == 0:
                            print()
                            print('Previous menu')
                            break
                        else:
                            print()
                            print('Invalid option')
                            continue
                    else:
                        print()
                        print("Invalid input")   
                        continue
            else:
                print()
                print('Access denied')
                pass
        # EXIT PROGRAM
        elif int(chooseOption) == 0:
            print('Exit the program')
            break
        else:
            print()
            print('Invalid option')
            continue
    else:
        print()
        print("Invalid input")
    continue

