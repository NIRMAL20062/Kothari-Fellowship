<<<<<<< HEAD
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
    pdf.output("C:\Users\kumar\OneDrive\Desktop\Kothari FelloShip Cloned\Kothari-Fellowship\Grant_Utilization_Proposal.pdf")

pdf_path = r"C:\Users\kumar\OneDrive\Desktop\Kothari-Fellowship\Grant_Utilization_Proposal.pdf"

=======
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
    pdf.output("C:\Users\kumar\OneDrive\Desktop\Kothari FelloShip Cloned\Kothari-Fellowship\Grant_Utilization_Proposal.pdf")

pdf_path = r"C:\Users\kumar\OneDrive\Desktop\Kothari-Fellowship\Grant_Utilization_Proposal.pdf"

>>>>>>> e4ce3669f3c7a7e766baea0e9889746d1afa2f2d
