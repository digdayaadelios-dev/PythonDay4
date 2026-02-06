import PySimpleGUI as sg
from datetime import datetime

# Konfigurasi Tema
sg.theme('SystemDefault')

# Data dummy untuk menyimpan riwayat parkir
data_parkir = []

# Layout Bagian Kiri (Input)
layout_kiri = [
    [sg.Text('Aplikasi Parkir Kelompok 6', font=('Arial', 16, 'bold'))],
    [sg.Text('Cari NoPol', size=(12, 1)), sg.Input(key='-CARI-', size=(20, 1)), sg.Button('Cari')],
    [sg.HorizontalSeparator()],
    [sg.Text('No Plat Polisi', size=(12, 1)), sg.Input(key='-NOPOL-', size=(25, 1))],
    [sg.Text('Waktu Masuk', size=(12, 1)), sg.Input(key='-MASUK-', size=(25, 1), tooltip='Format HH:mm')],
    [sg.Text('Waktu Keluar', size=(12, 1)), sg.Input(key='-KELUAR-', size=(25, 1), tooltip='Format HH:mm')],
    [sg.Text('Biaya', size=(12, 1)), sg.Input('0', key='-BIAYA-', size=(20, 1)), sg.Button('Hitung')],
]

# Layout Bagian Kanan (Info Biaya)
layout_kanan = [
    [sg.Text('Biaya Per Jam', text_color='red', font=('Arial', 20))],
    [sg.Text('Rp. 2.000', text_color='red', font=('Arial', 40, 'bold'))]
]

# Layout Tabel Bawah
header_tabel = ['No Plat Polisi', 'Masuk', 'Keluar', 'Biaya']
layout_bawah = [
    [
        sg.Column([
            [sg.Text('List Pelanggan Urut Terakhir Keluar', text_color='blue')],
            [sg.Table(values=data_parkir, headings=header_tabel, key='-TABEL1-', auto_size_columns=True, num_rows=5)]
        ]),
        sg.Column([
            [sg.Text('List Pelanggan Banyak Bayar', text_color='blue')],
            [sg.Table(values=data_parkir, headings=header_tabel, key='-TABEL2-', auto_size_columns=True, num_rows=5)]
        ])
    ]
]

# Gabungkan Semua Layout
layout_final = [
    [sg.Column(layout_kiri), sg.VerticalSeparator(), sg.Column(layout_kanan, element_justification='center')],
    [sg.HorizontalSeparator()],
    [sg.Column(layout_bawah)]
]

window = sg.Window('Aplikasi Parkir Kelompok 6', layout_final)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
        
    if event == 'Hitung':
        try:
            # Logika Sederhana: Selisih Jam (Asumsi format HH:mm)
            fmt = '%H:%M'
            t1 = datetime.strptime(values['-MASUK-'], fmt)
            t2 = datetime.strptime(values['-KELUAR-'], fmt)
            
            # Hitung selisih jam (minimal 1 jam)
            selisih = t2 - t1
            jam = max(1, selisih.seconds // 3600)
            total_biaya = jam * 2000
            
            # Update field biaya
            window['-BIAYA-'].update(f"{total_biaya}")
            
            # Tambah data ke tabel
            baru = [values['-NOPOL-'], values['-MASUK-'], values['-KELUAR-'], total_biaya]
            data_parkir.append(baru)
            
            # Update Tabel (Urut Terakhir Keluar & Sortir Biaya Terbesar)
            window['-TABEL1-'].update(values=data_parkir[::-1]) # Balik urutan
            window['-TABEL2-'].update(values=sorted(data_parkir, key=lambda x: x[3], reverse=True))
            
        except Exception as e:
            sg.popup_error("Format waktu salah! Gunakan HH:mm (Contoh: 08:00)")

window.close()