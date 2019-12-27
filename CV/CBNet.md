# CBNet: A Novel Composite Backbone Network Architecture for Object Detection

paper: https://arxiv.org/abs/1909.03625v1

code: https://github.com/PKUbahuangliuhe/CBNet



## 1 Introduction

## 2 Related work

## 3 Proposed method

### 3.1 Architecture of CBNet

![architecture](./assets/cbnet/1.png)

- CBNet은 K개의 backbone으로 구성

- K=2이면 Dual-Backbone (DB), K=3이면 Triple-Backbone (TB)

- K번째 Backbone은 Leader Backbone이고 1~K-1번째 Backbone은 Assistant Backbones

- 각 Backbone은 L개의 stage로 구성 (일반적으로 L=5)

- 각 stage는 같은 사이즈의 feature map을 갖는 여러개의 convolutional layers로 구성

- L번째 stage는 비선형 변환 ![](https://latex.codecogs.com/gif.latex?%24F%5El%28%5Ccdot%29%24)

  - Backbone이 한개인 경우:

    ![](https://latex.codecogs.com/gif.latex?%24%24x%5El%20%3D%20F%5El%28x%5E%7Bl-1%7D%29%2C%5Cquad%20l%20%5Cgeq%202%24%24)

    ![](https://latex.codecogs.com/gif.latex?%5Cmathit%7Bx%7D%5El)은 ![](https://latex.codecogs.com/gif.latex?%5Cmathit%7Bl%7D)번째 stage output

  - Backbone이 여러개인 경우(CBNet architecture):

    ![](https://latex.codecogs.com/gif.latex?%24%24x%5El_k%20%3D%20F%5El_k%20%28%20x%5E%7Bl-1%7D_k%20&plus;%20g%28x%5El_%7Bk-1%7D%29%29%2C%5Cquad%20l%20%5Cgeq%202%24%24)

    ![](https://latex.codecogs.com/gif.latex?%5Cmathit%7Bg%7D%28%5Ccdot%29)은 ![](https://latex.codecogs.com/gif.latex?1%5Ctimes%201) convolutional layer와 batch normalization layer로 구성되어 채널 축소 및 upsampling 동작 수행 (Composite connection)

  - ![](https://latex.codecogs.com/gif.latex?%5Cmathit%7BB%7D_%7Bk-1%7D)의 ![](https://latex.codecogs.com/gif.latex?%5Cmathit%7Bl%7D)번째 stage output features는 ![](https://latex.codecogs.com/gif.latex?%5Cmathit%7Bg%7D%28%5Ccdot%29)에 의해 변환되어 ![](https://latex.codecogs.com/gif.latex?%5Cmathit%7BB%7D_k)의 ![](https://latex.codecogs.com/gif.latex?%5Cmathit%7Bl%7D)번째 stage input으로 쓰임

  - 이러한 composition을 Adjacent Higher-Level Composition (AHLC) 라고 부름

- For object detection task,

  - Lead Backbone ![](https://latex.codecogs.com/gif.latex?%5Cmathit%7Bx%7D%5El_K%28l%3D2%2C3%2C...%2CL%29) 이 RPN/detection head의 input으로 쓰임
  - Assistant Backbone의 각 stage output은 이웃한 Backbone으로 전달

- CBNet의 Assistant Backbone은 다양한 backbone architecture를 적용할 수 있음 (e.g. ResNeXt), 또한 미리 학습된 single backbone 모델로 초기화할 수 있음



### 3.2 Other possible composite styles

<p align="center">
    <img src="./assets/cbnet/2.png">
    <br/>(a) AHLC, (b) SLC, (c) ALLC, (d) DHLC
</p>

#### Same Level Composition (SLC)

- ![](https://latex.codecogs.com/gif.latex?x%5El_k%3DF%5El_k%28x%5E%7Bl-1%7D_k&plus;x%5E%7Bl-1%7D_%7Bk-1%7D%29%2C%5Cquad%20l%5Cgeq%202)

#### Adjacent Lower-Level Composition (ALLC)

- ![](https://latex.codecogs.com/gif.latex?x%5El_k%3DF%5El_k%28x%5E%7Bl-1%7D_k&plus;g%28x%5E%7Bl&plus;1%7D_%7Bk-1%7D%29%29%2C%5Cquad%20l%5Cgeq%202)

#### Dense Higher-Level Composition (DHLC)

- ![](https://latex.codecogs.com/gif.latex?x%5El_k%3DF%5El_k%28x%5E%7Bl-1%7D_k&plus;%5Csum_%7Bi%3Dl%7D%5ELg_i%28x%5Ei_%7Bk-1%7D%29%29%2C%5Cquad%20l%5Cgeq%202)

