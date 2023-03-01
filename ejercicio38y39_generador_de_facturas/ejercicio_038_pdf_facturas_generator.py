#pip install reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
#Para abrir un programa desde Python
#import os;
#import del cargador de datos de factura
from ejercicio_039_cargador_datos_facturas import get_invoice_data

def create_canvas(file_name, page_size):
    nuevo_canvas = canvas.Canvas(file_name + ".pdf", pagesize=page_size)
    return nuevo_canvas


def set_font(canvas, font_family, font_size):
    canvas.setFont(font_family, font_size)


def draw_line(canvas, line_with, x0, y0, x1, y1):
    canvas.setLineWidth(line_with)
    canvas.line(x0,y0,x1,y1)


def generate_pdf(canvas):
    canvas.save()
    #Abre el programa lector de PDFs y carga el fichero que se acaba de almacenar
    #os.system("\"D:\Apps\Foxit Software\Foxit PDF Reader\FoxitPDFReader.exe\" " + canvas._filename)


def generate_company_header(canvas, supplier_data):
    set_font(canvas, "Helvetica-Bold", 14)
    canvas.drawString(100,760,supplier_data["nombre"])
    set_font(canvas, "Helvetica", 12)
    canvas.drawString(100,740,supplier_data["direccion"])
    canvas.drawString(100,720,supplier_data["email"])
    canvas.drawString(100,700,supplier_data["cif"])


def generate_client_header(canvas, client_data):
    x = 100
    y = 670
    set_font(canvas, "Helvetica-Bold", 14)
    canvas.drawString(x,y,"Facturar a:")
    set_font(canvas, "Helvetica", 12)
    for data in client_data.values():
        y-=20
        canvas.drawString(x, y, data)
    

def generate_invoice_data(canvas, items_list, tax):
    y=550
    x = 100
    offset = 125
    subtotal = 0
    total_tax = 0
    total = 0
    column_titles = ("Cant.","Descripción","Precio unitario", "Importe")
    set_font(canvas, "Helvetica-Bold", 14)
    for i in range(4):
        canvas.drawString(x+offset*i,y,column_titles[i])
    set_font(canvas, "Helvetica", 12)
    for item in items_list:
        y-=20
        name = item[0]
        unit_cost = item[1]
        units = item[2]
        subtotal=subtotal+(units*unit_cost)
        item_cost = unit_cost*units
        column_values = (name, unit_cost, units, item_cost)
        for i in range(4):
            canvas.drawString(x+offset*i,y,str(column_values[i]))
    
    total_tax = subtotal * tax
    total = subtotal + total_tax
    canvas.drawString(450,200,"Subtotal: "+str(subtotal))
    canvas.drawString(450,180,"IVA " +str(tax*100)+ "%:" +str(total_tax))
    canvas.drawString(450,160,"Total: "+str(total))


if __name__=="__main__":
    IVA = 0.12 #Impuesto
    #supplier_data = {"nombre":"Fernando Paniagua","direccion":"C/San Miguel, Alcorcón","email":"fernando.paniagua@gmail.com","cif":"B12345678"}
    #client_data = {"nombre":"Philips S.A.U.","direccion":"Hoyos del Espino","email":"philips@gmail.com","cif":"B87654321"}
    #items_list = [("Pan",15,1.5),("Leche",10,1.75),("Cerveza Sin Alcohol",5,0.60)]

    invoices_data = get_invoice_data()

    for invoice_data in invoices_data:
        canvas_factura = create_canvas(invoice_data[1]["cif"], A4)
        set_font(canvas_factura, 'Helvetica', 12)
        generate_company_header(canvas_factura, invoice_data[0])
        generate_client_header(canvas_factura, invoice_data[1])
        generate_invoice_data(canvas_factura, invoice_data[2], IVA)
        generate_pdf(canvas_factura)


"""
Crear un generador de facturas. El nombre del fichero PDF será el CIF del cliente.
Los datos de las facturas son:
Datos del emisor:
Nombre empresa
Dirección postal
CIF

Datos del cliente:
Nombre cliente
CIF

Datos de productos:
Nombre
Número de unidades
Precio unitario

Datos de impuestos:
Porcentaje de IVA
"""