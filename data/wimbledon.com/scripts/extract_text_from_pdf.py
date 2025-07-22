import pdfplumber
import sys
import os


def print_usage():
    print(
        "Usage:\n"
        "  python extract_text_from_pdf.py <input_pdf_file> <output_txt_file> [--page N]\n"
        "  python extract_text_from_pdf.py <input_pdf_file> <output_txt_file> [--page N]\n"
        "Examples:\n"
        "  python extract_text_from_pdf.py MS_Entries.pdf output.txt\n"
        "  python extract_text_from_pdf.py MS_Entries.pdf output.txt --page 1"
    )


def main():
    args = sys.argv[1:]

    if len(args) not in [2, 4]:
        print_usage()
        sys.exit(1)

    input_pdf_path = args[0]
    output_txt_path = args[1]
    page_number = None

    if len(args) == 4:
        if args[2] != "--page" or not args[3].isdigit():
            print_usage()
            sys.exit(1)
        page_number = int(args[3]) - 1  # pdfplumber is 0-based

    if not os.path.isfile(input_pdf_path):
        print(f"Error: File not found: {input_pdf_path}")
        sys.exit(1)

    with pdfplumber.open(input_pdf_path) as pdf:
        total_pages = len(pdf.pages)

        if page_number is not None:
            if 0 <= page_number < total_pages:
                pages_to_extract = [pdf.pages[page_number]]
                print(f"Extracting page {page_number + 1}")
            else:
                print(f"Warning: Page {page_number + 1} is out of range. Extracting entire document.")
                pages_to_extract = pdf.pages
        else:
            pages_to_extract = pdf.pages

        all_text = "\n\n".join(page.extract_text() or "" for page in pages_to_extract)

    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(all_text)

    print(f"Text written to: {output_txt_path}")


if __name__ == "__main__":
    main()
