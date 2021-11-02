-- 가장 최근에 들어온 동물의 시간을 조회

-- 풀이

select max(datetime) as 시간
from animal_ins