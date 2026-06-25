import subprocess
import sys

# Проверим, установлена ли библиотека qrcode
try:
    import qrcode
except ImportError:
    print("Устанавливаем qrcode...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode[pil]", "-q"])
    import qrcode

# Создаём QR-код с контактной информацией
contact_info = "BEGIN:VCARD\nVERSION:3.0\nFN:Белекбаев Даниел\nEMAIL:dan4ik0014@gmail.com\nTEL:+996506013001\nEND:VCARD"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data(contact_info)
qr.make(fit=True)

# Создаём изображение с белым фоном и чёрными квадратами
img = qr.make_image(fill_color="black", back_color="white")

# Сохраняем QR-код
img.save("qr.png")
print("✓ QR-код успешно создан и сохранён как qr.png")
