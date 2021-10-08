# coding=GBK

'''
@File  :test_tapd_ID1105085.py
@Author:gaohuajin
@Date  :9/27/2111:20 AM
@Desc  :
'''
import json,copy,pandas

class Test_tapd_ID1105085:
    def __init__(self):
        self.reuslt_json = {
            "status": 0,
            "msg": "操作成功",
            "data": {
                "keywords": [{
                    "category_id": 10000,
                    "href": "",
                    "name": "篮球鞋",
                    "position": 1
                }, {
                    "category_id": 10000,
                    "href": "",
                    "name": "闪现3",
                    "position": 2
                }, {
                    "category_id": 10000,
                    "href": "",
                    "name": "gap",
                    "position": 3
                }, {
                    "category_id": 10000,
                    "href": "",
                    "name": "外套女",
                    "position": 4
                }, {
                    "category_id": 10000,
                    "href": "",
                    "name": "天选2",
                    "position": 5
                }, {
                    "category_id": 10000,
                    "href": "",
                    "name": "双肩包",
                    "position": 6
                }, {
                    "category_id": 10000,
                    "href": "",
                    "name": "帽子",
                    "position": 7
                }, {
                    "category_id": 10000,
                    "href": "",
                    "name": "刷酸祛痘",
                    "position": 8
                }]}}

    def get_all_collection_id_list(self):
        soaring_list = []
        soaring = {
            "id": 0,
            "name": "千元爆款手机",
            "auxiliary_keywords": "性价比屠夫",
            "img": "https://shihuo.hupucdn.com/admin/imgs/20210427/19593a92d1ce7d35ec952abc5d9ca3a8_800x800.png",
            "sort": 0,
            "ctime": 0,
            "etime": 0,
            "href": "shihuo://www.shihuo.cn?route=RNProgram\u0026miniId=Shihuo_NewCategory\u0026page=BrandGoodsSet\u0026options=%7B%22collection_id%22%3A%22635%22%7D",
            "state": 0,
            "category_id": 0,
            "is_top": 0,
            "expose_key": ".bq.home.home.increase_words.0..1058618.千元爆款手机.38.."
        }
        pd = pandas.read_csv("/Users/gaohuajin/Downloads/3287bb81-5443-40e1-99bc-2bdd3d8085ef (1).csv",low_memory=False)
        pd_list = pd.values.tolist()
        for i in range(0,926):
            soaring["id"] = 0
            soaring["name"] = pd_list[i][1]
            try:
                auxiliary_keywords = float(pd_list[i][2])
                if auxiliary_keywords != auxiliary_keywords:
                    soaring["auxiliary_keywords"] = ""
                else:
                    pass
            except:
                soaring["auxiliary_keywords"] = pd_list[i][2]

            soaring[
                "img"] = "https://shihuo.hupucdn.com/admin/imgs/20210427/19593a92d1ce7d35ec952abc5d9ca3a8_800x800.png"
            soaring["sort"] = 0
            soaring["ctime"] = 0
            soaring["etime"] = 0
            soaring["state"] = 0
            soaring["category_id"] = 0
            soaring["is_top"] = 0
            soaring["expose_key"] = ".bq.home.home.increase_words.0..1058618.千元爆款手机.38.."
            soaring[
                "href"] = "shihuo://www.shihuo.cn?route=RNProgram\u0026miniId=Shihuo_NewCategory\u0026page=BrandGoodsSet\u0026options=%7B%22collection_id%22%3A%22{}%22%7D".format(pd_list[i][0])

            soaring_list.append(copy.deepcopy(soaring))
            soaring.clear()

        self.reuslt_json["data"]["soaring"] = soaring_list

        with open("/Users/gaohuajin/Downloads/test0916.txt","w") as f:
            f.write(json.dumps(self.reuslt_json))

if __name__ == '__main__':
    run = Test_tapd_ID1105085()
    run.get_all_collection_id_list()