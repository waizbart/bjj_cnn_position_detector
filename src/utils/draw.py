import cv2 as cv
import matplotlib.pyplot as plt

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