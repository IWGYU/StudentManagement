import os

from controller.StudentController import StudentController

class Menu:
    controller = StudentController()
    
    @staticmethod
    def menuChoice() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
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
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
        1. Thí sinh khối C
        2. Thí sinh khối D
        0. Quay lại
        ''')

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

