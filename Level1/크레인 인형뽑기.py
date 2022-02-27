def solution(board, moves):
    crain =[]
    answer=0
    for i in moves:
        i-=1
        for j in range(len(board)):
            if board[j][i] !=0:
                crain.append(board[j][i])
                board[j][i] =0
                if len(crain)>1 and crain[-1] == crain[-2]:
                    print(crain)
                    crain.pop(-1)
                    crain.pop(-1)
                    print(crain)
                    answer+=2
                break
                
    print(crain)      
    
            
    return answer
solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])