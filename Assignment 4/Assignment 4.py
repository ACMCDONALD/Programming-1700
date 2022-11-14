#Program: Assignment #4
#Written By: Andrew McDonald (W0426368)
#Date written: Started - 25 Feb 2019
#Purpose: Create a program to accurately do loan calculations for Larry's Loan

#Interest rate calculation function
def interest_rate(Credit_Rating):

    #Take credit rating input and output interest rate
        if Credit_Rating == 'a':
            Int_rate = 0.035
        elif Credit_Rating == 'b':
            Int_rate = 0.04
        elif Credit_Rating == 'c':
            Int_rate = 0.065
        elif Credit_Rating == 'd':
            Int_rate = 0.08
        elif Credit_Rating == 'e':
            Int_rate = 0.1

    #Calculate percent rate from interest rate
        Pct_rate = Int_rate * 100

    #Display Interest rate
        print('Interest rate:', format(Pct_rate, ',.2f'), '%')

        return Int_rate

#Loan payment calculation function
def loan_payment(principle, years, freq, rate):

    #Loan payment formula: A=P((r(1+r)^n) / ((1+r)^n -1))
    #Where:
    #A = payment amount per period
    #P = initial principle (loan amount)
    #r = interest rate per period
    #n = total number of payments or periods

    #calculate r and n
    if freq == 'm': #monthly
        rate_perperiod = float(rate/100) / 12
        payments = float(round(12 * years))
    elif freq == 'b': #bi-weekly
        rate_perperiod = float(rate/100) / 26
        payments = float(round(26 * years))
    
    #The formula in action
    Loan_Payment = float((principle*((rate_perperiod*(1+rate_perperiod)**payments) / ((1+rate_perperiod)**payments -1))))

    return Loan_Payment, payments

#Payment Schedule Function
def payment_schedule(Principle, period_rate, payment, Num_Payments):

        line = chr(124) #vertical line

        #Set variables to baseline
        Payment_Number = 1
        balance = Principle
        period_interest = float((balance/Num_Payments) * period_rate)
        initpayment = payment
        new_balance = balance - payment
        total_interest = period_interest
        

        #Display payment schedule
        print()
        print('----------------------------- Payment Schedule ---------------------------')
        print('==========================================================================')
        print(line, 'Payment:', line, 'Current Balance:\t', line, 'Interest:', line, 'Payment:\t', line, ' Balance:\t', line)
        print('==========================================================================')
        print(line, Payment_Number,  '\t  ', line, '$', format(balance, ',.2f'), '\t', line, '$', format(period_interest, ',.2f'), '  ',  line, '$', format(initpayment, ',.2f'), '\t',  line, '$', format(new_balance, ',.2f'), '\t',  line)
        print('--------------------------------------------------------------------------')
        
        #Loop until balance = 0
        while new_balance >= 0:

                #increment payment number
                Payment_Number += 1 
                #reset balance to previous new balance
                balance = new_balance
                #calculate new balance after payment
                new_balance = balance - payment
                #calculate period interest
                interestpp = ((new_balance/Num_Payments) * period_rate)
                #increment total interest
                total_interest += interestpp
                
                print(line, Payment_Number,  '\t  ', line, '$', format(balance, ',.2f'), '\t\t', line, '$', format(interestpp, ',.2f'), '  ',  line, '$', format(initpayment, ',.2f'), '\t',  line, '$', format(new_balance, ',.2f'), '\t',  line)
                print('--------------------------------------------------------------------------')
                #End loop

        #Add initial interest to looped interest amounts
        total_interest += period_interest
        
        #Display total interest on the loan
        print()
        print()
        print('Total interest on the loan is: $', format(total_interest, ',.2f'))


#Main function
def main():

        print('Larry\'s Loans')
        print()
        print()

        #Request inputs from user
        Principle = float(input('Enter the principle amount of the loan:'))
        Credit_Rating = input('Enter the client credit rating (a-e):')
        Years = int(input('Enter the number of years for the loan'))
        Payment_Freq = input('Select \'m\' for monthly payments -or- \'b\' for bi-weekly payments')

        print() 

        #Call interest rate function
        Int_rate = interest_rate(Credit_Rating)
                        
        print()
  
        #Display Loan Payment
        Loan_Payment, Payments = (loan_payment(Principle, Years, Payment_Freq, Int_rate))
        print('The loan payments will be $', format(Loan_Payment, ',.2f'))
        
        #Display Payment Schedule
        payment_schedule(Principle, Int_rate, Loan_Payment, Payments)
        

        #display end of program
        print()
        print('End of program')    
        
#Call the main
main()


