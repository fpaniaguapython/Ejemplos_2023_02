#pip install reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("factura1.pdf", pagesize=A4)
c.setLineWidth(.3)
c.setFont('Helvetica',12)

c.drawString(100,800,"Mi empresa. S.L.U")
c.drawString(100,780,"C/San Miguel, 10")
c.drawString(100,760,"Alcorcón, Madrid")
c.line(100,740,500,740)
c.save()

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