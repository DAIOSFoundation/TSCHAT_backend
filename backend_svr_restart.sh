#!/bin/bash

# 장고 서버 프로세스를 찾습니다.
# 여기서는 'manage.py runserver' 명령어를 사용하여 실행된 장고 서버 프로세스를 찾습니다.
# 필요에 따라 다른 명령어나 프로세스 이름을 사용할 수 있습니다.
process=$(ps aux | grep 'manage.py runserver' | grep -v grep | awk '{print $2}')

# 찾은 프로세스가 있다면 종료시킵니다.
if [ -n "$process" ]; then
    echo "장고 서버 프로세스를 종료합니다."
    kill -9 $process
    echo "장고 서버 종료 완료."
else
    echo "장고 서버 프로세스를 찾을 수 없습니다."
fi


# 장고 프로젝트의 디렉토리로 이동
cd ~/TSCHAT_BACKEND

# 필요한 환경 변수 설정 (예: 가상 환경 활성화)
source chat_venv/bin/activate

# 장고 서버를 백그라운드에서 실행하고, 출력을 로그 파일로 리디렉션
nohup chat_venv/bin/python3.11 manage.py runserver 0.0.0.0:8443 &> ~/TSCHAT_BACKEND/logfile.log &

echo "장고 서버가 백그라운드에서 실행되었습니다."
