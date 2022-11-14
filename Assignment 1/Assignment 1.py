#Program: Assignment 1 - Gas Guzzler
#Written By: Andrew McDonald (W0426368)
#Date Written: 29 Jan 2019
#Purpose: Interpret gas milage

#main routine
def main():
    
    #Define constants
    KMTOM = 0.621371 #kilometer to mile conversion
    LTOGAL = 0.264172 #litre to gallon conversion 

    #print title
    print('Assignment 1 - Gas Guzzler')
    print()

    #take all inputs
    start_odo = float(input('What was your starting odometer reading?'))
    end_odo = float(input('What was your final odometer reading?'))
    fuel_input = float(input('How many litres of fuel did you put in your car?'))
    fuel_cost = float(input('How much did your fuel cost?'))

    print()

    #calculate data
    totalkm = round (end_odo - start_odo)
    totalmile = round((totalkm * KMTOM))
    totalgal = round((fuel_input * LTOGAL))
    mpg = round(totalmile / totalgal)
    costperkm = ((fuel_cost / totalkm))

    #print outputs
    print('Total kilometers traveled:', totalkm)
    print('Total miles traveled:', totalmile)
    print('Total gallons of fuel used:', totalgal)
    print('Total miles per gallon:', mpg)
    print('It cost you per kilometer', end=' ')
    print('$', format(costperkm, ',.2f'))

    #display end of program
    print()
    print('End of program')
                      
#call the main
main()
