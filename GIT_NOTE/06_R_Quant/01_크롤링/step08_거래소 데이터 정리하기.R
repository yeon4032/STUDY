#step08_거래소 데이터 정리하기

#
down_sector = read.csv('data/krx_sector.csv', row.names = 1,
                       stringsAsFactors = FALSE)
down_ind = read.csv('data/krx_ind.csv',  row.names = 1,
                    stringsAsFactors = FALSE)

# row.names = 1을 통해 첫 번째 열을 행 이름으로 지정하고, 
#stringsAsFactors = FALSE를 통해 문자열 데이터가 팩터 형태로 변형되지 않게 합니다.

#intersect() 함수를 통해 두 데이터 간 중복되는 열 이름을 살펴보면 종목코드와 
#종목명 등이 동일한 위치에 있습니다.
intersect(names(down_sector), names(down_ind))

#setdiff() 함수를 통해 두 데이터에 공통적으로 없는 종목명, 
#즉 하나의 데이터에만 있는 종목을 살펴보면 위와 같습니다
setdiff(down_sector[, '종목명'], down_ind[ ,'종목명'])

KOR_ticker = merge(down_sector, down_ind,
                   by = intersect(names(down_sector),
                                  names(down_ind)),
                   all = FALSE
)

#merge() 함수는 by를 기준으로 두 데이터를 하나로 합치며,
#공통으로 존재하는 종목코드, 종목명, 종가, 대비, 등락률을 기준으로 입력해줍니다.
#또한 all 값을 TRUE로 설정하면 합집합을 반환하고, FALSE로 설정하면 교집합을 반환합니다.
#공통으로 존재하는 항목을 원하므로 여기서는 FALSE를 입력합니다.

# 내리차순 (시가총액 기준)
KOR_ticker = KOR_ticker[order(-KOR_ticker['시가총액']), ]
print(head(KOR_ticker))

#마지막으로 스팩, 우선주 종목 역시 제외해야 합니다.

library(stringr)
# 제외 시킬 주식 찾기 (스팩 , 우선주)
KOR_ticker[grepl('스팩', KOR_ticker[, '종목명']), '종목명']  # 스팩 종목 뽑기
KOR_ticker[str_sub(KOR_ticker[, '종목코드'], -1, -1) != 0, '종목명'] # 우선주 뽑기 (우선주는 마지막 숫자가 0 이 아님)
#grepl() 함수를 통해 종목명에 ‘스팩’이 들어가는 종목을 찾고
#, stringr 패키지의 str_sub() 함수를 통해 종목코드 끝이 0이 
#아닌 우선주 종목을 찾을 수 있습니다.

# 스팩 과 우선주 제거
KOR_ticker = KOR_ticker[!grepl('스팩', KOR_ticker[, '종목명']), ]  
KOR_ticker = KOR_ticker[str_sub(KOR_ticker[, '종목코드'], -1, -1) == 0, ]

# 행 이름을 초기화한 후 정리된 데이터를 csv 파일로 저장합니다.
rownames(KOR_ticker) = NULL
write.csv(KOR_ticker, 'data/KOR_ticker.csv')
