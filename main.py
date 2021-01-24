import javaneseDate as jd

def main():  
    x = jd.JavaneseDate() + jd.JavaneseDateDelta()
    print(x.format())

if __name__ == "__main__":
    main()