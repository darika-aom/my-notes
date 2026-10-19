#Match Statement
service=input("ป้อนหมายเลขบริการ(1-3):")
match service:
    case "1":print("ถอนเงิน") #if
    case "2":print("ฝากเงิน") #elif
    case "3":print("สอบถามยองคงเหลือ") #elif
    case "":print("หมายเลขบริการไม่ถูกต้อง") #else ถ้าไม่ใส่ข้อมูลมันก้จะทำหน้าที่รองรับทุกกรณีที่เหลือจากด้านบนทันที