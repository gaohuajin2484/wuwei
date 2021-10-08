'''
@File  :UserRecRecordFilter.py
@Author:gaohuajin
@Date  :9/27/2111:02 AM
@Desc  :过滤策略UserRecRecordFilter，根据用户的曝光数据对召回的数据做数据过滤。
'''

import time

class UserRecRecordFilter:
    def __init__(self,data,limit_time,sls_limit_reult):
        self.data = data
        self.limit_time = limit_time
        self.limit_result = self.get_limit_list()
        self.sls_limit_reult = sls_limit_reult
        self.diff_resut()

    def get_limit_list(self):
        result = []

        current_timestamp = int(round(time.time() * 1000))
        for i in self.data.split(","):
            if current_timestamp - int(i.split(":")[1]) <= self.limit_time:
                result.append(int(i.split(":")[0]))
        return result

    def diff_resut(self):
        if self.limit_result == self.sls_limit_reult:
            print("过滤集合没有问题")
        else:
            print(set(self.sls_limit_reult).symmetric_difference(set(self.limit_result)))
            print("脚本 reslut {}".format(self.limit_result))
            print("日志 reslut {}".format(self.sls_limit_reult))

if __name__ == '__main__':
    limit_time = 1*60*60*1000
    print(limit_time)
    data = "20717149:1630043475219,564889:1630043475219,10441415:1630043475219,20551311:1630043475219,5196616:1630043475219,20361883:1630043475219,4926924:1630043475219,20647736:1630043475219,7133171:1630043475219,18665819:1630043475219,6018250:1630050752278,23088324:1630050752278,6696553:1630050752278,23121379:1630050752278,6549981:1630050752278,4925497:1630050752278,5426967:1630050752278,7535601:1630050752278,6022228:1630050752278,4925362:1630050752278,4927053:1630057043953,4928150:1630057043953,6412843:1630057043953,6019802:1630057043953,23187866:1630057043953,21682155:1630057043953,4933676:1630057043953,7304349:1630057043953,1294695:1630057043953,23121129:1630057043953,1637554:1630057047584,23966719:1630057047584,1375660:1630057047584,8288069:1630057047584,5803751:1630057047584,4926753:1630057047584,7290588:1630057047584,4925465:1630057047584,22727064:1630057047584,23121241:1630057047584,23151857:1630206464596,4926854:1630206464596,5552355:1630206464596,5611066:1630206464596,23717886:1630206464596,22863510:1630206464596,109731:1630206464596,12539752:1630206464596,682237:1630206464596,19113665:1630206464596,24055513:1630233201287,19080613:1630233201287,23780051:1630233201287,4925681:1630233201287,18413119:1630233201287,38740:1630233201287,22688787:1630233201287,19687331:1630233201287,4926567:1630233201287,1434834:1630233201287,4925828:1630233292120,1305865:1630233292120,1289330:1630233292120,17550548:1630233292120,23693762:1630233292120,23717544:1630233292120,7057086:1630233292120,4925714:1630233292120,6368062:1630233292120,23693813:1630233292120,19392532:1630316140544,19699709:1630316140544,7294288:1630316140544,19666257:1630316140544,242822:1630316140544,434241:1630316140544,20563502:1630316140544,7212638:1630316140544,5847716:1630316140544,22746429:1630316140544,175362:1630316140544,19802445:1630316140544,1455501:1630316140544,5434929:1630316140544,6357931:1630316140544,20342810:1630316140544,20792287:1630316140544,7678131:1630316140544,21621081:1630316140544,20695792:1630316140544,19392532:1630316158304,19699709:1630316158304,7294288:1630316158304,19666257:1630316158304,242822:1630316158304,434241:1630316158304,20563502:1630316158304,7212638:1630316158304,5847716:1630316158304,22746429:1630316158304,175362:1630316158304,19802445:1630316158304,1455501:1630316158304,5434929:1630316158304,6357931:1630316158304,20342810:1630316158304,20792287:1630316158304,7678131:1630316158304,21621081:1630316158304,20695792:1630316158304,19392532:1630316167850,19699709:1630316167850,7294288:1630316167850,19666257:1630316167850,242822:1630316167850,434241:1630316167850,20563502:1630316167850,7212638:1630316167850,5847716:1630316167850,22746429:1630316167850,175362:1630316167850,19802445:1630316167850,1455501:1630316167850,5434929:1630316167850,6357931:1630316167850,20342810:1630316167850,20792287:1630316167850,7678131:1630316167850,21621081:1630316167850,20695792:1630316167850,19392532:1630316173517,19699709:1630316173517,7294288:1630316173517,19666257:1630316173517,242822:1630316173517,434241:1630316173517,20563502:1630316173517,7212638:1630316173517,5847716:1630316173517,22746429:1630316173517,175362:1630316173517,19802445:1630316173517,1455501:1630316173517,5434929:1630316173517,6357931:1630316173517,20342810:1630316173517,20792287:1630316173517,7678131:1630316173517,21621081:1630316173517,20695792:1630316173517,19392532:1630316188970,19699709:1630316188970,7294288:1630316188970,19666257:1630316188970,242822:1630316188970,434241:1630316188970,20563502:1630316188970,7212638:1630316188970,5847716:1630316188970,22746429:1630316188970,175362:1630316188970,19802445:1630316188970,1455501:1630316188970,5434929:1630316188970,6357931:1630316188970,20342810:1630316188970,20792287:1630316188970,7678131:1630316188970,21621081:1630316188970,20695792:1630316188970,19392532:1630316192963,19699709:1630316192963,7294288:1630316192963,19666257:1630316192963,242822:1630316192963,434241:1630316192963,20563502:1630316192963,7212638:1630316192963,5847716:1630316192963,22746429:1630316192963,175362:1630316192963,19802445:1630316192963,1455501:1630316192963,5434929:1630316192963,6357931:1630316192963,20342810:1630316192963,20792287:1630316192963,7678131:1630316192963,21621081:1630316192963,20695792:1630316192963,19392532:1630316194084,19699709:1630316194084,7294288:1630316194084,19666257:1630316194084,242822:1630316194084,434241:1630316194084,20563502:1630316194084,7212638:1630316194084,5847716:1630316194084,22746429:1630316194084,175362:1630316194084,19802445:1630316194084,1455501:1630316194084,5434929:1630316194084,6357931:1630316194084,20342810:1630316194084,20792287:1630316194084,7678131:1630316194084,21621081:1630316194084,20695792:1630316194084,19392532:1630316195234,19699709:1630316195234,7294288:1630316195234,19666257:1630316195234,242822:1630316195234,434241:1630316195234,20563502:1630316195234,7212638:1630316195234,5847716:1630316195234,22746429:1630316195234,175362:1630316195234,19802445:1630316195234,1455501:1630316195234,5434929:1630316195234,6357931:1630316195234,20342810:1630316195234,20792287:1630316195234,7678131:1630316195234,21621081:1630316195234,20695792:1630316195234,19392532:1630316196121,19699709:1630316196121,7294288:1630316196121,19666257:1630316196121,242822:1630316196121,434241:1630316196121,20563502:1630316196121,7212638:1630316196121,5847716:1630316196121,22746429:1630316196121,175362:1630316196121,19802445:1630316196121,1455501:1630316196121,5434929:1630316196121,6357931:1630316196121,20342810:1630316196121,20792287:1630316196121,7678131:1630316196121,21621081:1630316196121,20695792:1630316196121,19392532:1630316197300,19699709:1630316197300,7294288:1630316197300,19666257:1630316197300,242822:1630316197300,434241:1630316197300,20563502:1630316197300,7212638:1630316197300,5847716:1630316197300,22746429:1630316197300,175362:1630316197300,19802445:1630316197300,1455501:1630316197300,5434929:1630316197300,6357931:1630316197300,20342810:1630316197300,20792287:1630316197300,7678131:1630316197300,21621081:1630316197300,20695792:1630316197300,19392532:1630316198215,19699709:1630316198215,7294288:1630316198215,19666257:1630316198215,242822:1630316198215,434241:1630316198215,20563502:1630316198215,7212638:1630316198215,5847716:1630316198215,22746429:1630316198215,175362:1630316198215,19802445:1630316198215,1455501:1630316198215,5434929:1630316198215,6357931:1630316198215,20342810:1630316198215,20792287:1630316198215,7678131:1630316198215,21621081:1630316198215,20695792:1630316198215,19392532:1630316200962,19699709:1630316200962,7294288:1630316200962,19666257:1630316200962,242822:1630316200962,434241:1630316200962,20563502:1630316200962,7212638:1630316200962,5847716:1630316200962,22746429:1630316200962,175362:1630316200962,19802445:1630316200962,1455501:1630316200962,5434929:1630316200962,6357931:1630316200962,20342810:1630316200962,20792287:1630316200962,7678131:1630316200962,21621081:1630316200962,20695792:1630316200962,19392532:1630316202881,19699709:1630316202881,7294288:1630316202881,19666257:1630316202881,242822:1630316202881,434241:1630316202881,20563502:1630316202881,7212638:1630316202881,5847716:1630316202881,22746429:1630316202881,175362:1630316202881,19802445:1630316202881,1455501:1630316202881,5434929:1630316202881,6357931:1630316202881,20342810:1630316202881,20792287:1630316202881,7678131:1630316202881,21621081:1630316202881,20695792:1630316202881,19392532:1630316204091,19699709:1630316204091,7294288:1630316204091,19666257:1630316204091,242822:1630316204091,434241:1630316204091,20563502:1630316204091,7212638:1630316204091,5847716:1630316204091,22746429:1630316204091,175362:1630316204091,19802445:1630316204091,1455501:1630316204091,5434929:1630316204091,6357931:1630316204091,20342810:1630316204091,20792287:1630316204091,7678131:1630316204091,21621081:1630316204091,20695792:1630316204091,19392532:1630316209188,19699709:1630316209188,7294288:1630316209188,19666257:1630316209188,242822:1630316209188,434241:1630316209188,20563502:1630316209188,7212638:1630316209188,5847716:1630316209188,22746429:1630316209188,175362:1630316209188,19802445:1630316209188,1455501:1630316209188,5434929:1630316209188,6357931:1630316209188,20342810:1630316209188,20792287:1630316209188,7678131:1630316209188,21621081:1630316209188,20695792:1630316209188,19392532:1630316210232,19699709:1630316210232,7294288:1630316210232,19666257:1630316210232,242822:1630316210232,434241:1630316210232,20563502:1630316210232,7212638:1630316210232,5847716:1630316210232,22746429:1630316210232,175362:1630316210232,19802445:1630316210232,1455501:1630316210232,5434929:1630316210232,6357931:1630316210232,20342810:1630316210232,20792287:1630316210232,7678131:1630316210232,21621081:1630316210232,20695792:1630316210232,19392532:1630316212251,19699709:1630316212251,7294288:1630316212251,19666257:1630316212251,242822:1630316212251,434241:1630316212251,20563502:1630316212251,7212638:1630316212251,5847716:1630316212251,22746429:1630316212251,175362:1630316212251,19802445:1630316212251,1455501:1630316212251,5434929:1630316212251,6357931:1630316212251,20342810:1630316212251,20792287:1630316212251,7678131:1630316212251,21621081:1630316212251,20695792:1630316212251,19392532:1630316213273,19699709:1630316213273,7294288:1630316213273,19666257:1630316213273,242822:1630316213273,434241:1630316213273,20563502:1630316213273,7212638:1630316213273,5847716:1630316213273,22746429:1630316213273,175362:1630316213273,19802445:1630316213273,1455501:1630316213273,5434929:1630316213273,6357931:1630316213273,20342810:1630316213273,20792287:1630316213273,7678131:1630316213273,21621081:1630316213273,20695792:1630316213273,19392532:1630316220218,19699709:1630316220218,7294288:1630316220218,19666257:1630316220218,242822:1630316220218,434241:1630316220218,20563502:1630316220218,7212638:1630316220218,5847716:1630316220218,22746429:1630316220218,175362:1630316220218,19802445:1630316220218,1455501:1630316220218,5434929:1630316220218,6357931:1630316220218,20342810:1630316220218,20792287:1630316220218,7678131:1630316220218,21621081:1630316220218,20695792:1630316220218,169181:1630389088575,5873866:1630389088575,4760087:1630389088575,7310123:1630389088575,5305140:1630389088575,21377025:1630389088575,6314949:1630389088575,6159397:1630389088575,1360932:1630389088575,5408805:1630389088575,4244972:1630389392336,6021953:1630389392336,5163870:1630389392336,7631718:1630389392336,20588661:1630389392336,6022066:1630389392336,22746429:1630389392336,22863510:1630389392336,8970591:1630389392336,6640356:1630389392336,7342214:1630389710687,20888198:1630389710687,6222094:1630389710687,21509959:1630389710687,17911736:1630389710687,4792012:1630389710687,18715368:1630389710687,4925324:1630389710687,1714035:1630389710687,22566404:1630389710687,19379:1630389936622,4927491:1630389936622,5163867:1630389936622,4925306:1630389936622,22358497:1630389936622,4925836:1630389936622,169078:1630389936622,20787442:1630389936622,5983376:1630389936622,1624424:1630389936622,18588517:1630390143639,23151857:1630390143639,23121148:1630390143639,22812582:1630390143639,4922221:1630390143639,175362:1630390143639,4920620:1630390143639,7288119:1630390143639,6180881:1630390143639,19934694:1630390143639"
    sls_limit_reuslt = [169181, 5873866, 4760087, 7310123, 5305140, 21377025, 6314949, 6159397, 1360932, 5408805, 4244972, 6021953,
     5163870, 7631718, 20588661, 6022066, 22746429, 22863510, 8970591, 6640356, 7342214, 20888198, 6222094, 21509959,
     17911736, 4792012, 18715368, 4925324, 1714035, 22566404, 19379, 4927491, 5163867, 4925306, 22358497, 4925836,
     169078, 20787442, 5983376, 1624424, 18588517, 23151857, 23121148, 22812582, 4922221, 175362, 4920620, 7288119,
     6180881, 19934694]
    run = UserRecRecordFilter(data,limit_time,sls_limit_reuslt)