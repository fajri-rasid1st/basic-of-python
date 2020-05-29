from Biodata import Biodata
from time import sleep


class Registration:

    __biodata = ""
    __callName = ""

    def registration(self):
        # meletakkan daftar kode setiap fakultas
        facultyDict = {
            "A": "Kedokteran",
            "B": "Farmasi",
            "C": "Teknik",
            "D": "Kehutanan",
            "E": "Pertanian",
            "F": "Keperawatan",
            "G": "Kesehatan Masyarakat",
            "H": "MIPA",
        }

        while True:
            self.__registShow()
            choice = int(input("> "))

            if choice == 1:
                print("\n+---------------- Registration ---------------+")
                name = input("Nama           : ")
                callName = input("Nama Panggilan : ")
                born = input("Tanggal lahir  : ")
                nim = input("NIM            : ")

                # menginstansiasi object biodata
                bio = Biodata(name, callName, born, nim)
                print("\nLoading ...")
                sleep(2)

                # mengecek apakah inputan tanggal lahir sudah sesuai
                try:
                    bio.setAge(born)
                except ValueError:
                    print("Format tanggal lahir salah (gunakan format dd/mm/yyyy)")
                    continue
                except IndexError:
                    print("Format tanggal lahir salah (gunakan format dd/mm/yyyy)")
                    continue

                # mengecek apakah inputan NIM sudah sesuai
                try:
                    bio.setRegisterYear(nim)
                except ValueError:
                    print("Format NIM salah")
                    continue

                bio.setFaculty(facultyDict)
                bio.setEmail(name)

                # jika NIM yang diinput tidak ada dalam daftar dictionary di atas, maka:
                if bio.getFaculty() is None:
                    print("NIM anda tidak ada dalam daftar")
                    continue
                else:
                    self.__biodata = bio.info()
                    self.__callName = bio.callName
                    print("Pendaftaran berhasil!")
                    sleep(2)
                    break

    def __registShow(self):
        print("\n+---------------- To-Do-List ----------------+")
        print("\nTekan 1 untuk melakukan pendaftaran terlebih dahulu")
        print("Tekan ctrl+c untuk keluar")
        print("Note : Hasanuddin University College Only\n")

    def getBiodata(self):
        return self.__biodata

    def getCallName(self):
        return self.__callName
