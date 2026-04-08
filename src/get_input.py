def get_input(filename):

    with open(f"../data/{filename}", 'r') as file:
        #Whole file
        everything = file.read()

        everything = everything.split()

        # reading alphabet size and lists
        k = int(everything[0])
        everything.pop(0) #get rid of k from the list

        a = everything.pop(-2) #remove a & b, leaving just the letters and values
        b = everything.pop(-1)


        unfiltered = everything

        letters = []
        values = []

        for i, val in enumerate(unfiltered):
            # even indices are letters
            if i % 2 == 0:
                letters.append(val)
            #odd indices are values
            else:
                values.append(val)

    return k, letters, values, a, b


#testing purposes
#get_input("16_b43.in")