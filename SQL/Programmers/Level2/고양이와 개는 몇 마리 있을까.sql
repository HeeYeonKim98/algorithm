-- 동물 중 고양이와 개가 각각 몇 마리 인지 조회하기

-- 풀이

select animal_type, count(*) as count
from animal_ins
group by animal_type
order by animal_type