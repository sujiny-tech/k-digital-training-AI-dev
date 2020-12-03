def solution(brown, red):
    answer = []
    # red = (x-2)*(y-2)
    # brown = xy-red = 2x+2y-4 = (x+y-2)*2

    # x:가로, y:세로
    x = 3  # 3부터 시작 (최소 red가 1칸일 때)
    while True:
        # red=(x-2)(y-2)
        y = (red / (x - 2)) + 2  # red/(x-2)==(y-2)이니?
        if y == int(y):
            y = int(y)
            if (x + y - 2) * 2 == brown:
                if x < y:
                    x, y = y, x
                return [x, y]
        x += 1
    return answer