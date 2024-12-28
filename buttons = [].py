buttons = []
for i in range(3):
    def action():
        print(i)
    action


buttons = []
for i in range(3):
    action = lambda x=i: print(x)  # i의 현재 값을 캡처하여 x로 전달
    buttons.append(action)

