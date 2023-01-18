# 일반 FTP
import ftplib

# SFTP
import paramiko

host = "112.175.184.60"  # example, 실제 접속할 주소를 입력하세요
userId = "picolfs"  # example
password = "dydrndqkswja1125#"  # example

SFTP = False

if SFTP:
    # 변수를 선언해주고 초기 설정을 합니다.

    transprot = paramiko.transport.Transport(host, 22)  # 두 번째 인자는 port number

    # 연결
    transprot.connect(username=userId, password=password)
    sftp = paramiko.SFTPClient.from_transport(transprot)

    # Upload - 파일 업로드
    remotepath = "remote_trash_icon.md"  # sftp에 업로드 될때 파일 경로와 파일이름(이렇게 저장이 됨)을 써줍니다.
    localpath = "./README.md"  # local피시의 파일 경로와 파일이름(pc에 저장되어있는 파일이름)을 써줍니다.
    sftp.put(localpath, remotepath)

    # Get - 파일 다운로드
    sftp.get(
        remotepath, localpath
    )  # 위에 put과 반대로 생각하면 됩니다. remotepath에 sftp경로와 filename을 맞춰주시고, localpath에 다운로드 원하는 파일경로와 filenmae...

    # Close - 꼭 닫아줍시다.
    sftp.close()
    transprot.close()

else:
    session = ftplib.FTP()
    session.connect(host, 21)  # 두 번째 인자는 port number
    session.encoding = "utf-8"
    session.login(userId, password)  # FTP 서버에 접속

    # 읽기 모드로 FTP 서버로 올릴 파일 열기
    uploadfile = open("./README.md", mode="rb")
    # 파일 업로드
    session.storbinary("STOR " + "./pico-lfs/README.md", uploadfile)

    uploadfile.close()  # 파일 닫기

    session.quit()  # 서버 나가기

print("파일전송 완료")
