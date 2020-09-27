## chapter 5~7

### <5강 training NN part1>

### Activation funtion
linear한 단순 합으로 구해진 입력을 non-linear하게 변경해주는 함수

#### 1. sigmoid
good   
- range [0,1] -> 입력에 대해 가중치의 영향력을 주기에 적합

bad   
- saturated neurons kill the gradients   
(= 입력이 10이상이거나 -10이하가 되면 기울기가 거의 0이 나옴)   
- sigmoid outputs are not zero-centered
-> slow convergence   
(+ not zero centered output에 의해 slow convergence가 생기는 이유:   
```f(Σwi*xi+b) --> df/dwi = xi```   
이때 시그모이드 함수의 결과는 항상 양수이므로 xi가 항상 양수이고 df/dwi도 항상 양수   
chain rule에 의해 ```dl/dwi = dl/df * df/fwi```   
df/dwi는 항상 양수이므로 dl/dwi의 부호는 dl/df에 의해 결정된다.   
따라서 dl/df가 양수면 모든 i에 대한 df/wi는 모두 양수가 되고, dl/df가 음수면 모든 i에 대한 df/dwi가 음수가 되어   
지그재그 모양으로 이동을 하게 되어 convergence가 느려진다.)   
- exp() compute expensive

#### 2. hyperbolic tangent - tanh(x)
good   
- range [-1,1]
- zero centered 

bad   
- still kill gradients when saturated

#### 3. ReLU
```
f(x) = max(0,x)
```
good
- not saturate (in + region)
- computationally efficient
- converges much faster

bad
- not zero centered output
- kill gradient (in - region)
-> ReLU에 모든 입력이 -가 들어오면 dead ReLU (never active)   
가중치 초기화를 잘못해주어서 dead ReLU존에서 시작하는 경우나, learning rate가 너무 큰 경우 dead ReLU존으로 빠질 수 있다.

#### 4. leaky ReLU
```
f(x) = max(0.01x,x)
```
x가 0보다 작은 구간에서 기울기가 0이 아님

good
- doos not saturate -> will not die
- computationally efficient
- converges much faster

#### 5. Parametric Rectifier (PReLU)
```
f(x) = max(αx, x)
```
기울기인 α 자체도 backpropagation을 통해서 학습한다.

#### 6. Exponential Linear Units (ELU)
```
f(x) = x (x > 0)
f(x) = α(exp(x)-1) (x <= 0)
```
good
- all benefits of ReLU
- does not die
- closer to zero mean outputs

bad
- computation requires exp()

#### 7. maxout"Neuron"
```
f(x) = max(w1*x + b1, w2*x + b2)
```
does not have the basic form of dot product -> nonlinearity

Generalizes ReLU and Leaky ReLU

bad
- doubles the number of parameters/neuron

#### activation function priority

1. use ReLU. (be careful with learning rates)
2. try out leaky ReLU or Maxout or ELU
3. try out tanh but don't expect
4. don't use sigmoid

### Data preprocessing
step 1. preprocess the data
- Mean Subtraction -> zero-centered data
```
X -= np.mean(X, axis = 0)
```
- Normalization
```
X /= np.std(X, axis = 0)
```
- PCA(주성분 분석) -> 데이터를 비상관화하여 차원을 줄임
- whitening -> 인접하는 픽셀간의 중복성을 줄일 수 있음

### weight initialization
1. random numbers
```
W = n*np.random.randn(D,H)
```
이때, n을 너무 작게 해주면 큰 네트워크에서는 각 뉴론의 출력이 점점 0에 수렴하는 문제점이 있다.

또한 n을 너무 크게 잡으면 거의 모든 뉴론들이 포화되어 기울기가 0이 된다.

2. xavier initialization
```
W = np.random.randn(fan_in, fan_out)/np.sqrt(fan_in)
```
tanh에 잘 적용되는 방법 but, ReLU에는 잘 적용되지 않음

3. Kaiming He
```
W = np.random.randn(fan_in, fan_out)/np.sqrt(fan_in/2)
```
ReLU에 최적인 방법

#### Batch normalization
- 학습 속도가 개선된다 (학습률을 높게 설정할 수 있기 때문)
- 가중치 초깃값 선택의 의존성이 적어진다 (학습을 할 때마다 출력값을 정규화하기 때문)
- 과적합(overfitting) 위험을 줄일 수 있다 (드롭아웃 같은 기법 대체 가능)
- Gradient Vanishing 문제 해결

#### Hyperparameter optimization
1. random search (grid search xxx)
2. in log space when appropriate


### <6강 trainging NN part2>

### optimization
(싸코 블로그 참고)

1. 확률적 경사하강법 Stochastic Gradient Descent

SGD는 손실함수의 기울기를 계산하여서 이 기울기 값에 학습률(Learning Rate)를 계산하여 이 결과 값으로 기존의 가중치 값을 갱신한다.

```
class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr
    
    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]
```
위에서 update 함수를 통해 모듈화되어 가중치를 갱신할 수 있다.

경사하강법의 단점

경사하강법은 무작정 기울어진 방향으로 이동하는 방식이기 때문에 탐색경로가 비효율적이어서 한참을 탐색하게 된다. 또한 SGD는 방향에 따라서 기울기 값이 달라지는 경우에 적합하지 않은데 최소값의 방향으로만 움직이기 때문에 본래의 최저점으로 기울기의 방향이 좀처럼 향하지 않게 되고 다른 방향을 가리키게 되어 비효율이게 되기도 한다.


#### 2. 모멘텀 Momentum
모멘텀은 '운동량'을 의미한다. 기울기에서 속도의 개념이 추가된 것으로 고등학교 물리 시간을 떠올려보면 자세히는 아니지만 지상의 마찰력 때문에 물체의 이동속도가 점점 감소한다고 배웠던 기억이 어렴풋이 기억이 난다. 속도가 크게 나올수록 기울기가 크게 업데이트 되어 확률적 경사하강법이 가지는 단점을 보완할 수 있다.

Momentum은 마찰력/공기저항 같은 것에 해당하며 기울기 업데이트 시 이 폭을 조절하는 역할을 한다. 이에 따라 속도 velocity가 변화한다.


```
class Momentum:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None
    
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)
        
        for key in params.keys():
            self.v[key] = self.momentum * self.v[key] 
```

#### 3. AdaGrad
신경망 학습에서의 학습률 learning rate의 값은 일종의 보폭으로 생각할 수 있는데 한 번 갱신하는 가중치의 값을 양을 결정한다. 학습률을 너무 작게하면 보폭이 너무 작아서 많은 걸음을 걸어야 하므로 학습 시간을 아주 길게 해야 한다. 반대로 너무 크게 하면 최적의 점을 계속 지나치게 된다.

학습률을 정하는 방법으로 학습률 감소learning rate decay가 있다고 한다. 학습을 진행하면서 점차 학습률을 줄여나가는 방법이다. 하지만 학습이 계속되면서 학습률이 0에 가까워져서 학습이 진행이 안되는 문제가 발생한다.

AdaGrad는 과거의 기울기 값을 제곱해서 계속 더하는 식으로 학습률을 낮추는데 학습이 진행될수록 제곱의 값으로 학습의 정도가 크게 떨어진다. 
이를 개선하기 위해서 RMSProp이 사용된다. RMSProp은 과거의 모든 기울기를 균일하게 더하지 않고 새로운 기울기의 정보만 반영하도록 해서 학습률이 크게 떨어져 0에 가까워지는 것을 방지하는 방법이다.


```
class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None
    
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)
                
        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
```

#### 4. Adam
앞에서 언급했던 Momentum과 AdaGrad를 섞은 기법이라고 보면 된다.

따라서 하이퍼파라미터도 그만큼 많다. 모멘텀에서 사용하는 계수와 학습률에 대한 계수가 사용된다.

학습률을 줄여나가고 속도를 계산하여 학습의 갱신강도를 적응적으로 조정해나가는 방법이다.

##### Adam을 가장 일반적으로 많이 사용한다.


### Dropout
##### 일부 노드들을 0으로 설정하여 연결이 끊기도록 하는 것
* regularize하는 목적으로 사용
* batch normalization을 사용하는 경우에는 잘 사용하지 않음
* test할 때는 모든 뉴론을 키고 사용
* test시에 결과값과 train시의 결과값의 기대값이 다름
```
ex)
p=0, input = (x,y), output = a

during test:
    a = w0*x + w1*y
    
during train:
    E(a) = 1/4 * (w0*0 + w1*0 + w0*0 + w1*y + w0*x + w1*0 + w0*x + w1*y)
         = 1/2 * (w0*x + w1*y)
         
=> E(a) = p*a
```
-> test시에 결과값에 p를 곱해주어 scaling한다.
* inverted dropout은 train시에 p를 나누어줌
* 일반적으로 inverted dropout을 더 많이 사용함

### <7강 Convolutional NN>

#### 1. conv layer
* Accepts a volume of size W1×H1×D1
* Requires four hyperparameters:
    * Number of filters K,
    * their spatial extent F,
    * the stride S,
    * the amount of zero padding P.
* Produces a volume of size W2×H2×D2 where:
    * W2=(W1−F+2P)/S+1
    * H2=(H1−F+2P)/S+1 (i.e. width and height are computed equally by symmetry)
    * D2=K
* With parameter sharing, it introduces F⋅F⋅D1 weights per filter, for a total of (F⋅F⋅D1)⋅K weights and K biases.
* In the output volume, the d-th depth slice (of size W2×H2) is the result of performing a valid convolution of the d-th filter over the input volume with a stride of S, and then offset by d-th bias.

#### 2. pooling layer
##### max pooling을 가장 많이 사용
* Accepts a volume of size W1×H1×D1
* Requires two hyperparameters:
    * their spatial extent F,
    * the stride S,
* Produces a volume of size W2×H2×D2 where:
    * W2=(W1−F)/S+1
    * H2=(H1−F)/S+1
    * D2=D1
* Introduces zero parameters since it computes a fixed function of the input
* For Pooling layers, it is not common to pad the input using zero-padding.

#### 3. Fully connected layer (FC layer)



