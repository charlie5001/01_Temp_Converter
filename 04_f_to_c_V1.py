#quick component to convert degrees C to F
#Function takes in value, does conversion and puts answer into a list

def to_c(from_f):
    celcius  = (from_f - 32) * 5/9
    return celcius

#Main Routine
temperatures  = [40, 40, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statment = "{} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statment)
print(converted)