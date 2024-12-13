import os
from PIL import Image

import gradio as gr
from ultralytics import YOLO


class YOLODetector:
    def __init__(self, model_path=None):
        """ YOLO 모델 가중치 경로 설정(기본값: yolov8x.pt) """
        model_path = model_path or os.getenv("YOLO_MODEL", "yolov8x.pt")
        self.model = YOLO(model_path)

    def detect_objects(self, input_image):
        """
        입력 이미지에 대해 객체 감지 수행
        :param input_image: PIL 이미지 또는 numpy 배열
        :return: 객체 감지가 표시된 이미지
        """
        # 객체 감지 수행
        results = self.model(input_image)

        # 결과 이미지 렌더링
        annotated_image = results[0].plot()

        return annotated_image

def create_gradio_interface():
    """
    Gradio 인터페이스 생성
    """
    # YOLO 모델 초기화
    detector = YOLODetector()

    # Gradio 인터페이스 설정
    interface = gr.Interface(
        fn=detector.detect_objects,
        inputs=gr.Image(type="pil", label="Upload Image"),
        outputs=gr.Image(type="pil", label="Detected Objects"),
        title="YOLO Object Detection",
        description="Upload an image and detect objects using YOLOv8",
    )

    return interface

def main():
    # Gradio 인터페이스 생성 및 실행
    interface = create_gradio_interface()
    interface.launch(
        # Fix server name & port
        server_name="0.0.0.0",
        server_port=7860,
        share=True  # 공개 링크 생성
    )

if __name__ == "__main__":
    main()
