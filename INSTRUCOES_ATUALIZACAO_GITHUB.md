_# 🚀 Guia Rápido: Como Atualizar o Teste Vocacional no GitHub_

**Objetivo:** Substituir os arquivos antigos no seu repositório do GitHub pelos novos para que a Vercel atualize o site automaticamente.

**Tempo estimado:** 5 minutos

---

## 🎯 O Que Acontece Depois?

Assim que você atualizar os arquivos no GitHub, a Vercel irá:

1.  **Detectar** a mudança automaticamente.
2.  **Iniciar um novo build** da sua aplicação.
3.  **Publicar a nova versão** no seu domínio `teste.mapeandoconhecimentos.com`.

Tudo isso sem você precisar fazer mais nada!

---

## 📝 Passo a Passo para Atualizar

### Passo 1: Extraia o Novo Pacote

-   Primeiro, baixe e extraia o novo arquivo `.zip` que eu te enviei (`teste-vocacional-vercel-atualizado.zip`) no seu computador.

### Passo 2: Acesse seu Repositório no GitHub

-   Vá para a página do seu repositório `teste-vocacional-mapeando-conhecimentos`.

### Passo 3: Faça o Upload dos Novos Arquivos

1.  Na página principal do repositório, clique no botão **Add file** e depois em **Upload files**.

    ![Upload Files Button](https://i.imgur.com/2jVqJz7.png)

2.  **Arraste e solte** todos os arquivos da pasta `deploy-vercel-atualizado` (que você extraiu) para a área de upload do GitHub.

    -   **Importante:** O GitHub é inteligente e vai detectar que você está substituindo os arquivos existentes. Ele mostrará os arquivos antigos sendo "sobrescritos".

    ![Drag and Drop Files](https://i.imgur.com/9sL4sB1.png)

### Passo 4: Confirme as Alterações (Commit)

1.  No final da página, você verá uma caixa para descrever suas alterações.
2.  Escreva uma mensagem simples, como: `Atualiza teste para 34 profissões`.
3.  Clique no botão verde **Commit changes**.

    ![Commit Changes](https://i.imgur.com/P3fGj2g.png)

---

## ✅ Verificação Final

1.  **Acesse a Vercel:** Vá para o seu dashboard na Vercel.
2.  **Verifique o Build:** Você verá um novo build em andamento para o seu projeto. Geralmente leva de 1 a 2 minutos.
3.  **Teste o Site:** Assim que o build terminar, acesse `https://teste.mapeandoconhecimentos.com`. As atualizações (34 profissões) já estarão lá!

É só isso! O processo é muito simples e garante que seu site esteja sempre atualizado com a última versão do código. 🎉

