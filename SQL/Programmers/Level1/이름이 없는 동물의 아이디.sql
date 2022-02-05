-- 이름이 없는 동물을 조회하기

-- 풀이

select animal_id
from animal_ins
where name is null
order by animal_id