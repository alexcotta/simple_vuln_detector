def map_stride_to_checks(category, architecture_desc):
    """
    Simula verificações simples para cada categoria STRIDE baseado na arquitetura.
    Retorna uma lista de possíveis vulnerabilidades.
    """

    vulns = []
    components = architecture_desc.get('components', [])

    if category == 'Spoofing':
        # Exemplo: verifica componentes que usam autenticação fraca
        for comp in components:
            if comp.get('auth') == 'weak':
                vulns.append(f"Componente {comp['name']} pode permitir spoofing por autenticação fraca.")
    elif category == 'Tampering':
        for comp in components:
            if not comp.get('data_integrity', True):
                vulns.append(f"Componente {comp['name']} não garante integridade dos dados.")
    elif category == 'Repudiation':
        for comp in components:
            if not comp.get('logging', True):
                vulns.append(f"Componente {comp['name']} não possui logs adequados para auditoria.")
    elif category == 'Information Disclosure':
        for comp in components:
            if comp.get('confidential_data', False) and not comp.get('encryption', False):
                vulns.append(f"Componente {comp['name']} armazena dados confidenciais sem criptografia.")
    elif category == 'Denial of Service':
        for comp in components:
            if comp.get('rate_limiting', False) is False:
                vulns.append(f"Componente {comp['name']} não possui proteção contra DoS.")
    elif category == 'Elevation of Privilege':
        for comp in components:
            if comp.get('privileges', 'user') != 'user':
                vulns.append(f"Componente {comp['name']} pode permitir elevação inadequada de privilégios.")
    return vulns
