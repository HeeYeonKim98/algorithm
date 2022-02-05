-- 중성화 여부를 아이디 순으로 조회하기

-- 풀이

select animal_id, name, case when sex_upon_intake like "%neutered%" or sex_upon_intake like "%spayed%" then 'O' else 'X' end as '중성화'
from animal_ins
order by animal_id