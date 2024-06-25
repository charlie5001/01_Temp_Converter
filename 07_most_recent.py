#Get data from user and store it in a list, then
#display the most recent three entries nicely

#Set up empty list
all_caculations = []

#Get fice items of Data
for item in range(0, 5):
    get_item  = input("Enter an item: ")
    all_caculations.append(get_item)

#Show that everything is added to the list
print()
print("*** The Full List ***")
print(all_caculations)
print()
print("*** Most Recent 3 ***")
#print items starting at the end of the list
for item in range(0,3):
    print(all_caculations[len(all_caculations) - item - 1])