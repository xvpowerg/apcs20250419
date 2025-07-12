class list_node:
    def __init__(self):
        self.val=0
        self.next=None
        
head=[list_node()]*6                                #宣告一個節點型態串列

data=[[1,2],[2,1],[2,5],[5,2],                      #圖形陣列宣告
      [2,3],[3,2],[2,4],[4,2],
      [3,4],[4,3],[3,5],[5,3],
      [4,5],[5,4]]

print('圖形的鄰接串列內容：')
print('----------------------------------')
for i in range(1,6):
    head[i]=list_node()                             #建立首節點
    head[i].val=i                                   #串列首head
    head[i].next=None
    print('頂點 %d =>' %i,end='')                   #把頂點值列印出來
    ptr=head[i]
    for j in range(len(data)):                      #走訪圖形陣列
        if data[j][0]==i:                           #如果節點值=i，加入節點到串列首
            newnode=list_node()                     #建立新節點
            newnode.val=data[j][1]                  #宣告新節點，值為終點值
            newnode.next=None
            prver = None
            while ptr!=None:                        #判斷是否為串列的尾端
                ptr=ptr.next
            ptr=newnode                             #加入新節點
            print('[%d] ' %newnode.val,end='')      #列印相鄰頂點
    print()
