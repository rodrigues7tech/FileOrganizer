# FileOrganizer

## Automatização de Organização de Arquivos por Extensão

Este é um script de automação em Python para organizar arquivos em um diretório de acordo com a extensão do arquivo. Ele percorre um diretório alvo e move os arquivos para subdiretórios correspondentes à sua extensão.

## Como Usar

1. Clone este repositório ou baixe o arquivo `FileOrganizer.py` para o seu sistema.

2. Certifique-se de ter o Python instalado em seu sistema.

3. Abra um terminal ou prompt de comando e navegue até o diretório onde está o arquivo `FileOrganizer.py`.

4. Execute o script com o seguinte comando:

   ```bash
   python FileOrganizer.py
   ```

   Logo após execução do script insira o caminho `caminho/do/diretorio` que você deseja organizar.

   ```bash
   Digite o caminho do diretório:
   caminho/do/diretorio
   ```

## Exemplo

Suponha que temos os seguintes arquivos no diretório alvo:

```
/diretorio_alvo
    |- arquivo1.txt
    |- arquivo2.jpg
    |- arquivo3.txt
    |- arquivo4.docx
    |- arquivo5.jpg
```

Após executar o script, o diretório ficará assim:

```
/diretorio_alvo
    |- /txt
        |- arquivo1.txt
        |- arquivo3.txt
    |- /jpg
        |- arquivo2.jpg
        |- arquivo5.jpg
    |- /docx
        |- arquivo4.docx
```

## Observações

- Certifique-se de fazer um backup dos seus arquivos antes de executar o script, para evitar a perda acidental de dados.

- Este script organiza os arquivos em subdiretórios com base na extensão do arquivo. Se um subdiretório para uma determinada extensão já existir, o arquivo será movido para esse subdiretório.

- O script irá ignorar subdiretórios dentro do diretório alvo.

- A extensão do arquivo é determinada pelo texto após o último ponto no nome do arquivo. Por exemplo, em `arquivo1.txt`, a extensão é `.txt`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar um pull request com melhorias.

---

Espero que este script seja útil para organizar seus arquivos de forma automatizada. Se tiver alguma dúvida ou sugestão, não hesite em entrar em contato!
