# serving_practice
1. Overview
- Model serving practice using framework tools.
- Framework : [FastAPI](github.com/fastapi/fastapi), [BentoML](github.com/bentoml/BentoML), [Airflow](github.com/apache/airflow)
- Other Tools : [Poetry](github.com/python-poetry/poetry), [Pydantic](github.com/pydantic/pydantic), [Docker](github.com/docker/docker-py), [Gradio](github.com/gradio-app/gradio), [Poetry](github.com/python-poetry/poetry)
- BentoML은 docker, k8s와 연계되며 ML 배포 관리에 특화된 Open-Source framework 입니다.

2. Goal
- Web framework인 FastAPI, BentoML에 대해서 학습하는 것을 목표로 합니다.
- 우선 FastAPI(low-level)에 대해서 학습하고 (강의에서 권장된 내용), 익숙해진 뒤에 BentoML(high-level)을 학습합니다.
- 이전에 학습했던 gradio, docker, dstack를 활용해 간단한 프로젝트를 배포 가능한 단계로 경험해보는 것이 기본 목표입니다.

3. FastAPI의 단점
- GPU resource에 대한 유연한 상호작용이 어려움. (BentoML은 orchesrator를 통해 자동으로 관리)
- 따라서 다중 접속자가 발생한 경우에 대한 대응이 어려움. (GPU 부족하면 CPU 연산으로 돌려버려서 느려진다.)
- BentoML은 schedular를 지원해서 대기열 방식으로 이를 해결함.

4. BentoML 장점 : Model serving 통합 환경 제공
- 모델의 버전 별로 메타 데이터를 체계적으로 기록해줌.
- 기록된 내용은 Git처럼 버전 관리가 가능함.
- A/B test, Ensemble을 위한 유연한 구조로 설계됨.

5. BentoML 장점 : 대시보드 기능
- OpenAI Swagger UI를 활용해 모니터링 및 대시보드 기능 제공함.

9. Read more
- [Official Bento Tutorial](https://docs.bentoml.com/en/latest/examples/overview.html) : BentoML 공식 문서입니다.
- [BentoML guide - tistory](m.blog.naver.com/wooy0ng/223112039717) : FastAPI의 한계와 BentoML의 강점에 대해서 다룹니다.
- [Boostcamp-AI-Tech-Product-Serving](github.com/zzsza/Boostcamp-AI-Tech-Product-Serving) : Boostcamp AI Tech 강의 실습용 자료입니다.


## Claude : BentoML vs FastAPI
Q. GradCAM을 활용해 Segmentation model을 개발한 뒤에 이를 서빙해보고 싶어. 둘 중에서 어떤 도구가 더 좋을까?

 A. 이 시나리오에서는 BentoML이 더 적합할 것 같습니다. 그 이유를 상세히 설명드리겠습니다
1. ML 모델 서빙 특화 : GradCAM과 같은 딥러닝 모델을 위한 특화된 서빙 인프라 제공
이미지 처리, 딥러닝 모델 배포에 최적화된 기능들이 내장되어 있음

2. 모델 관리 기능 : 모델 버전 관리, 모델 메타데이터 추적, 쉬운 패키징 및 배포 프로세스

3. 통합 용이성 : TensorFlow, PyTorch 등 다양한 딥러닝 프레임워크와 원활한 통합. NumPy, OpenCV 등 이미지 처리 라이브러리와도 쉽게 연동 가능

4. 추가 장점 : 모델 성능 모니터링, 자동 스케일링 지원, 컨테이너 환경(Docker, Kubernetes)에 쉬운 배포

반면 FastAPI는:

- 웹 API 개발에는 탁월하지만, ML 모델 서빙에 필요한 특화된 기능이 상대적으로 부족하며 추가 설정과 커스터마이징 필요

따라서 GradCAM 기반 딥러닝 모델 서빙에는 BentoML을 강력히 추천드립니다.