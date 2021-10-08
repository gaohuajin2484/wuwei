'''
@File  :Tapd_test_ID1116587.py
@Author:gaohuajin
@Date  :9/28/2111:04 AM
@Desc  :
'''

import os,json,copy
from collections import Counter
from aliyun.log.logclient import LogClient

class Tapd_test_ID1116587:
    def __init__(self):
        self.excel_high_fee_tag_0 = []
        self.excel_high_fee_tag_1 = []
        self.excel_high_fee_tag_2 = []
        self.odps_high_fee_tag_0 = [513,3725,1231,970,2550,762,4634,1046,4668,2497,1799,3914,968,
                3711,1433,647,277,625,9503,4190,6775,2623,3895,3567,288]
        self.odps_high_fee_tag_1 = [910,6629,6743,3997,659,990,3730,4214,8223,4068,2032,11598,1003,
                640,8666,668,1312,5466,2389,6180,10092,1449,3081,3760,4674,721,4189,2639,8406,952,4524,
                3788,3294,3601,1431,11094,7560,9143,2494,4108,7562,3504,3728]
        self.odps_high_fee_tag_2 = [769,1341,2483,9409,3792,1035,3811,3727,4648,2632,8669,10135,5844,
                3943,3808,4478,11472,1126,453,4635,8248,3587,550,8123,3576,9576,9701,3862,5083,9644,2512,
                543,9504,9140,8397,987,8408,7587,3729,7738,1739,8663,10307,7745,3638,8390,9134,10576,2202,
                3726,747,8145,9575,2383,1021,2577,11599,11226,2543,10042,3719,3563]
        self.brand_len = 0

    def to_Excel_barnd_list(self):
        def get_txt(path):
            result = []
            with open(path, "r") as f:
                for i in f.readlines():
                    result.append(i.rstrip("\n"))
            return result
        brand = get_txt(os.path.join(os.path.abspath(os.getcwd()),"tapd_file_manage","ID1116587_brand.txt"))
        self.brand_len = len(brand)
        print(self.brand_len)
        if len(brand) == len(set(brand)):
            print("excel品牌集合的数据没有重复")
        else:
            repeat_items = {key: value for key, value in dict(Counter(brand)).items() if
                            value > 1}
            print("出现品牌重复的数据有 {}".format(repeat_items))
        tag = get_txt(os.path.join(os.path.abspath(os.getcwd()),"tapd_file_manage","ID1116587_tag.txt"))
        for i in range(len(tag)):
            if tag[i] == "high_fee_tag_0":
                self.excel_high_fee_tag_0.append(int(brand[i]))
            elif tag[i] == "high_fee_tag_1":
                self.excel_high_fee_tag_1.append(int(brand[i]))
            else:
                self.excel_high_fee_tag_2.append(int(brand[i]))

    def match(self):

        if len(self.odps_high_fee_tag_0) == len(set(self.odps_high_fee_tag_0)):
            print("odps_high_fee_tag_0数据无重复")
        else:
            print()

        if len(self.odps_high_fee_tag_1) == len(set(self.odps_high_fee_tag_1)):
            print("odps_high_fee_tag_1数据无重复")
        else:
            print()

        if len(self.odps_high_fee_tag_2) == len(set(self.odps_high_fee_tag_2)):
            print("odps_high_fee_tag_2数据无重复")
        else:
            print()

        if len(set(self.odps_high_fee_tag_0).intersection(set(self.odps_high_fee_tag_1))) == 0:
            print("odps_high_fee_tag_0和odps_high_fee_tag_1无交集")
        else:
            print()

        if len(set(self.odps_high_fee_tag_1).intersection(set(self.odps_high_fee_tag_2))) == 0:
            print("odps_high_fee_tag_1和odps_high_fee_tag_2无交集")
        else:
            print()

        if len(set(self.odps_high_fee_tag_0).intersection(set(self.odps_high_fee_tag_2))) == 0:
            print("odps_high_fee_tag_0和odps_high_fee_tag_2无交集")
        else:
            print()

        if self.excel_high_fee_tag_0 == self.odps_high_fee_tag_0:
            print("对比excel_high_fee_tag_0和dps_high_fee_tag_0的数据一致")
        else:
            print()
        if self.excel_high_fee_tag_1 == self.odps_high_fee_tag_1:
            print("对比excel_high_fee_tag_1和dps_high_fee_tag_1的数据一致")
        else:
            print()
        if self.excel_high_fee_tag_2 == self.odps_high_fee_tag_2:
            print("对比excel_high_fee_tag_2和dps_high_fee_tag_2的数据一致")
        else:
            print()
    def toutiao_tag_hit_match(self):
        hit_number = 0
        errer_list_1 = []
        errer_list_2 = []

        flag = False
        def get_aliyun_log(data):
            result = []
            result_dict = {}
            brand_data = "r{}$##$c0".format(data)
            aliyun_conf = dict(
                endpoint="cn-hangzhou.log.aliyuncs.com",
                accessKeyId="LTAI4GFz4pmtrYet71Aqo5cP",
                accessKey="J2Y2nHNdemgUfUC5hgXE6eQwzlmub9",
                project="shihuo-new",
                logstore="shihuo-bigdatalog",
                from_time="{}+08:00".format("2021-09-28 03:11:00"),
                to_time="{}+08:00".format("2021-09-28 15:39:22"),
                query="* and msg: r{}$##$c0".format(data),
                reverse=False,
            )

            aliyun = LogClient(
                endpoint=aliyun_conf["endpoint"], accessKeyId=aliyun_conf["accessKeyId"],
                accessKey=aliyun_conf["accessKey"]
            )

            logs = aliyun.get_log(project=aliyun_conf["project"], logstore=aliyun_conf["logstore"],
                                  from_time=aliyun_conf["from_time"], to_time=aliyun_conf["to_time"], topic='',
                                  query=aliyun_conf["query"], size=10, offset=0, reverse=True)
            for log in logs.body:
                try:
                    log = log["msg"].split("上报数据:")[1]
                    log = json.loads(log.split("  result")[0])
                    for i in log:
                        if i["brand"] == brand_data:
                            result_dict[i["id"]] = json.loads(i["extra_info"])["tag_rule"]
                        else:
                            pass
                except Exception as e:
                    print(e)
                result.append(copy.deepcopy(result_dict))
                result_dict.clear()
            return result

        for j in self.excel_high_fee_tag_0:
            result_list = get_aliyun_log(j)
            for result in result_list:

                for k,v in result.items():
                    tag_rule = v
                    pid = k
                for i in range(len(tag_rule)):
                    if tag_rule[i]["tag_name"] == "high_fee_tag_0":
                        flag = True
                        if int(tag_rule[i]["weight"]) == 10:
                            hit_number = hit_number+1
                        else:
                            errer_list_1.append("brand_id {}胖消息推送的tag_name是{},weight 是{}".format(i,tag_rule[i]["tag_name"],tag_rule[i]["weight"]))
                    else:
                        pass

                if flag == False:
                    errer_list_2.append(int(pid[1:]))
                else:
                    pass

                flag = False

        for j in self.excel_high_fee_tag_1:
            result_list = get_aliyun_log(j)
            for result in result_list:
                for k,v in result.items():
                    tag_rule = v
                    pid = k

                for i in range(len(tag_rule)):
                    if tag_rule[i]["tag_name"] == "high_fee_tag_1":
                        flag = True
                        if int(tag_rule[i]["weight"]) == 7:
                            hit_number = hit_number+1
                        else:
                            errer_list_1.append("brand_id {} 胖消息推送的tag_name是 {} ,weight 是 {} ".format(i,tag_rule[i]["tag_name"],tag_rule[i]["weight"]))
                    else:
                        pass

                if flag == False:
                    errer_list_2.append(int(pid[i:]))
                else:
                    pass

                flag = False

        for j in self.excel_high_fee_tag_2:
            result_list = get_aliyun_log(j)
            for result in result_list:
                for k,v in result.items():
                    tag_rule = v
                    pid = k
                for i in range(len(tag_rule)):
                    if tag_rule[i]["tag_name"] == "high_fee_tag_2":
                        flag = True
                        if int(tag_rule[i]["weight"]) == 5:
                            hit_number = hit_number+1
                        else:
                            errer_list_1.append("brand_id {}胖消息推送的tag_name是{},weight 是{}".format(i,tag_rule[i]["tag_name"],tag_rule[i]["weight"]))
                    else:
                        pass

                if flag == False:
                    errer_list_2.append(int(pid[1:]))
                else:
                    pass

                flag = False

        if self.brand_len == hit_number:
            pass
        else:
            print(errer_list_1)
            print(errer_list_2)


if __name__ == '__main__':
    test = Tapd_test_ID1116587()
    test.to_Excel_barnd_list()
    test.match()
    test.toutiao_tag_hit_match()