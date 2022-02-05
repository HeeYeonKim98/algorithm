-- el들어가는 개의 아이디와 이름 조회하기

-- 풀이

select animal_id, name
from animal_ins
where animal_type="dog" and name like '%el%'
order by name