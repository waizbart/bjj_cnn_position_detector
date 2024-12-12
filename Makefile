build:
	docker build -t bjj_ia .

run:
	docker run --name bjj_ia -d --rm --gpus all -p 8000:8000 bjj_ia
