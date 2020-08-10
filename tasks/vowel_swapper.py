def vowel_swapper(string):
    # ==============
    # Your code here
    string = string.replace('a', '4').replace('A', '4')
    string = string.replace('e', '3').replace('E', '3')
    string = string.replace('i', '!').replace('I', '!')
    string = string.replace('o', 'ooo').replace('O', '000')
    string = string.replace('u', '|_|').replace('U', '|_|')
    return string


   #commit pls
    # ==============

print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console