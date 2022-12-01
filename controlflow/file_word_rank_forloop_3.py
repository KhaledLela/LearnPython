# py4e.com
# File words rank...
# نطلب من المستخدم إدخال اسم الملف او المسار
# عدة سطور
# البرنامج يقرأ سطر بسطر
# نقرأ كلمة بكلمة من كل سطر
# مخزن عبارة عن فهرس
# كل كلمة - مقابل عدد مرات التكرار
# من خلال الفهرس نبحث على اكثر الكلمات تكرارا
# وعدد مرات تكررها
TEXT_IO = open(filename, 'r')

filename = input('Please enter file name/path:\n') # أدخل اسم الملف او المسار
lines = TEXT_IO  # r = read  للقراءة  & w = write للكتابة

w_counts = dict() # الفهرس بتاع التكرار
for line in lines: # تكرار على السطور داخل الملف
    words = line.split() # كل سطر بقوم بتحويلة لكلمات
    for word in words:
        w_counts[word] = w_counts.get(word, 0) + 1

print(w_counts)

bw = None # اكثر كلمة تكررا
bc = None # اكبر عدد تكرار

for word, count in list(w_counts.items()):
    if bc is None or bc < count:
        bc = count
        bw = word

print(bw,bc)
