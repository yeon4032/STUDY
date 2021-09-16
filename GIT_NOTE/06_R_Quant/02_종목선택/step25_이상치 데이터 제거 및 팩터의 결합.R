# step25_이상치 데이터 제거 및 팩터의 결합

#데이터에서 이상치 데이터를 탐색
library(magrittr)
library(ggplot2)

KOR_value = read.csv('data/KOR_value.csv', row.names = 1,
                     stringsAsFactors = FALSE)

max(KOR_value$PBR, na.rm = TRUE)

# 시각화
KOR_value %>%
  ggplot(aes(x = PBR)) +
  geom_histogram(binwidth = 0.1)


#방법2: 트림(Trim): 이상치 데이터 삭제 (상하위 데이터 1% 삭제)
library(dplyr)

value_trim = KOR_value %>%
  select(PBR) %>%
  mutate(PBR = ifelse(percent_rank(PBR) > 0.99, NA, PBR), #하위 데이터 1% 삭제
         PBR = ifelse(percent_rank(PBR) < 0.01, NA, PBR)) #하위 데이터 1% 삭제

# 시각화
value_trim %>%
  ggplot(aes(x = PBR)) +
  geom_histogram(binwidth = 0.1)


# 방법 2:윈저라이징(Winsorizing): 이상치 데이터 대체
value_winsor = KOR_value %>%
  select(PBR) %>%
  mutate(PBR = ifelse(percent_rank(PBR) > 0.99,
                      quantile(., 0.99, na.rm = TRUE), PBR), # 대체
         PBR = ifelse(percent_rank(PBR) < 0.01,
                      quantile(., 0.01, na.rm = TRUE), PBR)) # 대체
#시각화
value_winsor %>%
  ggplot(aes(x = PBR)) +
  geom_histogram(binwidth = 0.1)



# 방법2: 팩터의 결합 방법

library(tidyr)

KOR_value %>%
  mutate_all(list(~min_rank(.))) %>%
  gather() %>%
  ggplot(aes(x = value)) +
  geom_histogram() +
  facet_wrap(. ~ key)  

#랭킹을 구하는 것의 가장 큰 장점은 극단치로 인한 효과가 사라진다는 점과 균등한 분포를 가진다는 점입니다.

##이러한 문제를 해결하는 가장 좋은 방법은 랭킹을 구한 후 이를 Z-Score로 정규화하는 것입니다.
KOR_value %>%
  mutate_all(list(~min_rank(.))) %>%
  mutate_all(list(~scale(.))) %>%
  gather() %>%
  ggplot(aes(x = value)) +
  geom_histogram() +
  facet_wrap(. ~ key)  









