HARFLER = ["A", "B", "C", "D", "E", "F", "G", "H"]  # Tabloda kullanılacak harflerin listesi
SAYILAR = ["1", "2", "3", "4", "5", "6", "7"]  # Tabloda kullanılacak sayıların listesi
kareler_beyaz = []  # Tabloda oluşan beyaz kareleri tutan tablo
kareler_siyah = []  # Tabloda oluşan siyah kareleri tutan tablo
kordinat = {}  # Oyun tablosundaki verileri koordinat düzlemi şeklinde tutan sözlük


def oyun_baslat(yatay_cizgi):  # Koordinat düzleminde girilen yatay çizgiye göre sözlük oluşturan fonksiyon.
    for s in range(yatay_cizgi):
        for h in range(yatay_cizgi+1):
            kordinat[SAYILAR[s]+HARFLER[h]] = " "


def oyun_ciz(yatay_cizgi):  # 'kordinat' adlı sözlüğün içindekilere göre oyunun tahtasını çizen fonksiyon.
    sinir = 0

    print("  ", end='')
    for h in range(yatay_cizgi + 1):
        for harfler in HARFLER[h]:
            print(f"{harfler}   ", end='')
    print()
    for s in range(yatay_cizgi):
        cizgi = 0
        print(f"{s + 1} ", end='')
        for h in range(yatay_cizgi + 1):
            print(f"{kordinat[SAYILAR[s] + HARFLER[h]]}", end='')
            cizgi += 1
            if cizgi == (yatay_cizgi + 1):
                break
            print("---", end='')
        print(f" {s + 1}")
        print("  ", end='')
        sinir += 1
        if sinir == yatay_cizgi:
            break
        for l in range(yatay_cizgi + 1):
            print("|   ", end='')
        print()
    for h in range(yatay_cizgi + 1):
        for harfler in HARFLER[h]:
            print(f"{harfler}   ", end='')
    print()


def hamle_al(renk, yatay_cizgi):  # Kullanıcıdan taş yerleştirme için hamle alıp aldığı hamleyi kontrol eden fonksiyon.
    try:
        hamle = input(f"{renk} oyuncu, hamlenizi giriniz: ")
        hamle = hamle.upper()
        while kordinat[hamle] != " " or (hamle[:1] not in SAYILAR[:yatay_cizgi]) or (hamle[1:] not in HARFLER[:yatay_cizgi+1]):
            print("Hatalı işlem yaptınız!.9")
            hamle = input(f"{renk} oyuncu, hamlenizi giriniz: ")
            hamle = hamle.upper()
    except:
        print("Hatalı işlem yaptınız!.8")
        hamle = hamle_al(renk, yatay_cizgi)
    return hamle


def tas_al(yatay_cizgi):  # Taş alma işlemini döngüye sokan ve oyunculara göre hamle_al fonkiyonunu çağıran fonksiyon.
    siyah_tas = yatay_cizgi * (yatay_cizgi + 1) / 2
    beyaz_tas = yatay_cizgi * (yatay_cizgi + 1) / 2
    while siyah_tas != 0:
        beyaz_hamle = hamle_al("Beyaz", yatay_cizgi)
        kordinat[beyaz_hamle] = "B"
        beyaz_tas -= 1
        oyun_ciz(yatay_cizgi)
        siyah_hamle = hamle_al("Siyah", yatay_cizgi)
        kordinat[siyah_hamle] = "S"
        siyah_tas -= 1
        oyun_ciz(yatay_cizgi)


def kare_kontrol(yatay_cizgi):  # Oyun tahtasındaki tüm kareleri ve sayısını alan fonksiyon.
    kareler_beyaz.clear()
    kareler_siyah.clear()
    beyaz_kare_say = 0
    siyah_kare_say = 0
    for s in range(1, yatay_cizgi):
        for h in range(1, yatay_cizgi+1):
            konumlar = []
            if kordinat[SAYILAR[s] + HARFLER[h]] == "B" and kordinat[SAYILAR[s - 1] + HARFLER[h]] == "B" and \
                    kordinat[SAYILAR[s - 1] + HARFLER[h - 1]] == "B" and kordinat[SAYILAR[s] + HARFLER[h - 1]] == "B":
                konumlar.append(SAYILAR[s] + HARFLER[h])
                konumlar.append(SAYILAR[s - 1] + HARFLER[h])
                konumlar.append(SAYILAR[s - 1] + HARFLER[h - 1])
                konumlar.append(SAYILAR[s] + HARFLER[h - 1])
                kareler_beyaz.extend(konumlar)
                beyaz_kare_say += 1

            if kordinat[SAYILAR[s] + HARFLER[h]] == "S" and kordinat[SAYILAR[s - 1] + HARFLER[h]] == "S" and \
                    kordinat[SAYILAR[s - 1] + HARFLER[h - 1]] == "S" and kordinat[SAYILAR[s] + HARFLER[h - 1]] == "S":
                konumlar.append(SAYILAR[s] + HARFLER[h])
                konumlar.append(SAYILAR[s - 1] + HARFLER[h])
                konumlar.append(SAYILAR[s - 1] + HARFLER[h - 1])
                konumlar.append(SAYILAR[s] + HARFLER[h - 1])
                kareler_siyah.extend(konumlar)
                siyah_kare_say += 1


    return beyaz_kare_say, siyah_kare_say


def tas_cikar(hamle_sirasi):  # Oyuncuya göre taş çıkaran ve çıkarılacak taşın uygunluğunu kontrol eden fonksiyon.
    try:
        if hamle_sirasi in "Siyah":
            hamle = input("Siyah oyuncu, çıkarmak istediğiniz taşı giriniz: ").upper()

            while (hamle in kareler_beyaz) or kordinat[hamle] == "S" or kordinat[hamle] == " ":
                print("Hatalı işlem yaptınız!.10")
                hamle = input("Siyah oyuncu, çıkarmak istediğiniz taşı giriniz: ").upper()
            kordinat[hamle] = " "
        else:
            hamle = input("Beyaz oyuncu, çıkarmak istediğiniz taşı giriniz: ").upper()
            while (hamle in kareler_siyah) or kordinat[hamle] == "B" or kordinat[hamle] == " ":
                print("Hatalı işlem yaptınız!.7")
                hamle = input("Beyaz oyuncu, çıkarmak istediğiniz taşı giriniz: ").upper()
            kordinat[hamle] = " "
    except KeyError:
        print("Hatalı işlem yaptınız!.11")
        tas_cikar(hamle_sirasi)

# Taş yerleştirme aşaması tamamlandıktan sonra oyunun kalan yerlerini döngüye sokar ve oyunun kazananını belirler.
def oyuna_devam(beyaz_kare_say, siyah_kare_say, yatay_cizgi):
    siyah_tas_say = yatay_cizgi * (yatay_cizgi + 1) / 2
    beyaz_tas_say = yatay_cizgi * (yatay_cizgi + 1) / 2
    if beyaz_kare_say != 0 or siyah_kare_say != 0:
        for b in range(beyaz_kare_say):
            tas_cikar("Beyaz")
            siyah_tas_say -= 1
            oyun_ciz(yatay_cizgi)
        for s in range(siyah_kare_say):
            tas_cikar("Siyah")
            beyaz_tas_say -= 1
            oyun_ciz(yatay_cizgi)
    else:
        tas_cikar("Beyaz")
        siyah_tas_say -= 1
        oyun_ciz(yatay_cizgi)
    while siyah_tas_say > 3 and beyaz_tas_say > 3:
        hareket = tas_hareket("Beyaz", yatay_cizgi)
        kare_kontrol(yatay_cizgi)
        oyun_ciz(yatay_cizgi)
        if hareket:
            tas_cikar("Beyaz")
            siyah_tas_say -= 1
            oyun_ciz(yatay_cizgi)
        if siyah_tas_say < 4:
            break

        hareket = tas_hareket("Siyah", yatay_cizgi)
        kare_kontrol(yatay_cizgi)
        oyun_ciz(yatay_cizgi)
        if hareket:
            tas_cikar("Siyah")
            beyaz_tas_say -= 1
            oyun_ciz(yatay_cizgi)

    if siyah_tas_say < 4:
        print("Beyaz kazandı")
    else:
        print("Siyah kazandı")


def tas_hareket(renk, yatay_cizgi):  # Taş hareket ettirmenin uygunluğunu ve hareket ettirilen konumda kare oluşumunu kontrol eder.

    izin = False
    while not izin:
        hamle1, hamle2, hareket_sirasi, bekleme_sirasi = tas_hareket_al(renk)
        if hamle1[:1] != hamle2[:1] and hamle1[1:] == hamle2[1:]:  # sayılar farklı ise
            if int(hamle1[:1]) > int(hamle2[:1]):
                buyuk_hamle = hamle1[:1]
                kucuk_hamle = hamle2[:1]
            else:
                buyuk_hamle = hamle2[:1]
                kucuk_hamle = hamle1[:1]
            if (int(buyuk_hamle)-int(kucuk_hamle)) != 1:
                for kontrol in range(int(kucuk_hamle)+1, int(buyuk_hamle)):
                    if kordinat[str(kontrol)+hamle1[1:]] in ["S", "B"]:
                        print("Hatalı işlem yaptınız!.012")
                        break

                else:
                    kordinat[hamle1] = " "
                    kordinat[hamle2] = hareket_sirasi
                    izin = True
            else:
                kordinat[hamle1] = " "
                kordinat[hamle2] = hareket_sirasi
                izin = True
        elif hamle1[1:] != hamle2[1:] and hamle1[:1] == hamle2[:1]:  # harfler farklı ise
            harf1_index = HARFLER.index(hamle1[1:])
            harf2_index = HARFLER.index(hamle2[1:])
            if harf1_index > harf2_index:
                buyuk_index = harf1_index
                kucuk_index = harf2_index
            else:
                buyuk_index = harf2_index
                kucuk_index = harf1_index
            if (int(buyuk_index) - int(kucuk_index)) != 1:
                for kontrol in range(kucuk_index+1, buyuk_index):
                    if kordinat[hamle1[:1]+HARFLER[kontrol]] in ["S", "B"]:

                        print("Hatalı işlem yaptınız!.13")
                        break
                else:
                    kordinat[hamle1] = " "
                    kordinat[hamle2] = hareket_sirasi
                    izin = True

            else:
                kordinat[hamle1] = " "
                kordinat[hamle2] = hareket_sirasi

                izin = True
        else:
            hamle1, hamle2, hareket_sirasi, bekleme_sirasi = tas_hareket_al(renk)
    """
    Kare oluşumunun kontrol edildiği kısım.
    " .: "= Hareket ettirildiği konumun bir aşağısı sağı ve sağ aşağı çaprazını kontrol eder.
    " ': "= Hareket ettirildiği konumun bir yukarısı sağı ve sağ üst çaprazını kontrol eder.
    " :. "= Hareket ettirildiği konumun bir aşağısı solu ve sol alt çaprazını kontrol eder.
    " :' "= Hareket ettirildiği konumun bir yukarısı solu ve sol üst çaprazını kontrol eder.
    """
    kare = False
    if kordinat[hamle2] == hareket_sirasi:
        # Taşın hareket ettirildiği konum "A" sütununa göre etrafını kontrol eder
        if hamle2[1:] == "A" and hamle2[:1] != 1 and hamle2[:1] != SAYILAR[yatay_cizgi-1]:
            if int(hamle1[:1]) < int(hamle2[:1]):
                if kordinat[hamle2[:1]+HARFLER[(HARFLER.index(hamle2[1:]))+1]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1])+1)+hamle2[1:]] == hareket_sirasi and \
                        kordinat[str(int(hamle2[:1])+1)+HARFLER[(HARFLER.index(hamle2[1:]))+1]] == hareket_sirasi:  # .:
                    kare = True

            elif int(hamle1[:1]) > int(hamle2[:1]):
                if kordinat[hamle2[:1]+HARFLER[(HARFLER.index(hamle2[1:]))+1]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1])-1)+hamle2[1:]] == hareket_sirasi and\
                        kordinat[str(int(hamle2[:1])-1)+HARFLER[(HARFLER.index(hamle2[1:]))+1]] == hareket_sirasi:  # ':
                    kare = True
        # Taşın hareket ettirildiği konum tablodaki son harfe göre kontrol eder
        elif hamle2[1:] == HARFLER[yatay_cizgi] and hamle2[:1] != 1 and hamle2[:1] != SAYILAR[yatay_cizgi-1]:
            if int(hamle1[:1]) < int(hamle2[:1]):
                if kordinat[hamle2[:1]+HARFLER[(HARFLER.index(hamle2[1:]))-1]] == hareket_sirasi \
                    and kordinat[str(int(hamle2[:1])+1)+hamle2[1:]] == hareket_sirasi and \
                        kordinat[str(int(hamle2[:1])+1)+HARFLER[(HARFLER.index(hamle2[1:]))-1]] == hareket_sirasi:  # :.
                    kare = True

            elif int(hamle1[:1]) > int(hamle2[:1]):
                if kordinat[hamle2[:1]+HARFLER[(HARFLER.index(hamle2[1:]))-1]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1])-1)+hamle2[1:]] == hareket_sirasi and\
                        kordinat[str(int(hamle2[:1])-1)+HARFLER[(HARFLER.index(hamle2[1:]))-1]] == hareket_sirasi:  # :'
                    kare = True
        # Taşın hareket ettirildiği konum satır "1" e göre kontrol eder.
        elif hamle2[:1] == "1" and hamle2[1:] != "A" and hamle2[1:] != HARFLER[yatay_cizgi]:
            if hamle1[1:] < hamle2[1:]:
                if kordinat[hamle2[:1] + HARFLER[(HARFLER.index(hamle2[1:])) + 1]] == hareket_sirasi and \
                        kordinat[str(int(hamle2[:1]) + 1) + hamle2[1:]] == hareket_sirasi and \
                        kordinat[str(int(hamle2[:1]) + 1) + HARFLER[
                            (HARFLER.index(hamle2[1:])) + 1]] == hareket_sirasi:  # .:
                    kare = True
            elif hamle1[1:] > hamle2[1:]:
                if kordinat[hamle2[:1] + HARFLER[(HARFLER.index(hamle2[1:])) - 1]] == hareket_sirasi and \
                        kordinat[str(int(hamle2[:1]) + 1) + hamle2[1:]] == hareket_sirasi and \
                        kordinat[str(int(hamle2[:1]) + 1) + HARFLER[
                            (HARFLER.index(hamle2[1:])) - 1]] == hareket_sirasi:  # :.
                    kare = True
        # Taşın hareket ettirildiği konum tablodaki son satıra göre kontrol eder.
        elif hamle2[:1] == SAYILAR[yatay_cizgi-1] and hamle2[1:] != "A" and hamle2[1:] != HARFLER[yatay_cizgi]:
            if hamle1[1:] < hamle2[1:]:
                if kordinat[hamle2[:1] + HARFLER[(HARFLER.index(hamle2[1:])) + 1]] == hareket_sirasi and \
                        kordinat[str(int(hamle2[:1]) - 1) + hamle2[1:]] == hareket_sirasi and \
                        kordinat[str(int(hamle2[:1]) - 1) + HARFLER[
                            (HARFLER.index(hamle2[1:])) + 1]] == hareket_sirasi:  # ':
                    kare = True
            elif hamle1[1:] > hamle2[1:]:
                if kordinat[hamle2[:1] + HARFLER[(HARFLER.index(hamle2[1:])) - 1]] == hareket_sirasi and \
                        kordinat[str(int(hamle2[:1]) - 1) + hamle2[1:]] == hareket_sirasi and \
                        kordinat[str(int(hamle2[:1]) - 1) + HARFLER[
                            (HARFLER.index(hamle2[1:])) - 1]] == hareket_sirasi:  # :'
                    kare = True
        # Taşın hareket ettirildiği konumun kenarlarda olmadığı durumu kontrol eder
        elif hamle2 not in ["1A", '1'+HARFLER[yatay_cizgi], SAYILAR[yatay_cizgi-1]+'A', SAYILAR[yatay_cizgi-1]+HARFLER[yatay_cizgi]]:
            if kordinat[hamle2[:1] + HARFLER[(HARFLER.index(hamle2[1:])) + 1]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1]) + 1) + hamle2[1:]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1]) + 1) + HARFLER[(HARFLER.index(hamle2[1:])) + 1]] == hareket_sirasi:  # .:
                kare = True
            elif kordinat[hamle2[:1] + HARFLER[(HARFLER.index(hamle2[1:])) + 1]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1]) - 1) + hamle2[1:]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1]) - 1) + HARFLER[(HARFLER.index(hamle2[1:])) + 1]] == hareket_sirasi:  # ':
                kare = True
            elif kordinat[hamle2[:1] + HARFLER[(HARFLER.index(hamle2[1:])) - 1]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1]) + 1) + hamle2[1:]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1]) + 1) + HARFLER[(HARFLER.index(hamle2[1:])) - 1]] == hareket_sirasi:  # :.
                kare = True
            elif kordinat[hamle2[:1] + HARFLER[(HARFLER.index(hamle2[1:])) - 1]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1]) - 1) + hamle2[1:]] == hareket_sirasi and \
                    kordinat[str(int(hamle2[:1]) - 1) + HARFLER[(HARFLER.index(hamle2[1:])) - 1]] == hareket_sirasi:  # :'
                kare = True
    return kare


def tas_hareket_al(renk):  # Taş hareketini kullanıcıdan alan ve girişin doğru komutlarla yapıldığını kontrol eder.
    try:
        if renk == "Beyaz":
            hareket_sirasi = "B"
            bekleme_sirasi = "S"
        else:
            hareket_sirasi = "S"
            bekleme_sirasi = "B"
        hamle = input(f"{renk} oyuncu, hamlenizi giriniz[Örnek:1A 2A]:").upper().split()
        hamle1 = hamle[0]
        hamle2 = hamle[1]

        while hamle1 == hamle2 or kordinat[hamle1] != hareket_sirasi or kordinat[hamle2] == bekleme_sirasi or \
                (hamle1[:1] != hamle2[:1] and hamle1[1:] != hamle2[1:]) or kordinat[hamle1] == kordinat[hamle2]:
            print("Hatalı işlem yaptınız!.14")
            hamle1, hamle2, hareket_sirasi, bekleme_sirasi = tas_hareket_al(renk)
            if renk == "Beyaz":
                hareket_sirasi = "B"
                bekleme_sirasi = "S"
            else:
                hareket_sirasi = "S"
                bekleme_sirasi = "B"
    except:
        print("Hatalı işlem yaptınız!.15")
        hamle1, hamle2, hareket_sirasi, bekleme_sirasi = tas_hareket_al(renk)

    return hamle1, hamle2, hareket_sirasi, bekleme_sirasi


def main():  # kullanıcıdan yatay çizgi sayısını alır ve geri kalan fonksiyonları sırayla çağırır.
    try:
        yatay_cizgi = int(input("Oyunun yatay çizgi sayısını giriniz[3-7]: "))
        while yatay_cizgi < 3 or yatay_cizgi > 7:
            print("Hatalı işlem yaptınız!.16")
            yatay_cizgi = int(input("Oyunun yatay çizgi sayısını giriniz[3-7]: "))
    except:
        print("Hatalı işlem yaptınız!.17")
        main()
    else:
        oyun_baslat(yatay_cizgi)
        oyun_ciz(yatay_cizgi)
        tas_al(yatay_cizgi)
        beyaz_kare_say, siyah_kare_say = kare_kontrol(yatay_cizgi)
        print("Beyaz kare sayısı: ", beyaz_kare_say)
        print("Siyah kare sayısı: ", siyah_kare_say)
        oyuna_devam(beyaz_kare_say, siyah_kare_say, yatay_cizgi)


main()
