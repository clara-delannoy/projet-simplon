import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')


# 6.A Graphique de ventes par produit 
ventes_par_produit = données.groupby('produit')['qte'].sum().reset_index()
figure = px.bar(ventes_par_produit, x='produit', y='qte', title='quantité vendue par produit')
figure.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

#groupby('produit') : regroupe les données par produit mais les valeurs de produit sont en index
#['qte'].sum() : calcule la somme des quantités vendues pour chaque produit
#reset_index() : réinitialise l'index pour obtenir un tableau propre 
#px.bar() : crée un graphique à barres avec les données de ventes_par_produit, en utilisant 'produit' pour l'axe x et 'qte' pour l'axe y, et en définissant le titre du graphique
#write_html() : enregistre le graphique dans un fichier HTML nommé 'ventes-par-produit.html'




# 6.B Graphique du chiffre d'affaires par produit
données['ca'] = données['prix'] * données['qte']
#création d'une nouvelle colonne 'ca' dans le tableau données, calculée en multipliant les colonnes 'prix' et 'qte' pour chaque ligne. Cela représente le chiffre d'affaires généré par chaque vente.

chiffre_affaires_par_produit = données.groupby('produit')['ca'].sum().reset_index()
#['ca'].sum() : calcule la somme du chiffre d'affaires pour chaque produit

figure = px.bar(chiffre_affaires_par_produit, x='produit', y='ca', title='chiffre d\'affaires par produit')
figure.write_html('chiffre-affaires-par-produit.html')
print('chiffre-affaires-par-produit.html généré avec succès !')