import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

#ask the user for the code of the country and save it into a variable
countryCode = input("Please enter the code of your country: ")

#Scan the list l line by line and add 1 to the counter if the country is the one looked for
nCities = 0
for el in l:
    if el == countryCode:
        nCities += 1
#Format and print the result
print("There are {} cities in your country.".format(nCities))

#Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer
done = False
while done == False:
    try:
        iPopulation = int(input("Please enter the population you looked for: "))
        done = True
    except:
        print("Input is not a number, please try again.")
#Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5))

#Initialize a list lstOfRecords to an empty list
lstOfRecords = []

#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
for i in range(len(l1)):
    if l1[i] > iPopulation:
        lstOfRecords.append(i)


#Print the list lstOfRecords
print(lstOfRecords)

#Bonus: Print the name of the cities whose index is in lstOfRecords
l2 = list(db.ws(ws='Sheet1').col(col=2))
l3 = []
for el in lstOfRecords:
    l3.append(l2[el])
print("These cities have larger population: {}".format(l3))
