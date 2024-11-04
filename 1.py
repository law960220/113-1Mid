map:list[list[chr]]=[[' ']*10 for _ in range(10)]  #設定二維陣列
rowMap:list[int]=[0]*100  #設定一維陣列
for b in range (0,10):  #讓使用者輸入10個位子(炸彈)
    boom=int(input())
    rowMap[boom]=1
for i in range(0,10):  #將一維陣列中有炸彈的位子轉成二維的對應位子並設為*
    for j in range(0,10):
        if rowMap[i*10+j]==1:
            map[i][j]='*'
for i in range(0,10):  #判斷陣列每個位子周圍的炸彈數量
    for j in range(0,10):
        if map[i][j]!='*':
            n=0
            for x in range(max(0,i-1),min(10,i+2)):  #避免炸彈在邊緣時，計數到陣列另一邊
                for y in range(max(0,j-1),min(10,j+2)):
                    if map[x][y]=='*':
                        n=n+1
            if n>0:
                map[i][j]=chr(n+ord('0'))
            else:
                map[i][j]=' '
for row in map:  #顯示最終結果
    print('  '.join(row))