from stride.detector import analyze_architecture

def test_basic_architecture():
    architecture = {
        "components": [
            {"name": "AuthService", "auth": "weak", "logging": True},
            {"name": "DataStore", "confidential_data": True, "encryption": False},
            {"name": "WebServer", "rate_limiting": False, "privileges": "admin"}
        ]
    }
    results = analyze_architecture(architecture)
    assert 'Componente AuthService pode permitir spoofing por autenticação fraca.' in results['Spoofing']
    assert 'Componente DataStore armazena dados confidenciais sem criptografia.' in results['Information Disclosure']
    assert 'Componente WebServer não possui proteção contra DoS.' in results['Denial of Service']
    assert 'Componente WebServer pode permitir elevação inadequada de privilégios.' in results['Elevation of Privilege']
