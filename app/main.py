import os
import fitz
from dotenv import load_dotenv

load_dotenv()

def extract_raw_text(pdf_path, output_path):
    try:
        pdf_document = fitz.open(pdf_path)

        full_text = ""

        for page_num in range(len(pdf_document)):

            page = pdf_document.load_page(page_num)
            
            full_text += page.get_text() + "\n"
            full_text += "=========\n"

        pdf_document.close()

        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(full_text)
        
        success_log_path = os.path.join(os.getenv("OUTPUT_FOLDER", "data/raw"), "log_job.log")
        filename = os.path.basename(output_path)
        with open(success_log_path, "a", encoding="utf-8") as success_log_file:
            success_log_file.write(f"Successfully processed: {filename}\n")
    except Exception as e:
        error_log_path = os.path.join(os.getenv("OUTPUT_FOLDER", "data/raw"), "log_error.log")
        with open(error_log_path, "a", encoding="utf-8") as error_log_file:
            error_log_file.write(f"Error processing {pdf_path}: {str(e)}\n")


def process_pdfs(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")

            extract_raw_text(input_path, output_path)


if __name__ == "__main__":

    input_folder = os.getenv("INPUT_FOLDER", "data/pdf")

    output_folder = os.getenv("OUTPUT_FOLDER", "data/raw")

    process_pdfs(input_folder, output_folder)
