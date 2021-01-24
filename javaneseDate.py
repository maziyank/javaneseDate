###############
# javaneseDate.py
# ============
# Python script for handling and converting Javanese Date based on The Javanese calendar system.
# The Javanese calendar (Javanese: ꦥꦤꦁꦒꦭ꧀ꦭꦤ꧀ꦗꦮ, romanized: Pananggalan Jawa)
# is the calendar of the Javanese people which influenced by Hijri Calendar and Hindu Calendar.
# Reference : https://en.wikipedia.org/wiki/Javanese_calendar
###############
# 

import re
from datetime import date, timedelta

class Sasi:
    """
    A class used to represent month class (sasi) in javanese calendar system

    ...

    Parameters
    ----------
    index : int

    """

    class SasiModel:
        def __init__(self, name, index, days, alias=[]):
            self.name = name
            self.alias = alias
            self.days = days
            self.index = index

    SASI_SURA = SasiModel(name="Sura", index=1, days=30)
    SASI_SAPAR = SasiModel(name="Sapar", index=2, days=29)
    SASI_MULUD = SasiModel(name="Mulud", alias=[
                           'Rabingulawal'], index=3, days=30)
    SASI_BAKDAMULUD = SasiModel(name="Bakda Mulud", alias=[
        'Rabingulakir'], index=4, days=29)

    SASI_JUMADILAWAL = SasiModel(name="Jumadilawal", index=5, days=30)
    SASI_JUMADILAKIR = SasiModel(name="Jumadilakir", index=6, days=29)
    SASI_REJEB = SasiModel(name="Rejeb", index=7, days=30)
    SASI_RUWAH = SasiModel(name="Ruwah", alias=[
        'Arwah', 'Saban'], index=8, days=29)
    SASI_PASA = SasiModel(name="Pasa", alias=[
        'Puwasa', 'Siyam', 'Ramelan'], index=9, days=30)
    SASI_SAWAL = SasiModel(name="Sawal", index=10, days=29)
    SASI_SELA = SasiModel(name="Séla", alias=[
                          'Dulkangidah'],  index=11, days=30)
    SASI_BESAR = SasiModel(name="Besar", alias=[
                           'Dulkahijjah'], index=12, days=29)

    values = (SASI_SURA, SASI_SAPAR, SASI_MULUD, SASI_BAKDAMULUD, SASI_JUMADILAWAL,
              SASI_JUMADILAKIR, SASI_REJEB, SASI_RUWAH, SASI_PASA, SASI_SAWAL, SASI_SELA, SASI_BESAR)

    def __init__(self, value=1):
        self.value = value % len(Sasi.values)
        model = Sasi.values[self.value - 1]
        self.days = model.days
        self.index = model.index
        self.alias = model.alias
        self.name = model.name


class Pasaran:
    """
    A class used to represent market day (pasaran) in javanese calendar system

    ...

    Parameters
    ----------
    day : int

    """

    class PasaranModel:
        def __init__(self, index, name):
            self.name = name
            self.index = index

    PASARAN_PON = PasaranModel(1, 'Pon')
    PASARAN_WAGE = PasaranModel(2, 'Wage')
    PASARAN_KLIWON = PasaranModel(3, 'Kliwon')
    PASARAN_LEGI = PasaranModel(4, 'Legi')
    PASARAN_PAHING = PasaranModel(5, 'Pahing')

    values = (PASARAN_PON, PASARAN_WAGE, PASARAN_KLIWON,
              PASARAN_LEGI, PASARAN_PAHING)

    def __init__(self, day=1):
        self.index = day % len(Pasaran.values)
        model = Pasaran.values[self.index - 1]
        self.name = model.name
        self.index = model.index


class Dina:
    """
    A class used to represent day (dina) in javanese calendar system

    ...

    Parameters
    ----------
    value : int
    fromEpoch : int

    """

    class DinaModel:
        def __init__(self, index, name):
            self.name = name
            self.index = index

    DINA_SELASA = DinaModel(1, 'Selasa')
    DINA_REBO = DinaModel(2, 'Rebo')
    DINA_KEMIS = DinaModel(3, 'Kemis')
    DINA_JEMAH = DinaModel(4, 'Jemah')
    DINA_SEBTU = DinaModel(5, 'Sebtu')
    DINA_AKAD = DinaModel(6, 'Akad')
    DINA_SENEN = DinaModel(7, 'Senen')

    values = (DINA_SELASA, DINA_REBO, DINA_KEMIS,
              DINA_JEMAH, DINA_SEBTU, DINA_AKAD, DINA_SENEN)

    def __init__(self, value=1, fromEpoch=1):
        self.value = value
        self.fromEpoch = fromEpoch
        self.index = self.fromEpoch % len(Dina.values)
        model = Dina.values[self.index - 1]
        self.name = model.name
        self.pasaran = Pasaran(self.fromEpoch)


class Tahun:
    """
    A class used to represent year (tahun) in javanese calendar system

    ...

    Parameters
    ----------
    value : int

    """

    class TahunModel:
        def __init__(self, index, name, days):
            self.name = name
            self.days = days
            self.index = index

    TAHUN_ALIP = TahunModel(1, 'Alip', 354)
    TAHUN_EHE = TahunModel(2, 'Ehe', 355)
    TAHUN_JIMAWAL = TahunModel(3, 'Jimawal', 354)
    TAHUN_JE = TahunModel(4, 'Je', 354)
    TAHUN_DAL = TahunModel(5, 'Dal', 355)
    TAHUN_BE = TahunModel(6, 'Be', 354)
    TAHUN_WAWU = TahunModel(7, 'Wawu', 354)
    TAHUN_JIMAKIR = TahunModel(8, 'Jimakir', 355)

    values = (TAHUN_ALIP, TAHUN_EHE, TAHUN_JIMAWAL, TAHUN_JE,
              TAHUN_DAL, TAHUN_BE, TAHUN_WAWU, TAHUN_JIMAKIR)

    def __init__(self, value=1):
        self.value = value
        self.index = (value - 1867) % len(Tahun.values)
        model = Tahun.values[self.index]
        self.days = model.days
        self.name = model.name


class JavaneseDateDelta():
    """
    A class used to represent date difference object for Javanese Date

    ...

    Parameters
    ----------
    tahun : int
        tahun mean year in javanese 
    sasi : int
        sasi mean month in javanese
    dina : int
        dina mean day in javanese

    """

    def __init__(self, tahun=0, sasi=0, dina=0):
        self.tahun = tahun
        self.sasi = sasi
        self.dina = dina


class JavaneseDate:
    """
    A class used to represent a Javanese Date

    ...

    Parameters
    ----------
    tahun : int
        tahun mean year in javanese 
    sasi : int
        sasi mean month in javanese
    dina : int
        dina mean day in javanese

    Methods
    -------
    getDaysFromEpoch(tahun, sasi, dina)
        calculate number of days from epoch 1936-03-24

    getDateFromEpoch(daysFromEpoch)
        return JavaneseDate based on days calculated from epoch 1936-03-24 

    fromDate()
        return javanese date converted from gregorian date

    toDate()
        return datetime from this JavaneseDate object   

    format()
        return JavaneseDate based on customized string format

    """

    DAYS_IN_WINDU = 2835
    TAHUN_IN_WINDU = 8
    GREGORIAN_EPOCH_DATE = date(1936, 3, 24)
    EPOCH_YEAR = 1867

    def __init__(self, tahun=1867, sasi=1, dina=1):
        """ init javanese date. The default value is the first javanese date epoch (24 March 1936C or 1 Sura 1955J)         

        Parameters
        ----------
        tahun  : int, optional, tahun mean year in javanese              
        sasi : int, optional, sasi mean month in javanese
        dina  : int, optional, dina mean day in javanese             

        Returns
        -------
        JavaneseDate object                
         """

        if (tahun >= 1867 and sasi >= 1 and dina > -1):
            self.tahun = Tahun(tahun)
            self.sasi = Sasi(sasi)
            self.daysFromEpoch = self.getDaysFromEpoch(tahun, sasi, dina)
            self.dina = Dina(dina, self.daysFromEpoch)
            
        else:
            raise Exception(
                "Sorry, year must be later than 1867")

    def getDaysFromEpoch(self, tahun, sasi, dina):
        """ This function calculate number of days from epoch 1936-03-24           

            Parameters
            ----------
            tahun  : int, required, tahun mean year in javanese              
            sasi : int, required, sasi mean month in javanese
            dina  : int, required, dina mean day in javanese             

            Returns
            -------
            JavaneseDate object                
        """
        winduCount = (
            tahun - JavaneseDate.EPOCH_YEAR) // JavaneseDate.TAHUN_IN_WINDU
        tahunCount = (
            tahun - JavaneseDate.EPOCH_YEAR) % JavaneseDate.TAHUN_IN_WINDU

        totalDays = sum([
            winduCount * JavaneseDate.DAYS_IN_WINDU,
            sum(map(lambda x: x.days, Tahun.values[:tahunCount])),
            sum(map(lambda x: x.days, Sasi.values[:sasi - 1])),
            dina
        ])

        return totalDays

    def getDateFromEpoch(self, daysFromEpoch):
        """ This function return JavaneseDate based on days calculated from epoch 1936-03-24           

            Parameters
            ----------
            daysFromEpoch : int, required, number of days from epoch                                

            Returns
            -------
            JavaneseDate object                
        """

        if daysFromEpoch:
            windu = daysFromEpoch // JavaneseDate.DAYS_IN_WINDU
            tahun, sasi, days = 1, 1, daysFromEpoch % JavaneseDate.DAYS_IN_WINDU

            while days > 355:
                days, tahun = days - Tahun.values[tahun].days, tahun + 1
            while days > 30:
                days, sasi = days - Sasi.values[sasi].days, sasi + 1

            tahun = Tahun(JavaneseDate.EPOCH_YEAR - 1 +
                          (windu * JavaneseDate.TAHUN_IN_WINDU + tahun))
            sasi = Sasi(sasi)
            pasaran = Pasaran(self.daysFromEpoch)
            dina = Dina(days, self.daysFromEpoch)

            return tahun, sasi, dina, pasaran
        else:
            raise Exception("Required argument was missing")

    def __calculateDeltaDays(self, dt):
        """ This function calculate days difference between this JavaneseDate with other JavaneseDate           

            Parameters
            ----------
            dt          : JavaneseDate, required, other JavaneseDate                            

            Returns
            -------
            JavaneseDate object                
        """

        winduCount = (dt.tahun + dt.sasi //
                      12) // JavaneseDate.TAHUN_IN_WINDU
        tahunCount = (dt.tahun + dt.sasi //
                      12) % JavaneseDate.TAHUN_IN_WINDU

        totalDays = sum([
            winduCount * JavaneseDate.DAYS_IN_WINDU,
            sum(map(lambda x: x.days,
                    Tahun.values[self.tahun.value + 1:self.tahun.index + tahunCount + 1])),
            sum(map(lambda x: x.days,
                    Sasi.values[self.sasi.index + 1: (self.sasi.index + 1) + (dt.sasi % 12)])),
            dt.dina
        ])

        return totalDays

    def fromDate(self, year, month, day):
        """ This function return javanese date converted from gregorian date          

            Parameters
            ----------
            year  : int, required                
            month : int, required
            day : int, required                

            Returns
            -------
            JavaneseDate object                
        """

        if year and month and day:
            dt0 = JavaneseDate.GREGORIAN_EPOCH_DATE
            dt1 = date(year, month, day)
            delta = dt1 - dt0
            self.daysFromEpoch = delta.days + 1
            self.tahun, self.sasi, self.dina, self.pasaran = self.getDateFromEpoch(
                self.daysFromEpoch)

            return self
        else:
            raise Exception("One or more required arguments was missing")

    def toDate(self):
        """ This function return datetime from this JavaneseDate object          

            Returns
            -------
            datetime
        """

        dt0 = JavaneseDate.GREGORIAN_EPOCH_DATE
        dt1 = dt0 + timedelta(days=self.daysFromEpoch - 1)
        return dt1

    def format(self, dateformat='%D %P, %d %M %Y'):
        """ return JavaneseDate based on customized string format.           

            Parameters
            ----------
            dateformat : string format, default is D P, d M Y. Example return Selasa Pon, 1 Sura 186

            Format
            ----------            
            %d: javanese day (dina) value
            %D: javanese day (dina) full name
            %m: javanese month (sasi) value
            %M: javanese month (sasi) full name
            %y: 2-digits year (tahun) 
            %Y: 4-digits year (tahun) 
            %t: javanese year (tahun) name              
            %P: pasaran, daily javanese market name value

            Returns
            -------
            str
        """

        return re.sub(r'(%[a-zA-Z]{1})', '{\\1}', dateformat). \
            replace('%', '').format(d=self.dina.value,
                                    D=self.dina.name,
                                    m=self.sasi.value,
                                    M=self.sasi.name,
                                    y=str(
                                        self.tahun.value)[-2:],
                                    Y=self.tahun.value,
                                    t=self.tahun.name,
                                    P=self.dina.pasaran.name
                                    )

    def __add__(self, other):
        if (type(other) is JavaneseDateDelta):
            totalDays = self.daysFromEpoch + self.__calculateDeltaDays(other)
            self.daysFromEpoch = totalDays
            self.tahun, self.sasi, self.dina, self.pasaran = self.getDateFromEpoch(
                totalDays)
            return self
        else:
            return self

    def __sub__(self, other):
        if (type(other) is JavaneseDateDelta):
            totalDays = self.daysFromEpoch - self.__calculateDeltaDays(other)
            if totalDays > 0:
                self.daysFromEpoch = totalDays + 1
                self.tahun, self.sasi, self.dina, self.pasaran = self.getDateFromEpoch(
                    totalDays)
            else:
                raise Exception(
                    "Cant be performed because the resulted date earlier than 24 March 1936")
            return self
        else:
            return self
