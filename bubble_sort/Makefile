# Configurações de compiladores
CC = gcc
CXX = g++
RUSTC = rustc
CFLAGS = -O0
CXXFLAGS = -O0
RUSTFLAGS = -C opt-level=0

# Caminhos dos executáveis (agora relativos à pasta bubble_sort)
C_BIN = c/bubble_sort
CPP_BIN = cpp/bubble_sort_cpp
RUST_BIN = rust/bubble_sort_rust

# Caminhos dos scripts
JS_SRC = javascript/bubble_sort.js
PY_SRC = python/bubble_sort.py

# Valor padrão de N
N ?= 1000

.PHONY: all compile run clean

all: compile

compile:
	@echo "Compilando C..."
	@$(CC) $(CFLAGS) c/bubble_sort.c -o $(C_BIN)
	@echo "Compilando C++..."
	@$(CXX) $(CXXFLAGS) cpp/bubble_sort.cpp -o $(CPP_BIN)
	@echo "Compilando Rust..."
	@$(RUSTC) $(RUSTFLAGS) rust/bubble_sort.rs -o $(RUST_BIN)

run: compile
	@echo "--- Iniciando Benchmark Geral (N = $(N)) ---"
	@echo ""
	@echo "[C]"
	@./$(C_BIN) $(N)
	@echo ""
	@echo "[C++]"
	@./$(CPP_BIN) $(N)
	@echo ""
	@echo "[Rust]"
	@./$(RUST_BIN) $(N)
	@echo ""
	@echo "[JavaScript]"
	@node $(JS_SRC) $(N)
	@echo ""
	@echo "[Python]"
	@python3 $(PY_SRC) $(N)
	@echo ""
	@echo "--- Fim do Benchmark ---"

clean:
	rm -f $(C_BIN) $(CPP_BIN) $(RUST_BIN)