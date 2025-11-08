# 🚀 Guia Completo: Deploy do Teste Vocacional na Vercel (Grátis)

**Data:** 07/11/2025  
**Aplicação:** Teste Vocacional de Profissões do Futuro  
**Plataforma:** Vercel (Plano Hobby - Gratuito)

---

## 🎯 Objetivo

Publicar o Teste Vocacional de forma **permanente e gratuita** na Vercel, e conectá-lo ao seu subdomínio `teste.mapeandoconhecimentos.com`.

---

## ✨ Vantagens da Vercel

- **100% Gratuito:** O plano Hobby é perfeito para este projeto.
- **Deploy Automático:** Qualquer alteração no GitHub atualiza o site.
- **Performance Excelente:** Rede global de alta velocidade (CDN).
- **Domínio Customizado:** Use seu próprio subdomínio sem custo extra.
- **SSL Automático:** HTTPS ativado por padrão.
- **Não Hiberna:** Sua aplicação fica sempre online.

---

## 📦 Arquivos Inclusos no Pacote

- `main.py`: Aplicação Flask.
- `static/`: Frontend React compilado.
- `requirements.txt`: Dependências Python.
- `vercel.json`: Arquivo de configuração para a Vercel.
- `.gitignore`: Arquivos a serem ignorados pelo Git.

---

## 📝 Passo a Passo do Deploy (10-15 minutos)

### Parte 1: Preparar o GitHub

#### Passo 1: Criar uma Conta no GitHub

Se você ainda não tem, crie uma conta gratuita em [github.com](https://github.com).

#### Passo 2: Criar um Novo Repositório

1. No GitHub, clique em **New repository**.
2. **Nome do Repositório:** `teste-vocacional-mapeando-conhecimentos`
3. **Descrição:** "Teste Vocacional de Profissões do Futuro para o blog Mapeando Conhecimentos."
4. Selecione **Público** (Public).
5. Clique em **Create repository**.

#### Passo 3: Fazer Upload dos Arquivos

1. Na página do seu novo repositório, clique em **Add file** → **Upload files**.
2. **Extraia o ZIP** que eu te enviei no seu computador.
3. **Arraste todos os arquivos** da pasta `deploy-vercel-teste-vocacional` para a área de upload do GitHub.
4. Clique em **Commit changes**.

   > **Pronto!** Seu código agora está no GitHub, pronto para ser lido pela Vercel.

### Parte 2: Fazer o Deploy na Vercel

#### Passo 4: Criar uma Conta na Vercel

1. Acesse [vercel.com](https://vercel.com).
2. Clique em **Sign Up** e escolha **Continue with GitHub**. Autorize o acesso.

#### Passo 5: Importar o Projeto

1. No seu dashboard da Vercel, clique em **Add New...** → **Project**.
2. Na seção **Import Git Repository**, seu repositório do GitHub (`teste-vocacional-mapeando-conhecimentos`) deve aparecer. Clique em **Import**.

#### Passo 6: Configurar e Fazer o Deploy

A Vercel é inteligente e já vai detectar que é um projeto Python/Flask. As configurações padrão geralmente funcionam.

1. **Framework Preset:** Deve estar como `Other`.
2. **Build & Development Settings:** Não precisa mexer em nada.
3. **Environment Variables:** Não precisa adicionar nenhuma.
4. Clique em **Deploy**.

   > **Aguarde a mágica acontecer!** A Vercel vai instalar as dependências, construir o projeto e publicá-lo. Isso leva cerca de 1-2 minutos. Ao final, você receberá uma URL temporária (ex: `teste-vocacional-xyz.vercel.app`).

### Parte 3: Conectar seu Domínio

#### Passo 7: Adicionar o Domínio na Vercel

1. No dashboard do seu projeto na Vercel, vá para a aba **Settings** → **Domains**.
2. Digite seu subdomínio: `teste.mapeandoconhecimentos.com`
3. Clique em **Add**.

#### Passo 8: Configurar o DNS na Hostinger

A Vercel mostrará as instruções de DNS. Você precisará adicionar um registro **CNAME** no painel da Hostinger.

1. Acesse seu painel da Hostinger.
2. Vá para **Domínios** → `mapeandoconhecimentos.com` → **DNS / Nameservers**.
3. Em **Gerenciar registros DNS**, adicione um novo registro:
   - **Tipo:** `CNAME`
   - **Nome:** `teste`
   - **Aponta para:** `cname.vercel-dns.com` (ou o valor que a Vercel te informar).
   - **TTL:** Deixe o padrão (geralmente 14400).
4. Clique em **Adicionar Registro**.

   > **Aguarde a propagação do DNS.** Pode levar de alguns minutos a algumas horas. A Vercel avisará quando estiver tudo certo.

---

## ✅ Teste Final

Após a propagação do DNS, acesse **https://teste.mapeandoconhecimentos.com**. Seu teste vocacional estará online, seguro e rápido!

---

## 🔄 Como Atualizar o Site no Futuro?

É a parte mais fácil! Qualquer alteração que você fizer no repositório do GitHub (ex: editar o `main.py` para adicionar uma nova profissão) **automaticamente** fará um novo deploy na Vercel. Você não precisa fazer mais nada!

---

## 🔗 Integração com Iframe (URL Permanente)

Use este código no seu blog WordPress para incorporar o teste:

```html
<div style="position: relative; padding-bottom: 120%; height: 0; overflow: hidden; max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <iframe 
    src="https://teste.mapeandoconhecimentos.com"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"
    title="Teste Vocacional de Profissões do Futuro">
  </iframe>
</div>
```

---

**Parabéns!** Você terá uma aplicação profissional rodando de graça e com as melhores práticas do mercado. 🎉

