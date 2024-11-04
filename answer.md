# 期中考
>
>學號：112111208
><br />
>姓名：黃誌麒
><br />
>作業撰寫時間：30 (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2024/11/04
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容

## 說明程式與內容

開始寫說明，該說明需說明想法，
並於之後再對上述想法的每一部分將程式進一步進行展現，
若需引用程式區則使用下面方法，
若為.cs檔內程式除了於敘述中需註明檔案名稱外，
還需使用語法` ```語言種類 程式碼 ``` `，其中語言種類若是要用python則使用py，java則使用java，C/C++則使用cpp，
下段程式碼為語言種類選擇csharp使用後結果：

```csharp
public void mt_getResult(){
    ...
}
```

若要於內文中標示部分網頁檔，則使用以下標籤` ```html 程式碼 ``` `，
下段程式碼則為使用後結果：

```html
<%@ Page Language="C#" AutoEventWireup="true" ...>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" ...>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
    </form>
</body>
</html>
```
更多markdown方法可參閱[https://ithelp.ithome.com.tw/articles/10203758](https://ithelp.ithome.com.tw/articles/10203758)
請在撰寫"說明程式與內容"該塊內容，請把原該塊內上述敘述刪除，該塊上述內容只是用來指引該怎麼撰寫內容。


a小題

Ans:
```py
map:list[list[chr]]=[[' ']*10 for _ in range(10)]  #設定二維陣列
```

b小題

Ans:
```py
rowMap:list[int]=[0]*100  #設定一維陣列
```

c小題

Ans:
```py
for b in range (0,10):  #讓使用者輸入10個位子(炸彈)
    boom=int(input())
    rowMap[boom]=1
```


d小題

Ans:
```py
for i in range(0,10):  #將一維陣列中有炸彈的位子轉成二維的對應位子並設為*
    for j in range(0,10):
        if rowMap[i*10+j]==1:
            map[i][j]='*'
```


e小題

Ans:
```py
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
```
```py
for row in map:  #顯示最終結果
    print('  '.join(row))
```
