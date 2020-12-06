def solution(monster, s1, s2, s3):
    all_=[]
    
    #시작점이 1이므로
    #모든 경우에 대해 구해줌
    for num1 in range(2, s1+2):
        for num2 in range(1, s2+1):
            for num3 in range(1, s3+1):
                all_.append(num1+num2+num3)
                
    total_case=len(all_)
    meet_mons=0
    for pos in monster:
        meet_mons+=all_.count(pos)
    
    return int(((total_case-meet_mons)/total_case)*1000)
