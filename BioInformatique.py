#Préfixe d'une chaine de caractères
def prefixe(M,S):
    if len(M)>len(S):
        return False
    for i in range(len(M)):
        if M[i]!=S[i]:
            return False
    return True 

#Suffixe d'une chaine de caractères
def list_suffixe(s):
    l=[]
    for i in range(len(s)):
        elem1=s[i:]
        l.append((elem1,i))
    return l

#Tri de la liste des suffixes
def tri_liste(L):
    for x in range(len(L)-1):
        indice_min=x
        for j in range(x,len(L)):
            if L[j][0]<L[indice_min][0] : 
                indice_min=j
        L[x],L[indice_min]=L[indice_min],L[x]
    return(L)

#Recherche dichotomique d'un motif 
def recherche_dichotomique(M,L):
    debut=0
    fin=len(L)-1
    while(debut<=fin):
        milieu=(debut+fin)//2
        if L[milieu][0]==M:
            return milieu
        else:
            if L[milieu][0]<M:
                debut=milieu+1
            else:
                fin=milieu-1
    return False
#complexite:O(m)=log(k)*m
# la complexité de la recherche dichotomique est O(log k)
#A chaque étape de la recherche dichotomique, une comparaison est faite entre la chaîne M et un élément de la liste L. la complexité de cette comparaison  est linéaire et sera O(m).

#L'arbre des suffixes d'une chaine de caractères
def parcours_arbre(noeud,liste):
    if type(noeud) == list and len(noeud) > 1 and len(noeud[1]) == 0:
        liste.append(noeud[0])
    else:
        for fils in noeud[1]:
            parcours_arbre(fils,liste)
def feuilles(R):
    resultat = []
    parcours_arbre(R,resultat)
    return resultat

def vide(a):
    if a== [] :
        return True
    return False
def val(a):
    if vide(a):
        return None
    return a[0]
def est_feuille(noeud):
    return isinstance(noeud, list) and len(noeud) == 2 and len(noeud[1]) == 0

def recherche_arbre(motif, arbre):
    liste = []
    for noeud in arbre[1]:
        if not est_feuille(noeud):
            valeur = val(noeud)
            if prefixe(motif, valeur):
                liste = feuilles(noeud)
            elif prefixe(valeur, motif):
                x = len(valeur)
                liste = recherche_arbre(motif[x:], noeud)
    return liste

#Plus long motif commun
def matrice(P, Q):
    len_P, len_Q = len(P), len(Q)
    M = [[0] * len_Q for _ in range(len_P)]
    for i in range(len_P):
        for j in range(len_Q):
            if P[i] == Q[j]:
                if i == 0 or j == 0:
                    M[i][j] = 1
                else:
                    M[i][j] = M[i - 1][j - 1] + 1
    return M

def plus_long_mc(P, M):
    len_P, len_Q = len(P), len(M[0]) if M else 0
    if len_P == 0 or len_Q == 0:
        return []
    max_length = 0
    max_length_indices = []
    for i in range(len_P):
        for j in range(len_Q):
            if M[i][j] > max_length:
                max_length = M[i][j]
                max_length_indices = [(i, j)]
            elif M[i][j] == max_length:
                max_length_indices.append((i, j))
    motifs = set()
    for i, j in max_length_indices:
        motif = P[i - max_length + 1:i + 1]
        motifs.add(motif)
    return list(motifs)










 
        

