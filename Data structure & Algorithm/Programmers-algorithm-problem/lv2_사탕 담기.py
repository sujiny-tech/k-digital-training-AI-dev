import itertools

def solution(m, weights):
    answer = 0
    #3<=len(weights)<=15
    for i in range(1, len(weights)):
        #모든 조합을 따져서 더해준 값을 담기
        all_=list(map(sum, itertools.combinations(weights,i)))
        answer+=all_.count(m) #해당 무게의 갯수 카운트 업데이트
    return answer