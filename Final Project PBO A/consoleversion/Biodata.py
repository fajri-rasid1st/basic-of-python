from datetime import date


class Biodata:

    __age = ""
    __faculty = ""
    __registerYear = 0
    __email = ""

    def __init__(self, name, callName, dateOfBirth, nim):
        self.__name = name
        self.__callName = callName
        self.__dateOfBirth = dateOfBirth
        self.__nim = nim

    # mengatur dan mengambil setiap huruf pada nama menjadi lowercase (uppercase pada setiap huruf pertama kata)
    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        fullName = self.__name.lower().split(" ")
        fixName = ""
        for i in range(0, len(fullName)):
            fixName = fixName + fullName[i].capitalize() + " "
        return fixName[0 : len(fixName) - 1]

    # mengambil attribute callName
    @property
    def callName(self):
        pass

    @callName.getter
    def callName(self):
        return self.__callName

    # mengambil attribute dateOfBirth
    @property
    def dateOfBirth(self):
        pass

    @dateOfBirth.getter
    def dateOfBirth(self):
        return self.__dateOfBirth

    # mengambil attribute nim
    @property
    def nim(self):
        pass

    @nim.getter
    def nim(self):
        return self.__nim

    # mengatur class variabel age atau menghitung umur dari tanggal lahir yang diinput user
    def setAge(self, born):
        s = list(reversed(born.split("/")))
        dateBorn = date(int(s[0]), int(s[1]), int(s[2]))
        age = int((date.today() - dateBorn).days / 365.2425)
        self.__age = "{} Tahun".format(age)

    def getAge(self):
        return self.__age

    # mengatur fakultas user dengan melihat awalan NIM yang diinput
    def setFaculty(self, faculty):
        self.__faculty = faculty.get(self.__nim[0])

    def getFaculty(self):
        return self.__faculty

    # mengatur angkatan dengan melihat digit ke-5&6 dari NIM user
    def setRegisterYear(self, nim):
        self.__registerYear = 2000 + int(nim[4:6])

    def getRegisterYear(self):
        return self.__registerYear

    # mengatur email user
    def setEmail(self, name):
        nameEmail = name.split(" ")
        wordsName = ""
        for i in nameEmail:
            wordsName = wordsName + i[0]

        self.__email = (
            nameEmail[len(nameEmail) - 1]
            + wordsName[0 : len(wordsName) - 1]
            + str(self.__registerYear)[2:4]
            + self.__nim[0]
            + "@student.unhas.ac.id"
        ).lower()

    def getEmail(self):
        return self.__email

    # mencetak semua informasi user
    def info(self):
        return "Nama           : {}\nNama panggilan : {}\nTanggal lahir  : {}\nUmur           : {}\nNIM            : {}\nFakultas       : {}\nAngkatan       : {}\nEmail          : {}".format(
            self.name,
            self.callName,
            self.dateOfBirth,
            self.getAge(),
            self.nim,
            self.getFaculty(),
            self.getRegisterYear(),
            self.getEmail(),
        )
