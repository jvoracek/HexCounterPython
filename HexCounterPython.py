import binascii
my_dict = {'key':'value'}

#Change this to your filename
myFile = "myFile.txt"

print(" ")
print("Welcome to Hex Counter!")
print(" ")
print("This simple tool lists the sum of each hexadecimal value in your file.")
print(" ")
print("Now counting hex values for " + myFile + "... This can take a while for large files.")

with open(myFile, 'rb') as f:
   while 1:
      byte_s = f.read(1)
      key = (binascii.hexlify(byte_s))
      if key in my_dict:
          val = my_dict.get(key)
          my_dict[key] = (val + 1)  
      else:
          my_dict[key] = 1
      if not byte_s:
         break
      byte = byte_s[0]
   print(" ")
   print("Finished! Now displaying as hexValue - numOfValues pair.")
   print(" ")
   for k, v in my_dict.items():
       print(k, v)
   print(" ")
   print("Finished! Results displayed above as hexValue - numOfValues pairs.")
#Made with <3 by Jace Voracek