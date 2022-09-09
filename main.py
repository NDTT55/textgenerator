alphabet="йфяцычувскамепинртгоьшлбщдюзжэхъ"
numbers="1234567890"
import random
class Machine():
    #{слово-[{пара1:кол-во использований},...]}
    memo={}
    #читает текст и обрабатывает его#
    def look(self,filename):
        text=""
        #сохранение всего текста
        with open (filename,"r",encoding="utf-8") as f:
            text=f.read().lower()
            text=text.replace("\n","")

        # убираем ненужные символы, удаляем цифры и делим текст на слова
        words=text.split()
        del text
        bad=[]
        for i in range(len(words)):
            words[i].strip()
            if (len(words[i])==1 and words[i] not in alphabet) or (words[i][0] in numbers):
              bad.append(i)
            if "." in words[i]:
                words[i] = words[i].replace(".", "")
            if "!" in words[i]:
                words[i] = words[i].replace("!", "")
            if "?" in words[i]:
                words[i] = words[i].replace("?", "")
            if "," in words[i]:
                words[i] = words[i].replace(",", "")
            if ":" in words[i]:
                words[i] = words[i].replace(":", "")
            if ";" in words[i]:
                words[i] = words[i].replace(";", "")
            if "(" in words[i]:
                words[i] = words[i].replace("(", "")
            if ")" in words[i]:
                words[i] = words[i].replace(")", "")
            if "-" in words[i]:
                words[i] = words[i].replace("-", "")
            if "'" in words[i]:
                words[i] = words[i].replace("'", "")
            if "]" in words[i]:
                words[i] = words[i].replace("]", "")
            if "[" in words[i]:
                words[i] = words[i].replace("[", "")
            if "..." in words[i]:
                words[i] = words[i].replace("...", "")
            if "»" in words[i]:
                words[i] = words[i].replace("»", "")

            if "«" in words[i]:
                words[i] = words[i].replace("«", "")

        j=0
        #удаляем символы по типу № их номера сохраняли в массиве bad после удаления меняется и позиция относительно массива words
        #для контроля новой позиции заводим счетчик j
        for i in range(len(bad)):
            del words[bad[i]-j]
            j=j+1
        del bad



        #заполняем пары
        for i in range(len(words) - 2):
            #если слова еще нет в словаре и оно новое то добавляем новую пару
            if words[i] not in self.memo:
                self.memo[words[i]]=[words[i+1],1]

            #если словo есть смотрим есть ли у него эта пара если да +1 к веротяности
            else:
                if words[i+1] in self.memo[words[i]]:
                    self.memo[words[i]][self.memo[words[i]].index(words[i+1])+1]+=1
            #если пары нет добавляем новую пару
                if words[i+1] not in self.memo[words[i]]:
                    self.memo[words[i]].append(words[i+1])
                    self.memo[words[i]].append(1)
        del words
        #print(self.memo)
    #создаем цепь из слов
    #вспомогательная процедура создания цепи
    def __helpchain(self,first:str,size:int):
        # случай случайного ввода
        finalchain = ""
        firstchain = ""
        if first == "0":
            i = random.randint(1, len(self.memo.keys()))
            j = 1
            firstchain = ""
            for w in self.memo.keys():
                if j == i:
                    firstchain = w
                j = j + 1
            # выбрали первое рандомное слово
            finalchain = finalchain + firstchain
            # набираем цепочку
            # curchain-текущее слово
            max = 0
            curchain = finalchain
            for i in range(1, size):
                if curchain in self.memo.keys():
                    # открываем массив пар ищем максимальное число и запоминаем его индекс индекс это слова позиция-1
                    max = self.memo[curchain][1]
                    pos = 0
                    # находим максимальное число и запоминаем его позицию
                    for k in range(1, (len(self.memo[curchain])) - 1, 2):
                        if self.memo[curchain][k] >= max:
                            max = self.memo[curchain][k]
                            pos = self.memo[curchain].index(max)
                    if pos > 0:
                        pos = pos - 1
                    curchain = self.memo[curchain][pos]
                    finalchain = finalchain + " " + str(curchain) + " "

                # если такого слова нет в памяти
                else:
                    print("мы не достаточно обучились")
                    print(finalchain)
                    break
        # если первое слово задано
        if first != "0":
            finalchain = finalchain + first
            max = 0
            curchain = finalchain
            for i in range(1, size):
                if curchain in self.memo.keys():
                    # открываем массив пар ищем максимальное число и запоминаем его индекс индекс это слова позиция-1
                    max = self.memo[curchain][1]
                    pos = 0
                    # находим максимальное число и запоминаем его позицию
                    for k in range(1, (len(self.memo[curchain])) - 1, 2):
                        if self.memo[curchain][k] >= max:
                            max = self.memo[curchain][k]
                            pos = self.memo[curchain].index(max)
                    if pos > 0:
                        pos = pos - 1
                    curchain = self.memo[curchain][pos]
                    finalchain = finalchain + " " + curchain + " "

                # если такого слова нет в памяти
                else:
                    print("мы не достаточно обучились")
                    print(finalchain)
                    break
        print(finalchain)


    def chain(self):
        size=int(input("введите длину цепи"))
        first=input("введите первое слово цепи, для случайного слова введите 0")
        self.__helpchain(first,size)


def learn(M:Machine):
    print("для ввода своего файла нажмите 1, для обучения только на стандартных-0")
    x=int(input())
    if x == 1:
        s=input("введите путь к файлу")
        M.look(s)
    M.look("text")
    M.look("text2")
    M.look("text3")
    M.look("songs")
    M.look("text4")
    M.look("text5")
    M.look("text6")
    M.look("text7")
    M.look("text8")


def generate(M:Machine):
    M.chain()


def main():
    m1=Machine()
    learn(m1)
    generate(m1)
    generate(m1)
    generate(m1)
    generate(m1)
    generate(m1)


if __name__=="__main__":
    main()


