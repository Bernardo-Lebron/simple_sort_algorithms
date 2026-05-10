# Configurações de compiladores
CC = gcc
CXX = g++
RUSTC = rustc

# Flags de Otimização (Definidas como 0 para desativar otimizações)
CFLAGS = -O0
CXXFLAGS = -O0
RUSTFLAGS = -C opt-level=0

# Caminhos dos executáveis
C_BIN = c/selection
CPP_BIN = cpp/selection
RUST_BIN = rust/selection

# Caminhos dos scripts
JS_SRC = javascript/selection.js
PY_SRC = python/selection.py

# Valor padrão de N
N ?= 1000

.PHONY: all compile run clean

all: compile

compile:
	@echo "Compilando C (Sem otimizacao)..."
	@$(CC) $(CFLAGS) c/selection.c -o $(C_BIN) || echo "Erro ao compilar C"
	@chmod +x $(C_BIN) 2>/dev/null || true
	@echo "Compilando C++ (Sem otimizacao)..."
	@$(CXX) $(CXXFLAGS) cpp/selection.cpp -o $(CPP_BIN) || echo "Erro ao compilar C++"
	@chmod +x $(CPP_BIN) 2>/dev/null || true
	@echo "Compilando Rust (Sem otimizacao)..."
	@$(RUSTC) $(RUSTFLAGS) rust/selection.rs -o $(RUST_BIN) || echo "Erro ao compilar Rust"
	@chmod +x $(RUST_BIN) 2>/dev/null || true
	@echo "Compilacao concluida!"

run: compile
	@echo "--- Iniciando Benchmark Selection Sort SEM OTIMIZACAO (N = $(N)) ---"
	@echo ""
	@echo "[C]"
	@if [ -f $(C_BIN) ]; then cd c && ./selection $(N); else echo "Binario C nao encontrado"; fi
	@echo ""
	@echo "[C++]"
	@if [ -f $(CPP_BIN) ]; then cd cpp && ./selection $(N); else echo "Binario C++ nao encontrado"; fi
	@echo ""
	@echo "[Rust]"
	@if [ -f $(RUST_BIN) ]; then cd rust && ./selection $(N); else echo "Binario Rust nao encontrado"; fi
	@echo ""
	@echo "[JavaScript]"
	@node $(JS_SRC) $(N) || echo "Node.js nao instalado ou arquivo javascript/selection.js nao encontrado"
	@echo ""
	@echo "[Python]"
	@python3 $(PY_SRC) $(N) || echo "Python3 nao instalado ou arquivo python/selection.py nao encontrado"
	@echo ""
	@echo "--- Fim do Benchmark ---"

clean:
	@rm -f $(C_BIN) $(CPP_BIN) $(RUST_BIN)
	@echo "Binarios removidos."