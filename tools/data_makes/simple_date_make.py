'''
@File  :simple_date_make.py
@Author:gaohuajin
@Date  :9/27/211:47 PM
@Desc  :
'''

import jsonpath2
class Simple_date_make:
    def __init__(self,req_data):
        self.collect = req_data["collect"]
        self.output = req_data["output"]
        self.data = req_data["data"]

    def to_result(self):
        if isinstance(self.data,str):
            if self.collect == "keys":
                result = [x.split(":")[0] for x in self.data.split(",")]
            elif self.collect == "values":
                result = [x.split(":")[1] for x in self.data.split(",")]
            else:
                return "数据有误"

            return self.to_rank(result)

        elif isinstance(self.data,list):
            if self.collect == "keys":
                result = [x.split(":")[0] for x in self.data]
            elif self.collect == "values":
                result = [x.split(":")[1] for x in self.data]
            else:
                return "数据有误"
            return self.to_rank(result)
        else:
            result=self.make_json_or_dict()
            return self.to_rank(result)

    def to_rank(self,data):
        result = data
        if self.output == "default":
            return result
        elif self.output == "up":
            result = list(map(float, result))
            return sorted(result, reverse=False)
        elif self.output == "down":
            result = list(map(float, result))
            return sorted(result, reverse=True)
        else:
            return "数据有误"

    def make_json_or_dict(self):
        result = []
        if self.collect != "keys" and self.collect != "values":
            path = self.collect
            match_data = jsonpath2.Path.parse_str(path)
            for match in match_data.match(self.data):
                result.append(match.current_value)
        else:
            if self.collect == "keys":
                return self.data.keys()
            elif self.collect == "values":
                return self.data.values()
            else:
                return "数据有误"
        return result

if __name__ == '__main__':
    json_data = {
  "scene": "HOME_FEED_RECOMMEND_RANK",
  "userParam": {
    "deviceCode": "d78558079679ab45",
    "deviceType": "ANDROID",
    "location": {
      "province": "上海",
      "city": "上海"
    }
  },
  "categories": [
    {
      "type": "6",
      "rootId": 8
    },
    {
      "type": "6",
      "rootId": 10
    },
    {
      "type": "6",
      "rootId": 23
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 108
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 532
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 326
    },
    {
      "type": "6",
      "rootId": 29,
      "childId": 541
    },
    {
      "type": "6",
      "rootId": 29,
      "childId": 177
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 62
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 546
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 543
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 110
    },
    {
      "type": "6",
      "rootId": 29,
      "childId": 508
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 111
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 183
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 109
    },
    {
      "type": "4",
      "rootId": 29,
      "childId": 232
    },
    {
      "type": "4",
      "rootId": 53,
      "childId": 150
    },
    {
      "type": "6",
      "rootId": 53,
      "childId": 358
    },
    {
      "type": "4",
      "rootId": 53,
      "childId": 54
    },
    {
      "type": "4",
      "rootId": 53,
      "childId": 330
    },
    {
      "type": "4",
      "rootId": 53,
      "childId": 670
    },
    {
      "type": "6",
      "rootId": 53,
      "childId": 148
    },
    {
      "type": "6",
      "rootId": 53,
      "childId": 412
    },
    {
      "type": "6",
      "rootId": 53,
      "childId": 57
    },
    {
      "type": "6",
      "rootId": 53,
      "childId": 352
    },
    {
      "type": "4",
      "rootId": 59
    },
    {
      "type": "4",
      "rootId": 103,
      "childId": 530
    },
    {
      "type": "4",
      "rootId": 186
    },
    {
      "type": "4",
      "rootId": 188,
      "childId": 192
    },
    {
      "type": "4",
      "rootId": 188,
      "childId": 382
    },
    {
      "type": "4",
      "rootId": 188,
      "childId": 190
    },
    {
      "type": "4",
      "rootId": 188,
      "childId": 386
    },
    {
      "type": "4",
      "rootId": 188,
      "childId": 194
    },
    {
      "type": "4",
      "rootId": 188,
      "childId": 191
    },
    {
      "type": "4",
      "rootId": 195
    },
    {
      "type": "4",
      "rootId": 201
    },
    {
      "type": "4",
      "rootId": 214
    },
    {
      "type": "4",
      "rootId": 224
    },
    {
      "type": "4",
      "rootId": 228
    },
    {
      "type": "4",
      "rootId": 261
    },
    {
      "type": "4",
      "rootId": 305
    },
    {
      "type": "4",
      "rootId": 338
    },
    {
      "type": "4",
      "rootId": 377,
      "childId": 469
    },
    {
      "type": "4",
      "rootId": 377,
      "childId": 466
    },
    {
      "type": "4",
      "rootId": 377,
      "childId": 467
    },
    {
      "type": "4",
      "rootId": 377,
      "childId": 468
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 652
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 622
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 653
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 620
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 609
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 616
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 619
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 612
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 706
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 615
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 707
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 611
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 608
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 618
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 623
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 605
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 607
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 604
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 603
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 621
    },
    {
      "type": "4",
      "rootId": 413,
      "childId": 726
    },
    {
      "type": "6",
      "rootId": 458
    },
    {
      "type": "4",
      "rootId": 463
    },
    {
      "type": "4",
      "rootId": 464
    },
    {
      "type": "4",
      "rootId": 465
    },
    {
      "type": "4",
      "rootId": 495
    },
    {
      "type": "4",
      "rootId": 515,
      "childId": 531
    },
    {
      "type": "4",
      "rootId": 516,
      "childId": 525
    },
    {
      "type": "6",
      "rootId": 517,
      "childId": 524
    },
    {
      "type": "6",
      "rootId": 537
    },
    {
      "type": "4",
      "rootId": 568,
      "childId": 660
    },
    {
      "type": "4",
      "rootId": 568,
      "childId": 651
    },
    {
      "type": "4",
      "rootId": 568,
      "childId": 661
    },
    {
      "type": "4",
      "rootId": 568,
      "childId": 569
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 581
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 646
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 596
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 582
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 595
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 583
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 578
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 580
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 648
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 647
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 594
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 579
    },
    {
      "type": "4",
      "rootId": 577,
      "childId": 593
    },
    {
      "type": "4",
      "rootId": 584,
      "childId": 585
    },
    {
      "type": "4",
      "rootId": 584,
      "childId": 586
    },
    {
      "type": "4",
      "rootId": 587,
      "childId": 588
    },
    {
      "type": "4",
      "rootId": 587,
      "childId": 589
    },
    {
      "type": "4",
      "rootId": 587,
      "childId": 591
    },
    {
      "type": "4",
      "rootId": 587,
      "childId": 590
    },
    {
      "type": "4",
      "rootId": 587,
      "childId": 602
    },
    {
      "type": "4",
      "rootId": 587,
      "childId": 592
    },
    {
      "type": "4",
      "rootId": 624
    },
    {
      "type": "4",
      "rootId": 658
    },
    {
      "type": "4",
      "rootId": 720,
      "childId": 721
    },
    {
      "type": "4",
      "rootId": 770
    }
  ],
  "pageParam": {
    "pageNum": 2,
    "pageSize": 10
  },
  "extraInfo": {}
}
    test_data = {"collect":"$.categories[*].rootId","output":"down","data":json_data}
    run = Simple_date_make(test_data)
    print(run.to_result())