import csv
from fpdf import FPDF

# CSV file name
csv_filename = 'data.csv'

# Function to add new employee data
def add_employee(name, age, department):
    with open(csv_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, department])
    print(f"Added: {name}, {age}, {department}")

# Add new employees (You can take input dynamically)
add_employee("Michael Johnson", 40, "Marketing")
add_employee("Emma Wilson", 25, "Sales")
add_employee("Chris Evans", 45, "Operations")

# Read data from the CSV file
data = []
with open(csv_filename, newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        data.append(row)

# Create a PDF document
pdf = FPDF()
pdf.add_page()

# Set title
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Employee Report", ln=True, align='C')

# Set font for data
pdf.set_font('Arial', '', 12)

# Write data to PDF
for row in data:
    name, age, department = row
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}, Age: {age}, Department: {department}")

# Output PDF file
pdf.output('employee_report.pdf')

print("Report generated successfully: employee_report.pdf")
