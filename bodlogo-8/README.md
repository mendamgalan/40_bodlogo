<a href="https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true">Бодлога харах link</a>
🔤 Бодлогын нэр: Том нь илүү (Bigger is Greater)
Бодлогын тайлбар:
Танд нэгэн тэмдэгт мөр (string) өгөгдсөн. Та энгийн латин жижиг үсгүүд бүхий энэ тэмдэгт мөрөөс дараагийн үсгийн дараалалын хувьд том утгатай хувилбарыг олох ёстой.

Өөрөөр хэлбэл, үсгийн дарааллын хувьд өгөгдсөн үгээс дараачийн хамгийн бага боломжит "том" үгийг олох хэрэгтэй.

Хэрвээ ийм хувилбар байхгүй бол "no answer" гэж хэвлэнэ.

Жишээ:
Оролт: ab
Гаралт: ba

Оролт: bb
Гаралт: no answer

Оролт: hefg
Гаралт: hegf

Оролт: dhck
Гаралт: dhkc
Оролт:
Эхний мөр: бүхэл тоо T — шалгах үгсийн тоо

Дараагийн T мөр бүр: нэг тэмдэгт мөр (w)

Гаралт:
Үр дүн болгон:

Хэрэв w-ийн дараачийн "том" хувилбар байвал тэр үгийг хэвлэнэ.

Үгүй бол "no answer" гэж хэвлэнэ.

Санаа:
Энэ бодлого нь "дараачийн permutation" бодлого юм. Алгоритм дараах байдлаар ажиллана:

Үсгүүдийн баруун талаас эхлэн өсөхгүй дарааллыг хайж олно.

Түүнийг задалж, дараагийн том үсэгтэй солих байрлалыг олоод:

Хойш байгаа бүх үсгийг жижигээс том дарааллаар эрэмжилнэ.
![40 bodlogo 8](https://github.com/user-attachments/assets/3d8fa2df-ca1a-40ca-996d-c9a90d675df0)
