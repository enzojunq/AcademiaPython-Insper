def nota_quizzes(quiz1,quiz2,quiz3,quiz4,quiz5):
    menor=0
    if quiz1<0 or quiz2<0 or quiz3<0 or quiz4<0 or quiz5<0:
        return 0
    elif quiz1>10 or quiz2>10 or quiz3>10 or quiz4>10 or quiz5>10:
        return 0
    else:
        menor=min(quiz1,quiz2,quiz3,quiz4,quiz5)
        media=(quiz1+quiz2+quiz3+quiz4+quiz5-menor)/4
        
        return media
print(nota_quizzes(5,10,10,10,5))