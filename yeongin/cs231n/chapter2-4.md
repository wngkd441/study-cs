## chapter 2~4

### <2강 image classification>

#### - nearest neighbor classifier
모든 트레이닝 데이터를 메모리에 저장해두고 예측단계에서 테스트 이미지를 모든 트레이닝 이미지와 비교하여 가장 유사한 이미지의 레이블을 답으로 도출하는 방식   
트레이닝 이미지와 테스트 이미지를 비교할때는 distance를 이용한다.   
L1 distance : 두 이미지의 픽셀간의 차의 총 합   
L2 distance : 두 이미지의 픽셀간  의 제곱의 차의 총 합의 제곱근   

#### - k nearest neighbor 
트레이닝 이미지들 중에 테스트 이미지와 가장 가까운 k개의 이미지를 찾아서 k개의 이미지들의 레이블을 비교해보고 가장 많은 수의 레이블을 답으로 예측한다.   
일반적으로 k nearest neighbor가 nearest neighbor 보다 성능이 좋다.   

*하이퍼파라미터를 바꿔가면서 중간 중간 평가를 해볼때는 training data의 일부분인 validation data를 이용하고 test data는 모든 작업이 완료되고 마지막에 사용한다.

Q. "knn에서는 사람얼굴 사진 (1:원본, 2:shifted, 3:messed up, 4:darkened) 에서 2,3,4번 사진이 모두 원본과의 distance가 같기 때문에 모두 같은 이미지라고 판단하는 한계가 있다."에서   
Q1) 왜 2,3,4번이 모두 원본과의 distance가 같나?   
-> knn의 한계를 설명하기 위해 수업의 교수님이 일부러 그렇게 설계한 것   
Q2) 모두 같은 사람의 사진을 변형시킨 것이므로 같은 이미지로 판단하면 좋은 것 아닌가?   
-> 2,3,4번은 원본과 모두 다른 방식으로 차이를 보이지만 단순히 distance로 비교를 하게 되면 예제처럼 원본과의 distance가 우연히 같게 되었을 때 2,3,4번이 같은 이미지라고 판단하므로 좋지 않다.   
knn으로는 2,3,4를 구별할 수 없음

#### - linear classification   
->parametric approach   
x- > f(x,W) -> class score   
'''
f(x,W)=Wx (행렬곱)   
f(x,W,b)=Wx+b (b는 bias)
'''
*이미지의 feature를 추출하고 (ex. color histogram, edge) linear classfier에 적용   


### <3강 loss fn, optimization>

#### - loss fuction
loss function은 score에 대해 불만족하는 정도에 대해서 정량화하는 것   
*loss가 작아야 좋다.

#### - svm loss(hinge loss)
'''
 Li = Σmax(0,sj-syi+1) (j≠yi, syi : correct lable score, sj : incorrect lable score)
'''
->correct lable의 score가 incorrect lable의 score보다 1이상 크면 loss=0   
hinge loss의 한계는 loss가 0이 되도록 하는 W값이 여러개 일 수 있다.   
->regularization 필요   
'''
 L = ΣΣmax(0,sj-syi+1) + λR(W)
'''

Q1. regularization을 하는 것은 loss가 0이 되게 하는 W중 가장 작은 것을 택하기 위함 같은데 W가 왜 작아야 하나?   
Q2."regularization을 하게 되면 training data에 대한 정확도는 떨어지지만 결과적으로 test set에 대한 퍼포먼스는 더 좋아진다."는 말이 무슨 의미인가요?   
->(Q1&Q2) W가 작아지도록 학습을 한다는 것은 local noise가 학습에 큰 영향을 끼지치 않는다는 것을 의미하며 outlier(특이점)의 영향을 적게 받도록 하는 것이다.   
결과적으로 일반화에 적합한 특성을 갖게 만드는 것이라 볼 수 있다.   

#### - softmax classifier
'''
Li = -log(P(Y=k|X=xi))
'''

#### - svm vs softmax 
score가 살짝씩 변형되었을 때 svm은 Li = Σmax(0,sj-syi+1) 식의 +1에 의해 safety margin이 생겨 비교적 둔감하고 softmax는 민감하다.   
-> loss값이 변한다.   
일반적으로 softmax를 더 많이 쓴다.   

#### - optimization
optimization은 loss를 최소화 하는 파라미터 값을 찾는 과정

#### - 경사하강법
w를 살짝 변화시켰을 때 loss의 기울기를 보고 loss가 작아지는 쪽으로 w를 업데이트    
기울기를 구하는 방법   
1) numerical gradient : approximate, slow   
2) analytic gradient : exact, fast, error-prone   
->항상 analytic gradient를 사용하고 numerical gradient를 이용해서 검증하기   
weights 업데이트
'''
weights += -step_size*weights_grad
'''

Q. optimization의 방법 중 하나인 경사하강법에서 웨이트를 업데이트할 때, 왜 가중치의 변화에 따른 로스의 변화량을 가중치에 빼주나?   
(자료에서 보면 기울기를 구할때 (로스의 변화량)/(웨이트의 변화량)으로 구함)   
-> 가중치의 변화에 따른 로스의 변화가 급격할 수록 가중치의 변화를 크게 주는 것   
만약 로스의 변화의 +/-만 참고하고 가중치의 변화량 만큼만 가중치에서 빼주면 너무 시간이 오래걸리고 비효율적일 것이다.   


### <4강 backpropagation and NN part1>

*우리가 알고 싶은 것은 input에 대한 gradient   
즉, input이 마지막 단에 얼마나 영향을 미치는 가   
그런데 input이 마지막 단에 미치는 영향을 한번에 구할 수 없음   
-> chain rule을 이용하면  df/dx=(df/dq)*(dq/dx)   
여기서 dq/dx는 local gradient라고 하고, local gradient를 구하기 위해서는 forward pass   
df/dq는 global gradient라고 하고, global gradient를 구하기 위해서는 backward pass   
backpropagation(=backward pass)   
-> local gradient는 forward pass시에 구해서 메모리에 저장해 놓는다!!   

#### - pattens in backward flow
add gate: gradient distributor(전부 그대로 전달)   
max gate: gradient router(한쪽으로 전달, 나머지는 0)   
mul gate: gradient switcher(서로값을 바꿔서 곱함)   

#### - neural network
*nonparametric approach는 1class, 1classifier   
*parametric approach는 1class, multi-classifier   

#### - activation functions
ex. sigmoid, ReLU, maxout, ELU   

*weight를 가지는 것만 layer로 치기 때문에 input layer-hidden layer-output layer는 2-layer nn or 1 hidden layer nn라고 표현   
*모든 레이어가 연결된것 "fully connected"   

*뉴론이 많을 수록 정확도가 커진다.   
*일반화를 위해서는 뉴론의 개수를 늘리는 것이 아니라 regularization strength(λ)를 키워야함   
-> bigger = better (but regularize more strongly)    
