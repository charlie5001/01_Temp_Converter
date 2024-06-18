#quick component to convert degrees C to F
#Function takes in value, does conversion and puts answer into a list

def to_f(from_c):
    farhenheit = (from_c * 9/5) + 32
    return farhenheit

#Main Routine
temperatures  = [40, 40, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statment = "{} degrees C is {} degrees F".format(item, answer)
    converted.append(ans_statment)
print(converted)