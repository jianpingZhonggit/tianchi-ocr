import json
import numpy as np
import pandas as pd
result_list = ['yolov5l.json', 'yolov5x.json']
result = []


def py_cpu_nms(dets, thresh):
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    areas = (y2 - y1 + 1) * (x2 - x1 + 1)
    scores = dets[:, 4]
    keep = []
    index = scores.argsort()[::-1]
    while index.size > 0:
        i = index[0]  # every time the first is the biggst, and add it directly
        keep.append(i)

        x11 = np.maximum(x1[i], x1[index[1:]])  # calculate the points of overlap
        y11 = np.maximum(y1[i], y1[index[1:]])
        x22 = np.minimum(x2[i], x2[index[1:]])
        y22 = np.minimum(y2[i], y2[index[1:]])

        w = np.maximum(0, x22 - x11 + 1)  # the weights of overlap
        h = np.maximum(0, y22 - y11 + 1)  # the height of overlap

        overlaps = w * h
        ious = overlaps / (areas[i] + areas[index[1:]] - overlaps)

        idx = np.where(ious <= thresh)[0]
        index = index[idx + 1]  # because index start from 1
    out = dict()
    for _ in keep:
        out[dets[_][0]] = int(dets[_][5])
    return out


for i in range(len(result_list)):
    result.append(json.load(open(result_list[i])))
file_name = []
file_code = []
for key in result[0]:
    print(key)
    file_name.append(key)
    t = []
    for i in range(len(result_list)):
        for _ in result[i][key]:
            t.append(_)
    t = np.array(t)
    res = ''
    if len(t) == 0:
        res = '1'
    else:
        x_value = py_cpu_nms(t, 0.3)
        for x in sorted(x_value.keys()):
            res += str(x_value[x])
    file_code.append(res)
sub = pd.DataFrame({'file_name': file_name, 'file_code': file_code})
sub.to_csv('./submission-merge.csv', index=False)
