#------------------------------------------#
# Title: CDInventory.py
# Desc: CD Inventory Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# JMagat, 2021-Aug-08, Modified script to use dictionary, load data from memory and remove entry.
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow= {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 2. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # 3.TODO Add the functionality of loading existing data
        # Read the file line by line into in-memory list.
        ## Open the text file
        objFile = open(strFileName,'r')
        ## Use for loop to identify the lst Row
        for row in objFile:
            lstRow = row.strip().split(',')  
            ## Map the row items to the dictionary key
            dicRow = {'id': lstRow[0], 'title': lstRow[1], 'artist': lstRow[2]}
            ## Append the loaded data into the lstTbl
            lstTbl.append(dicRow)
        objFile.close()
        ## Display the data loaded into the lstTbl
        print('This is the Current CD Inventory')
        print('ID, CD Title, Artist')
        ## Use a for loop to print separate row values as separate lines
        for row in lstTbl:
            print(*row.values(), sep = ', ') 
        print()

    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 4. Add data to the table (2d-list) each time the user wants to add data
        ## Collect user input
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        ## Put user input to dictionary
        dicRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        ## Append row of user input into table
        lstTbl.append(dicRow)      
                       
    elif strChoice == 'i':
        # 5. Display the current data to the user each time the user wants to display the data
        print('This is the Current CD Inventory')
        print('ID, CD Title, Artist')
        ## Use a for loop to print list values as separate lines
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print()
        
    elif strChoice == 'd':
        # 6.TODO Add functionality of deleting an entry
        print('Enter the information for the entry you wish to delete.')
        ## Identify the CD Id to be deleted
        strTitle = input('Enter the CD Title to be deleted: ')
        ## Loop through list to match the CD Title and use remove method
        for cd in lstTbl:
            if cd['title'] == strTitle:
                lstTbl.remove(cd)
        print('You have removed a CD. This is the new CD Inventory')
        print('ID, CD Title, Artist')
        ## Use a for loop to print remaining list values as separate lines
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print()
                         
    elif strChoice == 's':
        # 7. Save the data to a text file CDInventory.txt if the user chooses so
        ## Open the text file using an append access
        objFile = open(strFileName, 'a')
        ## Unpack the list of list as separate entry per CD
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            ## Save the file into the text file
            objFile.write(strRow)
        objFile.close()
        
    else:
        # 8. Display options
        ## Print the menu option for the user
        print('Please choose either l, a, i, d, s or x!')

