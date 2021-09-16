#step15_ggplot() 기초

library(ggplot2)

data(diamonds)
head(diamonds)

##aes() 함수를 통해 데이터를 매핑해주며 x축에 carat을, y축에 price를 지정해줍니다.
ggplot(data = diamonds, aes(x = carat, y = price))

#geom_point() 함수를 입력하여 산점도가 표현되었습니다
ggplot(data = diamonds, aes(x = carat, y = price)) +
  geom_point()


library(magrittr)

##geom_point() 내부에서 aes()를 통해 점의 색깔을 매핑해줄 수 있습니다.
#color = cut을 지정하여 cut에 따라 점의 색깔이 다르게 표현하였습니다
diamonds %>%
  ggplot(aes(x = carat, y = price)) +
  geom_point(aes(color = cut))


##Facets
#Facets은 여러 집합을 하나의 그림에 표현하기 보다 하위 집합으로 나누어 시각화하는 요소입니다.
#세로 
diamonds %>%
  ggplot(aes(x = carat, y = price)) +
  geom_point() +
  facet_grid(. ~ cut) #facet_grid() 혹은 facet_wrap() 함수를 통해 그림을 분할할 수 있습니다. 

#가로
diamonds %>%
  ggplot(aes(x = carat, y = price)) +
  geom_point() +
  facet_grid(cut ~ .)

##Statistics
#stat_summary_*() 함수를 사용하여 통계값을 표현하였습니다.
#평균값
diamonds %>%
  ggplot(aes(x = cut, y = carat)) +
  stat_summary_bin(fun.y = 'mean', geom = 'bar') 

##Coordinates

#coord_cartesian() 함수를 통해 x축과 y축 범위를 지정해 줄 수 있습니다
diamonds %>%
  ggplot(aes(x = carat, y = price)) +
  geom_point(aes(color = cut)) +
  coord_cartesian(xlim = c(0, 3), ylim = c(0, 20000))

##Theme
#Theme은 그림의 제목, 축 제목, 축 단위, 범례, 디자인 등 그림을 꾸며주는 역할을 담당합니다.

diamonds %>%
  ggplot(aes(x = carat, y = price)) +
  geom_point(aes(color = cut)) +
  #꾸미기
  theme_bw() +
  labs(title = 'Relation between Carat & Price',
       x = 'Carat', y = 'Price') +
  theme(legend.position = 'bottom',
        panel.grid.major.x = element_blank(),
        panel.grid.minor.x = element_blank(),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank()
  ) +
  scale_y_continuous(
    labels = function(x) {
      paste0('$', 
             format(x, big.mark = ','))
    })










