import random
import sys

greetings = ["'чем я могу вам помочь?'", "'прохомдите'", "'слемдующий!'", "'драсьте'"]
positive_reactions = ["'вомт ваши бумаги'",
                      "'сейчас я вам помогу'",
                      "'ок ок ок'",
                      "'сейчас все бумдет'",
                      "'вот, помжалуйста'"
                      ]
negative_reactions = ["'моломдой человек, вы меня не учите'",
                      "'я здесь 60 лет рамботаю и ни разу такое не встремчала'",
                      "'без очереди не промходим'",
                      "'у нас технимческий перерыв для таких операций. приходите на второе полнолуние'",
                      "'у меня важный телемфонный разговор с галей, вы что, не видите?'",
                      "'это вам надо в камбинет 228, но он уже замкрыт'"
                      ]
negative_putin = [
    "'у нас связь тут не рамботает со времен телеграмфа'",
    "'Маску еще позвомни'",
    "'от меня примвет передай'",
    "'моломдой человек, давайте без вымкрутасов'"]
negative_laws = [
    "'где вас таких химтрых берут?'",
    "'дома камчать права будете'",
    "'здесь ваши фомкусы не пройдут!'"]
negative_ask = [
    "'у меня завтрак/обед/рожает кошка (подчеркните нужное)'",
    "'всем тут томлько спросить'",
    "'лумчшее, что вы можете сделать, это подождать до замкрытия'"]
negative_bribe = [
    "'вы сдумрели? я молочный не ем, только горьмкий'",
    "'немт, я тамкое не ношу'",
    "'у меня амллергия на цветы'"]
negative_threat = [
    "'да меня сам ельмцин ждал в свои времена, а вы...'",
    "'вас много, а я омдна' *вздох*",
    "'ваша хамризма на меня не работает'"]
NAMES = ["КЛАВА–ПОХИТИТЕЛЬНИЦА ВРЕМЕНИ",
         "ЖЕЛЕЗНАЯ НИНА",
         "ГАЛЯ РУКИ-ТЕЛЕФОНЫ",
         "ЕВДОКИЯ В ПЯТОМ ПОКОЛЕНИИ",
         "СВЕТЛАНА С ДЕСЯТИ ДО ТРЁХ",
         "ВАЛЯ ПОЛСТАКАНА ПОЛИТУРЫ",
         "ЛИДИЯ ГЕРОЙ СОЦИАЛИСТИЧЕСКОГО ТРУДА",
         "СТЕПАНИДА ПУРГЕНОВНА",
         "СТАЖЁР АДА",
         "НАСТЯ КОРОБОЧКА",
         "ТАМАРА БОГИНЯ ОДНОКЛАССНИКОВ",
         "ОКСАНА СУПЕРТЯЖЁЛАЯ",
         "СОФИЯ 32 КАРАТА",
         "ЗИНАИДА ТРАКТОРЕНКО",
         "ГАЛИНА 2 БЛАНКА",
         "ЭЛЛОЧКА-ЛЮДОЕДОЧКА"
         ]
NOTES = ["Й", "Ц", "Г", "Ш", "Х", "Ф", "Д", "Л", "Ж", "Э", "Ч", "И", "Б"]
MOODS = ('bad', 'average', 'good')
RANKS = ('low', 'medium', 'high')
ACTIONS = '[С]просить [В]зятка [У]молять [К]ачать права [З]вонить Путину [П]окинуть чат: '
dict = {'bad': "плохом", 'average': "обычном", 'good': "приподнятом", 'low': "низкой", 'medium': "неплохой",
        'high': "высокой"}


class Bureaucrat:

    def __init__(self):
        self.rank = random.choice(RANKS)
        self.mood = random.choice(MOODS)
        self.negative = False

    def greet(self):

        print(random.choice(greetings))
        print('*Она на {} должности.'.format(dict[self.rank]))
        print('*Она в {} настроении.'.format(dict[self.mood]))

    def react_positively(self):

        self.negative = False
        print(random.choice(positive_reactions))

    def react_negatively(self):

        self.negative = True
        print(random.choice(negative_reactions))
        fault = random.randint(0, 100)
        if (fault < 20):
            s = input("===================================\nМОЛОМДОЙ ЧЕЛОВЕК НАША СМЕНА ОКОНМЧЕНА!\nВы проиграли.")
            sys.exit()

    def act(self):
        self.action = input("Ваша реакция: {} ".format(ACTIONS))
        if self.action == 'П':
            print('спс за катку')
            sys.exit()
        else:
            self.react()

    def react(self):

        if self.action.upper() == "С":
            if ((self.mood == 'average' and self.rank == 'low') or (self.mood == 'good' and self.rank == 'low') or (
                    self.mood == 'good' and self.rank == 'medium') or (self.mood == 'good' and self.rank == 'high')):
                self.react_positively()
            else:
                print(random.choice(negative_ask))
                self.react_negatively()
        elif self.action.upper() == "В":
            if ((self.mood == 'average' and self.rank == 'high') or (self.mood == 'bad' and self.rank == 'medium') or (
                    self.mood == 'good' and self.rank == 'medium') or (self.mood == 'good' and self.rank == 'high')):
                self.react_positively()
            else:
                print(random.choice(negative_bribe))
                self.react_negatively()
        elif self.action.upper() == "У":
            if ((self.mood == 'average' and self.rank == 'high') or (self.mood == 'bad' and self.rank == 'high') or (
                    self.mood == 'good' and self.rank == 'medium') or (
                    self.mood == 'average' and self.rank == 'medium') or (self.mood == "good" and self.rank == "low")):
                self.react_positively()
            else:
                print(random.choice(negative_threat))
                self.react_negatively()
        elif self.action.upper() == "К":
            if ((self.mood == 'average' and self.rank == 'low') or (self.mood == 'bad' and self.rank == 'low') or (
                    self.mood == 'bad' and self.rank == 'medium') or (self.mood == 'bad' and self.rank == 'high')):
                self.react_positively()
            else:
                print(random.choice(negative_laws))
                self.react_negatively()
        elif self.action.upper() == "З":
            if ((self.mood == 'average' and self.rank == 'medium') or (self.mood == 'bad' and self.rank == 'low') or (
                    self.mood == 'bad' and self.rank == 'medium')):
                self.react_positively()
            else:
                print(random.choice(negative_putin))
                self.react_negatively()
        else:
            self.react_negatively()


print(
    "Вы пришли в МФЦ. Вам очень нужна одна справка, а сегодня 31 декабря и они работают только до трёх. Ваша задача пройти всех консультантов (12 кругов ада) и получить нужную справку!\n\n\n")
print("(1) ВАШ КОНСУЛЬТАНТ: %s" % (random.choice(NAMES)))
bureaucrat = Bureaucrat()
bureaucrat.greet()
i = 1
while i < 13:
    bureaucrat.act()
    if bureaucrat.negative is False:
        print("\n(%s) ВАШ КОНСУЛЬТАНТ: %s" % (i+1, random.choice(NAMES)))
        bureaucrat = Bureaucrat()
        bureaucrat.greet()
        i += 1
s = input(
    "\nПоздравляем, вы первый за сегодня, кто успешно получил справку %s%s-%i \nНо сможете ли вы получить ее в следующий раз?" % (
    random.choice(NOTES), random.choice(NOTES), random.randint(100, 999)))
sys.exit()
