import tabula
import pandas as pd

PDF_IN = "statment.pdf"

PDF = tabula.read_pdf(PDF_IN, pages='all', multiple_tables=True)

PDF_OUT_XLSX = "From_PDF.xlsx"
PDF_OUT_CSV = "From_PDF.csv"

#convert into Excel
PDF = pd.DataFrame(PDF)
PDF.to_excel(PDF_OUT_XLSX,index=False) 

#Convert into CSV
tabula.convert_into (PDF_IN, PDF_OUT_CSV, pages='all',multiple_tables=True)