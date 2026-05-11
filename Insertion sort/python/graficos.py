import matplotlib.pyplot as plt
import numpy as np

# =========================================================
# CENÁRIO 1 — DADOS ALEATÓRIOS
# =========================================================

titulo_grafico = "Insertion Sort — Dados Aleatórios"

tamanhos = ['10²', '10³', '10⁴', '10⁵', '10⁶']

dados = {
    'C (-O0)':      [0.000004, 0.000271, 0.025653, 2.591586, 262.592],
    'C (-O3)':      [0.000002, 0.000102, 0.006070, 0.615683, 60.79153],

    'C++ (-O0)':    [0.000021, 0.002454, 0.193293, 18.86, 1832.96],
    'C++ (-O3)':    [0.0000021, 0.0000664, 0.0059649, 0.587483, 60.1009],

    'Rust (-O0)':   [0.000015, 0.001176, 0.011176, 11.69859, 1123.52],
    'Rust (-O3)':   [0.000002, 0.000095, 0.008847, 0.897895, 90.24779],

    'JavaScript':   [0.000219, 0.000993, 0.016374, 1.525250, 152.74],

    'Python':       [0.000117, 0.010413, 1.239607, 136.295, 0]
}

# =========================================================
# FUNÇÃO PRINCIPAL
# =========================================================

def gerar_grafico():

    y = np.arange(len(tamanhos))

    altura_barra = 0.10

    fig, ax = plt.subplots(figsize=(16, 10))

    cores = {
        'C (-O0)': '#ff9999',
        'C (-O3)': '#ff0000',

        'C++ (-O0)': '#99ff99',
        'C++ (-O3)': '#008000',

        'Rust (-O0)': '#9999ff',
        'Rust (-O3)': '#0000ff',

        'JavaScript': '#f1c40f',

        'Python': '#8e44ad'
    }

    for i, (linguagem, valores) in enumerate(dados.items()):

        posicao = (
            y
            + (i * altura_barra)
            - (len(dados) * altura_barra / 2)
            + altura_barra / 2
        )

        valores_plot = [
            v if v > 0 else 1e-10
            for v in valores
        ]

        barras = ax.barh(
            posicao,
            valores_plot,
            altura_barra,
            label=linguagem,
            color=cores[linguagem]
        )

        # =================================================
        # LABELS
        # =================================================

        for j, barra in enumerate(barras):

            valor_real = valores[j]

            if valor_real > 0:

                if valor_real >= 1:
                    texto = f'{valor_real:.2f}s'
                else:
                    texto = f'{valor_real*1000:.2f}ms'

                ax.annotate(
                    texto,
                    xy=(
                        barra.get_width(),
                        barra.get_y() + barra.get_height()/2
                    ),
                    xytext=(5, 0),
                    textcoords="offset points",
                    ha='left',
                    va='center',
                    fontsize=7
                )

            else:

                ax.annotate(
                    'T.O.',
                    xy=(
                        1e-10,
                        barra.get_y() + barra.get_height()/2
                    ),
                    xytext=(5, 0),
                    textcoords="offset points",
                    ha='left',
                    va='center',
                    fontsize=8,
                    color='red',
                    fontweight='bold'
                )

    # =====================================================
    # CONFIGURAÇÕES DO GRÁFICO
    # =====================================================

    ax.set_xscale('log')

    ax.set_xlim(1e-6, 1e5)

    ax.set_xlabel(
        'Tempo de Execução (segundos — escala logarítmica)',
        fontsize=12,
        fontweight='bold'
    )

    ax.set_ylabel(
        'Quantidade de Elementos',
        fontsize=12,
        fontweight='bold'
    )

    ax.set_title(
        titulo_grafico,
        fontsize=18,
        fontweight='bold',
        pad=20
    )

    ax.set_yticks(y)

    ax.set_yticklabels(tamanhos)

    ax.grid(
        True,
        which="both",
        linestyle='--',
        alpha=0.3
    )

    ax.legend(
        loc='upper left',
        bbox_to_anchor=(1.02, 1),
        title='Linguagens'
    )

    plt.tight_layout()

    plt.savefig(
        'grafico_aleatorio.png',
        dpi=300,
        bbox_inches='tight'
    )

    print("Gráfico salvo como grafico_aleatorio.png")

    plt.show()

# =========================================================

if __name__ == "__main__":
    gerar_grafico()