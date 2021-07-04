'''A conversion calculator with GUI'''

import tkinter as tk


def mile_to_km():
    new_value = float(to_convert.get()) * 1.609
    out_value_l.config(text=f'{new_value}')


# Configurating window
window = tk.Tk()
window.title('Mi to Km')
window.config(padx=45, pady=10)

# Text input field
to_convert = tk.Entry(width=10)
to_convert.grid(row=0, column=1)
to_convert.focus()

# Labels
in_metric = tk.Label(text='Miles')
in_metric.grid(row=0, column=2, padx = 5, pady=5)

out_value_l = tk.Label(text='0')
out_value_l.grid(row=1, column=1)

out_metric = tk.Label(text='Kilometers')
out_metric.grid(row=1, column=2, padx = 5)

# Buttons
b_convert = tk.Button(text='Convert', command=mile_to_km)
b_convert.grid(row=2, column=1, pady=5)

window.mainloop()