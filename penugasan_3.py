import PySimpleGUI as sg

# Konfigurasi Tema
sg.theme('LightGrey1')

# Struktur Layout
layout = [
    # Header
    [sg.Text('DATA SISWA BARU', font=('Arial', 24, 'bold'), background_color='cyan', 
             text_color='black', expand_x=True, justification='center', pad=((0,0),(0,20)))],
    
    # Form Inputs
    [sg.Text('Nama Lengkap', size=(15, 1))],
    [sg.Input(key='-NAMA-', expand_x=True)],
    
    [sg.Text('Tanggal Lahir', size=(15, 1))],
    [sg.Input(key='-TGLLAHIR-', expand_x=True)],
    
    [sg.Text('Asal Sekolah', size=(15, 1))],
    [sg.Input(key='-ASAL-', expand_x=True)],
    
    [sg.Text('NISN', size=(15, 1))],
    [sg.Input(key='-NISN-', expand_x=True)],
    
    [sg.Text('Nama Ayah', size=(15, 1))],
    [sg.Input(key='-AYAH-', expand_x=True)],
    
    [sg.Text('Nama Ibu', size=(15, 1))],
    [sg.Input(key='-IBU-', expand_x=True)],
    
    [sg.Text('Nomor Telepon / HP', size=(15, 1))],
    [sg.Input(key='-TELP-', expand_x=True)],
    
    [sg.Text('Alamat', size=(15, 1))],
    [sg.Multiline(key='-ALAMAT-', size=(45, 5), expand_x=True)],
    
    # Tombol Aksi
    [sg.Push(), 
     sg.Button('Hapus', button_color=('white', '#d35400'), size=(10, 1)), 
     sg.Button('Simpan', button_color=('white', '#e67e22'), size=(10, 1))]
]

# Membuat Window
window = sg.Window('MainWindow', layout, size=(600, 750), resizable=True)

# Event Loop
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Hapus':
        # Reset semua field menjadi kosong
        for key in values:
            window[key].update('')
            
    if event == 'Simpan':
        nama = values['-NAMA-']
        if nama:
            sg.popup('Berhasil!', f'Data siswa {nama} telah disimpan.')
        else:
            sg.popup_error('Error', 'Nama Lengkap tidak boleh kosong!')

window.close()