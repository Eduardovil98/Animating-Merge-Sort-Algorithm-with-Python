# ///////////////////////////////////////////////////////////////
#
# BY: EDUARDO VILCHIS MARIN
# PROJECT MADE WITH: Qt Designer and PySide6
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
from widgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.anim_group = None
        self.new_numbers()
        # >> Set connections
        self.connections()
    #
    def new_numbers(self):
        # >> CHECK IF ANIMATION IS RUNNING
        if self.anim_group:
            self.anim_group.stop()
        # >> VARIABLES
        self.del_labels = []
        self.levels = {}
        self.labels = []
        self.numbers = []
        self.label_numbers = {}
        for label in self.ui.frame_2.findChildren(QLabel):
            # >> SET DEFAULT COLOR
            label.setStyleSheet('background-color: rgb(255, 0, 0);')
            # >> FILTER NUMBER
            number = int(re.findall(r'\d+', label.text())[0])
            if number in self.numbers or label.pos().y() != 40: continue
            self.numbers.append(number)
            self.label_numbers[number] = label
            self.labels.append(label)
        # >> REMOVE TEMPORAL LABELS
        label_names = list(map(lambda label: label.objectName(), self.labels))
        for label in self.ui.frame_2.findChildren(QLabel):
            if not label.objectName() in label_names:
                label.close()
    # >> SET CONNECTIONS
    def connections(self):
        self.ui.pushButton.clicked.connect(self.change_numbers)
        self.ui.pushButton_2.clicked.connect(self.animation)
    #
    def change_numbers(self):
        self.new_numbers()
        self.numbers = list(range(1, 9))
        random.shuffle(self.numbers)
        self.label_numbers = {}
        for i in range(len(self.numbers)):
            self.labels[i].setText(f'<html><head/><body><p align="center">{self.numbers[i]}</p></body></html>')
            self.label_numbers[self.numbers[i]] = self.labels[i]
        label_names = list(map(lambda label: label.objectName(), self.labels))
        for label in self.ui.frame_2.findChildren(QLabel):
            if not label.objectName() in label_names:
                label.close()
    #
    def animation(self):
        self.new_numbers()
        self.margin = 40
        self.step = {}
        self.merge_sort(self.numbers, self.step)
        self.animacion_index = 1
        self.current_index = 0
        # STAR THE FIRST ANIMATION
        self.animar_siguiente()
    # >>
    def get_label_num(self, pos_y):
        labels = {}
        # >> SELECT BEFORE GROUP
        current_position = pos_y - 90
        group_labels = self.levels[current_position]
        for number, label in group_labels.items():
            pos_x = label.pos().x()
            labels[pos_x] = {"label": label, "number": number}
        inds = list(labels.keys())
        inds.sort()
        label_selected = labels[inds[0]]
        # >> REMOVE LABEL SELECTED
        del group_labels[label_selected.get("number")]
        return label_selected.get("label")
    def get_first_level(self):
        labels = {}
        for i, label in enumerate(self.labels):
            pos_x = label.pos().x()
            labels[pos_x] = {"label": label, "number": i}
        inds = list(labels.keys())
        inds.sort()
        label_selected = labels[inds[0]]
        self.labels.pop(label_selected.get("number"))
        return label_selected.get("label")
    # >>
    def animar_siguiente(self):
        for label in self.del_labels:
            label.close()
        if self.animacion_index < len(self.step) + 1:
            current_numbers = self.step[self.animacion_index].get('array')
            self.del_labels = []
            current_size = len(current_numbers)
            direction = self.step[self.animacion_index].get('direction')
            self.anim_group = QParallelAnimationGroup()
            for i, number in enumerate(current_numbers):
                self.current_index += i
                current_label = self.label_numbers[number]
                # >> Get position (X, Y)
                x, y = current_label.pos().x(), current_label.pos().y()
                # >> Create new label
                if direction == 1:
                    self.new_label = QLabel(f'<html><head/><body><p align="center">{number}</p></body></html>', self.ui.frame_2)
                    font = QFont()
                    font.setPointSize(15)
                    font.setBold(True)
                    self.new_label.setFont(font)
                    self.new_label.setGeometry(x, y, 50, 50)
                    self.new_label.setStyleSheet('background-color: rgb(255, 0, 0);')
                    self.new_label.show()
                    if y in self.levels:
                        self.levels[y][number] = current_label
                    else:
                        self.levels[y] = {number: current_label}
                else:
                    self.new_label = current_label
                    self.new_label.setStyleSheet('background-color: rgb(0, 255, 0);')
                    label_selected = self.get_label_num(pos_y=self.new_label.pos().y())
                    x, y = label_selected.pos().x(), label_selected.pos().y()
                    self.del_labels.append(label_selected)
                # >> Replace previous label
                self.label_numbers[number] = self.new_label
                # >> Set parameter animation
                self.anim = QPropertyAnimation(self.new_label, b"pos")
                if self.animacion_index % 2 == 0:
                    if direction == 1:
                        self.anim.setEndValue(QPoint(x + self.margin, y + 90))
                    else:
                        self.anim.setEndValue(QPoint(x, y))
                else:
                    if direction == 1:
                        self.anim.setEndValue(QPoint(x - self.margin, y + 90))
                    else:
                        self.anim.setEndValue(QPoint(x, y))
                self.anim.setDuration(1500)
                self.anim_group.addAnimation(self.anim)
            self.anim_group.finished.connect(self.animar_siguiente)
            self.animacion_index += 1
        else:
            self.anim_group = QParallelAnimationGroup()
            for i, number in enumerate(self.numbers):
                new_label = self.label_numbers[number]
                new_label.setStyleSheet('background-color: rgb(0, 255, 0);')
                label_selected = self.get_first_level()
                x, y = label_selected.pos().x(), label_selected.pos().y()
                self.del_labels.append(label_selected)
                # >> Set parameter animation
                self.anim = QPropertyAnimation(new_label, b"pos")
                self.anim.setEndValue(QPoint(x, y))
                self.anim.setDuration(1500)
                self.anim_group.addAnimation(self.anim)
        self.anim_group.start()
    # Del labels
    def __del_labels(self):
        for label in self.del_labels:
            label.close()
    # Algorithm Merge Sort
    def merge_sort(self, arr, step):
        if len(arr) > 1:
            # Split the list into two halves
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            step[len(step) + 1] = {"array": L.copy(), "direction": 1}
            step[len(step) + 1] = {"array": R.copy(), "direction": 1}
            # Sort the two halves
            self.merge_sort(L, step)
            self.merge_sort(R, step)
            if len(L) != 1:
                step[len(step) + 1] = {"array": L.copy(), "direction": 0}
            if len(R) != 1:
                step[len(step) + 1] = {"array": R.copy(), "direction": 0}
            i = j = k = 0
            # Copy temporary data from L and R back to arr
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            # Check if elements were left in L
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            # Check if elements were left in R
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("fusion"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())