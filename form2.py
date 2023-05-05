import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QCheckBox,
                               QVBoxLayout, QDialog)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.resize(300, 100)

        # Create Input widget
        self.inputBox = QLineEdit("")

        # Hide the password characters
        # if 'self.isPasswordVisible' in locals():
        #     print('var is present')
        # else:
        # self.isPasswordVisible = False  # self made variable
        # self.inputBox.setEchoMode(QLineEdit.Normal)

        # Create Submit Button widget
        self.submitButton = QPushButton("Submit")

        # Create Password Visibility Button widget
        self.toggleVisibilityButton = QPushButton("Show/Hide Password")

        # Create Password Visibility Checkbox widget
        self.toggleVisibilityCheckbox = QCheckBox("Show Password")
        self.toggleVisibilityCheckbox.setChecked(False)
        if (self.toggleVisibilityCheckbox.isChecked() == False):
            self.inputBox.setEchoMode(QLineEdit.Password)
        elif (self.toggleVisibilityCheckbox.isChecked() == True):
            self.inputBox.setEchoMode(QLineEdit.Normal)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.inputBox)
        # layout.addWidget(self.toggleVisibilityButton)
        layout.addWidget(self.toggleVisibilityCheckbox)
        layout.addWidget(self.submitButton)

        # Set dialog layout
        self.setLayout(layout)

        # Add a function to button when clicked
        self.submitButton.clicked.connect(self.submitPassword)
        self.toggleVisibilityCheckbox.toggled.connect(
            self.toggleVisibilityOnChecked)
        # self.toggleVisibilityButton.clicked.connect(self.toggleVisibility)

    # Toggles visibility of the password

    def toggleVisibilityOnChecked(self):
        # print(checkedButton.isChecked())

        isChecked = self.sender().isChecked()
        if isChecked == True:
            self.sender().setChecked(False)

        elif isChecked == False:
            self.sender().setChecked(True)

    # def toggleVisibility(self):
    #     if self.isPasswordVisible == True:
    #         self.inputBox.setEchoMode(QLineEdit.Password)
    #         print('now password is hidden')
    #         self.isPasswordVisible == False

    #     elif self.isPasswordVisible == False:
    #         self.inputBox.setEchoMode(QLineEdit.Normal)
    #         print('now password is shown')
    #         self.isPasswordVisible == True

    # Submits the password

    def submitPassword(self):
        # print(f"Hello {self.inputBox.text()}")
        print(f"Text is {self.inputBox.text()}")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
