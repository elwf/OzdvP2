def gecis_tablosu_olustur():

    tablo = {}

    rakamlar      = "0123456789"
    harfler       = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kucuk_harfler = "abcdefghijklmnopqrstuvwxyz"


    for r in rakamlar:
        tablo[("q0", r)] = ("q1", "R")
    for h in harfler:
        tablo[("q0", h)] = ("qRED", "S")
    for k in kucuk_harfler:
        tablo[("q0", k)] = ("qRED", "S")


    for r in rakamlar:
        tablo[("q1", r)] = ("q2", "R")
    for h in harfler:
        tablo[("q1", h)] = ("qRED", "S")
    for k in kucuk_harfler:
        tablo[("q1", k)] = ("qRED", "S")


    for h in harfler:
        tablo[("q2", h)] = ("q3", "R")
    for r in rakamlar:
        tablo[("q2", r)] = ("qRED", "S")
    for k in kucuk_harfler:
        tablo[("q2", k)] = ("qRED", "S")


    for h in harfler:
        tablo[("q3", h)] = ("q4", "R")
    for r in rakamlar:
        tablo[("q3", r)] = ("qRED", "S")
    for k in kucuk_harfler:
        tablo[("q3", k)] = ("qRED", "S")


    for r in rakamlar:
        tablo[("q4", r)] = ("q5", "R")
    for h in harfler:
        tablo[("q4", h)] = ("qRED", "S")
    for k in kucuk_harfler:
        tablo[("q4", k)] = ("qRED", "S")


    for r in rakamlar:
        tablo[("q5", r)] = ("q6", "R")
    for h in harfler:
        tablo[("q5", h)] = ("qRED", "S")
    for k in kucuk_harfler:
        tablo[("q5", k)] = ("qRED", "S")


    for r in rakamlar:
        tablo[("q6", r)] = ("q7", "R")
    for h in harfler:
        tablo[("q6", h)] = ("qRED", "S")
    for k in kucuk_harfler:
        tablo[("q6", k)] = ("qRED", "S")


    tablo[("q7", "_")] = ("qKABUL", "S")
    for r in rakamlar:
        tablo[("q7", r)] = ("qRED", "S")   # fazla rakam → RED
    for h in harfler:
        tablo[("q7", h)] = ("qRED", "S")   # fazla harf  → RED
    for k in kucuk_harfler:
        tablo[("q7", k)] = ("qRED", "S")   # fazla küçük harf → RED

    return tablo

def bant_goster(bant, kafa):
    gosterim = ""
    for i, sembol in enumerate(bant):
        if i == kafa:
            gosterim += f"[{sembol}]"
        else:
            gosterim += sembol
    return gosterim

def calistir(girdi, tablo):
    print("=" * 60)
    print(f"  Girdi : '{girdi}'")
    print("=" * 60)

    # Girdiyi banta yerleştir; bant sonu sembolü "_" olarak eklenir
    bant  = list(girdi) + ["_"]
    kafa  = 0
    durum = "q0"
    adim  = 0

    print(f"  Başlangıç durumu : {durum}")
    print(f"  Bant             : {bant_goster(bant, kafa)}")
    print("-" * 60)

    while durum not in ("qKABUL", "qRED"):

        sembol  = bant[kafa]
        anahtar = (durum, sembol)

        # Geçiş tablosunda tanımsız → RED
        if anahtar not in tablo:
            sembol_goster = sembol if sembol != "_" else "bant_sonu(_)"
            print(
                f"  Adım {adim + 1:2d}: Tanımsız geçiş "
                f"({durum}, '{sembol_goster}') → RED"
            )
            print(f"  Bant  : {bant_goster(bant, kafa)}")
            durum = "qRED"
            break

        yeni_durum, hareket = tablo[anahtar]
        adim += 1

        sembol_goster = sembol if sembol != "_" else "bant_sonu(_)"

        print(
            f"  Adım {adim:2d}: {durum:8s} --[{sembol_goster}]--> "
            f"{yeni_durum:8s}  ({hareket})   Bant: {bant_goster(bant, kafa)}"
        )

        durum = yeni_durum

        if hareket == "R":
            kafa += 1

    print("-" * 60)
    kabul = (durum == "qKABUL")
    if kabul:
        print(f"  SONUÇ : KABUL ✓  (son durum: {durum})")
    else:
        print(f"  SONUÇ : RED ✗    (son durum: {durum})")
    print("=" * 60 + "\n")
    return kabul


if __name__ == "__main__":
    tablo = gecis_tablosu_olustur()

    print()
    print("   Turing Makinesi — Plaka Format Tanıyıcı            ")
    print("   Kabul edilen format : NNLLNNN  (örn: 06EF071)      ")
    print("   N = rakam (0-9)    L = büyük harf (A-Z)            ")
    print("   Çıkmak için 'q' yazınız.                           ")
    print()

    while True:
        girdi = input("Plaka giriniz: ").strip()

        if girdi.lower() == "q":
            print("Çıkılıyor...")
            break

        if girdi == "":
            print("Lütfen bir plaka giriniz.\n")
            continue

        calistir(girdi, tablo)