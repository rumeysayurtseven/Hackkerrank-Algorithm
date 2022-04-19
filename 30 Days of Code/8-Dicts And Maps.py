""" Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!
Task
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.
Note: Your phone book should be a Dictionary/Map/HashMap data structure.
Input Format
The first line contains an integer, , denoting the number of entries in the phone book.
Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line. The first value is a friend's name, and the second value is an -digit phone number.
After the  lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.
Note: Names consist of lowercase English alphabetic letters and are first names only. """

"start"
# Enter your code here. Read input from STDIN. Print output to STDOUT
phoneBook = {}
n = int(input())
for i in range(0,n):
    entry = str(input()).split(" ")
    name = entry[0]
    number = int(entry[1])
    phoneBook[name]= number
for i in range(0, n):
    name = input()
    if name in phoneBook:
        print(name + "=" + str(phoneBook[name]))
    else:
        print("Not found");

"end"


"OR"

N=int(input())
phoneBook={}

for _ in range(N):
    name,contact=input().split()
    phoneBook[name]=contact

try:
    while(True):
        check=str(input())
        if check in phoneBook:
            print(check+"="+phoneBook[check])
        else:
            print('Not found')

except(EOFError):
    pass
