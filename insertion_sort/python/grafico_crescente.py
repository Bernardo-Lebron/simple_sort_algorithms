import matplotlib.pyplot as plt
import numpy as np

titulo_grafico = "Insertion Sort — Dados Crescentes"

tamanhos = ['10²', '10³', '10⁴', '10⁵', '10⁶']

dados = {
    'C (-O0)':      [0.000001, 0.000001, 0.000014, 0.000142, 0.001413],
    'C (-O3)':      [0.0000001, 0.000001, 0.000007, 0.000055, 0.000587],

    'C++ (-O0)':    [0.0000015, 0.00010072, 0.0000093, 0.0010404, 0.009488],
    'C++ (-O3)':    [0.0000002, 0.0000002, 0.0000065, 0.0000634, 0.000622],

    'Rust (-O0)':   [0.000001, 0.000011, 0.000124, 0.001099, 0.011581],
    'Rust (-O3)':   [0.000000, 0.000001, 0.000008, 0.000079, 0.000861],

    'JavaScript':   [0.000042, 0.000191, 0.000514, 0.000809, 0.000809],

    'Python':       [0.000011, 0.000107, 0.000591, 0.005321, 0.05369]
}

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

        for j, barra in enumerate(barras):

            valor_real = valores[j]

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

    ax.set_xscale('log')

    ax.set_xlim(1e-8, 1)

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
        'grafico_crescente.png',
        dpi=300,
        bbox_inches='tight'
    )

    print("Gráfico salvo como grafico_crescente.png")

    plt.show()

if __name__ == "__main__":
    gerar_grafico()