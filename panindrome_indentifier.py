# Panindrome Indentifier code


def main():
    while 0 < 1:
        #User types an input, can exit the loop if they want
        palindrome = input("Enter string to test for palindrome or 'exit':")
        if palindrome == "exit":
            exit(0)

        #Converts string to all lowercase
        palindrome = palindrome.lower()

        #String containing all symbols and spaces to be removed
        punc = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
        
        #For loop removes symbols and spaces
        for c in palindrome:
            if c in punc:
                palindrome = palindrome.replace(c, "")

        #Creates a reversed copy of the palindrome to compare 
        reversed = palindrome[::-1]

        #For loop  compares each character 1 by 1, if it fails at any point it exits the loop immediately
        for n,c in enumerate(palindrome):
            if n == int(len(palindrome)/2): #Added as it only needs to ensure the first half of the string doesn't fail
                break
            elif c != reversed[n]:
                result = "Palindrome test: False"
                break
            else:
                result = "Palindrome test: True"           

        #Tells the user if they they entered is or is not a palindrome
        print(result)

#Main function runs on start up if this script is main script i.e. not called by another script
if __name__ == "__main__":
    main()
