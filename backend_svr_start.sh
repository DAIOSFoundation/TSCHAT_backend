#!/bin/bash

# 장고 프로젝트의 디렉토리로 이동
cd ~/TSCHAT_BACKEND

# 필요한 환경 변수 설정 (예: 가상 환경 활성화)
source chat_venv/bin/activate

# 장고 서버를 백그라운드에서 실행하고, 출력을 로그 파일로 리디렉션
nohup chat_venv/bin/python3.11 manage.py runserver 0.0.0.0:8443 &> ~/TSCHAT_BACKEND/logfile.log &

echo "장고 서버가 백그라운드에서 실행되었습니다."
