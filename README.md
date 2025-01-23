# Password-Strength-Checker-
A checker to make sure your passwords stay strong


**Installation :** 
    https://github.com/CraZyy-2/Password-Strength-Checker-.git



At some point, we have all lost accounts due to our use of weak passwords.
To prevent that from happening, all you have to do is to use this checker.
It will tell you if you are using the right password to protect yourself online.


It will take in consideration : 
  - length
  - the use of different characters
  - the use of numbers
  - the use of special characters
  - the complexity of the structure

**How it's made :**
    the script uses score points to decide wether the password should be used or not depending on some factors : 
   
    Common passwords 
      the script first checks if the given password is commonly used, it cross checks from a 10 million passwords list to make sure it isnt weak.
  
    Length 
      the script checks the passwords length and based on it, it assigns a certain amount of points to your score.

    Character types 
      based on how many character types have been used in your password, the script assigns the adequate amount of points to your score, the more the better.

    Your score 
      using if statements, the script tells how strong your password is depending on how many points you gained from all previous criteria.


