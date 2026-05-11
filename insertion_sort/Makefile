# Configurações de compiladores
CC = gcc
CXX = g++
RUSTC = rustc
CFLAGS = -O3
CXXFLAGS = -O3
RUSTFLAGS = -C opt-level=3

# Caminhos dos executáveis
C_BIN = c/insertion_sort
CPP_BIN = cpp/insertion_sort_cpp
RUST_BIN = rust/insertion_sort_rust

# Caminhos dos scripts
JS_SRC = Javascript/main.js
PY_SRC = python/main.py

# Valor padrão de N
N ?= 1000

.PHONY: all compile run clean

all: compile

compile:
	@mkdir -p c cpp rust
	@echo "Compilando C..."
	@$(CC) $(CFLAGS) c/main.c -o $(C_BIN) || echo "Erro ao compilar C"
	@echo "Compilando C++..."
	@$(CXX) $(CXXFLAGS) C++/main.cpp -o $(CPP_BIN) || echo "Erro ao compilar C++"
	@echo "Compilando Rust..."
	@$(RUSTC) $(RUSTFLAGS) rust/main.rs -o $(RUST_BIN) || echo "Erro ao compilar Rust"
	@echo "Compilacao concluida!"

run: compile
	@echo "--- Iniciando Benchmark Insertion Sort (N = $(N)) ---"
	@echo ""
	@echo "[C]"
	@if [ -f $(C_BIN) ]; then ./$(C_BIN) $(N); else echo "Binario C nao encontrado"; fi
	@echo ""
	@echo "[C++]"
	@if [ -f $(CPP_BIN) ]; then ./$(CPP_BIN) $(N); else echo "Binario C++ nao encontrado"; fi
	@echo ""
	@echo "[Rust]"
	@if [ -f $(RUST_BIN) ]; then ./$(RUST_BIN) $(N); else echo "Binario Rust nao encontrado"; fi
	@echo ""
	@echo "[JavaScript]"
	@node $(JS_SRC) $(N) || echo "Erro ao executar JavaScript"
	@echo ""
	@echo "[Python]"
	@python3 $(PY_SRC) $(N) || echo "Erro ao executar Python"
	@echo ""
	@echo "--- Fim do Benchmark ---"

clean:
	@rm -f $(C_BIN) $(CPP_BIN) $(RUST_BIN)
	@echo "Binarios removidos."