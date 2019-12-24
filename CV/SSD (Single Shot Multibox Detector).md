# SSD (Single Shot Multibox Detector)

> 참고문헌
>
> - [Understanding SSD MultiBox — Real-Time Object Detection In Deep Learning](https://towardsdatascience.com/understanding-ssd-multibox-real-time-object-detection-in-deep-learning-495ef744fab)
> - [[논문] SSD: Single Shot Multibox Detector 분석](https://taeu.github.io/paper/deeplearning-paper-ssd/)
> - [Liu, Wei et al. “SSD: Single Shot MultiBox Detector.” Lecture Notes in Computer Science (2016): 21–37. Crossref. Web.](https://arxiv.org/abs/1512.02325)



### 이름의 의미

- **Single Shot:** 네트워크 한번으로 object localization과 classification을 해낸다.
- **MultiBox:** Szegedy et al. 의 Bounding box regression 기술
- **Detector:** 발견된 객체를 분류하는 object detector



### Architecture

<p align="center">
    <img src="https://miro.medium.com/max/974/1*51joMGlhxvftTxGtA4lA7Q.png">
    <br/>SSD architecture
</p>

VGG-16 구조에서 fully connected layers 대신  보조 CNN이 추가된 형태로 다중 척도로 features를 뽑아내고 input size가 각 레이어를 지나면서 점차적으로 줄어듦

예를 들어 input image는 VGG-16 모델에서 conv4_3까지 적용하여 처리, 이대 300x300x3짜리 input image는 38x38x512로 바뀜

<p align="center">
    <img src="https://miro.medium.com/max/470/1*3-TqqkRQ4rWLOMX-gvkYwA.png">
	<br/>VGG architecture
</p>

### MultiBox

MultiBox loss는 **Confidence**와 **Location**의 weighted sum

- **Confidence**는 네트워크가 생성한 bounding box 안의 객체를 얼마나 신뢰할 수 있는지. <u>Categorical cross-entropy</u>로 계산
- **Location**은 네트워크가 생성한 bounding box가 실제 객체의 위치와 얼마나 떨어져 있는지. <u>L2-Norm</u>으로 계산

