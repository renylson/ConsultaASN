# 🤝 Guia de Contribuição

Obrigado por considerar contribuir para o ASN Lookup Tool! Este documento fornece diretrizes para contribuir com o projeto.

## 📋 Como Contribuir

### 🐛 Reportando Bugs

Antes de reportar um bug, verifique se ele já não foi reportado nas [Issues](https://github.com/renylson/consulta_asn/issues).

Para reportar um bug:
1. Use um título claro e descritivo
2. Descreva os passos para reproduzir o problema
3. Inclua informações sobre seu ambiente (OS, versão do Python, etc.)
4. Se possível, inclua screenshots ou logs

### 💡 Sugerindo Melhorias

Para sugerir uma melhoria:
1. Verifique se a sugestão já não existe nas Issues
2. Abra uma nova Issue com o label "enhancement"
3. Descreva claramente a melhoria proposta
4. Explique por que esta melhoria seria útil

### 🔧 Contribuindo com Código

#### Configuração do Ambiente de Desenvolvimento

1. **Fork do repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/consulta_asn.git
   cd consulta_asn
   ```

2. **Criar ambiente virtual**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/MacOS
   source venv/bin/activate
   ```

3. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar API Key**
   - Obtenha uma chave gratuita em [IPinfo.io](https://ipinfo.io/)
   - Substitua `XXXXXXXXXXXX` no arquivo `app.py`

#### Processo de Desenvolvimento

1. **Criar uma branch para sua feature**
   ```bash
   git checkout -b feature/nome-da-feature
   ```

2. **Fazer suas alterações**
   - Mantenha o código limpo e bem documentado
   - Siga as convenções de código Python (PEP 8)
   - Adicione comentários quando necessário

3. **Testar suas alterações**
   ```bash
   python app.py
   ```
   - Acesse `http://localhost:5000` e teste a funcionalidade
   - Teste com diferentes tipos de entrada (IPs, domínios, CIDRs)

4. **Commit suas alterações**
   ```bash
   git add .
   git commit -m "feat: adicionar nova funcionalidade X"
   ```

5. **Push para seu fork**
   ```bash
   git push origin feature/nome-da-feature
   ```

6. **Abrir Pull Request**
   - Descreva claramente as mudanças realizadas
   - Referencie Issues relacionadas
   - Inclua screenshots se aplicável

## 📝 Convenções

### Mensagens de Commit

Use o padrão [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` para novas funcionalidades
- `fix:` para correções de bugs
- `docs:` para mudanças na documentação
- `style:` para mudanças de formatação
- `refactor:` para refatoração de código
- `test:` para adição de testes
- `chore:` para tarefas de manutenção

### Código Python

- Siga o [PEP 8](https://pep8.org/)
- Use nomes descritivos para variáveis e funções
- Adicione docstrings para funções públicas
- Mantenha funções pequenas e focadas

## 🧪 Testes

Atualmente, o projeto não possui testes automatizados, mas esta é uma área onde contribuições são muito bem-vindas!

### Teste Manual

Teste os seguintes cenários:
- Consulta por IP válido
- Consulta por domínio válido
- Consulta por múltiplos IPs/domínios
- Entrada inválida
- Domínios que não resolvem

## 📚 Documentação

Ao adicionar novas funcionalidades:
- Atualize o README.md se necessário
- Adicione comentários no código
- Considere adicionar exemplos de uso

## ❓ Dúvidas

Se tiver dúvidas sobre como contribuir:
- Abra uma Issue com a label "question"
- Entre em contato: renylsonm@gmail.com

## 📄 Código de Conduta

Este projeto segue o [Contributor Covenant](https://www.contributor-covenant.org/). Esperamos que todos os participantes sigam este código de conduta.

## ⚖️ Licença e Direitos Autorais

**IMPORTANTE**: Este projeto está sob **todos os direitos reservados**. Ao contribuir:

- ✅ Suas contribuições serão incorporadas sob a mesma licença restritiva
- ✅ Você mantém os direitos autorais de suas contribuições
- ✅ Você concede ao proprietário do projeto direitos para usar suas contribuições
- ⚠️ O código resultante permanecerá sob licença proprietária

**Antes de contribuir**, certifique-se de que concorda com estes termos. Para dúvidas sobre licenciamento, entre em contato com o autor.

---

**Obrigado por contribuir! 🚀**
