#step09_ WICS 기준 섹터정보 크롤링

#R에서는 jsonlite 패키지의 fromJSON() 함수를 사용해 매우 손쉽게 JSON 형식의 데이터를 크롤링할 수 있습니다.
library(jsonlite)

url = 'http://www.wiseindex.com/Index/GetIndexComponets?ceil_yn=0&dt=20190607&sec_cd=G10'
data = fromJSON(url)

lapply(data, head)


data$list%>% View()


#모든 섹터의 구성종목 가지고 오기
biz_day=20210806
sector_code = c('G25', 'G35', 'G50', 'G40', 'G10',
                'G20', 'G55', 'G30', 'G15', 'G45')
data_sector = list()

for (i in sector_code) {
  
  url = paste0(
    'http://www.wiseindex.com/Index/GetIndexComponets',
    '?ceil_yn=0&dt=',biz_day,'&sec_cd=',i)
  data = fromJSON(url)
  data = data$list
  
  data_sector[[i]] = data
  
  Sys.sleep(1)
}

data_sector = do.call(rbind, data_sector)

#저장
write.csv(data_sector, 'data/KOR_sector.csv')


