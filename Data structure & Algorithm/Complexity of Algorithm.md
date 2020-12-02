# 알고리즘 복잡도(Complexity of Algorithm)
+ 시간 복잡도(Time Complexity)
 > 문제의 크기 - 걸리는 시간 간의 관계
   + 평균 시간 복잡도(Average Time Complexity)
    > 랜덤되는 입력에 따라 소요되는 시간의 평균
   + 최악 시간 복잡도(Worst-case Time Complexity)
    > 가장 최악의 경우인 입력(긴 시간을 요구하는 입력)에 대해 소요되는 시간
    
+ 공간 복잡도(Space Complexity)
 > 문제의 크기 - 필요한 메모리 공간 간의 관계

+ [Big-O Notation](https://ko.wikipedia.org/wiki/%EC%A0%90%EA%B7%BC_%ED%91%9C%EA%B8%B0%EB%B2%95)
   + 점근 표기법(asymptotic notation)의 하나로써 알고리즘의 복잡도를 표현할 때 많이 쓰임
   + 어떤 함수의 증가 양상을 파악할 수 있도록 (다른 알고리즘와 비교를 위해)
   + 계수는 생략 가능
    > ex) O(logn), O(n), O(n^2), O(2^n)...
    
+ 선형 시간 O(n)
 > ex) 크기가 n인 배열에서 최댓값을 찾는 선형 탐색 알고리즘
    + 최댓값을 따지려면 맨끝의 수까지 비교해야함 -> O(n)
    
+ 로그 시간 O(logn)
 > ex) 크기가 n인 정렬된 배열에서 특정 값 찾는 이진 탐색 알고리즘
 
+ 이차 시간 알고리즘 O(n^2)
 > ex) [삽입 정렬(insertion sort)](https://ko.wikipedia.org/wiki/%EC%82%BD%EC%9E%85_%EC%A0%95%EB%A0%AC)
    + 원소를 하나씩 꺼내서, 어느 부분에 삽입할지 
    + 하나의 원소를 집어넣을때 n번 횟수비교를 하는데, 이를 원소의 개수(n)만큼 반복
    
+ 상대적으로 낮은 복잡도를 갖는 정렬 알고리즘
   + 병합 정렬(merge sort) : O(nlogn)
      + 정렬할 데이터를 반씩 나눠 정렬시킴 O(logn) -> 정렬된 데이터를 두 묶음씩 합침 O(n)
