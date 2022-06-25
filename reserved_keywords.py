# الكلمات المحجوزة للغة ولا يمكن استخدمها كأسماء متغيرات
#
import keyword
kws = keyword.kwlist;
for i in range(len(kws)):
    print(str(i+1) + " -> " + kws[i])
