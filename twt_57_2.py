I=input
for _ in[int]*int(I()):
 v=[];m=0
 for l in '.' * _(I()):a,*b=I().split();v.append([a,b:=[*map(_,b)]]);m=max(m,b[0])
 while m and v:w=[i for i in v if i[1][0]>=m];n=max(i[1][1]for i in w);k=[i for i in w if i[1][1]==n][0];print(k[0],end=' ');v=[i for i in v if i!=k];m=min(m-1,max(i[1][0]for i in v))
 print()



