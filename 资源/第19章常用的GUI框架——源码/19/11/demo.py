    # 设置单选按钮的选中事件方法
    self.radioButton.toggled.connect(lambda :self.button_state(self.radioButton))
    self.radioButton_2.toggled.connect(lambda :self.button_state(self.radioButton_2))

def button_state(self,button):
    if button.text()=='RadioButton1':  # 判断单选按钮的名称
        if button.isChecked() == True:       # 判断单选按钮是否被选中
            print(button.text()+'已选中！')
        else:
            print(button.text()+'未选中！')

    if button.text()=='RadioButton2':  # 判断单选按钮的名称
        if button.isChecked() == True:       # 判断单选按钮是否被选中
            print(button.text()+'已选中！')
        else:
            print(button.text()+'未选中！')
