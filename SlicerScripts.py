def toggle():
    print('button clicked')

b = qt.QPushButton('Click me')
b.connect('clicked()', toggle)

b.show()
