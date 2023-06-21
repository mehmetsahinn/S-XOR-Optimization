import math

# 2.ODEV

#texti tek satırda okuma
with open('sample.txt', 'r') as file:
    veriler = file.read()
kelimeler = veriler.split()



#matrisleri listede tutma
matrislerb=[]
sayac=0
kacmatris=None
verii=[]
for i in kelimeler:
    sayac+=1
    if kacmatris == None:
        kacmatris=int(i)
        matrisler={}
        for j in range(int(kacmatris)):
            matrisler[f'm{j}']=None
        continue
    if i!='0' and i!='1' and kacmatris!=None and i!=kelimeler[sayac]:
        matrislerb.append(i)
    if (i=='1' or i=='0'):
        verii.append(i)


tempj=0
for i in range(kacmatris):
    temp=[]
    for j in range(int(matrislerb[i])**2):
        temp.append(verii[tempj])
        tempj=tempj+1
    matrisler[f'm{i}']=temp


# dictionary uzunluğu

kok = math.sqrt(len(matrisler['m0']))
denklemler={}
for i in range(kacmatris):
    denklemler[f'm{i}']=[None]
    temp=[]
    for j in range(int(math.sqrt(len(matrisler[f'm{i}'])))):
        temp.append(f'y{j}')
        denklemler[f'm{i}']=temp




for i in range(kacmatris):
    a=matrisler [f'm{i}']
    sayac=0
    for k in range(int(math.sqrt(len(matrisler[f'm{i}'])))):
        temp=[]

        for m in range(int(math.sqrt(len(matrisler[f'm{i}'])))):
            if a[sayac]=='1':
                temp.append(f'x{m}')
                denklemler[f"m{i}"][k]=temp
            sayac+=1


print(f'denklemler {denklemler}')




for matrix in denklemler:
    print(denklemler[matrix])

f = open("result.txt", "w")
for matrix in denklemler:

    print("***********************************************************")
    print("MATRIX "+matrix)
    dict_list = denklemler[matrix]
    dictX = {"x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10",
             "x11", "x12", "x13", "x14", "x15"}
    print(dict_list)
    key_count = {}
    key_count1 = {}
    count_xor = 0
    # Key lerin kaç tane olduğu sayısı ve xor sayısı
    for dictionary in dict_list:
        count_xor += len(dictionary) - 1;
        for key in dictionary:
            if key in key_count:
                key_count[key] += 1
            else:
                key_count[key] = 1
            # print(key)

    print("XOR count:", count_xor);

    print("x0:", key_count["x0"])
    print("x1:", key_count["x1"])
    print("x2:", key_count["x2"])
    print("x3:", key_count["x3"])
    print("x4:", key_count["x4"])
    print("x5:", key_count["x5"])
    print("x6:", key_count["x6"])
    print("x7:", key_count["x7"])
    print("x8:", key_count["x8"])
    print("x9:", key_count["x9"])
    print("x10:", key_count["x10"])
    print("x11:", key_count["x11"])
    print("x12:", key_count["x12"])
    print("x13:", key_count["x13"])
    print("x14:", key_count["x14"])
    print("x15:", key_count["x15"])

    # Key ikililerinden hangileri ne kadar ortak kullanılmış onun sayıları
    for key_x in dictX:
        for key_x1 in dictX:
            if (key_x != key_x1):
                if (key_x + "-" + key_x1) and (key_x1 + "-" + key_x) not in key_count1:
                    for dictionary in dict_list:
                        if key_x in dictionary:
                            if key_x1 in dictionary:
                                if (key_x + "-" + key_x1) in key_count1:
                                    key_count1[(key_x + "-" + key_x1)] += 1
                                else:
                                    key_count1[(key_x + "-" + key_x1)] = 1
                                # print(key)
    print(dictX)
    print(key_count1)
    sorted_items = sorted(key_count1.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict(sorted_items)
    print(sorted_dict)

    countYLine = 0
    finishAllPath = []
    for dictionary in dict_list:
        allPath = {}
        for path, value in sorted_dict.items():
            countX = 0
            countY = 0
            if len(path) == 5:
                countX = 2
                countY = -2
            if len(path) == 7:
                countX = 3
                countY = -3
            if len(path) == 6:
                if path.index("-") == 2:
                    countX = 2
                    countY = -3
                if path.index("-") == 3:
                    countX = 3
                    countY = -2
            if path[:countX] in dictionary:
                if path[countY:] in dictionary:
                    # tempPath.append(path[0:2])
                    allPath[path] = value
        print("Y" + str(countYLine) + "PATH")
        countYLine += 1
        print(allPath)

        tempPathPart = []


        countStart = 0
        tempSearchWord = ""
        allTempPathPart = []
        for path, value in allPath.items():
            tempPathPart = []
            checkFinish = []
            tempPathPart.append(path)
            countX = 0
            countY = 0
            if len(path) == 5:
                countX = 2
                countY = -2
            if len(path) == 7:
                countX = 3
                countY = -3
            if len(path) == 6:
                if path.index("-") == 2:
                    countX = 2
                    countY = -3
                if path.index("-") == 3:
                    countX = 3
                    countY = -2
            finishPath = True
            if countStart == 0:
                tempSearchWord = path[countY:]
                checkFinish.append(path[:countX])
                checkFinish.append(path[countY:])
            while finishPath:
                countFind = len(tempPathPart)
                for path1, value1 in allPath.items():
                    if len(path1) == 5:
                        countX1 = 2
                        countY1 = -2
                    if len(path1) == 7:
                        countX1 = 3
                        countY1 = -3
                    if len(path1) == 6:
                        if path1.index("-") == 2:
                            countX1 = 2
                            countY1 = -3
                        if path1.index("-") == 3:
                            countX1 = 3
                            countY1 = -2
                    if tempSearchWord == path1[:countX1]:
                        tempPathPart.append(path1)
                        checkFinish.append(path1[countY1:])
                        tempSearchWord = path1[countY1:]

                if len(tempPathPart) == countFind:
                    finishPath = False
            # Devam

            for key in checkFinish:
                for path1, value1 in allPath.items():
                    if len(path1) == 5:
                        countX1 = 2
                        countY1 = -2
                    if len(path1) == 7:
                        countX1 = 3
                        countY1 = -3
                    if len(path1) == 6:
                        if path1.index("-") == 2:
                            countX1 = 2
                            countY1 = -3
                        if path1.index("-") == 3:
                            countX1 = 3
                            countY1 = -2
                    if key == path1[:countX1]:
                        if path1[countY1:] not in checkFinish:
                            if len(checkFinish) < len(dictionary):
                                tempPathPart.append(path1)
                                checkFinish.append(path1[countY1:])
            # print("TempPathPart")
            # print(tempPathPart)
            # print("Check Finish")
            # print(checkFinish)
            if len(checkFinish) == len(dictionary):
                print("TempPathPart")
                print(tempPathPart)
                print("Check Finish")
                print(checkFinish)
                allTempPathPart.append(tempPathPart)
        # All Y line path added Main Array
        finishAllPath.append(allTempPathPart)

    # Main Array Last İndex
    print("Finish Path 0")
    print(finishAllPath[len(finishAllPath) - 1])
    cc = 0
    genelSamePath = []
    samePath = []
    tempPath1X = 0
    tempPath1Y = 0
    tempPath2X = 0
    tempPath2Y = 0
    genelInfoPath = []

    for i in range(0, len(finishAllPath)):
        maxOrtak = 0
        counPath1 = 0
        for path1 in finishAllPath[i]:
            for k in range(0, len(finishAllPath)):
                counPath2 = 0
                for path2 in finishAllPath[k]:
                    if i != k:
                        if path1 != path2:
                            ortak_elemanlar = []
                            ortak_elemanlar = set(path1).intersection(path2)
                            if len(ortak_elemanlar) > 0:
                                if (len(ortak_elemanlar) > (maxOrtak)):
                                    print("i:", i)
                                    print("k:", k)
                                    print("Path1")
                                    print(path1)
                                    print("Path2")
                                    print(path2)
                                    print("Ortak Eleman sayısı:", len(ortak_elemanlar))
                                    maxOrtak = len(ortak_elemanlar)
                                    tempPath1X = i
                                    tempPath1Y = counPath1
                                    tempPath2X = k
                                    tempPath2Y = counPath2
                    counPath2 += 1
            counPath1 += 1

        infoPath = [tempPath1X, tempPath1Y, tempPath2X, tempPath2Y, maxOrtak]
        genelInfoPath.append(infoPath)

    finalInfo = []
    finalInfoMainPath = []
    infoFinish = True
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    while infoFinish:
        maxAvg = 0
        tempLenFinal = len(finalInfo)
        for infoP in genelInfoPath:
            if ("Y" + str(infoP[0])) not in finalInfo:
                if ("Y" + str(infoP[2])) not in finalInfo:
                    if infoP[4] >= maxAvg:
                        maxAvg = infoP[4]
                        x = infoP[0]
                        y = infoP[1]
                        x1 = infoP[2]
                        y1 = infoP[3]
                        # print("Y" + str(infoP[0]) + " Path" + str(infoP[1]))
                        # print("Y" + str(infoP[2]) + " Path" + str(infoP[3]))
                # print("Ortak Kelime:", infoP[4])
        tyBool = True
        if infoFinish:
            if ("Y" + str(x)) in finalInfo:
                if ("Y" + str(x1)) in finalInfo:
                    tyBool = False
        if tyBool:
            finalInfo.append("Y" + str(x))
            finalInfo.append("Y" + str(x1))
            finalInfoMainPath.append(finishAllPath[x][y])
            finalInfoMainPath.append(finishAllPath[x1][y1])

        if len(finalInfo) == tempLenFinal:
            for i in range(0, 16):
                if ("Y" + str(i)) not in finalInfo:
                    finalInfo.append("Y" + str(i))
                    finalInfoMainPath.append(finishAllPath[i][0])
            infoFinish = False

    print("FinalInfo")
    print(finalInfo)
    print("finalInfoMainPath")
    print(finalInfoMainPath)

    mainDeviceBasic = []
    mainDevicePath = []
    SumXOR = 0
    tempPathBasic = ""
    finalInfoCount = 0
    for path in finalInfoMainPath:
        if tempPathBasic != "":
            mainDeviceBasic[-1] = tempPathBasic + "    " + finalInfo[finalInfoCount]
        for path1 in path:
            if path1 not in mainDevicePath:
                SumXOR += 1
                if len(path1) == 5:
                    countX1 = 2
                    countY1 = -2
                if len(path1) == 7:
                    countX1 = 3
                    countY1 = -3
                if len(path1) == 6:
                    if path1.index("-") == 2:
                        countX1 = 2
                        countY1 = -3
                    if path1.index("-") == 3:
                        countX1 = 3
                        countY1 = -2
                mainDevicePath.append(path1)
                tempPathBasic = path1[:countX1] + " = " + path1[:countX1] + " ^ " + path1[countY1:]
                mainDeviceBasic.append(path1[:countX1] + " = " + path1[:countX1] + " ^ " + path1[countY1:])
        finalInfoCount += 1


 
    print("main Device Basic")
    f.writelines(f"\nMatris {matrix[1:]}\n")

    for pathF in mainDeviceBasic:
        f.writelines(f"{pathF}\n")
        print(pathF)
    f.writelines(f"Toplam XOR sayisi(S-XOR optimizasyonu olmadan) {count_xor}\n")
    f.writelines(f"Toplam XOR sayisi(S-XOR optimizasyonuyla) {SumXOR}\n\n")
f.close()

# 3.ODEV

allSatirlar = []
with open('result.txt', 'r') as dosya:
    satirlar = []
    for satir in dosya.readlines():
        if satir.startswith("M"):
            if satirlar != []:
                allSatirlar.append(satirlar)
                satirlar = []
        if satir.startswith('x'):
            satirlar.append(satir.strip())
    allSatirlar.append(satirlar)


print("***********************************************************")

checkDenklemler = []
finCheck = 0
checkCount = 0
for co in range(0,len(denklemler)):
    for i in denklemler[("m" + str(co))]:
        for a in allSatirlar[co]:
            if a[a.find("=") + 2:a.find("^") - 1].strip() in i:
                if a[a.find("^") + 2:a.find("^") + 5].strip() in i:
                    if a[a.find("=") + 2:a.find("^") - 1].strip() not in checkDenklemler:
                        checkDenklemler.append(a[a.find("=") + 2:a.find("^") - 1].strip())
                    if a[a.find("^") + 2:a.find("^") + 5].strip() not in checkDenklemler:
                        checkDenklemler.append(a[a.find("^") + 2:a.find("^") + 5].strip())
            if len(checkDenklemler) == len(i):
                checkCount += 1
                print("-------------------------------------------")
                print("Devre Y")
                print(checkDenklemler)
                print("Matris Y")
                print(i)
                break
        checkDenklemler = []
    if checkCount == 16:
        print("****************************************** Matris " + str(
            finCheck) + " OK ! ******************************************")
        finCheck += 1
        checkCount = 0


if finCheck == len(denklemler):
    print("ALL MATRIS CHECK AND CODE SUCCESS !")

