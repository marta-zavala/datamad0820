/*  CHALLENGE 1  */

SELECT au.au_id AS 'AUTHOR ID', au.au_lname AS 'LAST NAME', au.au_fname AS 'FIRST NAME', t.title AS 'TITLE', p.pub_name AS 'PUBLISHER'
	FROM authors AS au
	INNER JOIN titleauthor AS tta
		ON au.au_id = tta.au_id
	INNER JOIN titles AS t
		ON tta.title_id = t.title_id
	INNER JOIN publishers AS p
		ON t.pub_id = p.pub_id
    ORDER BY 'AUTHOR ID' ASC


/*  CHALLENGE 2  */

SELECT au.au_id AS 'AUTHOR ID', au.au_lname AS 'LAST NAME', au.au_fname AS 'FIRST NAME', COUNT(t.title) AS 'TITLE COUNT', p.pub_name AS 'PUBLISHER'
	FROM authors AS au
	INNER JOIN titleauthor AS tta
		ON au.au_id = tta.au_id
	INNER JOIN titles AS t
		ON tta.title_id = t.title_id
	INNER JOIN publishers AS p
		ON t.pub_id = p.pub_id
    GROUP BY au.au_id, au.au_lname, au.au_fname, p.pub_name

/*  CHALLENGE 3  */

SELECT au.au_id as 'AUTHOR ID', au.au_lname AS 'LAST NAME', au.au_fname AS 'FIRST NAME', SUM(s.qty) AS 'TOTAL'
	FROM authors as au
	INNER JOIN titleauthor AS tta
		ON au.au_id = tta.au_id
	INNER JOIN sales AS s
		ON tta.title_id = s.title_id
    GROUP BY au.au_id
    ORDER BY SUM(s.qty) DESC LIMIT 3;


/*  CHALLENGE 4  */
