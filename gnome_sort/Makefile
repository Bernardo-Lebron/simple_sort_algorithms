# Configurações de compiladores
CC = gcc
CXX = g++
RUSTC = rustc
CFLAGS = -O3
CXXFLAGS = -O3
RUSTFLAGS = -C opt-level=3

# Caminhos dos executáveis (relativos à pasta gnome_sort)
C_BIN = c/GnomeSort
CPP_BIN = cpp/GnomeSort
RUST_BIN = rust/GnomeSort

# Caminhos dos scripts
JS_SRC = javascript/GnomeSort.js
PY_SRC = python/GnomeSort.py

# Valor padrão de N
N ?= 1000

.PHONY: all compile run clean

all: compile

compile:
	@echo "Compilando C..."
	@$(CC) $(CFLAGS) c/GnomeSort.c -o $(C_BIN)
	@echo "Compilando C++..."
	@$(CXX) $(CXXFLAGS) cpp/GnomeSort.cpp -o $(CPP_BIN)
	@echo "Compilando Rust..."
	@$(RUSTC) $(RUSTFLAGS) rust/GnomeSort.rs -o $(RUST_BIN)

run: compile
	@echo "--- Iniciando Benchmark Geral do Gnome Sort (N = $(N)) ---"
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