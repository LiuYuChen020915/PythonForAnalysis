products = [["iphone",6888],["MacPro",14800],["小米6",2499],
            ["Coffee",311],["Book",60],["Nike",699]]
index=0
n = 5
print("-----商品列表-----")
for item in products:
    if index<=n:
        print(index,item[0],item[1],end="\n")
    index+=1
