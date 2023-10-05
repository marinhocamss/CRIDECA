from fpdf import FPDF 
from time import sleep



class PDF(FPDF):
    def header(self):
        self.image("caneca.png", 10, 8, 25)
        self.set_font("Arial", "B", 20)
        self.cell(0, 10, "CridECA", ln = 1, align="C")
        self.ln(20)

def salvar(remetent,assunt,dat):
    pdf = PDF()    
    pdf.add_page() 
    pdf.set_font("Arial", size = 15) 
    txt = open(f"./crid/{remetent}-{assunt}-{dat}.txt", "r")
    linha = txt.readlines() 
    for i in linha: 
        pdf.multi_cell(180, 10, i) 
   
    pdf.output(f"./crid/cridpdf/{remetent}-{assunt}-{dat}.pdf") 
    pdf.close() 


def enviar(dat, remetent, destinatari,assunt, corp):
    txt = open(f'./crid/{remetent}-{assunt}-{dat}.txt', "w")
    txt.write(f'''    
    Data:           {dat}
    Professor:      {remetent}
    Destinatario:   {destinatari}
    Assunto:        {assunt}
    Corpo:          {corp}''')

       
    txt.close()


def dt(data):
    data = data.split("-")
    nda = f"{data[2]}-{data[1]}-{data[0]}"
    return nda

def cadastrar(nome, senha):
    txt = open("registro.txt", "a")
    txt.write(f"{nome}-{senha}\n")
    txt.close()

def mostrar():
    info = []
    txt = open("./registro.txt", "r")
    dados = txt.readlines()
    for i in dados:
        i=i.strip("\n")
        info.append(i.split("-"))
    txt.close()
    return info

mostrar()