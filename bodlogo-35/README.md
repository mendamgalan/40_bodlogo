<a href="https://www.hackerrank.com/challenges/and-product/problem?isFullScreen=true">Бодлога харах link</a>
🔩 Бодлогын нэр: AND Үржвэр (AND Product)
📘 Бодлогын тайлбар:
Танд A болон B гэсэн хоёр бүхэл тоо өгөгдсөн байна.

Та дараах утгыг ол:
A & (A+1) & (A+2) & ... & B
Энд & нь битийн AND үйлдэл юм.

🎯 Зорилго:
A-аас B хүртэлх бүх тооны битийн AND нийлбэрийг (бүгдийг AND хийсэн хариу) ол.

⛳ Оролт:
Эхний мөр: бүхэл тоо T — тестийн тоо (1 ≤ T ≤ 100)

Дараагийн T мөр бүр:

Хоёр бүхэл тоо A ба B (0 ≤ A ≤ B ≤ 2³² - 1)

📤 Гаралт:
Тест бүрийн хариуг нэг мөрөнд хэвлэнэ — A & (A+1) & ... & B гэсэн хариу.

💡 Санаа:
Хэрвээ A болон B-ийн битийн дүрслэл-д зөрүү гарвал, AND хийх үед 0 болж эхэлнэ.

Тиймээс зөвхөн A ба B-ийн хамгийн зүүн талаас ижил битүүдийг хадгалж үлдэнэ.

🔍 Жишээ:
Оролт:
2
12 15
2 3

Гаралт:
12
2
Тайлбар:

12 = 1100, 13 = 1101, 14 = 1110, 15 = 1111
→ 1100 & 1101 & 1110 & 1111 = 1100 → хариу: 12

2 = 10, 3 = 11
→ 10 & 11 = 10 → хариу: 2

✅ Хурдан арга:
A болон B-ийг 2-тын (binary) хэлбэрээр харьцуулж, хамгийн зүүн талаас яг ижил хэсгийг хадгалж, бусдыг 0 болгоно.


![40 bodlogo 35](https://github.com/user-attachments/assets/6fb668ad-fb1c-479c-9bb4-3d4ccaac6ef1)
