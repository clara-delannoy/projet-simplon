--3.A REQUETE SQL - Chiffre d affaire total :
SELECT  'Le Chiffre d Affaire Total est de :', SUM(qte*prix), '€'
FROM ventes;

--3.B REQUETE SQL - Ventes par produit :
SELECT produit, SUM(prix*qte) 
FROM ventes
GROUP BY produit;

--3.C REQUETE SQL - Ventes par région :
SELECT region, SUM(qte), SUM(prix * qte)
FROM ventes
GROUP BY region;