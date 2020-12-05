from datetime import datetime
import turtle




binary_series = [32, 16, 8, 4, 2, 1]

def prepareData():
    now = datetime.now()
    hourData = getBinaryFormat(now.hour)
    minuteData = getBinaryFormat(now.minute)
    secondData = getBinaryFormat(now.second)
    displayData([hourData, minuteData, secondData])
    # return ' '.join(str(x) for x in hourData) + '\r\n' + ' '.join(str(x) for x in minuteData) + '\r\n' + ' '.join(str(x) for x in secondData)


def getBinaryFormat(numb):
    binary_format = [0, 0, 0, 0, 0, 0]
    selectedIndices = []
    selectedTotal = 0
    for digit in binary_series:
        if digit <= numb:
            selectedTotal += digit
            if selectedTotal <= numb:
                selectedIndices.append(binary_series.index(digit))
            else:
                selectedTotal -= digit
            
    for ind in selectedIndices:
        binary_format[ind] = 1
    return binary_format


def displayData(timeDataBinaryFormats):
    turtle.setup(170, 90)
    s = turtle.getscreen()
    s.screensize(140, 70)
    t = s.turtles()[0]
    t.hideturtle()
    t.up()
    t.speed(10)
    t.setpos(-55, 15)
    addToScreen(s, t, timeDataBinaryFormats[0])
    addToScreen(s, t, timeDataBinaryFormats[1])
    addToScreen(s, t, timeDataBinaryFormats[2])
    s.exitonclick()

def addToScreen(s, t, binary_format):
    distance = 0
    for digit in binary_format:
        if (digit == 0):
            t.down()
            t.circle(5)
            t.up()
        else:
            t.down()
            t.begin_fill()
            t.circle(5)
            t.end_fill()
            t.up()
        t.forward(20)
        distance += 20
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(distance)
    t.right(180)
            
print(prepareData())
