# 📌 Convertitore Markdown to PDF

Questo script permette di convertire tutti i file **Markdown (.md)** presenti in una cartella e nelle relative sottocartelle in un **unico file PDF**. Supporta immagini e consente di applicare uno stile personalizzato tramite un file CSS.

---

## 📥 Installazione

### 1️⃣ Requisiti
Assicurati di avere installati:
- **Python 3.x** ([Scarica qui](https://www.python.org/downloads/))
- **Pandoc** ([Scarica qui](https://pandoc.org/installing.html))
- **TeX Live / MiKTeX** (necessario per la generazione del PDF con XeLaTeX)

### 2️⃣ Installazione delle dipendenze
Esegui il seguente comando per installare la libreria necessaria:
```sh
pip install pypandoc
```

---

## 🚀 Utilizzo
Esegui il seguente comando da terminale:
```sh
python main.py
```

### 🔹 Passaggi
1. Ti verrà chiesto di inserire il **percorso della cartella** contenente i file `.md`.
2. Dovrai specificare il **nome del file PDF di output**.
3. Il programma elaborerà tutti i file Markdown e genererà un unico PDF con le immagini incluse e una formattazione CSS personalizzata.

---

## 🎨 Personalizzazione del CSS
Il file `style.css` consente di personalizzare la formattazione del PDF.
- Per modificare lo stile di **tabelle**, **codice**, **titoli**, ecc., modifica il file `style.css` presente nella stessa cartella di `main.py`.

Esempio di `style.css` per migliorare le tabelle e il codice:
```css
table {
    width: 100%;
    border-collapse: collapse;
}

td, th {
    border: 1px solid black;
    padding: 8px;
    text-align: left;
}

code {
    background-color: #f4f4f4;
    padding: 2px 4px;
    font-family: monospace;
    border-radius: 4px;
}
```

---

## 🛠 Funzionalità
✅ **Supporta Windows, Linux e macOS** (gestione automatica dei percorsi).  
✅ **Ricerca automatica di tutti i file `.md` in sottocartelle**.  
✅ **Supporta immagini nei file `.md`**.  
✅ **Applica uno stile CSS personalizzato**.  
✅ **Sovrascrive automaticamente il file PDF se già presente**.  

---

## ⚠️ Risoluzione Problemi
- **Errore: `pandoc: command not found`** → Assicurati di aver installato Pandoc e di averlo aggiunto al `PATH`.
- **Errore di conversione a PDF** → Installa MiKTeX (Windows) o TeX Live (Linux/macOS) per supportare `xelatex`.
- **Le immagini non vengono incluse** → Assicurati che le immagini siano referenziate con percorsi relativi nei file Markdown.

---

## 📜 Licenza
Questo progetto è distribuito sotto licenza MIT. Sentiti libero di modificarlo e migliorarlo!

🚀 **Buona conversione!**

