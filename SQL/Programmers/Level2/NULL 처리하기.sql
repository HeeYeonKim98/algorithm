-- 조건대로 조회하는데, 이름이 없는 동물의 이름은 "No name"으로 표시하기

-- 풀이

SELECT animal_type, if(isnull(name),"No name",name), sex_upon_intake
from animal_ins
order by animal_id

SELECT animal_type, IFNULL(name,"No name"), sex_upon_intake
from animal_ins
order by animal_id