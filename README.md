# tianchi-ocr
使用yolov5进行目标检测
比赛链接:https://tianchi.aliyun.com/competition/entrance/531795/introduction?spm=5176.12281949.1003.5.493e3eafyUphsY
    本次比赛对街区门牌号识别,在初期可以简单使用目标检测框架(mmdetection,yolo系列)跑个分数,
之后做eda,合理设置anchor(主要针对anchor based方法).最后对于本次比赛我们发现会有很多错检的情况(3vs8,1vs4,7),而仅仅使用nms对结果框
处理是无法除去这些重复框的，我们知道门牌号大部分是水平排布的,因此出现同一个位置(近似)两个类别是不对的,因此选择对所有的候选框做无类别
NMS(全局NMS),此外还可以结合多个模型(将一张图片的所有候选框放一起做NMS,以此弥补各个模型之间的不足,同时利用了各个模型的优势****).此外
也可以尝试对分类标签不再使用one-hoe形式,one-hot只是强调了目标类别和其他类别的差异()
