Facial Keypoints Detection
================
Jinho Ahn
2019-04-11

<br>

### 데이터 읽어오기

``` r
# 데이터 경로
data.dir <- './data/'
train.file <- paste0(data.dir, 'training.csv')
test.file <- paste0(data.dir, 'test.csv')

# 데이터 읽기 (read.csv)
d.train <- read.csv(train.file, stringsAsFactors = F)
```

<br>

### 데이터 프레임 보기

``` r
# 데이터프레임 보기
str(d.train)  # 데이터 레코드 수: 7049개, 변수 수: 31개
```

    ## 'data.frame':    7049 obs. of  31 variables:
    ##  $ left_eye_center_x        : num  66 64.3 65.1 65.2 66.7 ...
    ##  $ left_eye_center_y        : num  39 35 34.9 37.3 39.6 ...
    ##  $ right_eye_center_x       : num  30.2 29.9 30.9 32 32.2 ...
    ##  $ right_eye_center_y       : num  36.4 33.4 34.9 37.3 38 ...
    ##  $ left_eye_inner_corner_x  : num  59.6 58.9 59.4 60 58.6 ...
    ##  $ left_eye_inner_corner_y  : num  39.6 35.3 36.3 39.1 39.6 ...
    ##  $ left_eye_outer_corner_x  : num  73.1 70.7 71 72.3 72.5 ...
    ##  $ left_eye_outer_corner_y  : num  40 36.2 36.3 38.4 39.9 ...
    ##  $ right_eye_inner_corner_x : num  36.4 36 37.7 37.6 37 ...
    ##  $ right_eye_inner_corner_y : num  37.4 34.4 36.3 38.8 39.1 ...
    ##  $ right_eye_outer_corner_x : num  23.5 24.5 25 25.3 22.5 ...
    ##  $ right_eye_outer_corner_y : num  37.4 33.1 36.6 38 38.3 ...
    ##  $ left_eyebrow_inner_end_x : num  57 54 55.7 56.4 57.2 ...
    ##  $ left_eyebrow_inner_end_y : num  29 28.3 27.6 30.9 30.7 ...
    ##  $ left_eyebrow_outer_end_x : num  80.2 78.6 78.9 77.9 77.8 ...
    ##  $ left_eyebrow_outer_end_y : num  32.2 30.4 32.7 31.7 31.7 ...
    ##  $ right_eyebrow_inner_end_x: num  40.2 42.7 42.2 41.7 38 ...
    ##  $ right_eyebrow_inner_end_y: num  29 26.1 28.1 31 30.9 ...
    ##  $ right_eyebrow_outer_end_x: num  16.4 16.9 16.8 20.5 15.9 ...
    ##  $ right_eyebrow_outer_end_y: num  29.6 27.1 32.1 29.9 30.7 ...
    ##  $ nose_tip_x               : num  44.4 48.2 47.6 51.9 43.3 ...
    ##  $ nose_tip_y               : num  57.1 55.7 53.5 54.2 64.9 ...
    ##  $ mouth_left_corner_x      : num  61.2 56.4 60.8 65.6 60.7 ...
    ##  $ mouth_left_corner_y      : num  80 76.4 73 72.7 77.5 ...
    ##  $ mouth_right_corner_x     : num  28.6 35.1 33.7 37.2 31.2 ...
    ##  $ mouth_right_corner_y     : num  77.4 76 72.7 74.2 77 ...
    ##  $ mouth_center_top_lip_x   : num  43.3 46.7 47.3 50.3 45 ...
    ##  $ mouth_center_top_lip_y   : num  72.9 70.3 70.2 70.1 73.7 ...
    ##  $ mouth_center_bottom_lip_x: num  43.1 45.5 47.3 51.6 44.2 ...
    ##  $ mouth_center_bottom_lip_y: num  84.5 85.5 78.7 78.3 86.9 ...
    ##  $ Image                    : chr  "238 236 237 238 240 240 239 241 241 243 240 239 231 212 190 173 148 122 104 92 79 73 74 73 73 74 81 74 60 64 75"| __truncated__ "219 215 204 196 204 211 212 200 180 168 178 196 194 196 203 209 199 192 197 201 207 215 199 190 182 180 183 190"| __truncated__ "144 142 159 180 188 188 184 180 167 132 84 59 54 57 62 61 55 54 56 50 60 78 85 86 88 89 90 90 88 89 91 94 95 98"| __truncated__ "193 192 193 194 194 194 193 192 168 111 50 12 1 1 1 1 1 1 1 1 1 1 6 16 19 17 13 13 16 22 25 31 34 27 15 19 16 1"| __truncated__ ...

<br>

### 데이터 보기

``` r
# 데이터 보기
im.train <- d.train$Image  # Image 변수 데이터를 im.train에 저장
d.train$Image <- NULL  # d.train의 Image 열 삭제
head(d.train)  # 5행의 데이터 레코드 확인
```

    ##   left_eye_center_x left_eye_center_y right_eye_center_x
    ## 1          66.03356          39.00227           30.22701
    ## 2          64.33294          34.97008           29.94928
    ## 3          65.05705          34.90964           30.90379
    ## 4          65.22574          37.26177           32.02310
    ## 5          66.72530          39.62126           32.24481
    ## 6          69.68075          39.96875           29.18355
    ##   right_eye_center_y left_eye_inner_corner_x left_eye_inner_corner_y
    ## 1           36.42168                59.58208                39.64742
    ## 2           33.44871                58.85617                35.27435
    ## 3           34.90964                59.41200                36.32097
    ## 4           37.26177                60.00334                39.12718
    ## 5           38.04203                58.56589                39.62126
    ## 6           37.56336                62.86430                40.16927
    ##   left_eye_outer_corner_x left_eye_outer_corner_y right_eye_inner_corner_x
    ## 1                73.13035                39.97000                 36.35657
    ## 2                70.72272                36.18717                 36.03472
    ## 3                70.98442                36.32097                 37.67811
    ## 4                72.31471                38.38097                 37.61864
    ## 5                72.51593                39.88447                 36.98238
    ## 6                76.89824                41.17189                 36.40105
    ##   right_eye_inner_corner_y right_eye_outer_corner_x
    ## 1                 37.38940                 23.45287
    ## 2                 34.36153                 24.47251
    ## 3                 36.32097                 24.97642
    ## 4                 38.75411                 25.30727
    ## 5                 39.09485                 22.50611
    ## 6                 39.36763                 21.76553
    ##   right_eye_outer_corner_y left_eyebrow_inner_end_x
    ## 1                 37.38940                 56.95326
    ## 2                 33.14444                 53.98740
    ## 3                 36.60322                 55.74253
    ## 4                 38.00790                 56.43381
    ## 5                 38.30524                 57.24957
    ## 6                 38.56553                 59.76628
    ##   left_eyebrow_inner_end_y left_eyebrow_outer_end_x
    ## 1                 29.03365                 80.22713
    ## 2                 28.27595                 78.63421
    ## 3                 27.57095                 78.88737
    ## 4                 30.92986                 77.91026
    ## 5                 30.67218                 77.76294
    ## 6                 31.65129                 83.31364
    ##   left_eyebrow_outer_end_y right_eyebrow_inner_end_x
    ## 1                 32.22814                  40.22761
    ## 2                 30.40592                  42.72885
    ## 3                 32.65162                  42.19389
    ## 4                 31.66573                  41.67151
    ## 5                 31.73725                  38.03544
    ## 6                 35.35806                  39.40800
    ##   right_eyebrow_inner_end_y right_eyebrow_outer_end_x
    ## 1                  29.00232                  16.35638
    ## 2                  26.14604                  16.86536
    ## 3                  28.13545                  16.79116
    ## 4                  31.04999                  20.45802
    ## 5                  30.93538                  15.92587
    ## 6                  30.54639                  14.94908
    ##   right_eyebrow_outer_end_y nose_tip_x nose_tip_y mouth_left_corner_x
    ## 1                  29.64747   44.42057   57.06680            61.19531
    ## 2                  27.05886   48.20630   55.66094            56.42145
    ## 3                  32.08712   47.55726   53.53895            60.82295
    ## 4                  29.90934   51.88508   54.16654            65.59889
    ## 5                  30.67218   43.29953   64.88952            60.67141
    ## 6                  32.15013   52.46849   58.80000            64.86908
    ##   mouth_left_corner_y mouth_right_corner_x mouth_right_corner_y
    ## 1            79.97017             28.61450             77.38899
    ## 2            76.35200             35.12238             76.04766
    ## 3            73.01432             33.72632             72.73200
    ## 4            72.70372             37.24550             74.19548
    ## 5            77.52324             31.19175             76.99730
    ## 6            82.47118             31.99043             81.66908
    ##   mouth_center_top_lip_x mouth_center_top_lip_y mouth_center_bottom_lip_x
    ## 1               43.31260               72.93546                  43.13071
    ## 2               46.68460               70.26655                  45.46791
    ## 3               47.27495               70.19179                  47.27495
    ## 4               50.30317               70.09169                  51.56118
    ## 5               44.96275               73.70739                  44.22714
    ## 6               49.30811               78.48763                  49.43237
    ##   mouth_center_bottom_lip_y
    ## 1                  84.48577
    ## 2                  85.48017
    ## 3                  78.65937
    ## 4                  78.26838
    ## 5                  86.87117
    ## 6                  93.89877

``` r
# 첫번째 이미지 데이터 보기
im.train[1]
```

<br>

### 첫번째 이미지 데이터 벡터 형태로 저장

``` r
as.integer(unlist(strsplit(im.train[1], " ")))
# strsplit: 문자열 나누기
# unlist: 문자열을 벡터에 담기
# as.integer: 정수형 벡터로 변환
```

<br>

### 병렬처리를 위한 doMC 라이브러리

``` r
# 위 작업을 반복하기 전에 멀티코어방식을 지원하도록
# doMC 라이브러리 이용
install.packages('doMC', repos = "http://R-Forge.R-project.org")
library(doMC)
registerDoMC()
```

<br>

### 전체 이미지 데이터 벡터 형태로 저장

``` r
im.train <- foreach(im = im.train, .combine = rbind) %dopar% {
  as.integer(unlist(strsplit(im, " ")))
}
```

``` r
str(im.train)
```

    ##  chr [1:7049] "238 236 237 238 240 240 239 241 241 243 240 239 231 212 190 173 148 122 104 92 79 73 74 73 73 74 81 74 60 64 75"| __truncated__ ...

<br>

### test 데이터에 대해서 같은 작업

``` r
d.test <- read.csv(test.file, stringsAsFactors = F)
im.test <- foreach(im = d.test$Image, .combine = rbind) %dopar% {
  as.integer(unlist(strsplit(im, " ")))
}
d.test$Image <- NULL
```

<br>

### 처리된 데이터 저장

``` r
save(d.train, im.train, d.test, im.test, file = 'data.Rd')
```
