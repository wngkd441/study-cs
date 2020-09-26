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









