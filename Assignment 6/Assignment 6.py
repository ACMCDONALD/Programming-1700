#Program: Assignment #6
#Written By: Andrew McDonald (W0426368)
#Date written: Started - 4 Apr 19
#Purpose: Create a program for the Savoy Theatre seating system

#Seating Chart
def Display_seats(seat_chart):

    row = 0
    col = 0
    print()
    print('\t\tSavoy Theatre Seating Plan')
    print()
    
    printline = format ('', '5') + '\t'
    
    for col in range(7):
        printline += format('Seat ' + str(col), '5') + '\t'
    print(printline)

    for row in range(11):
        printline = 'Row ' + str(row) + '\t'
        for col in range (7):
            printline += format(seat_chart [row] [col], '5') + '\t'
        print(printline)

    return seat_chart

#Inputs for purchase
def Take_inputsAdd(seat_chart):

    print()
    print()

    #Zeroize input data
    Seat_row = [0]
    Seat_col = [0]
    Cust_name = ['']

    #Gather data
    Seat_row = int(input('Enter Row '))
    Seat_col = int(input('Enter Seat '))
    Cust_name = input('Customer Name? ')

    #Check if seat exists and is empty
    try:
        if seat_chart[Seat_row][Seat_col] == 'empty':
            #change item in the list
            seat_chart[Seat_row][Seat_col] = Cust_name
        elif seat_chart[Seat_row][Seat_col] != 'empty':
            print('\nSorry that seat is already sold')
    except:
        print('Sorry, invalid seat entered')



#Inputs for Refund
def Take_inputsRem(seat_chart):

    print()
    print()

    #Zeroize input data
    Seat_row = [0]
    Seat_col = [0]
    Cust_name = ['']

    #Gather data
    Seat_row = int(input('Enter Row '))
    Seat_col = int(input('Enter Seat '))
    Cust_name = input('Customer Name? ')

    #Check if seat exists and is empty
    try:
        if seat_chart[Seat_row][Seat_col] == Cust_name:
            #change item in the list
            seat_chart[Seat_row][Seat_col] = 'empty'
        elif seat_chart[Seat_row][Seat_col] == 'empty':
            print('\nSorry that seat cannot be refunded')
    except:
        print('Sorry, invalid seat entered')

#Main
def main():

    #Begin 
    print('\t\t Welcome to the Savoy Theatre')
    print()
    print()
    
    #initalize array with 'empty' as value in all seats
    Seat_Chart = [['empty' for _ in range(7)] for _ in range (11)]

    #Start Loop
    #Have user choose Purchase or Refund
    Purpose = input('Enter \'p\' to purchase a seat or enter \'r\' to refund a seat: ')

    CustEntry = 1000
    
    while CustEntry >= 0:

        #If processing a Purchase
        if Purpose == 'p':

            #Call seat chart
            seating = Display_seats(Seat_Chart)

            #Gather our inputs
            Take_inputsAdd(seating)
        
            #Display NEW seating chart
            seating = Display_seats(Seat_Chart)
            print()
            print()

        #If processing a Refund
        elif Purpose == 'r':

            #Call seat chart
            seating = Display_seats(Seat_Chart)

            #Gather our inputs
            Take_inputsRem(seating)

            #Display NEW seating chart
            seating = Display_seats(Seat_Chart)
            print()
            print()

        CustEntry -=CustEntry

        #End Loop
        Purpose = input('Enter \'p\' to purchase a seat or enter \'r\' to refund a seat: ')
    
main()
