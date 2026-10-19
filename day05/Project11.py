pu="root"
with open("words.txt","r",encoding="utf-8") as file:
    for line in file:
        pp=line.strip()
        print("กําลังลองรหัส:",pp)  
        if pp==pu:
            print("เจาะระบบสําเร็จ รหัสผ่านคือ",pu)
            break
    else:
        print("ไม่พบรหัสผ่าน")