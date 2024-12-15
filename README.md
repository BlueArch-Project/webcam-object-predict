# obejct detection inference with Webcam

このプロジェクトは、YOLOv8 モデルを使用して Web カメラからの映像をリアルタイムで処理し、物体検出を行います。

## 必要なライブラリのインストール

以下のコマンドを実行して必要なライブラリをインストールしてください。

```sh
pip install opencv-python ultralytics argparse
```

使用方法
以下のコマンドを実行して、Web カメラからの映像を YOLOv8 モデルで処理します。

```sh
python run_detection.py --camera_index <カメラデバイスのインデックス> --model_path <モデルのパス>
```

引数
--camera_index: 使用するカメラデバイスのインデックス（デフォルトは 0）
--model_path: 使用する YOLO モデルのパス（デフォルトは"yolov8n.pt"）

カメラデバイスのインデックスが 1 で、モデルパスが yolov8n.pt の場合:

```sh
python run_detection.py --camera_index <カメラデバイスのインデックス> --model_path <モデルのパス>
```

```
python3 run_detection.py --camera_index 0  --model_path ./best.pt
```
