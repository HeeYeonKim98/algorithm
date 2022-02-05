-- 각 09~19 시간대별로 입양이 몇 건이나 발생했는지 조회하기

-- 풀이

select DATE_FORMAT(datetime,"%H") as HOUR ,count(*) as COUNT
from animal_outs
group by HOUR
having HOUR between 09 and 19
order by HOUR