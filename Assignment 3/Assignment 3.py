#Program: Assignment #3
#Written By: Andrew McDonald (W0426368)
#Date written: 4 Feb 2019
#Purpose: Track individual and daily sales for Bills Books

#Call the main
def main():

    #Define constants
    TAX = 1.15 #15% tax rate

    #Define variables needed
    cust_name = 0
    cust_total = 0 #total customers per day
    daily_total = 0 #total sales per day
    daily_books = 0 #number of books sold per day
    
    print('Bill\'s Books')
    print()
    
    #Gather customer name
    cust_name = input('Customer Name: (type 1 to stop)')

    #Start main loop
    while cust_name != "1":

                #Reset variables
                book_price = 0
                book_number = 0
                subtotal = 0
                discount = 0
                total = 0

                #Gather book price
                book_price = float(input('Enter book price (type 1 to stop):'))

                #Start book entry loop
                while book_price != 1:

                    subtotal = subtotal + book_price
                    book_number += 1
    
                    #print current information
                    print('# of books / Price / Subtotal')
                    print(book_number, '        /', book_price, '/  ', subtotal)

                    #Get next book price
                    book_price = float(input('Enter book price (type 1 to stop):'))

                #End book entry loop

    
                #print subtotal
                print('Subtotal is: $', format(subtotal, ',.2f'))

                #Calculate discount
                if subtotal <= 9.99:
                    discount = subtotal * 0
                elif subtotal >= 10.00 and subtotal <= 19.99:
                    discount = subtotal * 0.01
                elif subtotal >= 20.00 and subtotal <= 29.99:
                    discount = subtotal * 0.02
                elif subtotal >= 30.00 and subtotal <= 39.99:
                    discount = subtotal * 0.03
                elif subtotal >= 40.00:
                    discount = subtotal * 0.04
    
                #Display  discount
                print('Discount is: $', format(discount, ',.2f'))


                #calculate subtotal with discount
                subtotal = subtotal - discount
                #calculate total with tax
                total = subtotal * TAX
                #print customer total
                print('Customer Total: $', format(total, ',.2f'))

                #Increase customer count
                cust_total += 1
                #Increase daily book count
                daily_books += book_number
                #Increase daily total
                daily_total += total

                #Get next customer name
                cust_name = input('Customer Name: (type 1 to stop)')

    #End Main Loop

    #Display daily totals
    print()
    print('-------------Totals-------------')
    print()
    print('Total number of customers: ', cust_total)
    print('Total number of books sold:', daily_books)
    print('Total sales:              $', format(daily_total, ',.2f'))

    #display end of program
    print()
    print('End of program')
    
#Call the main
main()

