-- 코드를 입력하세요
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Milk'
INTERSECT
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Yogurt'
ORDER BY CART_ID

