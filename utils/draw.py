import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

from .constants import BODY_PARTS, KEYPOINTS_NUM, CONNECTIONS

def draw_image_with_keypoints(image_path, keypoints):
    image = cv.imread(image_path)
    
    colors = [(0, 0, 255), (255, 0, 0)]
    c = 0

    for keypoint_set in keypoints:
        for i in range(KEYPOINTS_NUM):
            x = int(keypoint_set[i][0])
            y = int(keypoint_set[i][1])
            cv.circle(image, (x, y), 3, colors[c], -1)  
            
        for connection in CONNECTIONS:
            part_a = BODY_PARTS.index(connection[0])
            part_b = BODY_PARTS.index(connection[1])

            if keypoint_set[part_a][2] > 0.5 and keypoint_set[part_b][2] > 0.5:
                x1 = int(keypoint_set[part_a][0])
                y1 = int(keypoint_set[part_a][1])
                x2 = int(keypoint_set[part_b][0])
                y2 = int(keypoint_set[part_b][1])
                cv.line(image, (x1, y1), (x2, y2), colors[c], 2)
                
        c += 1
        
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.show()
    
def draw_probability_bars(image, prob_dict):
    top_items = sorted(prob_dict.items(), key=lambda x: x[1], reverse=True)[:5]
    num_bars = len(top_items)
    
    bar_height = 20
    gap = 10
    inner_margin = 10 
    
    chart_height = inner_margin + num_bars * bar_height + (num_bars - 1) * gap + inner_margin
    
    chart_width = 350
    
    chart_img = np.ones((chart_height, chart_width, image.shape[2]), dtype=np.uint8) * 255
    
    max_bar_length = chart_width - 2 * inner_margin - 200
    
    max_label, _ = top_items[0]
    
    for idx, (label, prob) in enumerate(top_items):
        bar_length = int(prob * max_bar_length)
        y = inner_margin + idx * (bar_height + gap)
        color = (0, 0, 255) if label == max_label else (255, 0, 0)
        cv.rectangle(chart_img, (inner_margin, y), (inner_margin + bar_length, y + bar_height), color, -1)
        text = f"{label}: {prob*100:.1f}%"
        cv.putText(chart_img, text, (inner_margin + max_bar_length + 5, y + bar_height - 5),
                    cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)
    
    ext_margin = 10
    h, w, _ = image.shape
    
    x_offset = w - chart_width - ext_margin
    y_offset = h - chart_height - ext_margin
    
    output_img = image.copy()
    output_img[y_offset:y_offset+chart_height, x_offset:x_offset+chart_width] = chart_img
    
    return output_img