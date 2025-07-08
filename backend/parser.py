import textract
import re

def parse_schedule(filepath):
    # Use textract to extract all text from the file (PDF, DOCX, etc.)
    text = textract.process(filepath).decode('utf-8')

    # Example: Find all dates in format MM/DD/YYYY (e.g., 09/05/2025)
    date_pattern = r'\d{2}/\d{2}/\d{4}'
    dates = re.findall(date_pattern, text)

    # (Optional) You can add more logic here to detect keywords like "Exam", "Due", etc.
    # For now, just return the dates found
    return dates
