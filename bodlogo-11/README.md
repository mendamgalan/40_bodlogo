<a href="https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true">Бодлога харах link</a>
📦 Бодлогын нэр: 3D Гадаргуун талбай (3D Surface Area)
🧮 Бодлогын тайлбар:
Танд H x W хэмжээтэй 2D матриц A өгөгдсөн бөгөөд энэ нь 3D хэлбэрийн шоо (куб)-уудаар бүтсэн барилгын загварыг төлөөлнө.

A[i][j] нь i-р мөр, j-р баганад хэдэн куб давхарлаж байрласан болохыг заана.

Нэг кубын хэмжээ 1x1x1 гэж үзнэ.

Таны зорилго бол энэ бүтцийн нийт гадаргуун талбайг (surface area) тооцоолох юм.

🏗️ Гадаргуун талбайд дараах зүйлс хамаарна:
Дээд тал – үргэлж харагдана (1 давхар л байсан ч).

Доод тал – мөн адил.

Хананууд – хэрвээ тухайн хананы цаана ямар ч куб байхгүй бол бүрэн харагдана.

Зэргэлдээ байгаа кубуудын өндөр нь одоо байгаа кубын өндрөөс бага байвал илүү гарсан хэсэг харагдана.

Эсрэгээр, зэргэлдээ өндөр нь их байвал тэр талаас юу ч харагдахгүй.

🖼️ Жишээ:
A = [
  [1, 3, 4],
  [2, 2, 3],
  [1, 2, 4]
]
Энд 3x3 матриц байна. Матрицийн утга бүрт хэдэн куб давхарсан байгааг зааж өгсөн.

🧾 Оролт:
Эхний мөр: бүхэл тоо H ба W — матрицийн хэмжээ

Дараагийн H мөр бүрт: W ширхэг бүхэл тоо, тус бүр нь 1 ≤ A[i][j] ≤ 100

📤 Гаралт:
Нийт 3D бүтцийн гадаргуун талбай (бүх талаас харагдах нээлттэй талбайн нэгжүүдийн нийлбэр)

💡 Санаа:
Нийт талбай =
→ (дээд тал) + (доод тал)
→ + зүүн, баруун, урд, хойд талууд дээр ил гарсан хэсгүүд

Дээд болон доод талбай: 2 × (H × W)

Хананы талуудыг дараах байдлаар тооцно:

Давхар бүрийн ирмэг, зэргэлдээ талын кубын өндөртэй харьцуулж ил гарсан өндөр ялгааг тооцно.

🧠 Жишээ тайлбар (үр дүн):
Input:
3 3
1 3 4
2 2 3
1 2 4

Output:
60

![40 bodlogo 11](https://github.com/user-attachments/assets/358a8a94-90a9-433a-b6d3-e3050efbb9ef)
