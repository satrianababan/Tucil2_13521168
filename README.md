# Tucil2_13521168
Tugas Kecil 2 Strategi Algoritma terkait penerapan strategi divide and conquer dalam menentukan jarak terdekat antara dua buah titik.
Algoritma Pencarian Titik Terdekat :
  1. Awalnya, program akan menerima masukan banyaknya titik dan dimensi yang akan dicari. Jika masukan valid, yaitu titik > 0 dan dimensi > 0, maka masukan titik tersebut akan di random menggunkaan prosedure random_points.
  2. Selanjutnya, masukan titik yang telah dirandom akan diurutkan menggunakan pendekatan Quick Sort, yaitu mengurutkan titik berdasarkan referensi posisinya pada sumbu X.
  3. Jika masukan titik hanya berjumlah 2 maka dapat langsung mengitung jaraknya dengan perhitungan euclidean.
  4. Jika jumlah masukannya 3, akan dicari jarak dari setiap pasangan titik dan kemudian dibandingkan dan ditentukan pasangan titik dengan jarak terdekat.
  5. Jika masukan titik lebih banyak (> 3), secara rekursif akan memilih elemen rata-rata pada titik X sebagai pivot dan membagi larik titik menjadi 2 bagian sama rata berdasarkan referensi pivot yang telah ditentukan. Lalu larik dibagi kembali dengan metode yang sama secara terus-menerus hingga hanya tersisa 2 atau 3 elemen.
  6. Masing-masing dari daerah bagian larik dicari jarak terkecilnya, kemudian dibandingkan dan diambil nilai minimum dari hasil perbandingan.
  7. Perbandingan ini terus dilakukan untuk setiap pembagian larik, hingga akhirnya didapat pasangan titik yang memiliki jarak terkecil sebagai hasil akhirnya.

# Requirement program
1. Python (direkomentasikan menggunkaan versi terbaru)
2. matplotlib
3. Beberapa library yang digunakan (random, time, numpy, math, platform)
4. Code writer
