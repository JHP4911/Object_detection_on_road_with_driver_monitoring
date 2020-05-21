import sys
import xlsxwriter
from Tkinter import *
import pandas as pd							       #import Tkinter fpr python 2.7
workbook = xlsxwriter.Workbook('excel_data.xlsx')			       #passing filemane as an argument to workbook.
worksheet = workbook.add_worksheet()                                           #new worksheet is added in workbook
row = 0
column = 0	
with open('output.txt', 'w+') as c:                                            #open output txt file.
                                         
	with open('log.txt') as a:                                             #open the log file.
		substr= ('failure','error','fault')		 	       #make list of words to find in lof file.
		a1=[]
		count=0
		count_2=0
		for line in a:
			for i in substr:
				if i in line:
					c.write(line)                          #writing the lines with error to output file.
					count=count+1
			if "ClassID:" in line:				       #find the word ClassID in the log file.	
					count_2= count_2+1                     #counting number of times object has been found
              				for ID in line.split():
						if ID.isdigit():						
							a1.append(int (ID))    #int because by default.isdigit is a string fn.		
								
        	IDs = list(a1)                                                 #to remove duplicate elements from the array.
		cell_format= workbook.add_format()                             #adding font name and size.
		cell_format.set_font_name('Arial')
		cell_format.set_font_size(10)
		for item in IDs:                                               #loop in ClassID in log file.
			worksheet.write('A1', 'data', cell_format)             #writing the first column heading in excel_data.xlsx.
			worksheet.write(row,column, item, cell_format)         
			row +=1
		workbook.close()
		c.write("Total Failures: ")	                               #writing to output file(saini.txt).	
		a= str(count)        					       #converting integer into the string. 
		c.write(a + '\n\n')					       #writing no. of error lines into saini.txt file.	
		c.write("Total number of objects detected during Live streaming: ") 
		d= str(count_2) 
		c.write(d + '\n\n')
		df1=pd.read_excel('ClassID_Objects.xlsx')                      #using pandas to read excel file(objects and classID).
		df2=pd.read_excel('ClassIDs.xlsx')                             #excel_data.xlsx(ClassID)                         
		df = df1.merge(df2, how = 'inner' ,indicator=False)            #merge the two xlsx files.  
		result = df.drop_duplicates(keep='first',  inplace=False)      #delete the duplicate ClassIds.

		a= result['objects'].to_string(index= False)                   #removing indexes
		#print(a) 
		c.write("Objects detected during the video:\n")
		c.write(a)

window =Tk()								       #creating GUI application window
window.title("OUTPUT")                                                         #setting window title.
bottomframe = Frame(window)                                                    #assigning bottom frame of window
bottomframe.pack(side= BOTTOM)
with open("output.txt", "r+") as f:
	Label(window, text= f.read()).pack()                                   #reading and printing text as an label from the output file.	
btn = Button(bottomframe, text="Exit", fg= "red" , command= window.destroy)    #creating EXIT button.
btn.pack(side = BOTTOM)                                                        #button position at bottom of window(pack)
window.mainloop()                                                              #main event loop to take action.









						       
