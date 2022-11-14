#Program: Assignment 2
#Written By: Andrew McDonald (W0426368)
#Date Written: 30 Jan 2019
#Purpose: Calculate the cost of client's haircuts for Sally's Shear Delight

def main():

    #Define constants
    SVC1 = 18.75
    SVC2 = 29.50
    SVC3 = 38.75
    SVC4 = 79.80
    SVC5 = 95.50
    TAX = 0.15
    DISCOUNT = 0.9

    print('\n\n\t\tSally\'s Shear Delight')
    #Ask for input of service
    print('\n\n\t\tServices')
    print()
    print('Select 1 for Men\'s Dry Cut')
    print('Select 2 for Men\'s Wash and Cut')
    print('Select 3 for Ladies Wash, Cut, and Blowdry')
    print('Select 4 for Ladies Colour, Cut and Style')
    print('Select 5 for Ladies Colour, Foils, Cut and Style')
    service = input('Select a service 1-5')

    #Assign price to service selected (sevsel)
    if service == '1':
        svcsel = SVC1
    elif service == '2':
        svcsel = SVC2
    elif service == '3':
        svcsel = SVC3
    elif service == '4':
        svcsel = SVC4
    elif service== '5':
        svcsel = SVC5
    

    print()

    #Check for seniors discount
    sendisc = input('Is customer a senior? (y/n)')

    #Apply seniors discount to service selected if required.
    #Determine subtotal
    if sendisc == 'y':
        subtotal = svcsel * DISCOUNT
    else:
        subtotal = svcsel

    print()

    #Calculate tax and total
    taxtotal = subtotal * TAX
    total = subtotal + taxtotal
    print('Total is:', '$', format(total, ',.2f'))

    print()

    #Take payement input and calculate/output change due
    pay = input('Input payment $:')
    change = float(pay) - float(total)
    print('Change due is:', '$', format(change, '.2f'))


    print()
    print()

    #Sales Slip
    print('    Sally\'s Shear Delight')
    print()
    print()

    #svcprnt created to output name of service
    if service == '1':
        svcprnt = 'Men\'s Dry Cut'
    if service == '2':
        svcprnt = 'Men\'s Wash and Cut'
    if service == '3':
        svcprnt = 'Ladies Wash, Cut, and Blowdry'
    if service == '4':
        svcprnt = 'Ladies Colour, Cut and Style'
    elif svcsel == SVC5:
        svcprnt = 'Ladies Colour, Foils, Cut and Style'

    print('Service:', svcprnt)
    print('Service cost:', '$', format(svcsel, '10,.2f'))
    print('Seniors discount?:      ', sendisc)
    print()
    print('--------------------------')
    print('Subtotal:    ', '$', format(subtotal, '10,.2f'))
    print('Tax:         ', '$', format(taxtotal, '10,.2f'))
    print('Total:       ', '$', format(total, '10,.2f'))
    print()
    print('Payment:     ', '$', format(float(pay), '10,.2f'))
    print('Change Due   ', '$', format(change, '10,.2f'))
    print()
    print('==========================')
    print()
    print('Thank you, come again!')

    #display end of program
    print()
    print('End of program')
    
#Call the main
main()
