#step16_ 종목정보 시각화

library(ggplot2)

#x축은 ROE 열을 사용하고, y축은 PBR 열
#geom_point() 함수를 통해 산점도 그래프를 그려줍니다
ggplot(data_market, aes(x = ROE, y = PBR)) +
  geom_point()

#단치 효과를 제거하기 위해 coord_cartesian() 함수 내에 xlim과 ylim, 즉 x축과 y축의 범위를 직접 지정해줍니다.
ggplot(data_market, aes(x = ROE, y = PBR)) +
  geom_point() +
  coord_cartesian(xlim = c(0, 0.30), ylim = c(0, 3))


#ggplot() 함수 내부 aes 인자에 color와 shape를 지정해주면,
#코스피와 코스닥 종목들에 해당하는 데이터의 색과 점 모양을 다르게 표시할 수 있습니다
ggplot(data_market, aes(x = ROE, y = PBR,
                        color = `시장구분`,
                        shape = `시장구분`)) +

#geom_smooth() 함수를 통해 평활선을 추가할 수도 있으며,
#lm(linear model)을 지정할 경우 선형회귀선을 그려주게 됩니다
  geom_point() +
  geom_smooth(method = 'lm') +
  coord_cartesian(xlim = c(0, 0.30), ylim = c(0, 3))


##geom_histogram(): 히스토그램 나타내기

ggplot(data_market, aes(x = PBR)) +
  geom_histogram(binwidth = 0.1) +  # binwidth 인자를 통해 막대의 너비를 선택해줄 수 있습니다
  coord_cartesian(xlim = c(0, 10))

# PBR 히스토그램을 좀 더 자세하게 나타내보겠습니다
ggplot(data_market, aes(x = PBR)) +
  geom_histogram(aes(y = ..density..),
                 binwidth = 0.1,
                 color = 'sky blue', fill = 'sky blue') + 
  coord_cartesian(xlim = c(0, 10)) +
  geom_density(color = 'red') +
  geom_vline(aes(xintercept = median(PBR, na.rm = TRUE)),
             color = 'blue') +
  geom_text(aes(label = median(PBR, na.rm = TRUE),
                x = median(PBR, na.rm = TRUE), y = 0.05),
            col = 'black', size = 6, hjust = -0.5)
            
#위의 histogram 설명
#geom_histogram() 함수 내에 aes(y = ..density..)를 추가해 밀도함수로 바꿉니다.
#geom_density() 함수를 추가해 밀도곡선을 그려줍니다.
#geom_vline() 함수는 세로선을 그려주며, xintercept 즉 x축으로 PBR의 중앙값을 선택합니다.
#geom_text() 함수는 그림 내에 글자를 표현해주며, label 인자에 원하는 글자를 입력해준 후
#글자가 표현될 x축, y축, 색상, 사이즈 등을 선택할 수 있습니다.
          
            
##geom_boxplot(): 박스 플롯 나타내기            
#이상치를 확인하기 좋은 그림

ggplot(data_market, aes(x = SEC_NM_KOR, y = PBR)) +
  geom_boxplot() +
  coord_flip()
            
#x축 데이터로는 섹터 정보, y축 데이터로는 PBR을 선택합니다.
#geom_boxplot()을 통해 박스 플롯을 그려줍니다.
#coord_flip() 함수는 x축과 y축을 뒤집어 표현해주며 x축에 PBR,
#y축에 섹터 정보가 나타나게 됩니다.            
            
##dplyr과 ggplot을 연결하여 사용하기

data_market %>%
  filter(!is.na(SEC_NM_KOR)) %>%
  group_by(SEC_NM_KOR) %>%
  summarize(ROE_sector = median(ROE, na.rm = TRUE),
            PBR_sector = median(PBR, na.rm = TRUE)) %>%
  ggplot(aes(x = ROE_sector, y = PBR_sector,
             color = SEC_NM_KOR, label = SEC_NM_KOR)) +
  geom_point() +
  geom_text(color = 'black', size = 3, vjust = 1.3) +
  theme(legend.position = 'bottom',
        legend.title = element_blank())

#데이터 분석의 단계로 filter()를 통해 섹터가 NA가 아닌 종목을 선택합니다.
#group_by()를 통해 섹터별 그룹을 묶습니다.
#summarize()를 통해 ROE와 PBR의 중앙값을 계산해줍니다. 해당 과정을 거치면 다음의 결과가 계산됩니다.
#축과 y축을 설정한 후 색상과 라벨을 섹터로 지정해주면 각 섹터별로 색상이 다른 산점도가 그려집니다.
#geom_text() 함수를 통해 앞에서 라벨로 지정한 섹터 정보들을 출력해줍니다.
#theme() 함수를 통해 다양한 테마를 지정합니다. legend.position 인자로 범례를 하단에 배치했으며, legend.title 인자로 범례의 제목을 삭제했습니다.


##geom_bar(): 막대 그래프 나타내기

data_market %>%
  group_by(SEC_NM_KOR) %>%
  summarize(n = n()) %>%
  ggplot(aes(x = SEC_NM_KOR, y = n)) +
  geom_bar(stat = 'identity') +
  theme_classic()        
            
#group_by()를 통해 섹터별 그룹을 묶어줍니다.
#summarize() 함수 내부에 n()을 통해 각 그룹별 데이터 개수를 구합니다.
#ggplot() 함수에서 x축에는 SEC_NM_KOR, y축에는 n을 지정해줍니다.
#geom_bar()를 통해 막대 그래프를 그려줍니다. y축에 해당하는 n 데이터를 그대로 사용하기 위해서는 stat 인자를 identity로 지정해주어야 합니다. theme_*() 함수를 통해 배경 테마를 바꿀 수도 있습니다.        
            
# 막대그래프 모양 변경
data_market %>%
  filter(!is.na(SEC_NM_KOR)) %>%
  group_by(SEC_NM_KOR) %>%
  summarize(n = n()) %>%
  ggplot(aes(x = reorder(SEC_NM_KOR, n), y = n, label = n)) +
  geom_bar(stat = 'identity') +
  geom_text(color = 'black', size = 4, hjust = -0.3) +
  xlab(NULL) +
  ylab(NULL) +
  coord_flip() +
  scale_y_continuous(expand = c(0, 0, 0.1, 0)) + 
  theme_classic()

#filter() 함수를 통해 NA 종목은 삭제해준 후 섹터별 종목 개수를 구해줍니다.
#ggplot()의 x축에 reorder() 함수를 적용해 SEC_NM_KOR 변수를 n 순서대로 정렬해줍니다.
#geom_bar()를 통해 막대 그래프를 그려준 후 geom_text()를 통해 라벨에 해당하는 종목 개수를 출력합니다.
#xlab()과 ylab()에 NULL을 입력해 라벨을 삭제합니다.
#coord_flip() 함수를 통해 x축과 y축을 뒤집어줍니다.
#scale_y_continuous() 함수를 통해 그림의 간격을 약간 넓혀줍니다.
#theme_classic()으로 테마를 변경해줍니다.









































