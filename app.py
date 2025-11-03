import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

#graphs ventes
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')

#graphs produits
figure_prod = px.pie(données, values='qte', names='produit', title='quantité vendu par produit')
figure_prod.write_html('ventes-par-produit.html')

#ca = calcul chiffre d'affaires
données['ca'] = données['prix'] * données['qte']

# graphs chiffres d'affaires produits
figure_ca = px.pie(données, values='ca', names='produit', title="Chiffre d'Affaires par Produit")
figure_ca.write_html('ca-par-produit.html')

#graph ca en bar
ca_par_produit = données.groupby('produit')['ca'].sum().reset_index()
figure_ca_bar = px.bar(ca_par_produit, x='produit', y='ca', title="Chiffre d'Affaires par Produit", color='produit')
figure_ca_bar.write_html('ca-par-produit-bar.html')

print('Les graphs ont été générés avec succès !')
