Criando ambiente virtual

->No terminal VsCode: 
    py -m venv nomeAmbiente
    ou
    phyton -m venv nomeAmbiente

->Ativar ambiente, executar power shell adm
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned  
    - "S" para aceitar

->Voltar ao terminal VsCode
    - Scripts -> Activate.ps1 -> copy path
        C:\Users\natha\OneDrive\Desktop\ETL-cursophyton\test\Scripts\Activate.ps1
    - Pegar apenas essa parte: 
        test\Scripts\Activate.ps1 -> colar VsCode

->Confirmar se esta usando o ambiente virtual:
     py --version

->Desativar Ambiente virtual:
     deActivate

->Voltar a um ambiente: 
    test\Scripts\Activate.ps1 -> colar VsCode
