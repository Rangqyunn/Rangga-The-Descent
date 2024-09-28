# game loop
while True:
    max_height = 0  
    target_index = 0  
    
    for i in range(8):
        mountain_h = int(input())  
        
        if mountain_h > max_height:
            max_height = mountain_h
            target_index = i  
    
    print(target_index)
