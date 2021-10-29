"""
파일명 : addressbook.py
프로그램 설명 : 주소록 관리 프로그램
"""

filename  = "addressbook.txt"      # 주소록 원본 파일
filename2 = "addressbook.txt.tmp"  # 주소록 임시 파일

# 1. 주소록 추가
def add_addr():
    """사용자 추가 함수"""
    print("----- 사용자 추가 -----")

    # 사용자 정보를 입력하는 부분
    name  = input('이름: ')
    phone = input('전화번호: ')
    email = input('이메일: ')

    # 사용자 정보를 파일에 저장하는 부분
    f = open(filename, 'a')
    f.write(f'{name}\t{phone}\t{email}\n')
    f.close()
    print(f'{name} 사용자를 추가했습니다.')

# 2. 주소록 확인
def view_addr():
    """사용자 확인 함수"""
    print("----- 사용자 확인 -----")

    # 파일에서 사용자 정보를 읽어서 화면에 출력하는 부분
    f = open(filename, 'r')
    print(f.read())
    f.close()

# 3. 주소록 검색
def search_addr():
    """사용자 검색 함수"""
    print("----- 사용자 검색 -----")

# 4. 주소록 삭제
def del_addr():
     """사용자 삭제 함수"""
     print("----- 사용자 삭제 -----")

# 5. 주소록 도움말
def help_addr():
    """주소록 도움말 함수"""
    print("----- 주소록 도움말 -----")

# 6. 주소록 프로그램 정보
def about_addr():
    """주소록 프로그램 정보 함수"""
    print("----- 주소록 프로그램 정보 -----")

# 메뉴
def menu_addr():
    """주소록 프로그램 메뉴"""
    menu  = '1. 주소록 추가\n'
    menu += '2. 주소록 확인\n'
    menu += '3. 주소록 검색\n'
    menu += '4. 주소록 삭제\n'
    menu += '5. 주소록 도움말\n'
    menu += '6. 주소록 프로그램 정보\n'
    menu += 'q. 프로그램 종료\n'

    print(menu)

while True:
    # 메뉴 출력
    menu_addr()

    # 메뉴 입력
    x = input('선택 >>> ')

    # 메뉴 체크
    if   x == '1':  # 주소록 추가
        add_addr()
    elif x == '2':  # 주소록 확인
        view_addr()
    elif x == '3':  # 주소록 검색
        search_addr()
    elif x == '4':  # 주소록 삭제
        del_addr()
    elif x == '5':  # 주소록 도움말
        help_addr()
    elif x == '6':  # 주소록 프로그램 정보
        about_addr()
    elif x == 'q':  # 프로그램 종료
        break
    else:           # 그외의 모든 키
        print('1 ~ 6 or q 중에서 입력해야 합니다.')

print('주소록 프로그램을 종료합니다!!!')
-- addressbook.py --
