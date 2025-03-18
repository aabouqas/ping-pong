PY = python3
SRC = Ball.py Player.py Utils.py main.py

all: $(SRC) .venv
	source .venv/bin/activate && $(PY) main.py
push: clean
	@git add . && git commit -m "Done" && git push

.venv:
	@ echo "Creating virtual envirement" && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

clean:
	@ rm -rf __pycache__