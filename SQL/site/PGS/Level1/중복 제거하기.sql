-- 동물의 이름이 몇 개인지 중복과 null값은 제외하고 조회하기

-- 풀이

select count(distinct NAME)
from animal_ins