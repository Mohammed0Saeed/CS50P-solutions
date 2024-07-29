from fpdf import FPDF

class PDF(FPDF):
    # to set the header of the pdf
    def header(self):
        self.set_font("helvetica", "B", 25) 
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")


def main():
    name = input("name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 17)
    pdf.set_text_color(250, 250, 250)
    pdf.image("./shirtificate.png", 20, 50, 170)
    pdf.cell(-30, 200, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

main()
