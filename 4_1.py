import pickle

bfilename = "C:/Users/yoonjoo_and_sora/Downloads/education/python_crawling/Section4/test.bin"
tfilename = "C:/Users/yoonjoo_and_sora/Downloads/education/python_crawling/Section4/test.txt"


data1= 77;
data2= "hello, world";
data3= ["car","apple","house"];


with open(bfilename,"wb") as f:
    pickle.dump(data1,f) #dump(문자열 직렬화)
    pickle.dump(data2,f)
    pickle.dump(data3,f)

with open(tfilename,"wt") as f:
    f.write(str(data1));
    f.write("\n");
    f.write(data2);
    f.write("\n");
    f.writelines(data3);
    f.write("\n");

with open(bfilename,"rb") as f:
    b  = pickle.load(f); #load(문자열 역직렬화)
    print(type(b),"Bin1 :",b);
    b  = pickle.load(f); #load(문자열 역직렬화)
    print(type(b),"Bin2 :",b);
    b  = pickle.load(f); #load(문자열 역직렬화)
    print(type(b),"Bin3 :",b);


with open(tfilename,"rt") as f:
    for i, line in enumerate(f,1):
        print(type(line),"Txt :",i,line,end="");
