-- 코드를 입력하세요
SELECT ANIMAL_ID,A.NAME
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B USING(ANIMAL_ID)
WHERE A.DATETIME > B.DATETIME
ORDER BY A.DATETIME;