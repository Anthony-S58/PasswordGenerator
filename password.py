# Password Generator Test

#import random for randomize all
import random

#set variables for password with lower case, upper case, numbers and symbols

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&*-_\/"

#what we are using for 

usefor = lower_case + upper_case + numbers + symbols

# password length set to 12 to have secured password

length_password = input("Quelle taille doit faire votre mot de passe ? ")

# password variable with .join method avec random.sample function

password = "".join(random.sample(usefor, int(length_password)))

print("Votre mot de passe aléatoire est :" + password)

