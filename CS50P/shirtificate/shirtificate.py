from fpdf import FPDF

class PDF():
    def __init__(self, student):
        self._pdf = FPDF(orientation="portrait", format="A4")
        self._pdf.add_page()
        self._pdf.set_title("Naveen's CS50 shirtificate")
        self._pdf.set_font("helvetica", "B", 45)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("./shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(24)
        self._pdf.set_font(style="U")
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=45,y=125,txt=f"{student}  took CS50")

    def __str__(self):
        return

    def save(self,fname):
        self._pdf.output(fname)

def main():
    student = input("Name: ")
    pdf = PDF(student)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()
