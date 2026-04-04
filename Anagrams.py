s1=input('Enter a 1st string : ')
s2 = input('Enter a 2nd string : ')
s1 = s1.lower()
s2=s2.lower()
for x in s1:
    if x.isalpha():
        if s1.count(x) != s2.count(x):
            print('Not anagrams')
            break
else:
    print('Anagrams')