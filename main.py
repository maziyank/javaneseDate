import javaneseDate as jd

def main():  
    x = jd.JavaneseDate() + jd.JavaneseDateDelta(tahun=0, sasi=0, dina=2)
    print(x.format())

if __name__ == "__main__":
    main()