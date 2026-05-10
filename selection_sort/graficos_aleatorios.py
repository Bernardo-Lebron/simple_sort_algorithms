import matplotlib.pyplot as plt
import numpy as np

# Configuração dos dados (Cenário 1: Dados Aleatórios - Caso Médio)
titulo_grafico = "Cenário 2: Arquivo Decrescente.txt (Pior Caso)"
tamanhos = ['10^2', '10^3', '10^4', '10^5', '10^6']

# Tempos corrigidos (0.0 = Time Out)
dados = {
    'C (-O0)':      [0.0001, 0.0004, 0.0420, 4.1141, 10000.00],
    'C (-O3)':      [0.0001, 0.0002, 0.0207, 1.9618, 213.03],
    'C++ (-O0)':    [0.0001, 0.0010, 0.1070, 10.3462, 10000.00],
    'C++ (-O3)':    [0.0001, 0.0002, 0.0198, 1.9089, 217.39],
    'Rust (-O0)':   [0.0001, 0.0027, 0.2544, 24.6944, 10000.00],
    'Rust (-O3)':   [0.0001, 0.0002, 0.0263, 2.1320, 256.24],
    'JS (V8)':      [0.0006, 0.0022, 0.0530, 3.5851, 366.47],
    'Python':       [0.0001, 0.0089, 0.9334, 98.378, 10000.00]
}

def gerar_grafico_horizontal():
    # Invertemos a lógica: agora o eixo Y tem os tamanhos de N
    y = np.arange(len(tamanhos))
    altura_barra = 0.11 # No gráfico horizontal, a 'largura' vira 'altura'
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    cores = {
        'C (-O0)': '#ff9999', 'C (-O3)': '#ff0000',
        'C++ (-O0)': '#99ff99', 'C++ (-O3)': '#008000',
        'Rust (-O0)': '#9999ff', 'Rust (-O3)': '#0000ff',
        'JS (V8)': '#f1c40f', 'Python': '#8e44ad'
    }

    # Invertemos a ordem das chaves para a legenda bater com a ordem das barras
    for i, (lang, valores) in enumerate(dados.items()):
        # Calcula a posição vertical de cada barra dentro do grupo de N
        posicao = y + (i * altura_barra - (len(dados) * altura_barra / 2) + altura_barra / 2)
        
        # Valores para escala log (0 vira um valor quase nulo)
        plot_vals = [v if v > 0 else 1e-10 for v in valores]
        
        # barh = bar horizontal
        rects = ax.barh(posicao, plot_vals, altura_barra, label=lang, color=cores[lang])

        # Adicionar os rótulos de tempo na frente de cada barra
        for j, rect in enumerate(rects):
            val_real = valores[j]
            if val_real > 0:
                label = f' {val_real:.1f}s' if val_real >= 1 else f' {val_real*1000:.1f}ms'
                ax.annotate(label,
                            xy=(rect.get_width(), rect.get_y() + rect.get_height()/2),
                            xytext=(5, 0), # Pequeno deslocamento para a direita
                            textcoords="offset points",
                            ha='left', va='center', fontsize=8)
            elif j >= 3:
                ax.annotate(' T.O.',
                            xy=(1e-10, rect.get_y() + rect.get_height()/2),
                            xytext=(5, 0),
                            textcoords="offset points",
                            ha='left', va='center', fontsize=8, color='red', fontweight='bold')

    # Configurações de layout
    ax.set_xscale('log') # Escala logarítmica agora no eixo X
    ax.set_xlim(1e-6, 1e5)
    ax.set_xlabel('Tempo de Execução (Escala Logarítmica - Segundos)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Tamanho da Entrada (N)', fontsize=12, fontweight='bold')
    ax.set_title(titulo_grafico, fontsize=16, fontweight='bold', pad=25)
    
    # Invertemos o eixo Y para que o 10^2 fique no topo e o 10^6 embaixo (ou vice-versa)
    # Aqui deixei o 10^6 embaixo para dar a ideia de crescimento
    ax.set_yticks(y)
    ax.set_yticklabels(tamanhos)
    
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Linguagens/Flags")
    ax.grid(True, which="both", ls="--", alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('grafico_horizontal_final.png', dpi=300)
    print("Sucesso! O gráfico horizontal foi gerado como 'grafico_horizontal_final.png'.")
    plt.show()

if __name__ == "__main__":
    gerar_grafico_horizontal()