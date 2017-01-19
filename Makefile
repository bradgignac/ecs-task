default: clean test

test:
	tox

clean:
	rm -rf .cache
	rm -rf .tox
	rm -rf ecstask.egg-info
	find . -name \*.pyc -delete

.PHONY: clean test
