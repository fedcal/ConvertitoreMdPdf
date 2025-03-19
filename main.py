import os
import subprocess
import pypandoc
from pathlib import Path


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


def apply_css_styles(md_files, css_path):
    """
    Aggiunge direttamente gli stili CSS nel contenuto Markdown per forzare la formattazione nel PDF.
    """
    updated_files = []
    with open(css_path, "r", encoding="utf-8") as css_file:
        css_content = css_file.read()

    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as file:
            content = file.read()

        # Inserisce gli stili CSS direttamente nel Markdown
        styled_content = f"<style>{css_content}</style>\n\n" + content
        temp_file = md_file + ".styled.tmp"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(styled_content)

        updated_files.append(temp_file)

    return updated_files


def convert_md_to_pdf(folder_path, output_pdf, method):
    md_files = []

    # Percorre tutte le sottocartelle per trovare i file .md
    for root, _, files in os.walk(folder_path):
        for filename in sorted(files):
            if filename.endswith(".md"):
                md_path = os.path.join(root, filename)
                md_files.append(md_path)

    if md_files:
        try:
            script_dir = Path(__file__).parent.resolve()

            if method == "css":
                css_path = script_dir / "style.css"
                if not css_path.exists():
                    print(f"⚠️ ATTENZIONE: Il file CSS non è stato trovato! ({css_path})")
                    return
                else:
                    print(f"✅ File CSS trovato: {css_path}")

                # Normalizza il percorso in base al sistema operativo
                resource_path = Path(folder_path).resolve()
                updated_md_files = preprocess_md_files(md_files, folder_path)
                styled_md_files = apply_css_styles(updated_md_files, css_path)
                extra_args = [
                    "--pdf-engine=xelatex",
                    f"--resource-path={resource_path}:{resource_path}/img",
                    "--highlight-style=tango"
                ]

            elif method == "latex":
                template_path = script_dir / "eisvogel.tex"
                if not template_path.exists():
                    print(f"⚠️ ATTENZIONE: Il file template LaTeX non è stato trovato! ({template_path})")
                    return
                else:
                    print(f"✅ Template LaTeX trovato: {template_path}")

                updated_md_files = preprocess_md_files(md_files, folder_path)
                extra_args = [
                    "--pdf-engine=xelatex",
                    f"--template={template_path}",
                    "--highlight-style=tango",
                    "-V fontsize=12pt",
                    "-V mainfont='DejaVu Sans'",
                    "-V monofont='Fira Code'",
                    "-V colorlinks=true",
                    "-V linkcolor=blue",
                    "-V urlcolor=blue"
                ]
            else:
                print("❌ Metodo di conversione non valido. Scegli 'css' o 'latex'.")
                return

            print(f"🔄 Conversione in corso con il metodo {method}...")

            # Se il file PDF esiste già, lo elimina prima di crearne uno nuovo
            if os.path.exists(output_pdf):
                os.remove(output_pdf)
                print(f"🔄 Il file esistente {output_pdf} è stato eliminato.")

            # Conversione con Pandoc e il metodo scelto
            command = ["pandoc"] + (styled_md_files if method == "css" else updated_md_files) + ["-o",
                                                                                                 output_pdf] + extra_args
            subprocess.run(command, check=True)

            print(f"✅ PDF generato con successo: {output_pdf}")

            # Rimuove i file temporanei solo se la conversione è avvenuta con successo
            for temp_file in updated_md_files:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    print(f"🗑️ File temporaneo eliminato: {temp_file}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Errore durante la conversione: {e}")
    else:
        print("⚠️ Nessun file .md trovato per la conversione.")


if __name__ == '__main__':
    folder_path = input("📂 Inserisci il percorso della cartella contenente i file .md: ").strip()
    folder_path = str(Path(folder_path).resolve())

    if not os.path.isdir(folder_path):
        print("❌ Errore: la cartella specificata non esiste.")
    else:
        output_filename = input("📝 Inserisci il nome del file PDF (senza estensione): ").strip()
        output_pdf = os.path.join(folder_path, f"{output_filename}.pdf")
        method = input("🔧 Scegli il metodo di conversione ('css' o 'latex'): ").strip().lower()
        convert_md_to_pdf(folder_path, output_pdf, method)