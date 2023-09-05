score = int(input('점수를 입력하세요:'))

if (score>=90) :
    print("성적은 A입니다")
elif (score>=80 and score<90) :
    print("성적은 B입니다")
elif (score>=70 and score<80) :
     print("성적은 C입니다")
elif (score>=60 and score<70) :
     print("성적은 D입니다")
else :
    print("성적은 F입니다")