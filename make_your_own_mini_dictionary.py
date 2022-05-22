print ("Please enter the String: ", end = "")  
string = input()  
string_length = len(string)  
for i in string:  
    ASCII = ord(i)  
    print (i, "\t", ASCII)
    