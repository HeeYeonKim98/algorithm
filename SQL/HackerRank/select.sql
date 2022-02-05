-- 인구수가 100000보다 큰 미국 도시에 대해 모든 칼럼을 조회하기

-- 풀이

select *
from CITY
where population>100000 and countrycode="USA"