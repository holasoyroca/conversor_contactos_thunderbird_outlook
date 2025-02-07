#!/usr/bin/env python3
# Instalar Flask si no está instalado:
# pip install flask

from flask import Flask, request, send_file, render_template_string
import csv
import io

app = Flask(__name__)

mapping = {
	"Nombre": "First Name",
	"Apellidos": "Last Name",
	"Nombre mostrado": "Title",
	"Apodo": "Nickname",
	"Dirección de correo electrónico principal": "E-mail Address",
	"Dirección de correo electrónico secundaria": "E-mail 2 Address",
	"Teléfono (Trabajo)": "Business Phone",
	"Fax": "Business Phone 2",
	"Teléfono móvil": "Mobile Phone",
	"Dirección personal": "Home Street",
	"Ciudad donde vive": "Home City",
	"Provincia": "Home State",
	"Código postal": "Home Postal Code",
	"País de residencia": "Home Country/Region",
	"Dirección de trabajo": "Business Street",
	"Dirección de trabajo 2": "Other Street",
	"Ciudad (Trabajo)": "Business City",
	"Provincia (Trabajo)": "Business State",
	"Código postal (Trabajo)": "Business Postal Code",
	"País (Trabajo)": "Business Country/Region",
	"Puesto": "Job Title",
	"Organización": "Company",
	"Página web 1": "Web Page",
	"Año de nacimiento": "Birthday",
	"Notas": "Notes"
}

html_form = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Conversor Thunderbird a Outlook</title>
</head>
<body>
    <h1>Sube tu CSV de Thunderbird</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="csv_file" accept=".csv" required>
        <button type="submit">Convertir</button>
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('csv_file')
        if file:
            data = file.read().decode('utf-8', errors='replace')
            input_csv = io.StringIO(data)
            reader = csv.DictReader(input_csv)
            
            output_buffer = io.StringIO()
            new_fieldnames = [mapping.get(field, field) for field in reader.fieldnames]
            writer = csv.DictWriter(output_buffer, fieldnames=new_fieldnames)
            writer.writeheader()
            
            for row in reader:
                new_row = {}
                for old_field, value in row.items():
                    new_row[mapping.get(old_field, old_field)] = value
                writer.writerow(new_row)
            
            output_buffer.seek(0)
            return send_file(
                io.BytesIO(output_buffer.getvalue().encode('utf-8')),
                mimetype='text/csv',
                as_attachment=True,
                download_name='contactos_outlook.csv'
            )
    return render_template_string(html_form)

# Para ejecutar con flask:
# export FLASK_APP=este_script.py
# flask run --host=0.0.0.0 --port=5000
#
# Luego configurar Apache para servir la aplicación Flask vía mod_wsgi o similar.
