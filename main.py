import os
import pypandoc
from pathlib import Path
import platform


def preprocess_md_files(md_files, folder_path):
    """
    Modifica i percorsi relativi delle immagini nei file Markdown,
    sostituendo `./img/` con il percorso assoluto della cartella fornita e della cartella del file .md.
    """
    updated_files = []
    for md_file in md_files:
        md_dir = os.path.dirname(md_file)  # Ottiene la cartella del file .md
        with open(md_file, "r", encoding="utf-8") as file:
            content = file.read()

        # Sostituisce riferimenti a immagini con percorsi assoluti
        updated_content = content.replace("./img/", f"{folder_path}/img/")
        updated_content = updated_content.replace("./img/", f"{md_dir}/img/")

        temp_file = md_file + ".tmp"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(updated_content)

        updated_files.append(temp_file)

    return updated_files


def convert_md_to_pdf(folder_path, output_pdf):
    md_files = []

    # Percorre tutte le sottocartelle per trovare i file .md
    for root, _, files in os.walk(folder_path):
        for filename in sorted(files):
            if filename.endswith(".md"):
                md_path = os.path.join(root, filename)
                md_files.append(md_path)

    if md_files:
        try:
            # Percorso della cartella dello script (dove si trova main.py e style.css)
            script_dir = Path(__file__).parent.resolve()
            css_path = script_dir / "style.css"

            # Normalizza il percorso in base al sistema operativo
            resource_path = Path(folder_path).resolve()

            # Preprocessa i file Markdown per aggiornare i percorsi delle immagini
            updated_md_files = preprocess_md_files(md_files, folder_path)

            # Opzioni extra per Pandoc
            extra_args = [
                "--pdf-engine=xelatex",  # Usa XeLaTeX per una migliore formattazione
                f"--resource-path={resource_path}:{resource_path}/img",  # Permette di caricare immagini
                f"--css={css_path}"  # Applica il CSS personalizzato
            ]

            print(f"🔄 Percorsi risorse: {resource_path}, {resource_path}/img")

            # Se il file PDF esiste già, lo elimina prima di crearne uno nuovo
            if os.path.exists(output_pdf):
                os.remove(output_pdf)
                print(f"🔄 Il file esistente {output_pdf} è stato eliminato.")

            # Conversione a PDF
            pypandoc.convert_file(updated_md_files, "pdf", outputfile=output_pdf, extra_args=extra_args,
                                  format="markdown")
            print(f"✅ Conversione completata: {output_pdf}")

            # Rimuove i file temporanei solo se la conversione è avvenuta con successo
            for temp_file in updated_md_files:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    print(f"🗑️ File temporaneo eliminato: {temp_file}")
        except Exception as e:
            print(f"❌ Errore durante la conversione: {e}")
    else:
        print("⚠️ Nessun file .md trovato per la conversione.")


if __name__ == '__main__':
    # L'utente inserisce il percorso dei file Markdown
    folder_path = input("📂 Inserisci il percorso della cartella contenente i file .md: ").strip()

    # Normalizza il percorso in base al sistema operativo
    folder_path = str(Path(folder_path).resolve())

    # Controlla se la cartella esiste
    if not os.path.isdir(folder_path):
        print("❌ Errore: la cartella specificata non esiste.")
    else:
        output_filename = input("📝 Inserisci il nome del file PDF (senza estensione): ").strip()
        output_pdf = os.path.join(folder_path, f"{output_filename}.pdf")
        convert_md_to_pdf(folder_path, output_pdf)
