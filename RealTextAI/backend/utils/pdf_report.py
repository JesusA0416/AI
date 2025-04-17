from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "AI Detection Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_pdf_report(verdict, confidence, entropy_score, flagged_sentences):
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)

    pdf.cell(0, 10, f"Verdict: {verdict}", ln=True)
    pdf.cell(0, 10, f"Confidence: {confidence}%", ln=True)
    pdf.cell(0, 10, f"Entropy Score: {entropy_score}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Flagged Sentences:", ln=True)
    pdf.set_font("Arial", "", 12)

    for sentence in flagged_sentences:
        pdf.multi_cell(0, 10, f"- {sentence}")

    output_path = "/tmp/report.pdf"  # Use Windows path like "report.pdf" if needed
    pdf.output(output_path)
    return output_path
