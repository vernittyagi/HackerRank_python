N,M = map(int,input().split(" "))
print(N,M)

#  |, . and - these to be used 
'''
 Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
'''
line ='|'
dot='.'
dash = '-'
stn = '.'+'|'+'.'
pattern = [(stn*(2*i+1)).center(M,'-') for i in range(N//2)]
print('\n'.join(pattern + ['WELCOME'.center(M,'-')] + list(reversed(pattern))))
