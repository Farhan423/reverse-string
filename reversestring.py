#Question03 Write a program (using functions!) that asks the user for a long string containing multiple words.

#Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#                   My name is Michele
#Then I would see the string:
#                   Michele is name My
#shown back to me.



def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words
user_input = input("Enter your full name: ")  # Ask the user for input
reversed_string = reverse_words(user_input)   # Call the function to reverse the words
print(reversed_string)
