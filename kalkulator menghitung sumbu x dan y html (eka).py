<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Hitung Sumbu X dan Y - Kuadrat</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0;
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #83a4d4, #b6fbff);
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }
    .container {
      background: white;
      padding: 30px 25px;
      border-radius: 15px;
      box-shadow: 0 8px 20px rgba(0,0,0,0.1);
      max-width: 420px;
      width: 100%;
    }
    h2 {
      text-align: center;
      color: #2c3e50;
      margin-bottom: 10px;
    }
    p {
      text-align: center;
      color: #555;
      margin-bottom: 20px;
    }
    label {
      font-weight: 600;
      display: block;
      margin-top: 12px;
    }
    input[type="number"] {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border-radius: 8px;
      border: 1px solid #ccc;
      font-size: 15px;
      transition: 0.3s;
    }
    input[type="number"]:focus {
      border-color: #007bff;
      outline: none;
    }
    button {
      margin-top: 20px;
      width: 100%;
      padding: 12px;
      font-size: 16px;
      border: none;
      background: #007bff;
      color: white;
      font-weight: bold;
      border-radius: 8px;
      cursor: pointer;
      transition: 0.3s;
    }
    button:hover {
      background-color: #0056b3;
    }
    #output {
      margin-top: 25px;
      padding: 20px;
      border-radius: 12px;
      background-color: #f1f9ff;
      border-left: 6px solid #007bff;
      font-size: 15px;
      animation: fadeIn 0.5s ease-in-out;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .icon {
      font-size: 20px;
      margin-right: 6px;
      color: #007bff;
    }
  </style>
</head>
<body>

  <div class="container">
    <h2>🎯 Hitung Sumbu X & Y</h2>
    <p>Bentuk umum: <strong>y = ax² + bx + c</strong></p>

    <label for="a">Nilai a:</label>
    <input type="number" id="a" step="any" placeholder="Contoh: 1" oninput="resetOutput()">

    <label for="b">Nilai b:</label>
    <input type="number" id="b" step="any" placeholder="Contoh: -3" oninput="resetOutput()">

    <label for="c">Nilai c:</label>
    <input type="number" id="c" step="any" placeholder="Contoh: 2" oninput="resetOutput()">

    <button onclick="hitung()">Hitung Sekarang</button>

    <div id="output"></div>
  </div>

  <script>
    function resetOutput() {
      document.getElementById("output").innerHTML = "";
    }

    function hitung() {
      const a = parseFloat(document.getElementById("a").value);
      const b = parseFloat(document.getElementById("b").value);
      const c = parseFloat(document.getElementById("c").value);
      const output = document.getElementById("output");

      if (isNaN(a) || isNaN(b) || isNaN(c)) {
        output.innerHTML = "<span style='color: red;'>⚠️ Harap masukkan semua nilai dengan benar.</span>";
        return;
      }

      if (a === 0) {
        output.innerHTML = "<span style='color: red;'>⚠️ Nilai a tidak boleh 0 untuk persamaan kuadrat.</span>";
        return;
      }

      const D = b * b - 4 * a * c;
      let sumbuX;

      if (D > 0) {
        const x1 = (-b + Math.sqrt(D)) / (2 * a);
        const x2 = (-b - Math.sqrt(D)) / (2 * a);
        sumbuX = `📌 Dua akar real:<br>x₁ = ${x1.toFixed(3)}<br>x₂ = ${x2.toFixed(3)}`;
      } else if (D === 0) {
        const x = -b / (2 * a);
        sumbuX = `📌 Akar kembar:<br>x = ${x.toFixed(3)}`;
      } else {
        sumbuX = "📌 Tidak punya akar real (akar imajiner)";
      }

      const sumbuY = c.toFixed(3);

      output.innerHTML = `
        <div><span class="icon">🧮</span><strong>Sumbu X:</strong><br>${sumbuX}</div><br>
        <div><span class="icon">🎯</span><strong>Sumbu Y:</strong> y = ${sumbuY}</div>
      `;
    }
  </script>

</body>
</html>
