## chapter 5~7

### <5강 training NN part1>

#### - activation funtion
linear한 단순 합으로 구해진 입력을 non-linear하게 변경해주는 함수

#### 1. sigmoid
good
range [0,1] -> 입력에 대해 가중치의 영향력을 주기에 적합
bad
1. saturated neurons kill the gradients
(= 입력이 10이상이거나 -10이하가 되면 기울기가 거의 0이 나옴)
2. sigmoid outputs are not zero-centered
-> slow convergence
(+ not zero centered output에 의해 slow convergence가 생기는 이유:
```f(Σwi*xi+b) --> df/dwi = xi```
이때 시그모이드 함수의 결과는 항상 양수이므로 xi가 항상 양수이고 df/dwi도 항상 양수
chain rule에 의해
```dl/dwi = dl/df * df/fwi```
df/dwi는 항상 양수이므로 dl/dwi의 부호는 dl/df에 의해 결정된다.
따라서 dl/df가 양수면 모든 i에 대한 df/wi는 모두 양수가 되고, dl/df가 음수면 모든 i에 대한 df/dwi가 음수가 되어
지그재그 모양으로 이동을 하게 되어 convergence가 느려진다.)
3. exp() compute expensive

#### 2. hyperbolic tangent - tanh(x)
good
- range [-1,1]
- zero centered 
bad
- still kill gradients when saturated

#### 3. ReLU
```f(x) = max(0,x)```
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


