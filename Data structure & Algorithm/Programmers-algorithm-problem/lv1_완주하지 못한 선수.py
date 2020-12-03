import collections

def solution(participant, completion):
    cnt=collections.defaultdict(int) #default로 int형 0채워주는 딕셔너리
    completion.append("") #completion에 한명 비니까
    
    for p, c in zip(participant, completion):
        cnt[p]+=1 #참여자 카운트 1
        if c!="":
            cnt[c]-=1 #완주한 선수들 빼주기
            
    #딕셔너리 값이 0이 아니면 key(참가자이름) 반환
    for k, v in cnt.items():
        if v!=0:
            return k
    return ''
