def solution(numbers):
    num=list(map(str, numbers))

    sort_num=sorted(num, key=lambda x:(x*4)[:4], reverse=True)

    #000인 경우, 0이니까 0으로 처리 하기 위해
    return str(int(''.join(sort_num)))