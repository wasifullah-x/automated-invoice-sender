from fpdf import FPDF
from datetime import date
from pathlib import Path

def generate_invoice(name, service, amount, invoice_no, due_date):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Invoice title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Invoice", ln=True, align="C")

    # Metadata
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(100, 10, txt=f"Invoice No: {invoice_no}", ln=True)
    pdf.cell(100, 10, txt=f"Date Issued: {date.today()}", ln=True)
    pdf.cell(100, 10, txt=f"Due Date: {due_date}", ln=True)

    pdf.ln(10)
    pdf.cell(100, 10, txt=f"Bill To: {name}", ln=True)
    pdf.cell(100, 10, txt=f"Service: {service}", ln=True)
    pdf.cell(100, 10, txt=f"Amount Due: ${amount}", ln=True)

    # Save PDF
    invoice_folder = Path("invoices")
    invoice_folder.mkdir(exist_ok=True)
    filename = invoice_folder / f"{invoice_no}.pdf"
    pdf.output(str(filename))
    return filename
