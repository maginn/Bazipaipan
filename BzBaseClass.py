from StaticDict import DictClass
from BZBaseTools import BZBaseTools

class GanClass:
    ganid=0


    def __init__(self, ganid):
       self.ganid=ganid

    #获得十神名称,注意此方法为，自身天干是对方的什么十神，即需要输入的是日干，得出的结果是针对日干的十神
    def getSSName(self,tgid):
        return DictClass.ShishenName[BZBaseTools.ShishenList[tgid][GanClass.ganid]]


    def getGanName(self):
        return DictClass.Gan[self.ganid]

    def getWuxingName(self):
        return DictClass.Wuxing[self.ganid]

    def getWuxingshengwang(self,zhiid):
        id=BZBaseTools.WuxingShengwang[zhiid][BZBaseTools.ganwuxing[self.ganid]]
        return DictClass.WuxingShengwangName[id]


class GanYangClass(GanClass):
    yinyang="阳"

class GanYinClass(GanClass):
    yinyang="阴"


class ZhiClass:
    zhiid=0
    def __init__(self, zhiid):
       self.zhiid=zhiid

    def getZhiName(self):
        return DictClass.Zhi[self.zhiid]

    def getZhiingan(self):
       return BZBaseTools.DzinTg[self.zhiid]

    def getZhiinganname(self):
        list=[]
        for x in BZBaseTools.DzinTg[self.zhiid]:
            list.append(DictClass.Gan[x])
        return list

    def getJijie(self):
        id=BZBaseTools.Jijie[self.zhiid]
        return  DictClass.Jijie[id]


class ZhiYangClass(GanClass):
    yinyang="阳"

class ZhiYinClass(GanClass):
    yinyang="阴"


#单柱
class ZhuClass:
    tiangan=None
    dizhi=None

    def __init__(self, tigan,dizhi):
        self.tiangan=tigan
        self.dizhi=dizhi

    def getShierchangshengName(self,tg,dz):
        id=BZBaseTools.Shierchangsheng[tg.ganid][dz.zhiid]
        return DictClass.ShierchangshengName[id]

    def getNayin(self):
       return DictClass.Nayin[self.tiangan.getGanName()+self.dizhi.getZhiName()]


#八字原局
class BZyjClass:
    yZhu=None
    mZhu=None
    dZhu=None
    tZhu=None

    def __init__(self,yZhu,mZhu,dZhu,tZhu):
        self.yZhu=yZhu
        self.mZhu=mZhu
        self.dZhu=dZhu
        self.tZhu=tZhu

    def getPaiPan(self):
        print("年：" + self.yZhu.tiangan.getGanName() + " " + self.yZhu.dizhi.getZhiName(),self.yZhu.getNayin())

        print("月：" + self.mZhu.tiangan.getGanName() + " " + self.mZhu.dizhi.getZhiName(),self.mZhu.getNayin())

        print("日：" + self.dZhu.tiangan.getGanName() + " " + self.dZhu.dizhi.getZhiName(),self.dZhu.getNayin())

        print("时：" + self.tZhu.tiangan.getGanName() + " " + self.tZhu.dizhi.getZhiName(),self.tZhu.getNayin())


