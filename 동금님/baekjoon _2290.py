# 백준 알고리즘 2290 LCD Test study

import sys
print = sys.stdout.write
c = (
    (1,1,1,0,1,1,1), # 0
    (0,0,1,0,0,1,0), # 1
    (1,0,1,1,1,0,1), # 2
    (1,0,1,1,0,1,1), # 3
    (0,1,1,1,0,1,0), # 4
    (1,1,0,1,0,1,1), # 5
    (1,1,0,1,1,1,1), # 6
    (1,0,1,0,0,1,0), # 7
    (1,1,1,1,1,1,1), # 8
    (1,1,1,1,0,1,1)  # 9
)
s,n = input().split()
s = int(s)
m = len(n)
for i in range(5): # 최대 높이 5 (1.맨윗줄, 2.몸통 위쪽, 3.가운데줄, 4.몸통아래쪽, 5.맨아랫줄)
    if i in [0,2,4]: # 가로
        for j in range(m):
            now = int(n[j])
            if j != 0:
                print (' ')
            print(' ')
            if (i == 0 and c[now][0]) or (i == 2 and c[now][3]) or (i == 4 and c[now][6]):
                print('-'*s)
            else:
                print(' '*s)
            print(' ')
        print('\n')
        
    else:  # 세로
        for l in range(s):
            for j in range(m):
                now = int(n[j])
                if j != 0:
                    print(' ')
                if (i == 1 and c[now][1]) or (i == 3 and c[now][4]):
                    print('|')
                else:
                    print (' ')
                print(' '*s)
                if (i == 1 and c[now][2]) or (i == 3 and c[now][5]):
                    print('|')
                else:
                    print(' ')
            print('\n')
