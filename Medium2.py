def exam(l):
    # This function takes a list 'l' as input.

    k = []  # Initialize an empty list 'k' to store elements occurring more than (len(l)//3) times.

    for i in l:
        # Iterate through each element 'i' in the input list 'l'.

        if l.count(i) > (len(l) // 3):
            # Check if the count of the current element 'i' in the list 'l'
            # is greater than one-third of the length of the list 'l'.

            if i not in k:
                # Check if the element 'i' is not already in the list 'k'.
                # This is to avoid duplicate entries in the result list.

                k.append(i)  # Add the element 'i' to the list 'k'.

    return k
    # Return the list 'k' containing elements that occur more than one-third
    # of the length of the input list 'l'.
 print(exam(l))
time complexity is O(n^2), where n is the length of the input list
overall space complexity is O(n)
