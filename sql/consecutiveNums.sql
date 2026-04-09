-- select DISTINCT l.num as ConsecutiveNums from Logs l
-- join Logs l1 on l1.id-1 = l.id 
-- join Logs l2 on l2.id-2 = l.id
-- where l1.num = l.num and l1.num = l2.num;

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LAG(num,1) OVER (ORDER BY id) AS prev1,
           LAG(num,2) OVER (ORDER BY id) AS prev2
    FROM Logs
) t
WHERE num = prev1 AND num = prev2;