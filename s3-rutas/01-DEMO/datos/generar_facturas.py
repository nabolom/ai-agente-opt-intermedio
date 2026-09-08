from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

W, H = letter
OUT = "facturas"
os.makedirs(OUT, exist_ok=True)


# ---------- FACTURA 1 · ACME · formato limpio ----------
c = canvas.Canvas(f"{OUT}/factura_acme_2026-03-04.pdf", pagesize=letter)
y = H - 60

c.setFont("Helvetica-Bold", 20)
c.drawString(50, y, "ACME S.A. de C.V.")
c.setFont("Helvetica", 9)
c.drawString(50, y - 16, "RFC: ACM980312HB4")
c.drawString(50, y - 28, "Av. Insurgentes Sur 1234, Col. Del Valle, CDMX")

c.setFont("Helvetica-Bold", 12)
c.drawRightString(W - 50, y, "FACTURA")
c.setFont("Helvetica", 10)
c.drawRightString(W - 50, y - 16, "Folio: A-4471")
c.drawRightString(W - 50, y - 30, "Fecha: 04/03/2026")

y -= 60
c.line(50, y, W - 50, y)

y -= 25
c.setFont("Helvetica-Bold", 10)
c.drawString(50, y, "CLIENTE")
c.setFont("Helvetica", 10)
c.drawString(50, y - 14, "Grupo Meridiano S.A. de C.V.")

y -= 45
c.setFont("Helvetica-Bold", 9)
c.drawString(50, y, "CANT.")
c.drawString(100, y, "DESCRIPCION")
c.drawRightString(430, y, "P. UNITARIO")
c.drawRightString(W - 50, y, "IMPORTE")
c.line(50, y - 6, W - 50, y - 6)

y -= 24
c.setFont("Helvetica", 10)
c.drawString(50, y, "1")
c.drawString(100, y, "Servicio de mantenimiento preventivo")
c.drawRightString(430, y, "$10,732.76")
c.drawRightString(W - 50, y, "$10,732.76")

y -= 45
c.setFont("Helvetica", 10)
c.drawRightString(450, y, "Subtotal:")
c.drawRightString(W - 50, y, "$10,732.76")
y -= 16
c.drawRightString(450, y, "IVA 16%:")
c.drawRightString(W - 50, y, "$1,717.24")
y -= 22
c.setFont("Helvetica-Bold", 12)
c.drawRightString(450, y, "TOTAL:")
c.drawRightString(W - 50, y, "$12,450.00")

c.setFont("Helvetica", 8)
c.drawString(50, 60, "Metodo de pago: Transferencia electronica  ·  Forma de pago: PUE")
c.save()


# ---------- FACTURA 2 · TECNOGLOBAL · formato distinto ----------
c = canvas.Canvas(f"{OUT}/factura_tecnoglobal_2026-03-11.pdf", pagesize=letter)

c.setFillColorRGB(0.15, 0.15, 0.35)
c.rect(0, H - 90, W, 90, fill=1, stroke=0)
c.setFillColorRGB(1, 1, 1)
c.setFont("Helvetica-Bold", 22)
c.drawString(50, H - 50, "TecnoGlobal")
c.setFont("Helvetica", 9)
c.drawString(50, H - 68, "Soluciones Integrales de Tecnologia  |  RFC: TGL110725QX2")
c.setFillColorRGB(0, 0, 0)

y = H - 125
c.setFont("Helvetica", 9)
c.drawString(50, y, "Comprobante Fiscal Digital")
c.drawString(50, y - 13, "Serie TG   Folio 20268")
c.drawString(50, y - 26, "Expedido el 11 de marzo de 2026")

c.drawRightString(W - 50, y, "Receptor: Grupo Meridiano S.A. de C.V.")
c.drawRightString(W - 50, y - 13, "Uso CFDI: G03 Gastos en general")

y -= 55
c.setFont("Helvetica-Bold", 9)
c.drawString(50, y, "CONCEPTOS")
c.line(50, y - 5, W - 50, y - 5)

y -= 22
c.setFont("Helvetica", 9)
c.drawString(50, y, "Licencia anual software de gestion documental (5 usuarios)")
c.drawRightString(W - 50, y, "6,500.00")
y -= 15
c.drawString(50, y, "Soporte tecnico remoto - marzo 2026")
c.drawRightString(W - 50, y, "1,000.00")

y -= 35
c.setFont("Helvetica", 9)
c.drawRightString(470, y, "Importe:")
c.drawRightString(W - 50, y, "7,500.00")
y -= 14
c.drawRightString(470, y, "Impuestos trasladados:")
c.drawRightString(W - 50, y, "1,200.00")
y -= 20
c.setFont("Helvetica-Bold", 11)
c.drawRightString(470, y, "Importe total:")
c.drawRightString(W - 50, y, "8,700.00")
c.setFont("Helvetica", 8)
c.drawRightString(W - 50, y - 14, "(Ocho mil setecientos pesos 00/100 M.N.)")

c.setFont("Helvetica", 7)
c.drawString(50, 55, "Este documento es una representacion impresa de un CFDI")
c.save()


# ---------- FACTURA 3 · LA RARA · alias en el pie, total ambiguo ----------
c = canvas.Canvas(f"{OUT}/factura_dea_2026-03-18.pdf", pagesize=letter)
y = H - 70

c.setFont("Helvetica-Bold", 26)
c.drawCentredString(W / 2, y, "D E A")
c.setFont("Helvetica-Oblique", 10)
c.drawCentredString(W / 2, y - 18, "Suministro de oficina y consumibles")

y -= 60
c.setFont("Helvetica", 10)
c.drawString(50, y, "NOTA DE VENTA   No. 00812")
c.drawRightString(W - 50, y, "18-03-26")

y -= 30
c.setFont("Helvetica", 9)
items = [
    ("Resma papel bond carta (caja c/10)", "2", "1,180.00"),
    ("Toner compatible HP 26A", "3", "2,340.00"),
    ("Carpetas archivo tamano oficio", "20", "760.00"),
    ("Plumas tinta gel negro (caja c/12)", "5", "425.00"),
]
for desc, cant, imp in items:
    c.drawString(50, y, desc)
    c.drawString(390, y, cant)
    c.drawRightString(W - 50, y, imp)
    y -= 15

y -= 20
c.line(330, y + 8, W - 50, y + 8)
c.setFont("Helvetica", 10)
c.drawString(340, y, "Suma")
c.drawRightString(W - 50, y, "4,705.00")
y -= 15
c.drawString(340, y, "Descuento cliente frecuente 5%")
c.drawRightString(W - 50, y, "235.25")
y -= 15
c.drawString(340, y, "Base")
c.drawRightString(W - 50, y, "4,469.75")
y -= 15
c.drawString(340, y, "I.V.A.")
c.drawRightString(W - 50, y, "715.16")
y -= 15
c.setFont("Helvetica-Bold", 10)
c.drawString(340, y, "A pagar")
c.drawRightString(W - 50, y, "5,184.91")

y -= 45
c.setFont("Helvetica", 9)
c.drawString(50, y, "Anticipo recibido 15-03-26 . . . . . . . . . . 2,000.00")
y -= 14
c.drawString(50, y, "Saldo pendiente . . . . . . . . . . . . . . . . . 3,184.91")

c.setFont("Helvetica", 7)
c.drawCentredString(W / 2, 70, "Distribuidora El Aguila S. de R.L. de C.V.   ·   RFC: DEA050914TT9")
c.drawCentredString(W / 2, 60, "Calz. de Tlalpan 890, Col. Portales, CDMX   ·   Tel. 55 5544 2211")
c.save()

print("Facturas generadas en", OUT)
