# SSD (Single Shot Multibox Detector)

> 참고문헌
>
> - [Understanding SSD MultiBox — Real-Time Object Detection In Deep Learning](https://towardsdatascience.com/understanding-ssd-multibox-real-time-object-detection-in-deep-learning-495ef744fab)
> - [Liu, Wei et al. “SSD: Single Shot MultiBox Detector.” Lecture Notes in Computer Science (2016): 21–37. Crossref. Web.](https://arxiv.org/abs/1512.02325)



### 이름의 의미

- **Single Shot:** 네트워크 한번으로 object localization과 classification을 해낸다.
- **MultiBox:** Szegedy et al. 의 Bounding box regression 기술
- **Detector:** 발견된 객체를 분류하는 object detector



### 구조

<center>
<figure>
    <img src="https://miro.medium.com/max/974/1*51joMGlhxvftTxGtA4lA7Q.png" alt="" />
    <figcaption>SSD architecture</figcaption>
</figure>
</center>

VGG-16 구조에서 fully connected layers 대신  보조 CNN이 추가된 형태로 다중 척도로 features를 뽑아내고 input size가 각 레이어를 지나면서 점차적으로 줄어듦

<center>
<figure>
    <img src="https://miro.medium.com/max/470/1*3-TqqkRQ4rWLOMX-gvkYwA.png" alt="" />
    <figcaption>VGG architecture</figcaption>
</figure>
</center>



