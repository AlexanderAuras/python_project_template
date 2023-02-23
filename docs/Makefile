MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -E -a

.PHONY: help Makefile html

html: Makefile
	rm -rf source/*.rst
	sphinx-apidoc -o source -e -f -t source/_templates --tocfile index ../src/*
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -E -a
