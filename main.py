import pandas as pd
from datetime import date
from sendemail import send_email
from generatepdf import generate_invoice

# 1. Read the Excel sheet
df = pd.read_excel("invoices.xlsx")

# 2. Filter unpaid rows (if needed)
unpaid_df = df[df["status"] == "pending"]

# 3. Loop through each row and send invoice
for index, row in unpaid_df.iterrows():
    pdf_path = generate_invoice(
        name=row["client_name"],
        service=row["service"],
        amount=row["amount"],
        invoice_no=row["invoice_no"],
        due_date=row["due_date"]
    )

    send_email(
        subject="Invoice Reminder" + row["invoice_no"],
        reciever_mail=row["client_mail"],
        name=row["client_name"],
        service=row["service"],
        invoice_no=row["invoice_no"],
        amount=row["amount"],
        due_date=row["due_date"],
        attachment_path=pdf_path,
    )
