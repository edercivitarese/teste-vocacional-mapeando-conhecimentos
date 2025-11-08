# 📦 Pacote de Deploy: Teste Vocacional - Vercel

**Versão:** 2.0  
**Data:** 07/11/2025  
**Plataforma:** Vercel (Gratuito)

---

## 🎯 O Que É Este Pacote?

Este pacote contém tudo o que você precisa para publicar o **Teste Vocacional de Profissões do Futuro** de forma **gratuita e permanente** na Vercel, usando seu próprio domínio `teste.mapeandoconhecimentos.com`.

---

## 📋 Conteúdo

- **`main.py`** - Aplicação Flask com 34 profissões
- **`static/`** - Frontend React compilado
- **`requirements.txt`** - Dependências Python
- **`vercel.json`** - Configuração para deploy na Vercel
- **`.gitignore`** - Arquivos a ignorar no Git
- **`GUIA_DEPLOY_VERCEL.md`** - Instruções completas passo a passo

---

## 🚀 Início Rápido (3 Passos)

### 1. Criar Repositório no GitHub
- Crie uma conta no [GitHub](https://github.com)
- Crie um novo repositório público
- Faça upload de todos os arquivos deste pacote

### 2. Deploy na Vercel
- Crie uma conta no [Vercel](https://vercel.com) usando sua conta do GitHub
- Importe o repositório que você criou
- Clique em "Deploy"

### 3. Conectar seu Domínio
- Na Vercel, adicione `teste.mapeandoconhecimentos.com`
- Configure o DNS na Hostinger (registro CNAME)

**Tempo total:** 10-15 minutos  
**Custo:** R$ 0,00 (gratuito para sempre)

---

## ✨ Vantagens da Vercel

| Característica | Vercel | Hostinger Compartilhada |
|----------------|--------|-------------------------|
| **Custo** | Grátis | Não suporta Python |
| **Performance** | Excelente (CDN global) | Boa |
| **SSL** | Automático | Manual |
| **Deploy** | Automático (GitHub) | Manual |
| **Hibernação** | Nunca | N/A |
| **Domínio customizado** | Grátis | Grátis |

---

## 🔄 Migração Futura para VPS

Se você contratar uma VPS no futuro, a migração é trivial:

1. Faça upload dos mesmos arquivos
2. Rode `pip install -r requirements.txt`
3. Rode `python main.py`

**Pronto!** O código é 100% portável.

---

## 🔗 Integração com o Blog

Depois do deploy, use este iframe no WordPress:

```html
<iframe 
  src="https://teste.mapeandoconhecimentos.com"
  width="100%" 
  height="800" 
  frameborder="0">
</iframe>
```

Código responsivo completo está no guia.

---

## 📞 Suporte

Consulte o arquivo `GUIA_DEPLOY_VERCEL.md` para instruções detalhadas com screenshots e solução de problemas.

---

**Boa sorte com o deploy!** 🚀

