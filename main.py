import os
import subprocess
import pypandoc
from pathlib import Path
from weasyprint import HTML


def preprocess_md_files(md_files, folder_path):
    """Modifica i percorsi relativi delle immagini nei file Markdown."""
    updated_files = []
    for md_file in md_files:
        md_dir = os.path.dirname(md_file)
        with open(md_file, "r", encoding="utf-8") as file:
            content = file.read()
        updated_content = content.replace("./img/", f"{folder_path}/img/")
        updated_content = updated_content.replace("./img/", f"{md_dir}/img/")
        temp_file = md_file + ".tmp"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(updated_content)
        updated_files.append(temp_file)
    return updated_files


def convert_md_to_html(md_files, output_html):
    """Converte Markdown in HTML con Pandoc."""
    command = ["pandoc"] + md_files + ["-o", output_html, "--standalone"]
    subprocess.run(command, check=True)
    return output_html


def convert_html_to_pdf(html_file, css_file, output_pdf):
    """Converte HTML in PDF usando WeasyPrint."""
    html = HTML(filename=html_file)
    html.write_pdf(output_pdf, stylesheets=[css_file])


def cleanup_files(files):
    """Elimina i file temporanei generati."""
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"🗑️ File eliminato: {file}")


def convert_md_to_pdf(folder_path, output_pdf, method):
    md_files = [os.path.join(root, f) for root, _, files in os.walk(folder_path) for f in sorted(files) if
                f.endswith(".md")]
    if not md_files:
        print("⚠️ Nessun file .md trovato per la conversione.")
        return

    try:
        script_dir = Path(__file__).parent.resolve()
        temp_files = []

        if method == "css":
            css_path = script_dir / "style.css"
            if not css_path.exists():
                print(f"⚠️ File CSS non trovato: {css_path}")
                return
            output_html = output_pdf.replace(".pdf", ".html")
            updated_md_files = preprocess_md_files(md_files, folder_path)
            temp_files.extend(updated_md_files)
            convert_md_to_html(updated_md_files, output_html)
            convert_html_to_pdf(output_html, css_path, output_pdf)
            temp_files.append(output_html)
            print(f"✅ PDF generato con successo: {output_pdf}")

        elif method == "latex":
            template_path = script_dir / "eisvogel.tex"
            if not template_path.exists():
                print(f"⚠️ Template LaTeX non trovato: {template_path}")
                return
            updated_md_files = preprocess_md_files(md_files, folder_path)
            temp_files.extend(updated_md_files)
            command = ["pandoc"] + updated_md_files + ["-o", output_pdf, "--pdf-engine=xelatex",
                                                       f"--template={template_path}", "--highlight-style=tango"]
            subprocess.run(command, check=True)
            print(f"✅ PDF generato con successo: {output_pdf}")

        elif method == "pandoc":
            updated_md_files = preprocess_md_files(md_files, folder_path)
            temp_files.extend(updated_md_files)
            command = ["pandoc"] + updated_md_files + ["-o", output_pdf, "--pdf-engine=xelatex",
                                                       "--highlight-style=tango"]
            subprocess.run(command, check=True)
            print(f"✅ PDF generato con successo: {output_pdf}")

        elif method == "weasyprint":
            css_path = script_dir / "style.css"
            output_html = output_pdf.replace(".pdf", ".html")
            updated_md_files = preprocess_md_files(md_files, folder_path)
            temp_files.extend(updated_md_files)
            convert_md_to_html(updated_md_files, output_html)
            convert_html_to_pdf(output_html, css_path, output_pdf)
            temp_files.append(output_html)
            print(f"✅ PDF generato con successo: {output_pdf}")

        cleanup_files(temp_files)

    except subprocess.CalledProcessError as e:
        print(f"❌ Errore durante la conversione: {e}")


if __name__ == '__main__':
    folder_path = input("📂 Inserisci il percorso della cartella contenente i file .md: ").strip()
    folder_path = str(Path(folder_path).resolve())
    if not os.path.isdir(folder_path):
        print("❌ Errore: la cartella specificata non esiste.")
    else:
        output_filename = input("📝 Inserisci il nome del file PDF (senza estensione): ").strip()
        output_pdf = os.path.join(folder_path, f"{output_filename}.pdf")
        method = input("🔧 Scegli il metodo di conversione ('css', 'latex', 'pandoc', 'weasyprint'): ").strip().lower()
        convert_md_to_pdf(folder_path, output_pdf, method)
