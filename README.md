# Convertitore Markdown to PDF

## Descrizione
Questo progetto permette di convertire file Markdown (`.md`) in un unico file PDF mantenendo la struttura e i riferimenti alle immagini.
Il codice si assicura di aggiornare automaticamente i percorsi delle immagini, adattandoli in base al sistema operativo e alla struttura del progetto.

## Struttura del progetto
La cartella principale contiene diverse sottocartelle con i file `.md`, oltre a una cartella `img/` per le immagini:

```
sql course advanced/
├── 01 Introduzione/
├── 02 sql basics/
├── 03 Manipolazione di dati/
├── 04 Definizione di tabelle/
├── 05 Query multi tabella/
├── 06 Funzioni aggregate/
├── 07 funzioni scalari/
├── 08 Sottoquery e CTE/
├── 09 Window function/
└── img/
```

Ogni sottocartella contiene file Markdown che devono essere convertiti in PDF, preservando la struttura e i riferimenti alle immagini.

## Requisiti
Assicurati di avere installati:
- Python 3.x
- [Pandoc](https://pandoc.org/installing.html)
- Il pacchetto Python `pypandoc`

Per installare `pypandoc`, usa:
```bash
pip install pypandoc
```

## Esecuzione
Per eseguire lo script di conversione, apri un terminale nella cartella del progetto e lancia:

```bash
python main.py
```

Lo script chiederà di inserire:
1. Il percorso della cartella principale (`sql course advanced/` nella struttura sopra).
2. Il nome del file PDF di output.

Il codice modificherà i percorsi delle immagini in modo che siano riconosciuti correttamente e genererà il file PDF finale.

## Funzionamento dello script
1. **Individuazione dei file Markdown**: Lo script cerca tutti i file `.md` nelle sottocartelle della cartella indicata.
2. **Aggiornamento dei percorsi delle immagini**: Qualsiasi riferimento a `./img/` viene aggiornato per riflettere la posizione corretta.
3. **Conversione con Pandoc**: I file Markdown vengono convertiti in PDF, applicando anche un eventuale file CSS personalizzato.
4. **Pulizia**: Dopo la conversione, i file temporanei generati dallo script vengono rimossi.

## Contatti
Per ulteriori dettagli, visita il mio sito: [federicocalo.dev](https://federicocalo.dev)

