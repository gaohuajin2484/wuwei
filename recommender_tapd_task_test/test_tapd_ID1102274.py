'''
@File  :test_tapd_ID1102274.py
@Author:gaohuajin
@Date  :9/27/2111:19 AM
@Desc  :
'''
import json
import requests
import jsonpath2
import copy

class Test_TAPD_ID1102274():
    def __init__(self):
        self.request_body = {
            "scene": "HOME_ICON_LIST_REC",
            "userParam": {
                "deviceType": "IOS",
                "deviceCode": "e2764b9c38367a59997bf287b2b78fb7",
                "sex": ""
            },
            "iconList": []
        }
        self.iconList = []
        self.item= {
            "verticalId": "",
            "originPosition": "",
            "categories": [
                {
                    "rootId": 0,
                    "childId": 0
                }
            ]
        }
        self.lanqiuxie_item = {
            "verticalId": 16,
            "originPosition": 16,
            "categories": [
                {
                    "childId": 9
                }
            ]
        }
        self.tixushan_item = {
            "verticalId": 17,
            "originPosition": 17,
            "categories": [
                {
                    "childId": 11
                }
            ]
        }
        self.youxiyule_item = {
            "verticalId": 18,
            "originPosition": 18,
            "categories": [
                {"childId": 196}, {"childId": 197}, {"childId": 198}, {"childId": 199}, {"childId": 200},
                {"childId": 325}, {"childId": 202}, {"childId": 203}, {"childId": 204}, {"childId": 205},
                {"childId": 207}, {"childId": 209}, {"childId": 210}, {"childId": 211}, {"childId": 212},
                {"childId": 213}, {"childId": 402}, {"childId": 411}, {"childId": 306}, {"childId": 307},
                {"childId": 308}, {"childId": 309}, {"childId": 310}, {"childId": 311}, {"childId": 312},
                {"childId": 313}, {"childId": 371}
            ]
        }
        self.nvzhuang_item = {
            "verticalId": 19,
            "originPosition": 19,
            "categories": [
                {"childId": 11}, {"childId": 19}, {"childId": 20}, {"childId": 21}, {"childId": 22}, {"childId": 39},
                {"childId": 45}, {"childId": 52}, {"childId": 64}, {"childId": 71}, {"childId": 79}, {"childId": 80},
                {"childId": 81}, {"childId": 86}, {"childId": 91}, {"childId": 106}, {"childId": 141}, {"childId": 142},
                {"childId": 144}, {"childId": 176}, {"childId": 395}, {"childId": 404}, {"childId": 442},
                {"childId": 443}, {"childId": 444}, {"childId": 445}, {"childId": 446}, {"childId": 447},
                {"childId": 448}, {"childId": 449}, {"childId": 704}, {"childId": 24}, {"childId": 25}, {"childId": 26},
                {"childId": 27}, {"childId": 28}, {"childId": 40}, {"childId": 65}, {"childId": 83}, {"childId": 146},
                {"childId": 184}, {"childId": 405}, {"childId": 450}, {"childId": 451}, {"childId": 452},
                {"childId": 453}, {"childId": 705}
            ]
        }
        self.categories = []

    def getchuizhiList(self):
        CUIZHI_URL = "https://sh-gateway.shihuo.cn/v4/services/sh-goodsbackendadmin/goodsCategoryBusiness/list"
        chuizhi_data = requests.get(CUIZHI_URL).json()
        leimu_ids = list(self.jsonParse(chuizhi_data, "$.data.list[*].id").values())
        leimu_ids = (','.join([str(i) for i in leimu_ids]))
        LEIMU_URL = "https://sh-gateway.shihuo.cn/v4/services/sh-goodsinnerapi/v2/category/businessType?clientName=test&innerApiToken=26b8109a2184e0b1e3fd5bcd1ba3480d&ids={}".format(leimu_ids)
        lemu_data = requests.get(LEIMU_URL).json()
        for i in lemu_data["data"]:
            self.item["verticalId"] = int(i["id"])
            self.item["originPosition"] = int(i["id"])
            for j in i["category_list"]:
                self.categories.append({"rootId":j["root_category_id"]})
            self.item["categories"] = self.categories
            copy_item = copy.deepcopy(self.item)

            if i["name"] == "鞋类":
                self.iconList.insert(0,copy_item)
            elif i["name"] == "服":
                self.iconList.insert(1,copy_item)
            elif i["name"] == "数码":
                self.iconList.insert(2,copy_item)
            elif i["name"] == "美妆":
                self.iconList.insert(3,copy_item)
            else:
                self.iconList.append(copy_item)
            self.categories.clear()
            self.item.clear()
        self.iconList.append(self.lanqiuxie_item)
        self.iconList.append(self.nvzhuang_item)
        self.iconList.append(self.youxiyule_item)
        self.iconList.append(self.tixushan_item)
        self.request_body["iconList"] = self.iconList

    def jsonParse(self,json_data,path):
        __result = {}

        parse_path = jsonpath2.Path.parse_str(path)

        for match_data in parse_path.match(json_data):
            __result[match_data.node.tojsonpath()] = match_data.current_value

        return __result

    def rankScoreDiff(self):
        hbase_user_Score = "515:0.08,358:0.77,261:0.02,645:0.55,767:0.0,54:0.25,467:0.48,305:0.0,76:0.25,176:0.81,224:0.77,481:0.16,587:0.76,770:0.0,294:0.61,692:0.66,53:1.53,9:0.05,29:0.62,146:0.12,658:0.19,205:0.16,464:0.05,40:0.16,122:0.13,371:0.32,410:0.14,214:0.0,14:4.72,81:0.44,188:0.1,126:0.17,413:0.0,584:0.0,20:2.87,223:0.12,338:0.64,191:0.18,706:0.42,463:0.0,33:1.49,608:0.12,10:3.98,636:0.32,640:0.18,458:0.0,442:0.27,577:0.0,765:0.61,8:6.37,455:0.78,624:0.03,198:1.73,639:0.18,537:0.0,661:0.16,495:0.0,461:0.33,568:0.38,616:0.17,672:0.18,465:0.24,621:0.14,23:0.01,581:0.44,623:0.13,511:0.04,363:0.31,377:0.0,219:0.16,103:0.0,626:0.2,517:0.01,713:0.21,195:2.4,400:0.0,485:0.28,59:0.16,460:0.18,431:0.12,642:0.14,201:0.0,262:0.01,228:0.03,690:0.31,720:0.0,579:0.2,186:0.05,488:0.23,516:0.13,86:0.14,386:0.15,44:0.9,542:0.31,532:0.39,199:0.72,685:0.15,657:0.16,505:0.14,79:0.2,500:0.6,525:0.23,572:0.38,204:0.3,622:0.11,556:0.15,575:0.14,497:0.45,64:0.0,192:0.19,564:1.32,482:0.5,144:0.18,607:0.13,210:0.17,762:0.23,503:0.14,754:0.35,200:0.24,230:0.71,665:0.57,352:0.77,739:0.19,62:0.16,769:0.32,593:0.13,170:0.15,70:0.0,348:0.65,677:0.39,266:0.54,561:0.3,179:0.15,468:0.19,656:0.3,27:0.49,546:0.13,469:0.39,491:0.01,501:0.39,590:0.59,676:0.78,168:0.16,142:0.22,471:0.75,763:0.21,565:0.15,649:0.31,473:0.51,61:0.0,766:0.2,402:0.27,456:1.01,520:0.24,647:0.28,366:0.57,506:0.15,196:0.14,124:0.38,547:0.18,518:0.33,574:0.13,550:0.32,772:1.22,115:0.15,328:0.17,486:0.25,543:0.46,753:0.2,342:0.2,45:3.06,22:0.12,63:0.28,187:0.05,474:0.26,519:0.17,695:0.15,655:0.2,16:0.12,483:0.23,756:0.23,370:0.13,502:0.13,52:0.88,641:0.16,751:0.18,539:0.22,51:0.75,591:0.39,603:0.3,227:0.01,776:0.4,554:0.2,725:0.64,630:0.13,43:1.55,633:0.12,139:0.3,148:0.62,218:0.21,202:1.28,628:0.18,619:0.17,508:0.46,229:0.43,209:0.55,406:0.13,592:1.14,26:0.63,604:0.21,11:0.04,36:0.13,194:0.35,401:1.73,459:1.23,660:0.13,439:0.4,203:1.38,221:0.23,382:0.42,450:0.12,217:0.34,190:0.37,447:0.25,664:0.93,752:2.98,651:0.23,268:0.01,183:0.84,673:0.23,507:0.65,549:0.92,538:0.59,449:0.0,492:0.42,330:0.18,643:0.45,666:0.25,671:0.2,476:0.13,360:0.48,523:1.11,80:0.0,15:0.31,487:0.94,694:0.12,750:0.15,496:0.16,317:0.77,412:0.5,526:0.2,553:0.19,477:0.67,585:0.46,541:0.73,697:0.16,114:0.15,211:0.61,443:0.13,181:0.19,466:0.8,441:0.3,724:0.19,646:0.18,19:0.15,269:0.22,612:0.17,689:0.13,429:0.21,531:0.41,586:0.19,405:0.16,433:0.28,128:0.25,140:0.19,453:0.13,499:0.27,340:2.59,65:0.66,17:0.22,323:0.22,675:0.25,12:0.04,674:0.2,452:0.15,490:0.2,437:0.13,25:0.01,663:0.15,662:0.14,714:0.21,562:0.14,759:0.19,434:0.68,732:0.25"
        hbase_user_Score_list = hbase_user_Score.split(",")
        hbase_user_Score_dict = {}
        for i in hbase_user_Score_list:
            hbase_user_Score_dict[i.split(":")[0]] =i.split(":")[1]
        rec_rank = []
        for i in self.request_body["iconList"]:
            rec_rank.append({i["verticalId"]:self.scoreSum(i["categories"],hbase_user_Score_dict)})

        rec_rank_zip = []
        for i in rec_rank:
            for k,v in i.items():
                rec_rank_zip.append((k,v))
        print(rec_rank_zip)
        rec_rank_zip.sort(key=lambda x:x[1],reverse=True)
        print(rec_rank_zip)

    def scoreSum(self,categories,hbase_user_Score_dict):
        sum = 0
        for i in categories:
            for k,v in i.items():
                try:
                    sum = sum + float(hbase_user_Score_dict[str(v)])
                except:
                    print("{} 召回级没有此类目".format(v))
        return sum



if __name__ == '__main__':
    # run_test = Test_TAPD_ID1102274()
    # run_test.getchuizhiList()
    # run_test.rankScoreDiff()
    # aa = [11,19,20,21,22,39,45,52,64,71,79,80,81,86,91,106,141,142,144,176,395,404,442,443,444,445,446,447,448,449,704,24,25,26,27,28,40,65,83,146,184,405,450,451,452,453,705]
    # bb = {}
    # cc = []
    # for i in aa:
    #     bb["childId"] = i
    #     copy_bb = copy.deepcopy(bb)
    #     cc.append(copy_bb)
    #     bb.clear()
    # print(json.dumps(cc))
    result_11 =[18857634, 1640954, 19142595, 918739, 20668724, 22124039, 1639894, 5287142, 19329551, 22588117, 18703578, 19471309, 19412524, 2820326, 7341192, 944425, 21475507, 592343, 2815772, 22756100, 4742158, 4792012, 2828442, 5484358, 2462938, 19043593, 20541802, 1630759, 19328447, 2491955, 2485058, 2846078, 19960833, 20489508, 22396879, 5855884, 622895, 4879265, 20390380, 2529966, 8949055, 20685415, 2688780, 4512445, 21707536, 9036422, 980555, 20858437, 1338380, 680975, 310391, 2462945, 20738950, 4231110, 1709638, 20740040, 20670172, 22426464, 2577083, 4256666, 5303477, 2774601, 906526, 1707010, 20542062, 4257421, 1566037, 22262032, 4288928, 20400708, 1573076, 7410325, 906864, 4225546, 19469455, 22600108, 5703302, 1711664, 20257198, 20439594, 5651531, 4765917, 288203, 4260921, 23340120, 4778113, 20855244, 4495792, 21627747, 2817217, 2624297, 4765915, 4488912, 184562, 20857195, 766526, 5651773, 2647739, 22841791, 20387468]
    result_12 =[18857634, 1640954, 19142595, 918739, 20668724, 22124039, 1639894, 5287142, 19329551, 22588117, 18703578, 19471309, 19412524, 2820326, 7341192, 944425, 21475507, 592343, 2815772, 22756100, 4742158, 4792012, 2828442, 5484358, 2462938, 19043593, 20541802, 1630759, 19328447, 2491955, 2485058, 2846078, 19960833, 20489508, 22396879, 5855884, 622895, 4879265, 20390380, 2529966, 8949055, 20685415, 2688780, 4512445, 21707536, 9036422, 980555, 20858437, 1338380, 680975, 310391, 2462945, 20738950, 4231110, 1709638, 20740040, 20670172, 22426464, 2577083, 4256666, 5303477, 2774601, 906526, 1707010, 20542062, 4257421, 1566037, 22262032, 4288928, 20400708, 1573076, 7410325, 906864, 4225546, 19469455, 22600108, 5703302, 1711664, 20257198, 20439594, 1563834, 4243937, 5696586, 21624669, 2689632, 22588103, 1710203, 19480645, 2624297, 1297106, 4203151, 19236903, 1533190, 1709538, 5484354, 5651531, 19068287, 2816474, 288203, 19291163, 20886965, 7749295, 22316320, 4253083, 22600086, 1590110, 971651, 4359621, 20775420, 2485096, 2820835, 836010, 20722660, 4211230, 2850091, 5390342, 2535240, 806650, 2637536, 5196158, 4253150, 21530747, 2521968, 1700848, 802698, 4545563, 2556546, 945153, 21474020, 184562, 9109853, 20835218, 20835365, 20745363, 1693250, 2522508, 4480833, 5773945, 19319554, 5225784, 20715323, 1702863, 2594881, 2792982, 22071231, 4260921, 1618199, 22426703, 20857099, 7316507, 2554078, 22396870, 2634923, 2595298, 2459448, 2821547, 2541519, 4238734, 21984526, 20980964, 2497141, 19378239, 975631, 21591196, 4495792, 2462944, 5433445, 4765917, 4801708, 2493532, 20832473, 4787377, 728387, 834895, 1524622, 21612483, 19140904, 19052531, 4253235, 5174565, 602513, 1233938]
    is_equal = []
    is_diff = []

    for i in result_12[0:100]:
        if i in result_11:
            is_equal.append(i)
        else:
            is_diff.append(i)
    print(result_12[99:100])

    print("12路styleid和11路相同的数据有：{},数量是{}".format(is_equal,len(is_equal)))
    print("12路styleid和11路不同的数据有：{},数量是{}".format(is_diff,len(is_diff)))
