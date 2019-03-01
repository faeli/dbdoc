check:
	twine check ./dist/*
build_dist:
	python setup.py sdist bdist_wheel
upload_test:
	twine upload -r pypitest ./dist/*
upload:
	twine upload --skip-existing ./dist/*

