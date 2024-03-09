import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def adicionar_subtrair_tempo():
    data_input = entry_data.get()
    tempo = entry_tempo.get()
    operacao = entry_operacao.get()

    try:
        data = datetime.strptime(data_input, "%Y/%m/%d").date()
        quantidade = int(tempo)
        
        if operacao == "Adição":
            if combo_tempo.get() == "Anos":
                nova_data = data + relativedelta(years=quantidade)
            elif combo_tempo.get() == "Meses":
                nova_data = data + relativedelta(months=quantidade)
            else:
                nova_data = data + timedelta(days=quantidade)
        else:
            if combo_tempo.get() == "Anos":
                nova_data = data - relativedelta(years=quantidade)
            elif combo_tempo.get() == "Meses":
                nova_data = data - relativedelta(months=quantidade)
            else:
                nova_data = data - timedelta(days=quantidade)
        
        messagebox.showinfo("Resultado", f"A nova data é: {nova_data.strftime('%d/%m/%Y')}")
        # Limpar os dados do formulário
        entry_data.delete(0, tk.END)
        entry_tempo.set("1")
        entry_operacao.set("Adição")
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido. Utilize o formato yyyy/mm/dd.")
        # Limpar os campos de entrada
        entry_data.delete(0, tk.END)
        entry_tempo.set("1")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de tempo")

# Estilizar a interface
root.configure(bg="black")
tk.Label(root, text="Calculadora de tempo", bg="black", fg="pink", font=("Arial", 16)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Criar os campos de entrada e rótulos

label_operacao = tk.Label(root, text="Operação:", anchor="w", bg="black", fg="pink")
label_operacao.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_operacao = tk.StringVar(root)
entry_operacao.set("Adição")
radio_adicao = tk.Radiobutton(root, text="Adição", variable=entry_operacao, value="Adição", anchor="w", bg="black", fg="pink", selectcolor="darkred")
radio_adicao.grid(row=1, column=1, padx=10, pady=5, sticky="w")
radio_subtracao = tk.Radiobutton(root, text="Subtração", variable=entry_operacao, value="Subtração", anchor="w", bg="black", fg="pink", selectcolor="darkred")
radio_subtracao.grid(row=1, column=2, padx=(0, 5), pady=5, sticky="w")  # Ajuste aqui

label_data = tk.Label(root, text="Digite uma data (yyyy/mm/dd):", anchor="w", bg="black", fg="pink")
label_data.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_data = tk.Entry(root)
entry_data.grid(row=2, column=1, padx=10, pady=5, sticky="w")

label_tempo = tk.Label(root, text="Unidade de Tempo:", anchor="w", bg="black", fg="pink")
label_tempo.grid(row=3, column=0, padx=10, pady=5, sticky="w")
combo_tempo = tk.StringVar(root)
combo_tempo.set("Dias")
combo_tempo_dropdown = tk.OptionMenu(root, combo_tempo, "Anos", "Meses", "Dias")
combo_tempo_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky="w")

label_tempo = tk.Label(root, text="Quantidade para adicionar ou subtrair:", anchor="w", bg="black", fg="pink")
label_tempo.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_tempo = tk.StringVar(root)
entry_tempo.set("1")
entry_tempo_dropdown = tk.OptionMenu(root, entry_tempo, *range(1, 1001))
entry_tempo_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky="w")  # Alteração aqui

# Botão para calcular
btn_calcular = tk.Button(root, text="Calcular", command=adicionar_subtrair_tempo, bg="black", fg="pink")
btn_calcular.grid(row=5, column=2, padx=10, pady=5, sticky="e")  # Alteração aqui

# Executar a interface
root.mainloop()
