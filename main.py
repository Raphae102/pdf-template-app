from fpdf import FPDF
import pandas as pd

# Set the format how you want the page to look like
pdf = FPDF(orientation="P",unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

# read the csv files
df = pd.read_csv("topics.csv")

# creates the content of the pdf
for index,row in df.iterrows():
    # set the header
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],align='L',
             ln=1,border=0)
    #  add lines
    for y in range(20,298,10):
        pdf.line(10,y,200,y)
    # pdf.line(10,21,200,21)

    # set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")

    # add page
    for i in range(row["Pages"]-1):
        pdf.add_page()
        # adding lines
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # set the footer
        pdf.ln(278)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")