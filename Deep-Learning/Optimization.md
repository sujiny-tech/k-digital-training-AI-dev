# 최적화 (Optimization)
> 깊은 신경망 최적화에 대한 효과적인 방안 🤔

+ 훈련 집합으로 학습 진행 후, 현장에서 발생하는 **새로운 샘플을 잘 예측**해야함
   + 다시말해 **일반화(generalization)** 능력이 좋아야 함 !
      + 훈련 집합 : 전체 데이터 대리자 역할
      + 검증 집합 : 테스트집합 대리자 역할
      + 손실함수(MSE, log-likelihood 등) : 주어진 과업의 학습 성능(=판단 기준) 대리자 역할
      
+ 기계학습의 최적화 어려운 이유
   + 대리자 관계
   + 매개탐색 공간에서 목적함수의 non-convex 성질, 고차원 특징 공간, 데이터의 희소성...
   + 긴 훈련 시간
   
## 목적함수
+ 평균제곱 오차(MSE)
   + <a href="https://www.codecogs.com/eqnedit.php?latex=e=\frac{1}{2}\left&space;\|&space;\mathbf{y}-\mathbf{o}&space;\right&space;\|_2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e=\frac{1}{2}\left&space;\|&space;\mathbf{y}-\mathbf{o}&space;\right&space;\|_2" title="e=\frac{1}{2}\left \| \mathbf{y}-\mathbf{o} \right \|_2" /></a>   
      
   + 한계   
      + MSE가 목적함수로서 부적절한 상황이 존재
      + 신경망 학습 과정에서 학습은 e를 줄이는 방향으로 가중치와 편향을 교정
         >  **큰 교정이 필요함에도 작은 경사도로 작게 갱신됨**

+ 교차 엔트로피 목적함수
   + 교차 엔트로피   
      > <a href="https://www.codecogs.com/eqnedit.php?latex=H(P,Q)=-\sum_x&space;P(x)\textup{log}_2&space;Q(x)=-\sum_{i=1,...,k}P(e_i)\textup{log}_2&space;Q(e_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(P,Q)=-\sum_x&space;P(x)\textup{log}_2&space;Q(x)=-\sum_{i=1,...,k}P(e_i)\textup{log}_2&space;Q(e_i)" title="H(P,Q)=-\sum_x P(x)\textup{log}_2 Q(x)=-\sum_{i=1,...,k}P(e_i)\textup{log}_2 Q(e_i)" /></a>   
   
   + 2-class에 대해 
      + <a href="https://www.codecogs.com/eqnedit.php?latex=e=-(y\textup{log}_2o&plus;\left&space;(&space;1-y&space;\right&space;)\textup{log}_2\left&space;(&space;1-o&space;\right&space;))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e=-(y\textup{log}_2o&plus;\left&space;(&space;1-y&space;\right&space;)\textup{log}_2\left&space;(&space;1-o&space;\right&space;))" title="e=-(y\textup{log}_2o+\left ( 1-y \right )\textup{log}_2\left ( 1-o \right ))" /></a>   
   
         > 이때, <a href="https://www.codecogs.com/eqnedit.php?latex=Q=\sigma(Z),&space;\textup{z=wx&plus;b}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q=\sigma(Z),&space;\textup{z=wx&plus;b}" title="Q=\sigma(Z), \textup{z=wx+b}" /></a>   
      
         + y=1, o=0.98인 경우(=예측 잘된 경우)   
            + e=0.0291로 낮은 값   
         
         + y=1, o=0.0001인 경우 (=예측 잘못된 경우 or 오분류된 경우)   
            + e=13.2877로 높은 값   
         
   + 미분을 해보면, MSE와 달리 에러만으로 경사도가 정해지고 있는 것을 알 수 있음.   
      > 에러에 비례해서 오류가 더 큰 쪽에 더 큰 벌점부과.
   
+ softmax함수 & 로그우도 목적함수 
   + softmax : **최댓값이 아닌 값을 억제하여 0에 가깝게 만든다** 는 의도 내포 ✨   
      > <a href="https://www.codecogs.com/eqnedit.php?latex=o_j=\frac{e^{s_i}}{\sum_{i=1,c}e^{s_i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?o_j=\frac{e^{s_i}}{\sum_{i=1,c}e^{s_i}}" title="o_j=\frac{e^{s_i}}{\sum_{i=1,c}e^{s_i}}" /></a>   
      
      
   + 음의 로그우도(negative log-likelihood) 목적함수
      > <a href="https://www.codecogs.com/eqnedit.php?latex=e=-\textup{log}_2&space;o_y" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e=-\textup{log}_2&space;o_y" title="e=-\textup{log}_2 o_y" /></a>   
      
      > 모든 출력 노드값을 사용하는 MSE나 교차 엔트로피와 달리 **하나의 노드(샘플의 정담에 해당하는 노드의 출력값)만 적용**   
   
   + softmax와 로그우도
      + 신경망에 의한 **샘플의 정답에 해당하는 노드만 보겠다는 로그우도**와 잘 어울림
      + 따라서 **둘을 결합하여 사용하는 경우**가 많음 ⭐
   
## 성능향상을 위한 요령
+ **주어진 데이터에 잘 들어맞을지는 실험을 통해** 신중히 확인해야함 ✨   

### 1. 데이터 전처리

<details>
<summary><b>자세히 👀</b></summary>   
<div markdown="1"> 

+ **scale** 문제
   + 예) 건강 데이터 (키(m), 몸무게(kg), 혈압 특징값을 가지는)
      + 1.885m와 1.525m는 33cm 차이/ 65.5kg와 45.0kg는 20.5 차이로 규모차이 발생(대략 100배 차이)
      + 몸무게에 연결된 가중치의 갱신이 훨씬 더 빠르게 진행됨. 즉, 키에 연결된 가중치의 갱신은 100여배 느리게 학습진행 → **느린 학습의 요인**   
   
+ **모든 특징이 양수인 경우** 의 문제
   + 특징이 모두 양수일 때, 가중치가 뭉치로 갱신 (output gradient에 의해 결정되므로)
      > 최저점을 찾아가는 경로가 갈팡질팡해서 느린 수렴   
      
   <details> 
   <summary><b>scale과 양수 문제 해결 - 정규화 ✨</b></summary>   
   <div markdown="1">   
   
   + **정규화(normalization)**   
      + 특징별 독립적으로 적용
      + **표준화 변환** (일반적으로 표준화 변환 사용), 최대 최소 변환
 
   + **명목 변수(norminal value)**을 **one-hot 코드** 로 변환   
      + 명목 변수 : 객체간 서로 구분하기 위한 변수
         + 거리 개념이 x
         + 원핫 코드는 값의 개수만큼 비트 부여
      
            > 성별은 남여(2비트), 체질은 태양인, 태음인, 소양인, 소음인(4비트)   

   </div>
   </details>

</div>
</details>

### 2. 가중치 초기화
            
<details>
<summary><b>자세히 👀</b></summary>   
<div markdown="1">             

+ **대칭적 가중치** 문제   
   + 대칭적 가중치에서 두 노드가 똑같은 값을 갱신하는 중복 발생 💥   
   
   
   <details>
   <summary><b>대칭적 가중치 문제 해결 - 난수 초기화 ✨</b></summary>   
   <div markdown="1">   
   
   + **난수로 초기화** 함으로써 대칭 파괴 ✨   
      + 가우시안 or 균일 분포에서 난수 추출 (두 분포 성능차이 거의 x)
      + 난수 범위 매주 중요
      + 편향으로 보통 0으로 초기화    
      
         > 사례 1) AlexNet : 평균 0, 표준편차 0.01인 가우시안에서 난수 생성   
      
         > 사례 2) ResNet : 평균 0, 표준 편차 <a href="https://www.codecogs.com/eqnedit.php?latex=\sqrt{2/n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sqrt{2/n}" title="\sqrt{2/n}" /></a> 인 난수 생성, 편향 0으로 세팅 (n : 입력노드 개수)
       
   + 초기화가 **너무 작으면** 모든 활성 값 0으로 경사도도 역시 0 (학습 x), **너무 크면** 활성값 포화로 경사도는 0 (학습 x)
      > 초기화가 적당하면, 모든 층에서 활성 값의 분포가 좋음 (적절한 학습 수행)
      
   + 요즘에는 배치단위로 각각 층의 출력값의 분포를 정규분포 형태로 만드는 **배치 정규화 사용** 
      > 가중치 초기화에 대한 의존성이 낮아짐 
      > [가중치 초기화 실습 예제 ✨](https://www.deeplearning.ai/ai-notes/initialization/)   
      
      
   </div>
   </details>

</div>
</details>

### 3. 탄력(가속도, 관성)

<details>
<summary><b>자세히 👀</b></summary>   
<div markdown="1"> 

+ **경사도의 잡음** 현상   
   + 훈련 집합을 이용해서 파라미터의 경사도를 추정하기 때문에 잡음 가능성 ↑   
   + **탄력(가속도, 관성)** 은 경사도에 부드러움을 가하여 잡음 효과 줄임
      + **과거에 이동했던 방식을 기억** 하기 때문에, 기존의 방향을 유지
      + **지역 최저, 안장점에 빠지는 문제 해소 (수렴 속도 향상)**  
      
   + 딥러닝과 같이 매개 탐색 공간이 많으면 (local minima보다) **saddle points** 문제가 많이 발생 - **모멘텀** 을 이용해서 효율적으로 해결될 수 있음 ✨

   + **네스테로프 가속 경사도(nesterov accelerated gradient)** 관성
      + 현재 위치가 아니라 모멘텀 방향으로 미리 앞서서 다음 이동할 곳을 예견한 후, 예견한 곳의 경사도를 사용(멈춤 용이)   
      
      + 실제 구현에서 앞선 경사도를 계산하는 대신 모멘텀 방식을 두번 적용해서 네스테로프의 근사값을 구한다고 한다.

</div>
</details>


### 4. 적응적 학습률

<details>
<summary><b>자세히 👀</b></summary>   
<div markdown="1"> 

+ **학습률(learning rate)** 중요성 ✨
   + 너무 크면 overshooting에 따른 진자 현상 발생, 너무 작으면 수렴이 느림 → 적절한 lr 필요
   
+ **적응적 학습률** (adaptive learning rates, per-parameter learning rates)
   + 기존 경사도 갱신은 모든 매개변수에 같은 크기의 lr 사용했음
   + 적응적 학습률은 **매개변수마다** 자신의 상황에 따라 **학습률을 조절**해서 사용
      + 예) 학습률 담금질(stimulated annealing, SA)
         > 이전과 현재 경사도가 부호가 같은 파라미터는 값을 키우고, 다른 파라미터는 값을 줄이는 전략
   
+ AdaGrad(Adaptive gradient)
   + 이전 경사도를 누적한 벡터를 활용
      + 그 값이 크면 갱신값은 작으므로 조금 이동
      + 반대로 작으면, 갱신값은 커서 많이 이동
      + 따라서 상황에 따라 보폭을 정해서 적응적으로 학습 진행

+ RMSProp
   + AdaGrad - 현재값이 중요한데 과거값이 발목을 잡을수 있음 (오래된 경사도와 최근 경사도는 같은 비중의 역할)
      > 이전 경사도를 누적한 벡터값이 점점 커져서 수렴방해할 가능성있음      
      
   + **가중 이동 평균**(weight moving average) 기법 적용   
      > 경사도 누적 벡터값에서 과거와 최근의 비중을 둠(alpha) - 보통 alpha : 0.9, 0.99, 0.999 사용   
      
+ Adam 
   + Adam = RMSProp + Momentum(관성)
   + 하이퍼파라미터로 lr, alpha1,2(=beta)
      + alpha 1,2 : momentum 계수와 adaptive 계수   
      
   + 보통 adam 많이 사용하는 편 
      > SGD에 lr를 조금씩 변경하면서 탐색하는 것이 성능적인 측면에서 이점 (경험이 중요)
</div>
</details>

### 5. 활성함수

### 6. 배치 정규화
