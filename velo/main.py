import matplotlib.pyplot as plt
import json

def plot(dict):
    plt.pie(dict.values(), labels = dict.keys())
    plt.show()
    return None


def main():
    raw = json.load(open("pvo_patrimoine_voirie.pvoamenagementcyclable.json", 'r'))
    data = raw['values']
    nbr_piste_super_struct = 0
    localisation = {"Sur chaussee": 0, "Sans objet":0, "Sur trottoir" : 0, None: 0}
    typeamenagement ={'Piste Cyclable':0,  'Bande Cyclable':0,  'Voie verte':0,  'Couloir bus velo non elargi':0,  'Couloir bus velo elargi':0,  'Double sens cyclable':0,  'Chaussee à voie centrale banalisee (CVCB)':0}
    typeamenagement2 = {None:0,  'Couloir bus velo non elargi':0,  'Bande Cyclable':0,  'Couloir bus velo elargi':0,  'Piste Cyclable':0}
    typologiepiste = {'Piste sur chaussee':0,  None:0,  'Piste sur trottoir':0,  'Piste intercalee entre trottoir et stationnement':0,  'Autre':0,  'Piste sur chaussee à hauteur intermediaire':0}
    positionnement = {'Unilaterale bidirectionnelle':0,  'Bilaterale unidirectionnelle':0,  'Unilaterale unidirectionnelle':0,  'Sans objet':0,  'Bilaterale bidirectionnelle':0}
    environnement = {'Tunnel - Passerelle':0,  'Voie de circulation':0,  'Sans objet':0,  'Berges - Chemin de halage':0,  'Parc':0,  None:0}
    reglementation = {'Velo facultatif':0,  None:0,  'Velo obligatoire':0,  'Contresens (sens reserve)':0,  'Voie verte':0,  'Autre':0,  'Zone 30':0,  'Aire pietonne':0}
    zonecirculationapaisee = {None:0, 'Zone 30':0, 'Aire Pietonne':0, 'Zone de rencontre':0}
    anneelivraison = {None:0,  2011:0,  2008:0,  2009:0,  2006:0,  2022:0,  2003:0,  2004:0,  2005:0,  2017:0,  2015:0,  2018:0,  2010:0,  2000:0,  2001:0,  2013:0,  2020:0,  1998:0,  2007:0,  2014:0,  2021:0,  2019:0,  2012:0,  2016:0,  1996:0,  2002:0}
    longueurcalculee = 0
    for v in data:
        if v["reseau"] == "Reseau super structurant":
            nbr_piste_super_struct +=1
            localisation[v["localisation"]] += 1
            typeamenagement[v['typeamenagement']] += 1
            typeamenagement2[v['typeamenagement2']] +=1
            typologiepiste[v['typologiepiste']] +=1
            positionnement[v['positionnement']] +=1
            environnement[v['environnement']] += 1
            reglementation[v['reglementation']] += 1
            zonecirculationapaisee[v['zonecirculationapaisee']]+=1
            anneelivraison[v['anneelivraison']] += 1
            longueurcalculee += v['longueurcalculee']

    print("Nombre de piste sur le réseau super structurant :" , nbr_piste_super_struct)
    plot(localisation)
    plot(typeamenagement)
    plot(typeamenagement2)
    plot(typologiepiste)
    plot(positionnement)
    plot(environnement)
    plot(reglementation)
    plot(zonecirculationapaisee)
    plot(anneelivraison)
    print(longueurcalculee)
    return None



if __name__ == '__main__':
    main()
