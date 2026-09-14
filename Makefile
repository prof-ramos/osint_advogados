.PHONY: help lint test check-links build-ebook clean all

PYTHON ?= python3

help:
	@echo "Comandos disponíveis no projeto OSINT Jurídico:"
	@echo "  make lint         - Executa o linter forense de evidências (livro e casos práticos)"
	@echo "  make test         - Executa a suíte de testes unitários automatizados"
	@echo "  make check-links  - Valida a sintaxe e integridade dos links da base dinâmica"
	@echo "  make build-ebook  - Compila o manual nos formatos Markdown, HTML e EPUB"
	@echo "  make clean        - Remove diretórios de compilação (dist/ e site/)"
	@echo "  make all          - Executa lint, test, check-links e build-ebook"

lint:
	$(PYTHON) scripts/lint_evidencias.py --path casos_praticos
	$(PYTHON) scripts/lint_evidencias.py --path livro

test:
	$(PYTHON) -m unittest discover -s tests -v

check-links:
	$(PYTHON) scripts/check_links.py --path base_dinamica
	$(PYTHON) scripts/check_links.py --path osint_brazuca_dataset

build-ebook:
	$(PYTHON) scripts/build_ebook.py

clean:
	rm -rf dist/ site/ .pytest_cache/ tests/__pycache__/ scripts/__pycache__/

all: lint test check-links build-ebook
