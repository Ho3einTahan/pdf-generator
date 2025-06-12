import pdfkit

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 20px;
    background-color: #f7f9fc;
    color: #333;
  }
  h2 {
    color: #2c3e50;
    text-align: center;
    margin-bottom: 30px;
  }
  table {
    width: 80%;
    margin: 0 auto 40px auto; /* وسط چین و فاصله پایین */
    border-collapse: collapse;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    background-color: #fff;
  }
  th, td {
    padding: 12px 15px;
    border: 1px solid #ddd;
    text-align: left;
  }
  th {
    background-color: #3498db;
    color: white;
    font-weight: 600;
  }
  tr:nth-child(even) {
    background-color: #f2f6fa;
  }
  p {
    margin-top: 20px;
    font-size: 14px;
    color: #555;
  }
</style>
</head>
<body>

<h2>Developed By Hosein Tahan</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Family</th>
      <th>National Code</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alfreds Futterkiste</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Germany</td>
    </tr>
    <tr>
      <td>Centro comercial Moctezuma</td>
      <td>Francisco Chang</td>
      <td>—</td>
      <td>Mexico</td>
    </tr>
  </tbody>
</table>

</body>
</html>
"""

pdfkit.from_string(html, 'out.pdf', configuration=config)