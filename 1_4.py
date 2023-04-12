def info():
    __author__ = 'Minseo Choi'
    __version__ = '1.1'
    __email__ = 'abcabc@gmail.com'
    print("-----information-----")
    print("author:"+__author__)
    print("version:"+__version__)
    print("email:"+__email__)

season = input("좋아하는 계절은 무엇인가요?")
print(season)

year = int(input("태어난 년도는?"))
year = 2021 - year + 1
print(year)

print("************************")

print("***** 문자열 형태로 *****")
print("좋아하는 계절은" + season + "이고," + "나이는" + str(year) + "살 입니다...")
print("***** 정수형 형태로 *****")
print("좋아하는 계절은" + season + "이고," + "나이는" + year + "살 입니다...")

info()