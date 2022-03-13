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
        # reversed = palindrome[::-1]

        #Compares if the word given and it reversed match
        if palindrome == palindrome[::-1]:
            result = "True"
        else:
            result = "False"          

        #Tells the user if they they entered is or is not a palindrome
        print("Palindrome test:", result)

#Main function runs on start up if this script is main script i.e. not called by another script
if __name__ == "__main__":
    main()
