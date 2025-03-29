from fpdf import FPDF

def create_pdf(data, date):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("Arial", "", fname="", uni=True)
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt=f"תאריך: {date}", ln=True, align="R")
    pdf.multi_cell(0, 10, txt=f"הערות:\n{data.get('comments', '')}", align="R")

    pdf.cell(200, 10, txt="חתימות:", ln=True, align="R")
    pdf.cell(200, 10, txt=f"בוקר: {data.get('morning', '')}", ln=True, align="R")
    pdf.cell(200, 10, txt=f"צהרים: {data.get('noon', '')}", ln=True, align="R")
    pdf.cell(200, 10, txt=f"לילה: {data.get('night', '')}", ln=True, align="R")

    pdf.output(f"data/archive/{date}.pdf")
