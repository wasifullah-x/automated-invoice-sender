# 🧾 Automated Invoice Sender with PDF & Email

A Python automation tool that reads client data from an Excel sheet, generates personalized PDF invoices, and sends them via email. Ideal for freelancers, small businesses, or anyone who wants to automate billing.

---

## ✅ Features

- 📥 Reads customer data from an Excel spreadsheet
- 🧾 Generates personalized invoice PDFs
- 📤 Sends emails with invoice attachments
- 📂 Saves a copy of each invoice locally

---

## 🛠 Tech Stack

| Tool        | Purpose                         |
|-------------|---------------------------------|
| **Python**  | Core programming language       |
| `pandas`    | Excel file reading/parsing      |
| `fpdf`      | PDF invoice generation          |
| `smtplib`   | Sending emails via SMTP         |
| `openpyxl`  | Excel `.xlsx` file support      |
| `email`     | Constructing email messages     |

---

## 🔧 How It Works

1. The script reads rows from `clients.xlsx`
2. For each client:
   - A PDF invoice is generated and saved in `/invoices/`
   - An email is composed with the invoice as an attachment
   - The email is sent via Gmail SMTP (or any other SMTP server)


---

