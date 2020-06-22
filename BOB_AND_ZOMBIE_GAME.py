'''
In order to move to the next level
Bob need to kill all the N zombie's
but Bob can select any one among N Zombie's.
If energy of Bob (B) is less than Zombie energy (Zi)
then Bob will die and lose the round else Bob will won,
during the fighting with zombie,
Bob will lose his energy by (Zi%2)+(Zi/2).
At any point of game Bob will play optimally.
Now your task is to find out whether Bob can reach to the next level or not.
Input:
35 3 
5 9 6
Sample Output
YES
'''

b,zs=map(int,input().split())
z=list(map(int,input().split()))[:zs]
for i in z:
    if b <= i:
        #print(b)
        print('NO')
        break
    elif(b > i):
        #print(b)
        b-=(i%2)+(i/2)
        #continue
else:
    print('YES')
