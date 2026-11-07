#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Bahane Jeneratörü
Dünyanın en tembel ama en yaratıcı asistanı.
Kullanım: python bahane_uretec.py
"""

import random
import time

bahaneler = [
    "Bugün güneş biraz fazla parlak, gözlerim kamaştı, kod yazamadım.",
    "Kedi klavyemin üstüne oturdu ve 'commit' butonuna bastı, her şey ters gitti.",
    "Çay demlenirken düşündüm, sonra çay bitti, düşünce de bitti.",
    "WiFi şifresini unuttum, sonra şifreyi hatırladım ama motivasyonumu unuttum.",
    "Saat 15:00'te 'bir çay daha' dedim, şimdi 15:00 oldu ama farklı bir 15:00.",
    "Bilgisayar ısındı, ben de ısındım, ikimiz de dinlenmeye çekildik.",
    "GitHub Copilot bana 'sen dinlen' dedi, ona güvendim.",
    "Bugün kod yazarsam yarın daha az yazacağım için bugün yazmadım, uzun vadeli plan.",
    "Klavye tuşları yorulmuş, onlara da izin verdim.",
    "Projeyi bitirsem ne olacak ki, zaten bir sonraki projeye başlayacağım."
]

def bahane_uret():
    print("Bahane üretiliyor... lütfen bekleyin (çünkü acele işe şeytan karışır).")
    time.sleep(random.uniform(1.5, 3.5))  # Gerçekten yavaş olsun
    bahane = random.choice(bahaneler)
    print(f"\n🎭 Bugünkü resmî bahane:\n{bahane}\n")
    print("Bu bahane bilimsel olarak doğrulanmıştır. İş yapmama hakkınız saklıdır.")

if __name__ == "__main__":
    print("=== Abartılı Bahane Jeneratörü v1.0 ===")
    print("Herhangi bir şey yapmamak için hazır.")
    bahane_uret()
    input("\nÇıkmak için Enter'a basın (ama basmak zorunda değilsiniz)...")

# Gizli not: bazen en büyük devrimler en küçük tembelliklerden doğar. 👑
