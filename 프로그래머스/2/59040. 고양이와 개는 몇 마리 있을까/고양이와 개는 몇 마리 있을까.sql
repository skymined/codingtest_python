SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) AS 'COUNT'
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC
;