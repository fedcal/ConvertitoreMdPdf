import os
import pypandoc


def convert_md_to_pdf(folder_path, output_pdf):
    md_files = []

    for root, _, files in os.walk(folder_path):
        for filename in sorted(files):  # Ordina per mantenere un ordine logico
            if filename.endswith(".md"):
                md_path = os.path.join(root, filename)
                md_files.append(md_path)

    if md_files:
        try:
            pypandoc.convert_file(
                md_files,
                "pdf",
                outputfile=output_pdf,
                extra_args=["--pdf-engine=xelatex", "--css=style.css"]
            )
            print(f"Conversione completata: {output_pdf}")
        except Exception as e:
            print(f"Errore durante la conversione: {e}")
    else:
        print("Nessun file .md trovato per la conversione.")


if __name__ == '__main__':
    folder_path = "D:/prj/roadmapsh/"
    output_filename = input("Inserisci il nome del file PDF (senza estensione): ")
    output_pdf = os.path.join(folder_path, f"{output_filename}.pdf")
    convert_md_to_pdf(folder_path, output_pdf)


