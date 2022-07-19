#US population difference finder from 1950 to 1990
#Jeremy Bargy
#4/7/20


# This program reads numbers from a file into a list.

def main():
    menuOption = ""

    welcome()

    # Open a file for reading.
    infile = open('USPopulation.txt', 'r')

    # Read the contents of the file into a list.
    numbers = infile.readlines()
    
    # Close the file.
    infile.close()

    # initialize variable
    index = 0

    # Convert each element to an int.
    convertElemToInt(numbers, index)

    print('File has been read and elements have been converted to integers into a list.')

    # Create list for years in time period
    years = createYearList(numbers, index)

    print('...New List created for years asscoiated with file.')

    # Create List for population change per year
    changeList = createChangeList(numbers,index)

    print('...New List created for population change asscoiated with years. \n')
    
    # Find the max and min values from created list
    smallestPopIncrease = min(changeList)
    largestPopIncrease = max(changeList)

    # Find average annual change during time period
    averageAnnualChange = getAverage(index,changeList)

    # Find years asscoiated with Max and Min values from created list
    smallChangeYear = getAssociatedYear(index, changeList, years, smallestPopIncrease)
    largeChangeYear = getAssociatedYear(index, changeList, years, largestPopIncrease)
    
    # Print the contents of the list.
    print('Calculations completed... \n')

    while menuOption != "D" and menuOption != "d":

        menuOption = input("Menu\n--------\nSelect A to display Annual Average of Change.\nSelect B to display the Greatest Change of Population.\nSelect C to display the Smallest Change of Population.\nSelect D to end the program.\n")

        # validates the entry. The user has to pick a menu option  
        while menuOption != "A" and menuOption != "a" and menuOption != "B" and menuOption != "b" and menuOption != "C" and menuOption != "c" and menuOption != "D" and menuOption != "d":
            print("Error: Please enter option A, B,C, or D.\n")
            menuOption = input("\nSelect A to display Annual Average of Change.\nSelect B to display the Greatest Change of Population.\nSelect C to display the Smallest Change of Population.\nSelect D to end the program.\n")

        # Display caluclations based on menu option
        if menuOption =="A" or menuOption =="a":
            print('\n\nAnnual Average Change \n -------------------- \n')
            print(averageAnnualChange, '\n\n')

        elif menuOption == "B" or menuOption == "b":
            print('\n\nGreatest Increase of Population \n ------------------------------ \n')
            print('Amount: ', largestPopIncrease, '\n')
            print('Year: ', largeChangeYear,'-', largeChangeYear+1, '\n\n')

        elif menuOption == "C" or menuOption == "c":
            print('\n\nSmallest Increase of Population \n ------------------------------ \n')
            print('Amount: ', smallestPopIncrease, '\n')
            print('Year: ', smallChangeYear,'-', smallChangeYear+1, '\n\n')

        else: 
            print('\n\nThanks for using our program!')
            print('Goodbye!')

def welcome():  #define welcome function
    print('\n\t\t\t\tWelcome Users\n\t\t\t\t---------------')
    print('Thank you for taking the time to use this program.')
    print('The program was made by Jeremy Bargy.')
    print('Last update April 2020')

    #Display description of program
    print('\n\t\t\t\tInstructions\n\t\t\t\t------------')
    print('The program being used is designed to read a file that contains number related to the midyear US population from 1950 to 1990.\n')
    print('With this information, the program will calculate the average annual change in population given the time frame. \n')
    print('This program will also find the largest and smallest increases in population during this time.\n\n')

# Function used to convert elements of a list to integers
def convertElemToInt(numbers, index):
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1

# Function to create a list of years given the constant of the starting year
def createYearList(numbers, index):
    years=[]
    STARTYEAR=1950
    while index < len(numbers):
        years.append(STARTYEAR)
        index += 1
        STARTYEAR +=1
    return years

# Function used to create a list of the changes in population based on numbers of another list
def createChangeList(numbers,index):
    changeList = []
    for index in range(1, len(numbers)):
        increaseChange = numbers[index]-numbers[index-1]
        changeList.append(increaseChange)
        index += 1
    return changeList

# Function used to calculate the average based on the numbers of another list
def getAverage(index,changeList):
    total = 0
    for num in changeList:
        total += num
        index+=1
    average = total // index
    return average

# Function used to determine the value of a specific item indexed from another list
def getAssociatedYear(index, changeList, years, variableName):
    itemIndex = changeList.index(variableName)
    returnYear = years[itemIndex]
    return returnYear
    
# Call the main function.
main()
