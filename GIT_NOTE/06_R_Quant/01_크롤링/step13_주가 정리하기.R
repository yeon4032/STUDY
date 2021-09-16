# step13_주가 정리하기
library(stringr)
library(xts)
library(magrittr)

# csv 파일 부르기
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1)
#csv 파일을 불러온 후 티커를 6자리로 맞춰줍니다
KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, side = c('left'), pad = '0')

# 빈 리스트 만들기
price_list = list()

# 데이터 가지고 오기
for (i in 1 : nrow(KOR_ticker)) {
  
  name = KOR_ticker[i, '종목코드']
  price_list[[i]] =
    read.csv(paste0('data/KOR_price/', name,
                    '_price.csv'),row.names = 1) %>% # row.names = 1 은 첫번째 열을 행이름으로 한다. 
    as.xts() # xts 파일 형식으로 변경
  
}

# do.call() 함수를 통해 리스트를 열 형태로 묶습니다.
#na.locf() 함수를 통해 결측치에는 전일 데이터를 사용합니다.
price_list = do.call(cbind, price_list) %>% na.locf()

# 종목 코드로 열이름 지정
colnames(price_list) = KOR_ticker$'종목코드'

#저장
write.csv(data.frame(price_list), 'data/KOR_price.csv')


#재무제표 정리하기
library(stringr)
library(magrittr)
library(dplyr)

# csv 파일 부르기
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1)

#
KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, side = c('left'), pad = '0')

# 빈리스트 만들기
data_fs = list()

# 데이터 가지고 오기
for (i in 1 : nrow(KOR_ticker)){
  
  name = KOR_ticker[i, '종목코드']
  data_fs[[i]] = read.csv(paste0('data/KOR_fs/', name,
                                 '_fs.csv'), row.names = 1)# row.names = 1 은 첫번째 열을 행이름으로 한다.
}


#재무제표 항목의 기준을 정해줄 필요가 있습니다
#재무제표 작성 항목은 각 업종별로 상이하므로, 
#이를 모두 고려하면 지나치게 데이터가 커지게 됩니다

# 즉 삼성전자의 재무 항목을 선택하며, 총 237개 재무 항목이 있습니다.
fs_item = data_fs[[1]] %>% rownames()
length(fs_item) # 237

#lapply() 함수를 이용해 모든 재무 데이터가 들어 있는 data_fs 데이터를 대상으로 함수를 적용합니다
#%in% 함수를 통해 만일 매출액이라는 항목이 행 이름에 있으면 해당 부분의 데이터를 select_fs 리스트에 저장하고, 
#해당 항목이 없는 경우 NA로 이루어진 데이터 프레임을 저장합니다.

select_fs = lapply(data_fs, function(x) {
  # 해당 항목이 있을시 데이터를 선택
  if ( '매출액' %in% rownames(x) ) {
    x[which(rownames(x) == '매출액'), ]
    
  # 해당 항목이 존재하지 않을 시, NA로 된 데이터프레임 생성
  } else {
    data.frame(NA)
  }
})

#ind_rows() 함수를 이용해 리스트 내 데이터들을 행으로 묶어줍니다.
select_fs = bind_rows(select_fs)

# 확인
print(head(select_fs))

# 전처리
select_fs = select_fs[!colnames(select_fs) %in%
c('.', 'NA.')]
select_fs = select_fs[, order(names(select_fs))]
rownames(select_fs) = KOR_ticker[, '종목코드']

print(head(select_fs))

#!와 %in% 함수를 이용해, 열 이름에 . 혹은 NA.가 들어가지 않은 열만 선택합니다.
#order() 함수를 이용해 열 이름의 연도별 순서를 구한 후 이를 바탕으로 열을 다시 정리합니다.
#행 이름을 티커들로 변경합니다.



######################################################################################################
#for loop 구문을 이용해 모든 재무 항목에 대한 데이터를 정리하는 방법
fs_list = list()

for (i in 1 : length(fs_item)) {
  select_fs = lapply(data_fs, function(x) {
    # 해당 항목이 있을시 데이터를 선택
    if ( fs_item[i] %in% rownames(x) ) {
      x[which(rownames(x) == fs_item[i]), ]
      
      # 해당 항목이 존재하지 않을 시, NA로 된 데이터프레임 생성
    } else {
      data.frame(NA)
    }
  })
  
  # 리스트 데이터를 행으로 묶어줌 
  select_fs = bind_rows(select_fs)
  
  # 열이름이 '.' 혹은 'NA.'인 지점은 삭제 (NA 데이터)
  select_fs = select_fs[!colnames(select_fs) %in%
                          c('.', 'NA.')]
  
  # 연도 순별로 정리
  select_fs = select_fs[, order(names(select_fs))]
  
  # 행이름을 티커로 변경
  rownames(select_fs) = KOR_ticker[, '종목코드']
  
  # 리스트에 최종 저장
  fs_list[[i]] = select_fs
  
}

# 리스트 이름을 재무 항목으로 변경
names(fs_list) = fs_item

# csv 파일 정장 불가 (list 형이여서) so, RDS 파일로 저장
saveRDS(fs_list, 'data/KOR_fs.Rds')


#가치지표 정리하기

library(stringr)
library(magrittr)
library(dplyr)

# 파일 호출및 6자리 
KOR_ticker = read.csv('data/KOR_ticker.csv', row.names = 1)
KOR_ticker$'종목코드' =
  str_pad(KOR_ticker$'종목코드', 6, side = c('left'), pad = '0')

# 빈리스트
data_value = list()

#for loop 구문을 통해 가치지표 데이터를 data_value 리스트에 저장합니다
for (i in 1 : nrow(KOR_ticker)){
  
  name = KOR_ticker[i, '종목코드']
  data_value[[i]] =
    read.csv(paste0('data/KOR_value/', name,
                    '_value.csv'), row.names = 1) %>%
    t() %>% data.frame()   # t() 를 이용해서 표을 형태 를 변경한다.
  
}

# ind_rows() 함수를 이용하여 리스트 내 데이터들을 행으로 묶어준 후 데이터를 확인해보면 PER, PBR, PCR, PSR 열 
#외에 불필요한 NA로 이루어진 열이 존재합니다
data_value = bind_rows(data_value)
print(head(data_value))

#전처리 
#열 이름이 가치지표에 해당하는 부분만 선택합니다.
ata_value = data_value[colnames(data_value) %in%
                         c('PER', 'PBR', 'PCR', 'PSR')]
#일부 종목은 재무 데이터가 0으로 표기되어 가치지표가 Inf로 계산되는 경우가 있습니다. 
#mutate_all() 내에 na_if() 함수를 이용해 Inf 데이터를 NA로 변경합니다.행 이름을 티커들로 변경합니다.
data_value = data_value %>%
  mutate_all(list(~na_if(., Inf)))

# 행 이름을 종목 코드 변경합니다.
rownames(data_value) = KOR_ticker[, '종목코드']
print(head(data_value))

#저장
write.csv(data_value, 'data/KOR_value.csv')
