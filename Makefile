PY = python3
SRC = Ball.py Player.py Utils.py main.py

all: $(SRC)
	$(PY) main.py
push:
	@git add . && git commit -m "Done" && git push origin master

install:
	@if [ ! -d .venv ]; then \
  		python3 -m venv .venv && .venv/bin/pip install -r requirements.txt; \
	else \
	  echo "Evrything is good"; \
  	fi

clean:
	@ rm -rf __pycache__