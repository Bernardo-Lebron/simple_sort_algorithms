import matplotlib.pyplot as plt
import numpy as np

titulo_grafico = "Insertion Sort — Dados Decrescentes"

tamanhos = ['10²', '10³', '10⁴', '10⁵', '10⁶']

dados = {
    'C (-O0)':      [0.00001, 0.000545, 0.059135, 5.02298, 543.40],
    'C (-O3)':      [0.000003, 0.000129, 0.011672, 1.188966, 118.26],

    'C++ (-O0)':    [0.00004, 0.0050692, 0.389041, 37.81, 3670.49],
    'C++ (-O3)':    [0.0000031, 0.0001221, 0.0120779, 1.183, 119.147],

    'Rust (-O0)':   [0.000024, 0.003093, 0.223538, 23.3430, 0],
    'Rust (-O3)':   [0.000004, 0.000181, 0.020271, 1.774292, 182.6751],

    'JavaScript':   [0.000340, 0.001215, 0.032820, 3.033301, 312.910],

    'Python':       [0.000196, 0.02094, 2.25077, 226.560, 0]
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
        'grafico_decrescente.png',
        dpi=300,
        bbox_inches='tight'
    )

    print("Gráfico salvo como grafico_decrescente.png")

    plt.show()

if __name__ == "__main__":
    gerar_grafico()