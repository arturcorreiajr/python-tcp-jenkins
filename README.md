## Construindo a aplicaçāo
```console
docker build -t arturcorreiajunior/python-tcp:latest .
```
```console
docker push arturcorreiajunior/python-tcp:latest 
```
```console
docker run arturcorreiajunior/python-tcp:latest
```
Acessar container da aplicaçāo python
```console 
docker exec -it 5e4accc947cf bash
```

Executar aplicaçāo
```console 
python3 main.py
```

Preencher inputs
```console 
Informar host:
Informar port:
Mensagem a enviar:
```
Mensagem formato json:
```console
{"message":"Eu sou uma mensagem."}
```