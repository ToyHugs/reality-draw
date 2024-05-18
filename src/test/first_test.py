import pynput.mouse as mouse

mouses = mouse.Controller()

list_point = [] # list of point (x, y) when mouse click

def on_click(x, y, button, pressed):
    if pressed:
        list_point.append((x, y))
        print(f'Point: {x}, {y}')

def test_mouse():
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    while len(list_point) < 2:
        pass

    listener.stop()

    assert len(list_point) == 2

    print('Test passed')
    print(f'Point 1: {list_point[0]}')
    print(f'Point 2: {list_point[1]}')


if __name__ == '__main__':
    test_mouse()