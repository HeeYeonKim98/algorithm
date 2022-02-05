-- 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하기

-- 풀이

select name, count(*) as COUNT
from animal_ins
group by name
having name is not null and COUNT>1
order by name