# Chanllenge_Dentsu_Aegis_Network

Per questa challenge ho utilizzato python per estrarre il file pickle, mergiare i dataset e fare le prime analisi esplorative.
I pacchetti utilizzati sono stati Pandas, Numpy e Matplotlib, grazie ai quali ho verificato i missing values, ragruppato le varie 
categorie e preso visione di com'era fatto il dataset.

L' idea iniziale era di creare una pagina HTML e usare Highcharts, libreria Javascript, per fare dei grafici e quindi una dashboard,
ma il poco tempo mi ha portato a scegliere Tableau, d'altro canto è stato creato apposta, per fare analisi, grafici e reportistica
in breve tempo.

Nel folder Dashboard_Tableau troverai un extract, che ho fatto per rendere le performance migliori, un .twb e un .twbx , su quest'ultimo
si trovano le tre dashboard create. Nella cartella Old_versions, ci sono dei .twbx nelle ultime 4 versioni, non sapendo quale avete.

Le tre dashboard riguardano:
- User Activity: quanto gli utenti sono attivi e per quali categorie, mostra come sono distribuiti gli utenti in Italia e la loro attività
                  E' inoltre possibile selezione gli utenti TOP rispetto all'attività
- User Behaviour: mostra ogni utente nel giorno in cui ha iniziato ad essere attivo, sul grafico viene descritto il comportamento dei dati
- Browser View: visione su quali sono i browser più utilizzati negli anni e quali i device
