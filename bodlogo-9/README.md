<a href="https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true">Бодлога харах link</a>
🕰️ Бодлогын нэр: Цагийг үгээр илэрхийлэх (The Time in Words)
Бодлогын тайлбар:
Танд 12 цагийн форматтай цагийн мэдээлэл өгөгдөнө: h (цаг), m (минут).

Таны зорилго бол энэ цагийг үгээр (англи хэл дээр) илэрхийлэх юм.

Жишээ:
Оролт: h = 5, m = 0
Гаралт: five o' clock

Оролт: h = 5, m = 1
Гаралт: one minute past five

Оролт: h = 5, m = 10
Гаралт: ten minutes past five

Оролт: h = 5, m = 15
Гаралт: quarter past five

Оролт: h = 5, m = 30
Гаралт: half past five

Оролт: h = 5, m = 40
Гаралт: twenty minutes to six

Оролт: h = 5, m = 45
Гаралт: quarter to six
Оролт:
Хоёр бүхэл тоо:

h — цаг (1 ≤ h ≤ 12)

m — минут (0 ≤ m < 60)

Гаралт:
h цаг m минут гэсэн хугацааг англи үгээр илэрхийлж, нэг мөрөнд хэвлэнэ.

Тайлбар:
Хэрвээ минут = 0 бол:

→ "five o' clock" гэх мэт

Хэрвээ минут ≤ 30 бол:

→ "X minutes past h"

Хэрвээ минут > 30 бол:

→ "Y minutes to h+1" (60 - m = Y минут дараагийн цаг хүртэл)

Тусгай тохиолдлууд:

15 минут → quarter

30 минут → half

1 минут → minute (нэг тоон дээр minute гэж ганцаар бичнэ, бусад тоонд minutes)
![Alt text](\images\40 bodlogo 9.png)