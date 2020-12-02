import random

i = 0
count = 0 #정답 갯수
mul_1 = random.randint(1,9) #퀴즈의 첫번째 숫자
mul_2 = random.randint(1,9) #퀴즈의 두번째 숫자
mytext = str(mul_1)+ " "+"X"+" "+ str(mul_2) #퀴즈
wrong = "wrong"
correct = "correct"
pcount = "count" +" "+ str(count)
answer = mul_1 * mul_2 #퀴즈 답

offscreen_canvas.Clear()
len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor,mytext)
offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas) #정답 출력
time.sleep(3)
while i < 10: #퀴즈 10번 실행
    i += 1
    if (key = input("정답 입력: ")):
        if (answer == int(key)): #답 맞음
            count += 1
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor,correct)
            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas) #correct 문구 출력
            time.sleep(1)
        else: #답 틀림
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor,wrong)
            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas) #wrong 문구 출력
            time.sleep(1)

        mul_1 = random.randint(1,9)
        mul_2 = random.randint(1,9)
        mytext = str(mul_1)+ " "+"X"+" "+ str(mul_2)
        answer = mul_1 + mul_2

    offscreen_canvas.Clear()
    len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor,mytext)
    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas) #퀴즈 다시 설정 후 출력
    time.sleep(3)

offscreen_canvas.Clear()
len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor,pcount))
offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas) #정답 갯수 출력
time.sleep(5)

