import pylightxl as xl

with open('cities.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

#ask the user for the code of the country and save it into a variable


#Scan the list l line by line and add 1 to the counter if the country is the one looked for


#Format and print the result


#Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer


#Store the population values into a list called l1 (see line 6)


#Initialize a list lstOfRecords to an empty list


#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords


#Print the list l1


#Bonus: Print the name of the cities whose index is in l1