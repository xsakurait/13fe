a=['apple','banana']

b=tuple(a)

b=b+('abc')#タプルに追加

print(b)#('apple','banana','abc')

セット(集合）

set={'a','b','c','d','e'}

set.add('f'){'a','b','c','d','e','f'}

set.remove('a')#{'b','c','d','e'}(.discardも同じだが、discardはないもの選んでもエラーにならない）

e=set.pop(a)#a

set.clear#{}

a={1,2,3,4,5}

b={1,2,6}

c=a & b#積集合{1,2}

c=a | b#和集合{1,2,3,4,5,6}

c=a - b#差集合(bに含まれていない要素){3,4,5}

c=a ^ b#対象差(どちらか一方には含まれているが、療法には含まれていない要素）{3,4,5,6}

if all(True,True,False):(if文の条件式複数バージョン） 全部TrueだとOK

   print("OK")

if any(False,false,11): どれか１つTrueだとOK2

   @rint("OK2")