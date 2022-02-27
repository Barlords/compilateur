# Fonctionnalitées
 - noms de variables à plusieurs caractères
 - affectation
 - affichage
 - instructions conditionnelles
 - structures itératives
 - Affichage de l’arbre de syntaxe
 - Gérer les fonctions sans paramètre
 - Gestion de quelques erreurs
 - incrémentation et affectation élargie



# TESTS

## affectation, print
s1 = 'x=4; x=x+3; print(x);'
TEST : OK

## affectation élargie, affectation 
s2 = 'x=9; x+=4; x++; print(x);'
TEST : OK

## while, for
s3 = 'x=4; while(x<30){x=x+3;print(x);};for(i=0 ; i<4 ; i=i+1){print(i*i) ;};'
TEST : OK

## fonctions void avec paramètres
s4='func toto(a, b){print(a+b) ;}; toto(3, 5) ;'

## fonctions value avec paramètres et return explicite
s5='func toto(a, b){c=a+b ;return c ;} toto(3, 5) ;'

## fonctions value avec paramètres et return implicite
s5='func toto(a, b){c=a+b ; toto=c ;} toto(3, 5) ;'

## fonctions value avec paramètres et return coupe circuit
s6='func toto(a, b){c=a+b ;return c ; print(666) ;} x=toto(3, 5) ; print(x) ;'

## fonctions value avec paramètres, return coupe circuit et scope des variables
s7='func toto(a, b){if(a==0) return b ; c=toto(a-1, b-1) ;return c ; print(666) ;} x=toto(3, 5) ;
print(x) ;'