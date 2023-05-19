def reverse_str():
   input_str = input("Enter the string to reverse it: ")
   reversed_word = ""
   i = len(input_str) - 1
   while i >= 0:
     reversed_word += input_str[i]
     i -= 1
   print("Reversed word is :", reversed_word)
reverse_str()