.PHONY: test
test: .venv/bin/zope-testrunner
	.venv/bin/zope-testrunner --auto-progress --color --verbose --test-path=src

.venv/bin/zope-testrunner:
	uvx git+https://github.com/collective/plonex dependencies
