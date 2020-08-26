#CHALLENGE1

SELECT au.au_id AS 'AUTHOR ID', au.au_lname AS 'LAST NAME', au.au_fname AS 'FIRST NAME', t.title AS 'TITLE', p.pub_name AS 'PUBLISHER'
	FROM authors AS au
	INNER JOIN titleauthor AS tta
		ON au.au_id = tta.au_id
	INNER JOIN titles AS t
		ON tta.title_id = t.title_id
	INNER JOIN publishers AS p
		ON t.pub_id = p.pub_id
    ORDER BY 'AUTHOR ID' ASC

