-- 코드를 입력하세요
SELECT CAR_ID,
ROUND(AVG(DATEDIFF(END_DATE,START_DATE)+1),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING  AVERAGE_DURATION >=7
ORDER BY 2 DESC,1 DESC;
