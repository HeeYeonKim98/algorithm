-- 특정 동물의 아이디, 이름, 성별 및 중성화 여부 조회하기

-- 풀이

select distinct animal_id, name, sex_upon_intake
from animal_ins
where name="Lucy" or name="Ella" or name="Pickle" or name="Rogan" or name="Sabrina" or name="Mitty"