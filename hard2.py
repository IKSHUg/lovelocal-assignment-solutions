def shortest_palindrome(s):
    # This function takes a string 's' as input and returns the shortest palindrome
    # that can be obtained by adding characters to the beginning of the string.

    for i in range(len(s) - 1, -1, -1):
        # Iterate through the indices of the string 's' in reverse order.

        if s[:i + 1] == s[:i + 1][::-1]:
            # Check if the substring from the beginning of 's' up to index 'i'
            # is a palindrome. This is done by comparing it to its reverse.

            return s[i + 1:][::-1] + s
            # If it's a palindrome, return the concatenation of the reverse of
            # the substring after index 'i' and the original string 's'.

    return s
    # If the input string is already a palindrome, return the string 's' as is.

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    # Take user input for a string.

    print(shortest_palindrome(user_input))
    # Print the shortest palindrome obtained from the input string using the
    # 'shortest_palindrome' function.
time complexity is approximately O(n^2)
space complexity is approximately O(n)
