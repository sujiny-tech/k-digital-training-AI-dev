#올바른 순서인지 체크
def check(skill, skill_tree):
    ch=False #fasle로 초기화
    skill=list(skill) #비교할때 동일하게 맞춰주려고
    index=[v for i, v in enumberate(skill_tree) if v in skill] #선행스킬(skill)에 해당하는 skill만 순서대로 뽑음
    return index==skill[:len(index)] #올바른 순서라면 앞에서부터 index개수까지 들었어야함
    
def solution(skill, skill_trees):
    ans=0
    for skill_tree in skill_trees:
        #주어진 skill_trees에 대해 check했을때 true면 카운트
        if check(skill, skill_tree):
            ans+=1
            
    return ans
