#โปรเเกรมตัดเกรด(ตัวดําเนินการทางตรรกศาสตร์)

#input
score=int(input("ป้อนคะเเนนสอบของคุณ:"))
print("คะเเนนสอบของคุณ คือ",score)
gal=None #Noneคือค่าว่าง(อยู่ในระหว่างการคํานวน)

#process
if score>=80 and score<=100 : #มากกว่าเท่ากับ80 เเละ น้อยกว่าเท่ากับ100 ถ้าคะเเนนอยุ่ในช่วงนี้จะได้เกรด A
    gal="A"
elif score>=70 and score<=79 : #elif สามารถใช้ได้หลายรอบ
    gal="B"
elif score>=60 and score<=69 : #อย่าลืมตัว :
    gal="C"
elif score>=0 and score<=59 :
    gal="F"
else: #ถ้าเงื่อนไขข้างบนไม่เป็นจริงมันก้จะปริ้นเเทน 
    gal="N(ระบบผิดพลาด)"

#output
print("เกรดของคุณ คือ",gal) #ปริ้นเกรดอีกที
# python Project6.py