## javaneseDate.py

Python script for handling and converting Javanese Date based on The Javanese calendar system.
The Javanese calendar (Javanese: ꦥꦤꦁꦒꦭ꧀ꦭꦤ꧀ꦗꦮ, romanized: Pananggalan Jawa)
is the calendar of the Javanese people which influenced by Hijri Calendar and Hindu Calendar.

Reference : https://en.wikipedia.org/wiki/Javanese_calendar

## Usage

```python

## Initialize JavaneseDate
import JavaneseDate
date1 = JavaneseDate()

## Initialize JavaneseDate with specific date
import JavaneseDate
date1 = JavaneseDate(tahun=1867,sasi=3,dina=1).format()
  ## -> Jemah Pahing, 1 Mulud 1867 

## Create JavaneseDate From Gregorian Date
date1 = JavaneseDate().fromDate(year=2020, month=1, day=24).format()
  ## -> Jemah Wage, 28 Jumadilawal 1953
  
## Convert JavaneseDate To Python DateTime Object
date1 = JavaneseDate().toDate()
  ## -> 1936-03-24
  
## Format Date
date1 = JavaneseDate().format(dateformat='%D %P, %d %M %Y')
  ## -> Selasa Pon, 1 Sura 1867 

```

## Date Formatting
```       
%d: javanese day (dina) value

%D: javanese day (dina) full name

%m: javanese month (sasi) value

%M: javanese month (sasi) full name

%y: 2-digits year (tahun) 

%Y: 4-digits year (tahun) 

%t: javanese year (tahun) name      

%P: pasaran, daily javanese market name value
```

## Unit Test

```
python test.py
```
