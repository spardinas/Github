"""
#
# Este script crea un archivo 
#


"""

from email.mime import image

from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from markdown import markdown
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import PIL
import os
import sys


output = "C:\\Path\\to\\plan_de_seguridad_largo.pdf"
c = canvas.Canvas(output, pagesize=A4)

form = c.acroForm
for page_num in range(1, 4): 1 # Example: 5 pages
# Título
c.setFont("Helvetica-Bold", 18)
c.drawString(50, 800, "Mi plan de seguridad")

# Recordatorio
c.setFont("Helvetica-Bold", 14)
c.drawString(50, 780, "Recuerda:")
c.setFont("Helvetica",10)
c.drawString(50, 770, "siempre hay ayuda disponible")
c.setFont("Helvetica",10)
c.drawString(50, 760, "TLF de emergencias")
c.setFont("Helvetica-Bold",14)
c.drawString(50, 740, "112")
c.setFont("Helvetica",10)
c.drawString(50, 720, "Línea de atención a la conducta suicida")
c.setFont("Helvetica-Bold",14)
c.drawString(50, 700, "024")
c.drawImage("C:\\Path\\to\\phone.png", 200, 750 , width=25, height=25, mask='auto')
c.drawImage("C:\\Path\\to\\phone.png", 250, 720 , width=25, height=25, mask='auto')
# Set vertical line color and width
c.setStrokeColor(colors.red)  
c.setLineWidth(2)  # Thickness in points

# Draw a vertical line from (x, y_start) to (x, y_end)
x_position = 90  
y_start = 700            # points from bottom
y_end = 50     # points from bottom

c.line(x_position, y_start, x_position, y_end)

#Señales de alarma
c.setFont("Helvetica-Bold", 12)
c.drawString(100, 690, "Mis señales de alarma son:")
c.setFont("Helvetica", 10)
c.drawString(100, 680, "Disparadores: situaciones, pensamientos, emociones, imágenes, sensaciones…")
form.textfield(
    name='señales',
    x=100, y=650, width=300, height=30,
    borderStyle='inset', forceBorder=True,
    maxlen= 300,
    fieldFlags= 'multiline'
)

# Estrategias de afrontamiento
c.setFont("Helvetica-Bold", 12)
c.drawString(100, 630, "Mis estrategias de afrontamiento son:")
c.setFont("Helvetica", 10)
c.drawString(50, 620, "Cosas que puedo hacer para mejorar mi estado de ánimo cuando estoy yo solo y sin tener que recurrir a otras personas:")
form.textfield(
    name='estrategias',
    x=100, y=590, width=300, height=30,
    borderStyle='inset', forceBorder=True,
    maxlen= 300,
    fieldFlags= 'multiline'
)

# Personas, actividades y lugares que me ayudaran a distraerme en una crisis
c.setFont("Helvetica-Bold", 12)
c.drawString(100, 570, "Personas, actividades y lugares que me ayudaran a distraerme en una crisis")
c.setFont("Helvetica", 10)
c.drawString(100, 560, "¿A quién puedo recurrir para distraerme? ¿A dónde puedo ir?")
form.textfield(
    name='distraerme1',
    x=100, y=530, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
c.drawImage("C:\\Path\\to\\smartphone.png", 250, 530 , width=20, height=20, mask='auto')
form.textfield(
    name='distraerme_telefono1',
    x=270, y=530, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
form.textfield(
    name='distraerme2',
    x=100, y=500, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
c.drawImage("C:\\Path\\to\\smartphone.png", 250, 500 , width=20, height=20, mask='auto')
form.textfield(
    name='distraerme_telefono2',
    x=270, y=500, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
form.textfield(
    name='distraerme3',
    x=100, y=470, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
c.drawImage("C:\\Path\\to\\smartphone.png", 250, 470 , width=20, height=20, mask='auto')
form.textfield(
    name='distraerme_telefono3',
    x=270, y=470, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)

# Personas a las que puedo pedir ayuda
c.setFont("Helvetica-Bold", 12)
c.drawString(100, 440, "Personas a las que puedo pedir ayuda:")
c.setFont("Helvetica", 10)
c.drawString(100, 430, "A amigos, a un familiar o a otra persona")
form.textfield(
    name='personas',
    x=100, y=400, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
c.drawImage("C:\\Path\\to\\smartphone.png", 250, 400 , width=20, height=20, mask='auto')
form.textfield(
    name='persona_telefono3',
    x=270, y=400, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
form.textfield(
    name='personas2',
    x=100, y=370, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
c.drawImage("C:\\Path\\to\\smartphone.png", 250, 370 , width=20, height=20, mask='auto')
form.textfield(
    name='persona_telefono2',
    x=270, y=370, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
form.textfield(
    name='personas3',
    x=100, y=340, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
c.drawImage("C:\\Path\\to\\smartphone.png", 250, 340 , width=20, height=20, mask='auto')
form.textfield(
    name='persona_telefono3',
    x=270, y=340, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)

# Profesionales a los que puedo pedir ayuda
c.setFont("Helvetica-Bold", 12)
c.drawString(100, 300, "Profesionales a los que puedo pedir ayuda:")
form.textfield(
    name='personas4',
    x=100, y=270, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
c.drawImage("C:\\Path\\to\\smartphone.png", 250, 270 , width=20, height=20, mask='auto')
form.textfield(
    name='persona_telefono3',
    x=270, y=270, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
form.textfield(
    name='personas5',
    x=100, y=240, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
c.drawImage("C:\\Path\\to\\smartphone.png", 250, 240 , width=20, height=20, mask='auto')
form.textfield(
    name='persona_telefono3',
    x=270, y=240, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
form.textfield(
    name='personas6',
    x=100, y=210, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)
c.drawImage("C:\\Path\\to\\smartphone.png", 250, 210 , width=20, height=20, mask='auto')
form.textfield(
    name='persona_telefono3',
    x=270, y=210, width=150, height=20,
    borderStyle='inset', forceBorder=True,
    maxlen= 300
)

# Pasos que puedo tomar para que mi entorno sea más seguro
c.setFont("Helvetica-Bold", 12)
c.drawString(100, 180, "Pasos que puedo tomar para que mi entorno sea más seguro.")
form.textfield(
    name='pasos1',
    x=100, y=150, width=300, height=30,
    borderStyle='inset', forceBorder=True,
    maxlen= 300,
    fieldFlags= 'multiline'
)
form.textfield(
    name='pasos2',
    x=100, y=120, width=300, height=30,
    borderStyle='inset', forceBorder=True,
    maxlen= 300,
    fieldFlags= 'multiline'
)
form.textfield(
    name='pasos3',
    x=100, y=90, width=300, height=30,
    borderStyle='inset', forceBorder=True,
    maxlen= 300,
    fieldFlags= 'multiline'
)

c.showPage()

with open(r"C:\\Path\\to\\alarma.md", encoding="utf-8") as f:
    texto = f.read()

y = 800

for linea in texto.splitlines():
    c.drawString(50, y, linea)
    y -= 15

    if y < 50:
        c.showPage()
        y = 800
    
    
c.showPage()

with open(r"C:\\Path\\to\\comunicacion.md", encoding="utf-8") as f:
    texto = f.read()

y = 800

for linea in texto.splitlines():
    c.drawString(50, y, linea)
    y -= 15

    if y < 50:
        c.showPage()
        y = 800
    
    
c.showPage()

with open(r"C:\\Path\\to\\mitos_a_desterrar.md", encoding="utf-8") as f:
    texto = f.read()

y = 800

for linea in texto.splitlines():
    c.drawString(50, y, linea)
    y -= 15

    if y < 50:
        c.showPage()
        y = 800
    
    
c.showPage()

c.save()

print("PDF creado:", output)
