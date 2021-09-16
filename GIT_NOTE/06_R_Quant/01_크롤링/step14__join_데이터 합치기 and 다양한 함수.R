#step14__join_데이터 합치기 and 다양한 함수

library(dplyr)

data_market = left_join(KOR_ticker, KOR_sector,
                        by = c('종목코드' = 'CMP_CD',
                               '종목명' = 'CMP_KOR'))

head(data_market)


#glimpse(): 데이터 구조 확인하기
glimpse(data_market)

#rename(): 열 이름 바꾸기
#rename() 함수는 열 이름을 바꾸는 함수로서, rename(tbl, new_name = old_name) 형태로 입력합니다.
head(names(data_market), 15)
data_market = data_market %>%
  rename(`배당수익률(%)` = `배당수익률`)

head(names(data_market), 15)

# distinct(): 고유한 값 확인
data_market %>%
  distinct(SEC_NM_KOR) %>% c() 


##select(): 원하는 열만 선택

#종목명만 뽑기
data_market %>%
  select(`종목명`) %>% head()

#종목명, `PBR`, `SEC_NM_KOR` 뽑기
data_market %>%
  select(`종목명`, `PBR`, `SEC_NM_KOR`) %>% head()

#'시'로 시작하는 뽑기
data_market %>%
  select(starts_with('시')) %>% head()

# 끝이 R 인거 가지고 오기
data_market %>%
  select(ends_with('R')) %>% head()

# '가'라는 단어가 들어간 거 뽑기
data_market %>%
  select(contains('가')) %>% head()



# mutate(): 열 생성 및 데이터 변형
#mutate() 함수는 원하는 형태로 열을 생성하거나 변형하는 함수입니다.

#as.numeric() 함수를 통해 숫자형으로 변경한 후 PBR을 PER로 나눈 값을 ROE 열에 생성합니다. 
#그 후 round() 함수를 통해 ROE 값을 반올림하며,
#ifelse() 함수를 통해 시가총액의 중앙값보다 큰 기업은 big, 아닐 경우 small임을 size 열에 저장합니다.

data_market = data_market %>%
  mutate(`PBR` = as.numeric(PBR),
         `PER` = as.numeric(PER),
         `ROE` = PBR / PER,
         `ROE` = round(ROE, 4),
         `size` = ifelse(`시가총액` >=
                           median(`시가총액`, na.rm = TRUE),
                         'big', 'small')
  )

data_market %>%
  select(`종목명`, `ROE`, `size`) %>% head()

##filter(): 조건을 충족하는 행 선택

# PBR이 일보다 작은 것만 가지고 와라
data_market %>%
  select(`종목명`, `PBR`) %>%
  filter(`PBR` < 1) %>% head()

# PBR < 1 & PER < 20 & ROE > 0.1  것 만 가지고 와라
data_market %>%
  select(`종목명`, `PBR`, `PER`, `ROE`) %>%
  filter(PBR < 1 & PER < 20 & ROE > 0.1 ) %>% head()

##summarize(): 요약 통곗값 계산
#summarize() 혹은 summarise() 함수는 원하는 요약 통곗값을 계산합니다.

#PBR_max는 PBR 열에서 최댓값을, PBR_min은 최솟값을 계산해줍니다.
data_market %>%
  summarize(PBR_max = max(PBR, na.rm = TRUE),
            PBR_min = min(PBR, na.rm = TRUE))

## arrange(): 데이터 정렬
data_market %>%
  select(PBR) %>%
  arrange(PBR) %>%
  head(5)


# 내림차순
data_market %>%
  select(ROE) %>%
  arrange(desc(ROE)) %>%
  head(5)


##row_number(): 순위 계산

# PBR 순으로 정렬
data_market %>%
  mutate(PBR_rank = row_number(PBR)) %>%
  select(`종목명`, PBR, PBR_rank) %>%
  arrange(PBR) %>%
  head(5)

#ROE 순으로 정렬
data_market %>%
  mutate(ROE_rank = row_number(desc(ROE))) %>%
  select(`종목명`, ROE, ROE_rank) %>%
  arrange(desc(ROE)) %>%
  head(5)

##ntile(): 분위수 계산
#ntile() 함수는 분위수를 계산해주며, n 인자를 통해 몇 분위로 나눌지 선택할 수 있습니다.
data_market %>%
  mutate(PBR_tile = ntile(PBR, n = 5)) %>%
  select(PBR, PBR_tile) %>%
  head()

##group_by(): 그룹별로 데이터를 묶기
#group_by() 함수는 선택한 열 중 동일한 데이터를 기준으로 데이터를 묶어줍니다. 

# SEC_NM_KOR(색터(산업)) 기준으로 데이터를 묶었으며
data_market %>%
  group_by(`SEC_NM_KOR`) %>%
  summarize(n())

#묶은 후 summarize()를 통해 각 섹터에 속하는 종목의 PBR 중앙값을 구한 후 정렬했습니다.
data_market %>%
  group_by(`시장구분`, `SEC_NM_KOR`) %>%
  summarize(PBR_median = median(PBR, na.rm = TRUE)) %>%
  arrange(PBR_median)



