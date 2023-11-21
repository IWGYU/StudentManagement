from os import system

from model.Certification import Certification
from model.Student import Student
from model.StudentC import StudentC


class Menu:
    @staticmethod
    def menuChoice():
        system('clear')
        print("""Chức năng:
        1.Thêm mới thí sinh
        2.Tìm kiếm thí sinh theo SBD
        3.Tìm kiếm thí sinh theo CCCD
        4.Sửa thông tin thí sinh
        5.Xóa thí sinh
        6.Hiển thị danh sách thí sinh có điểm từ thấp đến cao
        7.Hiển thị danh sách thí sinh có điểm từ cao đến thấp
        8.Hiển thị danh sách thí sinh đạt học bổng
        9.Hiển thị danh sách thí sinh không liệt môn nào
        0. Thoát""")

    @staticmethod
    def addStudentChoice():
        system('clear')
        print('''
        1. Thí sinh khối C
        2. Thí sinh khối D
        0. Quay lại
        ''')

    def inputStudentInfo(self):
        si = int(input('Nhập số CCCD: '))
        sn = int(input('Nhập số SBD: '))
        name = str(input('Nhập họ và tên: '))
        address = str(input('Nhập địa chỉ: '))
        cert = None
        has_cert = str(input('Có chứng chỉ tiếng Anh? (y/n)').lower().strip())
        if has_cert == 'y':
            cert_type = str(input('Nhập loại chứng chỉ (toeic/ielts): '))
            cert_score = float(input('Nhập số điểm: '))
            cert = Certification(cert_type, cert_score)
        elif has_cert == 'n':
            pass
        else:
            raise ValueError


    # @staticmethod
    # def chooseAddStudentOption():
    #     choice = int(input('Lựa chọn khối sinh viên muốn thêm: '))
    #     match choice:
    #         case 1:
    #
    #
    # @staticmethod
    # def chooseOption():
    #     choice = int(input('Lựa chọn chức năng: '))
    #     match choice:
    #         case 1:

