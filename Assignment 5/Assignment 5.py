#Program: Assignment #5
#Written By: Andrew McDonald (W0426368)
#Date written: 11 Mar 19
#Purpose:Import student grade data, determine average and honours then output data to new file

def header():

        #Display header data
        print()
        print('\t\t\t\t\t\t\t\tStudent Grade Report')
        print('------------------------------------------------------------------------------------------------------------------------------------')
        print('Student ID \tStudent Name \t\tWindows \tHTLM \tCommunications \tProgramming \tHardware \tGrade Average')
        print('------------------------------------------------------------------------------------------------------------------------------------')


        #Write header to studentAverage.txt
        Grade_Output = open('studentAverage.txt', 'w')

        Grade_Output.write ('Student ID \tStudent Name \t\tGrade Average \n')

        Grade_Output.close()

def read_data(Student_Grades):

        #begin to read file line by line
        Grade_Data = Student_Grades.readline()

        #begin reading loop until empty string
        while Grade_Data !='':
            Student_ID = Grade_Data.rstrip('\n')
            Grade_Data = Student_Grades.readline()
            Student_Name = Grade_Data.rstrip('\n')
            Grade_Data = Student_Grades.readline()
            gradeWin = float(Grade_Data)
            Grade_Data = Student_Grades.readline()
            gradeHTLM = float(Grade_Data)
            Grade_Data = Student_Grades.readline()
            gradeCom = float(Grade_Data)
            Grade_Data = Student_Grades.readline()
            gradePro = float(Grade_Data)
            Grade_Data = Student_Grades.readline()
            gradeHar = float(Grade_Data)
            
            #Calculate total grade for average
            Grades_total = gradeWin + gradeHTLM + gradeCom + gradePro + gradeHar
            #Calculate average grade
            Grade_average = (Grades_total/5)

            #Determine honours
            if gradeWin >= 80 and gradeHTLM >= 80 and gradeCom >= 80 and gradePro >= 80 and gradeHar >= 80:
                Grade_check = 1
            else:
                Grade_check = 0

            if Grade_average >=80 and Grade_check == 1:
                Honours = '(Hons.)'
            else:
                Honours = ''

            #Print data from studentGrades.txt
            Grades = Student_ID + '\t\t' + Student_Name + '\t\t'
            Grades += format(gradeWin, '.2f') + '%\t\t'
            Grades += format(gradeHTLM, '.2f') + '%\t'
            Grades += format(gradeCom, '.2f') + '%\t\t'
            Grades += format(gradePro, '.2f') + '%\t\t'
            Grades += format(gradeHar, '.2f') + '%\t\t'
            Grades += format(Grade_average, '.2f') + '%\t'
            Grades += Honours

            print(Grades)
            

            #Write to studentAverage.txt
            Grade_Output = open('studentAverage.txt', 'a')

            Grade_Output.write (Student_ID + '\t\t')
            Grade_Output.write (Student_Name + '\t\t')
            Grade_Output.write (str(Grade_average) + '% ')
            Grade_Output.write (Honours + '\n')

            Grade_Output.close()

            Grade_Data = Student_Grades.readline()
        
def main():
        
    #Open studentGrades.txt
    try:
        Student_Grades = open('studentGrades.txt', 'r') 

    #Show errors with file if any exist
    except Exception as err:
        print('Error - Problem trying to read file!')
        print('      ǀ The following problem has occured')
        print()
        print(err)

    #If no errors continue on
    else:

        header()

        read_data(Student_Grades)
        
    #Close studentGrades.txt
    Student_Grades.close()   
        
main()
