I used Claude to:
- Find Python libraries and functions that would be useful in solving my problem
- recommend using enumerate to find the index of the char
- verify syntax
- import logic class into testing class

What I did myself:
- I wrote the tests to go through each typical situation the method has to handle
- I wrote the function once I decided to use Counter and enumerate
- I set up the workflow to integrate the tests on push

Verification: 
- Counter and enumerate did what they were supposed to, counting each instance of each character and returning the character with the index
- Being used to Java and C#, sometimes I needed a bump in the right direction syntactically, either with formatting a for loop or setting up main correctly
- I was able to call the method from utils.py just fine within test_utils.py.
