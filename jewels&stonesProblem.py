
'''
input: jewels ="aA", stones= "aAAbbbbb"

outbut== 3
'''

def jewelStone(jewels:str,stones:str):
    jewel_set = set(jewels)
    count = 0
    
    for stone in stones:
        if stone in jewel_set:
            count+=1
    
    return count

jewels = "CaA"
stones = "aAAbbAab"
result = jewelStone(jewels,stones)

print(result)