# Создание и запуск приложения, программирование интерфейса экранов и действий на них
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test
btn_color = (0, 0.05, 0.8, 1)
# Создадим класс-наследник App. В нём будет дописываться функционал приложения.
name = ''
age = 7
P1 = 0
P2 = 0
P3 = 0
txt_result = name + ', Ваш результат:'
color = (.39, .87, 1, 1)
Window.clearcolor = color

def get_result():
    global name, P1, P2, P3, age
    res = test(P1, P2, P3, age)
    a = str(name + '\n' + res[0] + '\n' + res[1])
    return a

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        txt1 = '[color=#000000]' + txt_instruction + '[/color]'
        lbl = Label(text=txt1, markup=True)
        txt2 = '[color=#000000]' + 'Введите имя:' + '[/color]'
        txt_name = Label(text=txt2, markup=True)
        self.in_name = TextInput(multiline=False)
        txt3 = '[color=#000000]' + 'Введите возраст:' + '[/color]'
        txt_age = Label(text=txt3, markup=True)
        self.in_age = TextInput(multiline=False)
        self.btn1 = ScrButton(self, direction='left', goal='t1', text="Далее")
        self.btn1.background_color = btn_color
        box_name = BoxLayout(orientation='vertical', padding=8, spacing=8)
        box_name.add_widget(txt_name)
        box_name.add_widget(self.in_name)
        box_age = BoxLayout(orientation='vertical', padding=8, spacing=8)
        box_age.add_widget(txt_age)
        box_age.add_widget(self.in_age)
        box1 = BoxLayout(padding=8, spacing=8)
        box1.add_widget(box_name)
        box1.add_widget(box_age)
        box2 = BoxLayout(orientation='vertical', padding=8, spacing=8)
        box2.add_widget(lbl)
        box2.add_widget(box1)
        box2.add_widget(self.btn1)
        self.add_widget(box2)
        self.btn1.on_press = self.next
#        self.next()
    def next(self):
        global age, name
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 't1'

class Test1Scr(Screen):
    def __init__(self, name='t1'):
        super().__init__(name=name)
        txt1 = '[color=#000000]' + 'Первый тест' + '[/color]'
        lbl1 = Label(text=txt1, markup=True)
        txt2 = '[color=#000000]' + txt_test1 + '[/color]'
        lbl2 = Label(text=txt2, markup=True)
        self.in_test1 = TextInput(multiline=False)
        self.btn1 = ScrButton(self, direction='left', goal='t2', text="Далее")
        self.btn1.background_color = btn_color
        box = BoxLayout(orientation='vertical', padding=8, spacing=8)
        box.add_widget(lbl1)
        box.add_widget(lbl2)
        box.add_widget(self.in_test1)
        box.add_widget(self.btn1)
        self.add_widget(box)
        self.btn1.on_press = self.next
    def next(self):
        global P1
        P1 = check_int(self.in_test1.text)
        if P1 == False or P1 <= 0:
            P1 = 0
            self.in_test1.text = str(P1)
        else:
            self.manager.current = 't2'

class Test2Scr(Screen):
    def __init__(self, name='t2'):
        super().__init__(name=name)
        txt1 = '[color=#000000]' + 'Второй тест' + '[/color]'
        lbl1 = Label(text=txt1, markup=True)
        txt2 = '[color=#000000]' + txt_test2 + '[/color]'
        lbl2 = Label(text=txt2, markup=True)
        self.in_test2 = TextInput(multiline=False)
        self.btn1 = ScrButton(self, direction='left', goal='t3', text="Далее")
        self.btn1.background_color = btn_color
        box = BoxLayout(orientation='vertical', padding=8, spacing=8)
        box.add_widget(lbl1)
        box.add_widget(lbl2)
        box.add_widget(self.in_test2)
        box.add_widget(self.btn1)
        self.add_widget(box)
        self.btn1.on_press = self.next
    def next(self):
        global P2
        P2 = check_int(self.in_test2.text)
        if P2 == False or P2 <= 0:
            P2 = 0
            self.in_test2.text = str(P2)
        else:
            self.manager.current = 't3'

class Test3Scr(Screen):
    def __init__(self, name='t3'):
        super().__init__(name=name)
        txt1 = '[color=#000000]' + 'Третий тест' + '[/color]'
        lbl1 = Label(text=txt1, markup=True)
        txt2 = '[color=#000000]' + txt_test3 + '[/color]'
        lbl2 = Label(text=txt2, markup=True)
        self.in_test3 = TextInput(multiline=False)
        self.btn1 = ScrButton(self, direction='left', goal='result', text="Далее")
        self.btn1.background_color = btn_color
        box = BoxLayout(orientation='vertical', padding=8, spacing=8)
        box.add_widget(lbl1)
        box.add_widget(lbl2)
        box.add_widget(self.in_test3)
        box.add_widget(self.btn1)
        self.add_widget(box)
        self.btn1.on_press = self.next
    def next(self):
        global P3
        P3 = check_int(self.in_test3.text)
        if P3 == False or P3 <= 0:
            P3 = 0
            self.in_test3.text = str(P3)
        else:
            self.manager.current = 'result'

class ResultScr(Screen):
    def __init__(self, name='result'):
        super().__init__(name=name)
        self.txt = Label(text='', markup=True)
        #txt.set_text(get_result())
        box = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.btn = ScrButton(self, direction='left', goal='result', text="Нажмите чтобы получить результат")
        self.btn.background_color = btn_color
        box.add_widget(self.txt)
        box.add_widget(self.btn)
        self.add_widget(box)
        self.btn.on_press = self.before
    def before(self):
        a = '[color=#000000]' + get_result() + '[/color]'
        self.txt.text = a


# Здесь должен быть твой код
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(Test1Scr())
        sm.add_widget(Test2Scr())
        sm.add_widget(Test3Scr())
        sm.add_widget(ResultScr())
        return sm

app = MyApp()
app.run()
