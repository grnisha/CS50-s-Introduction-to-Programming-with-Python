from fpdf import FPDF

# 210mm wide by 297mm

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 50)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(10)

    def body(self, name):
        self.set_font("helvetica", size=24)
        self.set_text_color(255,255,255)
        self.cell(0, 213, f"{name} took CS50", align="C")



def main():
    name = input("Name: ")

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.body(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()