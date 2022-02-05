-- el들어가는 개의 아이디와 이름 조회하기

-- 풀이

select animal_id, name, date_format(datetime, '%Y-%m-%d') as "날짜"
from animal_ins
order by animal_id