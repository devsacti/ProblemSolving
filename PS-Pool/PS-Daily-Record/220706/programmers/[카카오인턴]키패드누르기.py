def compare_dist(target,hand):
    dist=abs(target[0]-hand[0])+abs(target[1]-hand[1])
    return dist

def solution(numbers, hand):
    answer = ''
    # assume keypad by matrix
    matrix=[[0]* 3 for _ in range(4)]
    
    # dict[number] is coordinate
    num_coord={}
    
    for r in range(3):
        for c in range(3):
            key=3*r+(c+1)
            num_coord[key]=[r,c]
    # *, 0, #
    num_coord["*"]=[3,0]
    num_coord[0]=[3,1]
    num_coord["#"]=[3,2]
    # print(num_coord)
    
    # left, right coordinate init
    coord_left=num_coord["*"]
    coord_right=num_coord["#"]

    for number in numbers:
        left_move=False
        right_move=False
        # (1 or 4 or 7) -> Wrong
        # number == 1 or number == 4 or number == 7 -> Correct, and futher is below
        if number in [1,4,7]:
            left_move=True
        elif number in [3,6,9]:
            right_move=True
        else:
            coord_target=num_coord[number]
            
            left_dist=compare_dist(coord_target,coord_left)
            right_dist=compare_dist(coord_target,coord_right)
            
            if left_dist<right_dist:
                left_move=True
            elif left_dist>right_dist:
                right_move=True
            else:
                if hand=='left':
                    left_move=True
                else:
                    right_move=True
                    
        if left_move:
            answer+='L'
            coord_left=num_coord[number]
        
        if right_move:
            answer+='R'
            coord_right=num_coord[number]
            
            
    return answer