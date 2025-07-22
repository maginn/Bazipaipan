import sxtwl
import sys
from StaticDict import DictClass
import BzBaseClass

type=sys.getfilesystemencoding()

class BzPaipan:
    yZhu=None
    mZhu=None
    dZhu=None
    tZhu=None

    lunar=None

    ySun=None
    mSun=None
    dSun=None
    tSun=None

    yLunar=None
    mLunar=None
    dLunar=None
    tLunar=None

    def __init__(self):
        pass  # No need to instantiate a Lunar object in the new API


    def getPaipanbySun(self,y,m,d,t):

        day=sxtwl.fromSolar(y,m,d)

        #农历
        self.yLunar=day.getLunarYear()
        self.mLunar=day.getLunarMonth()
        self.dLunar=day.getLunarDay()
        self.tLunar=t

        # 找到节气 (Note: JieQi functionality may need separate handling)
        jieqilist=None  # This may need to be implemented differently


        #组装干支
        yGanZhi=day.getYearGZ()
        yGan=BzBaseClass.GanClass(yGanZhi.tg)
        yZhi=BzBaseClass.ZhiClass(yGanZhi.dz)

        mGanZhi=day.getMonthGZ()
        mGan=BzBaseClass.GanClass(mGanZhi.tg)
        mZhi=BzBaseClass.ZhiClass(mGanZhi.dz)

        dGanZhi=day.getDayGZ()
        dGan=BzBaseClass.GanClass(dGanZhi.tg)
        dZhi=BzBaseClass.ZhiClass(dGanZhi.dz)

        tGanZhi=sxtwl.getShiGz(dGanZhi.tg, t)
        tGan=BzBaseClass.GanClass(tGanZhi.tg)
        tZhi=BzBaseClass.ZhiClass(tGanZhi.dz)

        #组装四柱
        yZhu=BzBaseClass.ZhuClass(yGan,yZhi)
        mZhu=BzBaseClass.ZhuClass(mGan,mZhi)
        dZhu=BzBaseClass.ZhuClass(dGan,dZhi)
        tZhu=BzBaseClass.ZhuClass(tGan,tZhi)

        print("农历", yGan.getGanName(), "年", DictClass.ymc[self.mLunar], "月",
              DictClass.rmc[self.dLunar], "日", tZhi.getZhiName(), "时")

        return BzBaseClass.BZyjClass(yZhu,mZhu,dZhu,tZhu)

    def getPaipanbyLunar(self,y,m,d,t):

        day=sxtwl.fromLunar(y,m,d)

        #公历
        self.ySun=day.getSolarYear()
        self.mSun=day.getSolarMonth()
        self.dSun=day.getSolarDay()
        self.tSunr=t
        print("公历",self.ySun , "年" ,self.mSun , "月" , self.dSun , "日" , self.tSunr ,"时")

        #找到所有节气 (Note: JieQi functionality may need separate handling)
        jieqilist=None  # This may need to be implemented differently

        #组装干支
        yGanZhi=day.getYearGZ()
        yGan=BzBaseClass.GanClass(yGanZhi.tg)
        yZhi=BzBaseClass.ZhiClass(yGanZhi.dz)

        mGanZhi=day.getMonthGZ()
        mGan=BzBaseClass.GanClass(mGanZhi.tg)
        mZhi=BzBaseClass.ZhiClass(mGanZhi.dz)

        dGanZhi=day.getDayGZ()
        dGan=BzBaseClass.GanClass(dGanZhi.tg)
        dZhi=BzBaseClass.ZhiClass(dGanZhi.dz)

        tGanZhi=sxtwl.getShiGz(dGanZhi.tg, t)
        tGan=BzBaseClass.GanClass(tGanZhi.tg)
        tZhi=BzBaseClass.ZhiClass(tGanZhi.dz)

        #组装四柱
        yZhu=BzBaseClass.ZhuClass(yGan,yZhi)
        mZhu=BzBaseClass.ZhuClass(mGan,mZhi)
        dZhu=BzBaseClass.ZhuClass(dGan,dZhi)
        tZhu=BzBaseClass.ZhuClass(tGan,tZhi)

        return BzBaseClass.BZyjClass(yZhu,mZhu,dZhu,tZhu)