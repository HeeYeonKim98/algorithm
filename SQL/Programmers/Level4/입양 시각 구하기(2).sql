-- 각 0~23시 시간대 별로 입양이 몇 건이나 발생했는지 조회하기

-- 풀이

SET @hour := -1; -- 변수 선언

SELECT (@hour := @hour + 1) as HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23