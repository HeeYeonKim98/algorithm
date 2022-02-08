-- 모든 동물들 보호소 들어온 날짜 조회

-- 풀이

select animal_id, name, date_format(datetime, '%Y-%m-%d') as "날짜"
from animal_ins
order by animal_id