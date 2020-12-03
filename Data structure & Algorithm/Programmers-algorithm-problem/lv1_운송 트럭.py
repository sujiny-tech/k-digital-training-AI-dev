import collections

def solution(max_weight, specs, names):
    answer = 1 #기본적으로 트럭 1대
    sp = collections.defaultdict(int)
    # 딕셔너리로 상품이름을 키 값으로 해당 상품 무게 매핑시켜줌
    for s in specs:
        sp[s[0]] = int(s[1])

    mid = 0 #무게를 담을 변수

    while names:
        # 상품 스펙이름
        n = names.pop()

        # 최대 무게를 넘지 않으면
        if mid + sp[n] <= max_weight:
            mid += sp[n]

        # 최대 무게를 넘으면
        else:
            mid = sp[n]
            answer += 1

    return answer