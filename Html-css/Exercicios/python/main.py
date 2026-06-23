"""
Calculadora simples com interface grafica (tkinter)
===================================================
Faz as quatro operacoes basicas: soma, subtracao,
multiplicacao e divisao.

Como executar no VS Code:
  - Abra este arquivo e clique em "Run Python File" (botao de play)
  - Ou no terminal:  python calculadora.py
O tkinter ja vem junto com o Python, nao precisa instalar nada.
"""

import tkinter as tk

# Cores do tema (deixam a calculadora mais bonita)
COR_FUNDO = "#1e1e2e"
COR_VISOR = "#11111b"
COR_NUMERO = "#313244"
COR_OPERADOR = "#f9a825"
COR_IGUAL = "#43a047"
COR_LIMPAR = "#e53935"
COR_TEXTO = "#ffffff"

FONTE_VISOR = ("Segoe UI", 28, "bold")
FONTE_BOTAO = ("Segoe UI", 18, "bold")


class Calculadora:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora")
        self.janela.config(bg=COR_FUNDO, padx=12, pady=12)
        self.janela.resizable(False, False)

        # Texto que aparece no visor
        self.expressao = ""
        self.visor_texto = tk.StringVar(value="0")

        self._criar_visor()
        self._criar_botoes()

    def _criar_visor(self):
        visor = tk.Label(
            self.janela,
            textvariable=self.visor_texto,
            anchor="e",
            bg=COR_VISOR,
            fg=COR_TEXTO,
            font=FONTE_VISOR,
            padx=16,
            pady=24,
        )
        visor.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0, 12))

    def _criar_botoes(self):
        # (texto, linha, coluna, cor)  -- layout de uma calculadora comum
        botoes = [
            ("C", 1, 0, COR_LIMPAR), ("(", 1, 1, COR_NUMERO),
            (")", 1, 2, COR_NUMERO), ("/", 1, 3, COR_OPERADOR),

            ("7", 2, 0, COR_NUMERO), ("8", 2, 1, COR_NUMERO),
            ("9", 2, 2, COR_NUMERO), ("*", 2, 3, COR_OPERADOR),

            ("4", 3, 0, COR_NUMERO), ("5", 3, 1, COR_NUMERO),
            ("6", 3, 2, COR_NUMERO), ("-", 3, 3, COR_OPERADOR),

            ("1", 4, 0, COR_NUMERO), ("2", 4, 1, COR_NUMERO),
            ("3", 4, 2, COR_NUMERO), ("+", 4, 3, COR_OPERADOR),

            ("0", 5, 0, COR_NUMERO), (".", 5, 1, COR_NUMERO),
            ("=", 5, 2, COR_IGUAL), ("←", 5, 3, COR_LIMPAR),
        ]

        for (texto, linha, coluna, cor) in botoes:
            tk.Button(
                self.janela,
                text=texto,
                font=FONTE_BOTAO,
                bg=cor,
                fg=COR_TEXTO,
                activebackground=cor,
                bd=0,
                width=4,
                height=2,
                command=lambda t=texto: self._clicar(t),
            ).grid(row=linha, column=coluna, sticky="nsew", padx=4, pady=4)

    def _clicar(self, tecla):
        if tecla == "C":            # limpa tudo
            self.expressao = ""
            self.visor_texto.set("0")
        elif tecla == "←":          # apaga o ultimo caractere
            self.expressao = self.expressao[:-1]
            self.visor_texto.set(self.expressao or "0")
        elif tecla == "=":          # calcula o resultado
            self._calcular()
        else:                       # numero ou operador
            self.expressao += tecla
            self.visor_texto.set(self.expressao)

    def _calcular(self):
        try:
            # aceita apenas numeros e operadores permitidos (seguranca)
            permitidos = set("0123456789.+-*/() ")
            if not self.expressao or not set(self.expressao) <= permitidos:
                raise ValueError

            resultado = eval(self.expressao)  # calcula a conta

            # mostra inteiro sem o ".0" desnecessario
            if resultado == int(resultado):
                resultado = int(resultado)

            self.visor_texto.set(str(resultado))
            self.expressao = str(resultado)
        except ZeroDivisionError:
            self.visor_texto.set("Nao da pra dividir por 0")
            self.expressao = ""
        except Exception:
            self.visor_texto.set("Erro")
            self.expressao = ""


if __name__ == "__main__":
    janela = tk.Tk()
    Calculadora(janela)
    janela.mainloop()