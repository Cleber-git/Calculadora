#from ex114.lib.interface import título, menu
#from ex114.lib.arquivo import arquivoExiste, CriarArquivo, Cadastrar, lerArquivo


arquivo = str(input('Digite o nome do arquivo junto com a sua extensão: '))
while True:
  #  if not arquivoExiste(arquivo):
        escolha = str(input('O seu arquivo não existe nesse diretório, deseja criá-lo? ')).strip().upper()[0]
        if escolha == 'S':
  #          CriarArquivo(arquivo)
            continue
        else:
#            título('Saindo do sistema, até logo...')
            break
   # if arquivoExiste(arquivo):
 #        escolha = menu(['\033[34mCadastrar uma pessoa\033[m', '\033[34mVer lista de cadastro\033[m', '\033[34mSair do sistema\033[m'])
      #   if escolha == 1:
            Cadastrar(arquivo)
      #   elif escolha == 2:
      #       lerArquivo(arquivo)
       #  elif escolha == 3:
  #           título('Saindo do sistema, até logo...')
       #      break
       #  else:
       #      print('\033[31mDigite uma opção válida!\033[m')
