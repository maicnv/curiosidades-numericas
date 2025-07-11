# 🔢 Curiosidades Numéricas - Senac Minas

Este é um projeto em Python utilizando **CustomTkinter** para a interface gráfica (GUI) e consumo de uma **API pública**, desenvolvido como atividade prática para o curso Técnico em Informática do **Senac Minas**.

---

## 🔧 Tecnologias Utilizadas

- Python  
- CustomTkinter  
- Deep Translator  
- Requests  
- API Numbers (http://numbersapi.com)

---

## 📌 Funcionalidades

Este aplicativo permite ao usuário consultar curiosidades numéricas em tempo real e traduzi-las para o português:

✅ Consultar curiosidade sobre um número  
🌐 Consumir dados da API pública [Numbers API](http://numbersapi.com)  
🗣️ Traduzir a curiosidade para o português (PT-BR)  
❗ Tratar erros como entradas inválidas ou campos vazios  

---

## 💡 Como Funciona

O usuário digita um número na interface, clica em **"CURIOSIDADE"** e o aplicativo retorna uma curiosidade sobre esse número. Caso deseje, também pode clicar em **"TRADUZIR"** para traduzir o conteúdo para o português.

---

## 🧩 Organização do Projeto

- `curiosidades.py` – Script principal com a interface, consumo da API e botão de tradução.  
- API usada: http://numbersapi.com  
- Tradução feita com: `deep_translator.GoogleTranslator`  

---

## ▶️ Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/maicnv/curiosidades-numericas.git
