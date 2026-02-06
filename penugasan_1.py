import PySimpleGUI as sg

# Tema dan Layout
sg.theme('SystemDefault')
layout = [
    [sg.Text('Harga:')],
    [sg.Input(key='-HARGA-', size=(20,1))],
    [sg.Text('Kuantitas:')],
    [sg.Input(key='-KUANTITAS-', size=(20,1))],
    [sg.Button('Hitung Total')],
    [sg.Text('Total: Rp.0.00', key='-TOTAL-')]
]

window = sg.Window('Kalkulator Harga', layout, element_justification='center')

# Event Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Hitung Total':
        try:
            h = float(values['-HARGA-'])
            k = float(values['-KUANTITAS-'])
            total = h * k
            window['-TOTAL-'].update(f"Total: Rp.{total:,.2f}")
        except ValueError:
            window['-TOTAL-'].update("Input salah!")

window.close()