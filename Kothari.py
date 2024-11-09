from fpdf import FPDF

def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Grant Utilization Proposal", ln=True, align="C")
    
    # Add content as per project details
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.multi_cell(0, 10, 
        "This document outlines the plan to utilize the grant for supporting individuals in realizing the value of their education..."
    )
    
    # Save PDF
    pdf.output("Grant_Utilization_Proposal.pdf")


