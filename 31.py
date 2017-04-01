def combination(coins,obj):
    size = len(coins)

    if obj == 0:
        return 1
    if obj < 0:
        return 0
    if size == 0 and obj > 0:
        return 0

    return combination(coins[1:size],obj) + combination(coins,obj-coins[0])
    
coins=[200,100,50,20,10,5,2,1]
print combination(coins,200)