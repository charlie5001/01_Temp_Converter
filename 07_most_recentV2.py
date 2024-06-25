#Get data from user and store it in a list, then
#display the most recent three entries nicely

#Set up empty list
all_caculations = []

#Get fice items of Data
get_item = ""
while get_item != "xxx":
    get_item  = input("Enter an item: ")
    
    if get_item == "xxx":
        break
    
    all_caculations.append(get_item)

if len(all_caculations) == 0:
    print("The list is empty")
else:
    
    #Show that everything is added to the list
    print()
    print("*** The Full List ***")
    print(all_caculations)
    print()

    if len(all_caculations) > 3:
        print("*** Most Recent 3 ***")
        #print items starting at the end of the list
        for item in range(0,3):
            print(all_caculations[len(all_caculations) - item - 1])
    else:
        #Video does not show rest of the code
        print("*** Items from Newest to Oldest ***")
        print(all_caculations[0-len(all_caculations):])
