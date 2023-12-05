def word(s):
    # This function takes a string 's' as input and calculates the length of the last word in the string.

    s = s.strip()
    # Remove leading and trailing whitespaces from the string.

    last_space_index = s.rfind(' ')
    # Find the rightmost occurrence of a space (' ') in the string.
    # If no space is found, last_space_index will be -1.

    if last_space_index == -1:
        # If no space is found in the string, it means there is only one word.
        # Return the length of the entire string.
        return len(s)
    else:
        # If a space is found, calculate the length of the last word by subtracting
        # the index of the last space from the total length of the string.
        return len(s) - last_space_index - 1
overall time complexity is O(n)
overall space complexity is O(n)
