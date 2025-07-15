from deep_translator import GoogleTranslator
from tkinter import messagebox
import customtkinter as ctk
import requests

# função para traduzir a curiosidade
def traduzir():
    '''
    Traduz uma informação do inglês (EUA) para o português (BR)
    '''

    # texto para traduzuir
    texto = curiosidade_numero.cget('text')

    # traduzindo o texto
    texto_traduzido = GoogleTranslator(source='en', target='pt').translate(texto)
    curiosidade_numero.configure(text=texto_traduzido)


# função para pegar a curiosidade
def consultar_api():
    '''
    Consulta a API e pega uma curisoidade sobre um valor informado pelo usuário
    '''
    
    # valor informado pelo usuário
    numero = valor_usuario.get().strip()

    # usuário informou algum valor
    if numero:

        # usuário informou um valor númerico
        if numero.isnumeric():

            # pegando a curiosidade sobre o valor informado
            curiosidade = requests.get(f'http://numbersapi.com/{numero}?json')
            curiosidade_json = curiosidade.json()


            curiosidade_numero.configure(text=curiosidade_json['text'])

        else:

            messagebox.showerror(title='ERRO', message='Informe apenas valores númericos.')

    else:

        messagebox.showinfo(title='AVISO', message='Informe um valor númerico antes de buscar a curiosidade.' )


# criando o app
app = ctk.CTk()

# aparencia do aplicativo
app.title('Curiosidades Númericas')
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

# tamanho do aplicativo
app.geometry('800x170')
app.resizable(False, False)


# titulos 
titulo_principal = ctk.CTkLabel(master=app, width=150, text='Curiosidades Numéricas', font=('System', 20, 'bold'))
titulo_curiosidade = ctk.CTkLabel(master=app, width=150, text='', font=('System', 13, 'bold'))
curiosidade_numero = ctk.CTkLabel(master=app, text='', font=('System', 9))

# pegando o valor e traduzindo a curiosidade
valor_usuario = ctk.CTkEntry(master=app, width=40, text_color='black', placeholder_text='Valor', font=('System', 12), corner_radius=5, fg_color='white')
botao_curiosidade = ctk.CTkButton(master=app, width=90, text='CURIOSIDADE', fg_color="#229FB5", hover_color="#13616F", font=('System', 13, 'bold'), command=consultar_api)
botao_traducao = ctk.CTkButton(master=app, width=90, text='TRADUZIR', fg_color="#229FB5", hover_color="#13616F", font=('System', 13, 'bold'), command=traduzir)


# informações na tela
titulo_principal.place(x=250, y=0)
valor_usuario.place(x=250, y=40)
botao_curiosidade.place(x=300, y=40)
botao_traducao.place(x=415, y=40)
curiosidade_numero.pack(pady=80)

# rodando o app
app.mainloop()
