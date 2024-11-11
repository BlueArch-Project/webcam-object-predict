import cv2
import os
import argparse
from ultralytics import YOLO

def run_yolo_inference(camera_index=0, model_path="yolov8n.pt"):
    """
    指定されたカメラデバイスから映像を取得し、YOLOモデルを使用して物体検出を行います。
    検出結果を画面に表示します。

    Parameters:
    camera_index (int): 使用するカメラデバイスのインデックス。デフォルトは0。
    model_path (str): 使用するYOLOモデルのパス。デフォルトは"yolov8n.pt"。

    Returns:
    None
    """
    # モデルを選択
    model = YOLO(model_path)

    # Open the web camera stream
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Error: Could not read frame.")
            break

        k = cv2.waitKey(1)  # 一応キー入力で終了できるようにしておく

        if k != -1:
            break

        results = model(frame)
        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 Inference", annotated_frame)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # コマンドライン引数を解析
    parser = argparse.ArgumentParser(description="YOLOv8 Inference with Webcam")
    parser.add_argument("--camera_index", type=int, default=0, help="使用するカメラデバイスのインデックス")
    parser.add_argument("--model_path", type=str, default="yolov8n.pt", help="使用するYOLOモデルのパス")
    args = parser.parse_args()

    # 関数を呼び出して実行
    run_yolo_inference(camera_index=args.camera_index, model_path=args.model_path)