<a href="https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true">Бодлога харах link</a>

💣 Бодлогын нэр: Бомбермэн тоглоом (The Bomberman Game)
🕹️ Бодлогын тайлбар:
"Бомбермэн" тоглоом дараах дүрмүүдтэйгээр ажилладаг:

Эхлэлд (0 секундэд): Тоглоом эхлэхэд дэлгэцэн дээр хэд хэдэн тэсрэх бөмбөг байрласан байна.

Бүх бөмбөг 3 секунд тутамд тэсэрнэ.

1 болон 2 секундэд:

1 секунд: юу ч болохгүй.

2 секунд: Бомбермэн бүх хоосон эсүүдэд шинэ бөмбөг тавина.

3 секунд болоход: эхэнд байсан бөмбөгнүүд тэсэрнэ:

Тэсрэх бөмбөг өөрийн байрлал + дээш/доош/баруун/зүүн талын эсүүдийг устгана.

Тэсэрсэн бөмбөгүүд болон тэдгээртэй залгаа бөмбөгнүүд хамтаар устдаг.

4-р секундэд: бүх хоосон эсүүдэд дахин бөмбөг тавигдана.

5-р секундэд: өмнөх (2-р сек) үеийн бөмбөгнүүд тэсэрнэ, гэх мэт...

🎯 Таны зорилго:
R x C хэмжээтэй эхний төлөвтэй тоглоом өгөгдөнө.

n секундийн дараах тоглоомын дэлгэцийн байдлыг гаргаж үзүүл.

🔢 Оролт:
Эхний мөр: гурван бүхэл тоо R, C, n

R — мөрийн тоо (1 ≤ R ≤ 200)

C — баганын тоо (1 ≤ C ≤ 200)

n — хэдэн секунд өнгөрөхийг хүсэж байгаа тоо

Дараагийн R мөр бүрт: C ширхэг тэмдэгт бүхий мөр

'.' — хоосон эс

'O' — бөмбөгтэй эс

📤 Гаралт:
n секундийн дараах дэлгэцийн төлөвийг R мөрөөр хэвлэнэ.

💡 Санаа:
Нэгж бөмбөг яг 3 секундийн дараа тэсэрнэ.

2 секунд тутамд бөмбөг тавигддаг (хоосон бүх эсүүдэд).

Цаг хугацааны явц дахь тоглоомын төлөв давтагддаг!

n = 1 → анхны төлөв

n % 2 == 0 → бүхэлд нь бөмбөгөөр дүүрэн дэлгэц

n % 4 == 3 → эхний тэсрэлт хийсний дараах төлөв

n % 4 == 1 ба n > 1 → хоёр дахь тэсрэлт хийсний дараах төлөв

🧠 Жишээ:
Оролт:
6 7 3
.......
...O...
....O..
.......
OO.....
OO.....

Гаралт:
OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO


![40 bodlogo 13](https://github.com/user-attachments/assets/12d96b6e-1db9-4808-9712-fffaf31fbff2)
