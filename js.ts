const shapeSelector = document.getElementById("shape");
const inputFields = document.getElementById("inputFields");
const hasilDiv = document.getElementById("hasil");
const riwayatList = document.getElementById("riwayat");

let riwayat = [];

const fields = {
  persegi: ["Sisi"],
  persegiPanjang: ["Panjang", "Lebar"],
  segitiga: ["Alas", "Tinggi", "Sisi A", "Sisi B", "Sisi C"],
  lingkaran: ["Jari-jari"],
  jajarGenjang: ["Alas", "Tinggi", "Sisi Miring"],
  belahKetupat: ["Diagonal 1", "Diagonal 2", "Sisi"]
};

// Perbarui field input saat pilihan bentuk berubah
shapeSelector.addEventListener("change", function () {
  const shape = this.value;
  inputFields.innerHTML = "";
  hasilDiv.innerHTML = "";

  if (fields[shape]) {
    fields[shape].forEach(label => {
      const id = label.toLowerCase().replace(/\s/g, '');
      inputFields.innerHTML += `
        <label>${label} (cm):</label>
        <input type="number" min="0" step="any" id="${id}" required />
      `;
    });
  }
});

// Fungsi hitung luas dan keliling
function hitung() {
  const shape = shapeSelector.value;
  const getVal = id => {
    const val = parseFloat(document.getElementById(id)?.value);
    return isNaN(val) ? null : val;
  };

  let luas = 0, keliling = 0;

  try {
    switch (shape) {
      case "persegi":
        const sisi = getVal("sisi");
        if (!sisi || sisi <= 0) throw "Input tidak valid";
        luas = sisi * sisi;
        keliling = 4 * sisi;
        break;

      case "persegiPanjang":
        const panjang = getVal("panjang");
        const lebar = getVal("lebar");
        if (!panjang || !lebar || panjang <= 0 || lebar <= 0) throw "Input tidak valid";
        luas = panjang * lebar;
        keliling = 2 * (panjang + lebar);
        break;

      case "segitiga":
        const alas = getVal("alas");
        const tinggi = getVal("tinggi");
        const a = getVal("sisia");
        const b = getVal("sisib");
        const c = getVal("sisic");
        if ([alas, tinggi, a, b, c].some(v => !v || v <= 0)) throw "Input tidak valid";
        luas = 0.5 * alas * tinggi;
        keliling = a + b + c;
        break;

      case "lingkaran":
        const r = getVal("jarijari");
        if (!r || r <= 0) throw "Input tidak valid";
        luas = Math.PI * r * r;
        keliling = 2 * Math.PI * r;
        break;

      case "jajarGenjang":
        const ajg = getVal("alas");
        const tjg = getVal("tinggi");
        const sisiMiring = getVal("sisimiring");
        if ([ajg, tjg, sisiMiring].some(v => !v || v <= 0)) throw "Input tidak valid";
        luas = ajg * tjg;
        keliling = 2 * (ajg + sisiMiring);
        break;

      case "belahKetupat":
        const d1 = getVal("diagonal1");
        const d2 = getVal("diagonal2");
        const sisiBK = getVal("sisi");
        if ([d1, d2, sisiBK].some(v => !v || v <= 0)) throw "Input tidak valid";
        luas = 0.5 * d1 * d2;
        keliling = 4 * sisiBK;
        break;

      default:
        hasilDiv.innerHTML = "Silakan pilih bangun datar.";
        return;
    }

    const teksHasil = `Luas: ${luas.toFixed(2)} cm², Keliling: ${keliling.toFixed(2)} cm`;
    hasilDiv.innerHTML = teksHasil;
    riwayat.push(`${capitalize(shape)} - ${teksHasil}`);
    updateRiwayat();

  } catch (err) {
    hasilDiv.innerHTML = `❌ ${err}`;
  }
}

function updateRiwayat() {
  riwayatList.innerHTML = "";
  riwayat.forEach((item, index) => {
    const li = document.createElement("li");
    li.textContent = `${index + 1}. ${item}`;
    riwayatList.appendChild(li);
  });
}

function capitalize(text) {
  return text.charAt(0).toUpperCase() + text.slice(1);
}
