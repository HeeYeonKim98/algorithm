-- 이름이 없는 동물을 조회하기

-- 풀이

SELECT animal_id
from animal_ins
where name is not null
order by animal_id