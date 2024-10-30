import math
import speedtest

# 1024 bytes = 1 Kb
# 1024 Kb = 1 Mb
# bytes -> kilobyte -> megabites
def bytes_to_megabytes(bytes):
    # print(int(math.floor(math.log(bytes, 1024))))
    power = math.pow(1024, 2)
    megabytes = round(bytes / power, 3)
    return f"{megabytes} Mbps"


def test_my_speed(threads=1):
    s = speedtest.Speedtest()

    print("\nTesteando velocidad de subida...")
    upload = s.upload(threads=threads)
    print("Test de subida completado!")

    print("\nTesteando velocidad de bajada...")
    download = s.download(threads=threads)
    print("Test de descarga completado!")

    print("\nTest finalizado!")
    print("Subida: ", bytes_to_megabytes(upload))
    print("Bajada: ", bytes_to_megabytes(download))
