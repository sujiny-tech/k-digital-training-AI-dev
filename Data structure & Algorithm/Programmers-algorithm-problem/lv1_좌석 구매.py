def solution(seat):
    #처음에 그냥 list(set(seat))으로 처리했는데, 리스트의 경우 해시불가능이여서 x
    #사전의 키는 변경 불가이므로, 가변인 리스트는 key로 사용불가 -> unhashable type : 'list'
    #set에 들어있는 값들은 해시 가능해야함
    #문자열, 숫자, 튜플인 경우에만 set에 넣으면 중복제거가 가능
    seat=list(set(map(tuple, seat)))
    return len(seat)
    
