# Convert Md To Pdf

## Descrizione
Questo progetto permette di convertire file Markdown (`.md`) in PDF utilizzando diversi metodi, tra cui CSS, LaTeX, Pandoc e WeasyPrint. Supporta la generazione automatica di un indice e la personalizzazione con fogli di stile CSS o template LaTeX.

## Requisiti
Assicurati di avere installati i seguenti strumenti:
- Python 3
- Pandoc
- WeasyPrint
- XeLaTeX (se si utilizza il metodo LaTeX)

Installa le dipendenze Python necessarie con:
```sh
pip install pypandoc weasyprint
```

## Utilizzo
Esegui lo script Python con:
```sh
python convert_md_to_pdf.py
```
Il programma chiederà di inserire:
1. Il percorso della cartella contenente i file Markdown
2. Il nome del file PDF di output
3. Il metodo di conversione (`css`, `latex`, `pandoc`, `weasyprint`)
4. Il nome e l'URL dell'autore

## Metodi di Conversione
- **CSS**: Utilizza Pandoc per convertire Markdown in HTML e WeasyPrint per generare il PDF.
- **LaTeX**: Utilizza un template LaTeX con Pandoc per una resa tipografica avanzata.
- **Pandoc**: Conversione diretta da Markdown a PDF usando il motore XeLaTeX.
- **WeasyPrint**: Converte Markdown in HTML e poi in PDF usando WeasyPrint.

## Struttura del Progetto
- `convert_md_to_pdf.py` - Script principale per la conversione.
- `style.css` - Foglio di stile opzionale per la conversione CSS/WeasyPrint.
- `eisvogel.tex` - Template LaTeX per la conversione con Pandoc e LaTeX.

## Licenza
Questo progetto è distribuito sotto la licenza MIT.