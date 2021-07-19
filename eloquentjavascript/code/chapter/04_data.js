var journal = [];

function ajouteEntree(evenements, ecureuil) {
  journal.push({evenements, ecureuil});
}

function phi(tableau) {
  return (tableau[3] * tableau[0] - tableau[2] * tableau[1]) /
    Math.sqrt((tableau[2] + tableau[3]) *
              (tableau[0] + tableau[1]) *
              (tableau[1] + tableau[3]) *
              (tableau[0] + tableau[2]));
}

function tableauPour(evenement, journal) {
  let tableau = [0, 0, 0, 0];
  for (let i = 0; i < journal.length; i++) {
    let entree = journal[i], index = 0;
    if (entree.events.includes(evenement)) index += 1;
    if (entree.ecureuil) index += 2;
    tableau[index] += 1;
  }
  return tableau;
}

function evenementsJournal(journal) {
  let evenements = [];
  for (let entree of journal) {
    for (let evenement of entree.evenements) {
      if (!evenements.includes(evenement)) {
        evenements.push(evenement);
      }
    }
  }
  return evenements;
}

function max(...nombres) {
  let resultat = -Infinity;
  for (let nombre of nombres) {
    if (nombre > resultat) resultat = nombre;
  }
  return resultat;
}

var liste = {
  valeur: 1,
  reste: {
    valeur: 2,
    reste: {
      valeur: 3,
      reste: null
    }
  }
};
