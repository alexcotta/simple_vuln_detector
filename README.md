# Agente de Detecção de Vulnerabilidades usando STRIDE

Este projeto implementa um agente simples para detectar vulnerabilidades em arquiteturas de sistemas usando a metodologia STRIDE. Utiliza Python e a biblioteca Unicorn para realizar análises e oferece uma API REST fácil de usar.

## Importância

Identificar vulnerabilidades por STRIDE ajuda a mitigar riscos de segurança fundamentais como spoofing, tampering e negação de serviço, protegendo sistemas de ataques comuns.

## Tecnologias utilizadas

- Pythton 3.10
- Flask
  
## Como executar

1. Instale as dependências:

```bash
	pip install -r requirements.txt
```

2. Execute o servidor API:
```bash
	python api/server.py
```

3. Envie um POST para `http://localhost:5000/analyze` com JSON contendo sua arquitetura:
```
{
  "architecture": {
                    "components": [{"name": "Componente1", "auth": "weak", "logging": false}]
                  }
}
```

O serviço retornará a análise de vulnerabilidades segundo STRIDE.
